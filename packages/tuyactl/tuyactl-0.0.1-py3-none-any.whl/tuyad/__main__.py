#!/usr/bin/env python
import tinytuya
import json
import os
import struct
import subprocess
import asyncio
import aiofiles
import numpy as np
import time
import random
import logging
from scipy.fft import fft
from scipy.signal import butter, filtfilt
from quart import Quart, request, jsonify
from colour import Color
from collections import deque

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

DEVICES_FILE = os.environ.get('DEVICES', os.path.expanduser('~/snapshot.json'))
XDG_RUNTIME_DIR = os.environ.get('XDG_RUNTIME_DIR', f'/run/user/{os.getuid()}')
AUDIO_TARGET = os.environ.get('TUYA_MCP_AUDIO_TARGET', 'alsa_output.pci-0000_00_1b.0.analog-stereo.monitor')
CHANNELS    = 2
SAMPLE_RATE = 48000
BUFFER_SIZE = SAMPLE_RATE * CHANNELS # 16 bits LE gives 500ms of data
CHUNK_SIZE  = 1024

app = Quart(__name__)
devices = []
stop_event = asyncio.Event()

async def load_devices():
    global devices
    try:
        async with aiofiles.open(DEVICES_FILE, 'r') as f:
            data = await f.read()
            devices = json.loads(data).get("devices", [])
        logging.info("Devices loaded")
    except FileNotFoundError:
        logging.error(f"Error: {DEVICES_FILE} not found.")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error: Invalid JSON format in {DEVICES_FILE}.")
        raise

async def control_device(device, action, *args, timeout=0.5, retries=1, **kwargs):
    try:
        device_id   = device['id'  ]
        device_name = device['name']
        local_key   = device['key' ]
        ip_address  = device['ip'  ]
        version     = device['ver' ]

        d = tinytuya.BulbDevice(
                device_id,
                ip_address,
                local_key,
                connection_retry_limit=retries,
                connection_timeout=timeout)
        d.set_version(version)
        function = getattr(d, action)
        logging.info(f"Executing {action} on {device_name}: {args} {kwargs}")
        function(*args, **kwargs)
        logging.info(f"Executed {action} on {device_name}")
    except Exception as e:
        logging.error(f"Error controlling {device_name or 'unknown device'}: {e}")
        raise

async def handle_action_over_devices(action, request_data, *args, **kwargs):
    all_devices = request_data.get('all', False)
    devices_names = request_data.get('devices', [])

    kwargs['nowait'] = kwargs.get('nowait',True)

    if not all_devices and not devices_names:
        return jsonify({"status": "error", "message": "At least one device name must be provided"}), 400

    tasks = []
    for device in devices:
        if device.get('name') in devices_names or all_devices:
            tasks.append(asyncio.create_task(control_device(device, action, *args, **kwargs)))

    return jsonify({
        "status": "success",
        "message": f"Action {action} executed over {'all devices' if all_devices else 'devices: '}{','.join(devices_names)}."
    })

def generate_dp27_payload(mode: int,
                          hue: int,
                          saturation: int,
                          value: int,
                          brightness: int = 1000, 
                          white_brightness: int = 0, 
                          temperature: int = 1000) -> str:
    """
    Generate a DP27 payload for Tuya music mode.

    :param mode: 0 for jumping mode, 1 for gradient mode.
    :param hue: Hue value (0-360).
    :param saturation: Saturation (0-1000).
    :param value: Value (0-1000).
    :param brightness: Brightness (0-1000), default is 1000.
    :param white_brightness: White brightness (0-1000), default is 1000.
    :param temperature: Color temperature (0-1000), default is 1000.
    :return: DP27 string payload.
    """
    return f"{mode:01X}{hue:04X}{saturation:04X}{brightness:04X}{white_brightness:04X}{temperature:04X}"

from collections import deque

class AsyncDeque(deque):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._not_empty = asyncio.Condition()  # For signaling when items are added
        self._stopped = False  # To indicate when the deque is stopped

    def __aiter__(self):
        return self

    async def __anext__(self):
        async with self._not_empty:
            while not self and not self._stopped:
                await self._not_empty.wait()  # Wait until an item is added or stopped
            if self._stopped and not self:
                raise StopAsyncIteration
            return self.popleft()

    async def put(self, item):
        """Add an item to the deque and notify waiting consumers."""
        async with self._not_empty:
            self.append(item)
            self._not_empty.notify()

    async def stop(self):
        """Stop all waiting consumers by notifying them."""
        async with self._not_empty:
            self._stopped = True
            self._not_empty.notify_all()

    async def __aenter__(self):
        """Enter context, returning the deque."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit context, ensuring proper cleanup."""
        await self.stop()

class AudioBufferManager:
    def __init__(self):
        self.sample_rate = SAMPLE_RATE
        self.chunk_size  = CHUNK_SIZE 
        self.max_buffer_size = 1
        self.consumers = []
        self.lock = asyncio.Lock()

    async def add_audio_data(self, data):
        """Add new audio data to the buffer and all consumer queues"""
        async with self.lock:
            # Add to all consumer queues
            for queue in self.consumers:
                await queue.put(data)

    def register_consumer(self):
        """Create a new async generator for a consumer"""
        queue = AsyncDeque(maxlen=self.max_buffer_size)
        self.consumers.append(queue)
        return queue

buffer_manager = AudioBufferManager()

async def audio_reader():
    global stop_event, buffer_manager

    process = await asyncio.create_subprocess_exec(
        #'parec', f'--device={AUDIO_TARGET}', '--format=s16', f'--rate={SAMPLE_RATE}',
        'pw-record', f'--target={AUDIO_TARGET}', '--format=s16', f'--rate={SAMPLE_RATE}', '-',
        env={'XDG_RUNTIME_DIR': XDG_RUNTIME_DIR},
        stdout=asyncio.subprocess.PIPE,
    )
    logging.info("Initializing audio reader task.")

    try:
        while not stop_event.is_set():
            chunk = await process.stdout.read(CHUNK_SIZE)
            #if not any(chunk): logging.info('empty chunk')
            await buffer_manager.add_audio_data(chunk)
    except Exception as e:
        logging.error(f"Audio reader error: {e}")
        raise

async def audio_consumer(device, freq_range, *args, timeout=0.5, retries=1, **kwargs):
    global stop_event, buffer_manager
    consumer = buffer_manager.register_consumer()
    device_id   = device['id']
    device_name = device['name']
    local_key   = device['key']
    ip_address  = device['ip']
    version     = float(device['ver'])

    d = tinytuya.BulbDevice(
        device_id,
        ip_address,
        local_key,
        connection_retry_limit=retries,
        connection_timeout=timeout)
    d.set_version(version)
    d.set_socketPersistent(True)
    d.set_mode('music')

    status = d.status()
    error_message = status.get('Error',None)
    if error_message:
        logging.error(f'{device_name} error: {error_message}')
        return

    logging.info(f"{device_name} will handle {freq_range[0]} Hz - {freq_range[1]} Hz")

    # Parameters for beat detection and processing
    BEAT_THRESHOLD_FACTOR = 1.5  #  Base beat detection threshold.  Dynamic adjustment target.
    DYNAMIC_ADJUSTMENT_RATE = 0.01 # How quickly the threshold adapts
    RUNNING_AVG_COEFF = 0.90     # For smoothing the volume (increased responsiveness, was 0.975)
    MIN_BRIGHTNESS = 0  # Ensure this is never negative.
    MAX_BRIGHTNESS = 1000
    MIN_SATURATION = 0
    MAX_SATURATION = 1000
    
    # Beat detection variables
    history_length = int(SAMPLE_RATE / CHUNK_SIZE)  # 1 second history
    volume_history = np.zeros(history_length)
    current_index = 0
    dynamic_threshold = 0
    last_beat_time = 0

    # Color rotation parameters
    sensitivity=1.5       # Beat detection sensitivity (higher = more sensitive)
    decay_rate=0.97       # How quickly peaks decay over time
    flash_duration=0.1    # Duration of light flash in seconds

    hue = 0
    brightness = 0
    saturation = 0

    def calculate_rms(audio_data):
        """Calculate root mean square of audio chunk"""
        return np.sqrt(np.mean(np.square(audio_data)))

    def is_beat(current_volume):
        """Improved beat detection using dynamic threshold"""
        nonlocal dynamic_threshold, last_beat_time
        # Update dynamic threshold
        dynamic_threshold = decay_rate * dynamic_threshold + (1 - decay_rate) * current_volume
        
        # Check if current volume exceeds threshold and cooldown has passed
        now = time.time()
        if current_volume > dynamic_threshold * sensitivity and (now - last_beat_time) > flash_duration:
            last_beat_time = now
            return True
        return False

    async def fade_back(device, duration):
        """Gradual fade back to rhythm-based brightness"""
        start_time = time.time()
        while time.time() - start_time < duration:
            brightness = int(1000 * (1 - (time.time() - start_time)/duration))
            value = generate_dp27_payload(0, hue, saturation, brightness)
            payload = device.generate_payload(tinytuya.CONTROL, {"27": value})
            device.send(payload)
            await asyncio.sleep(0.05)

    async def fft_analysis(np_audio):
        # FFT analysis focused on bass frequencies
        fft_data = np.fft.rfft(np_audio)
        frequencies = np.fft.rfftfreq(len(np_audio), 1/SAMPLE_RATE)
        mask = (frequencies >= freq_range[0]) & (frequencies <= freq_range[1])
        fft_abs = np.abs(fft_data[mask])
        energy = np.sum(fft_abs)
        # Convert to dB scale
        volume_db = 10 * np.log10(energy + 1e-9)  # Add epsilon to avoid log(0)

        max_index = np.argmax(fft_abs)
        dominant_frequency = frequencies[mask][max_index]
        
        return dominant_frequency, volume_db

    try:
        async for audio_chunk in consumer:
            if stop_event.is_set(): break
            np_audio = np.frombuffer(audio_chunk, dtype=np.int16).astype(float)

            frequency, volume = await fft_analysis(np_audio)
            
            hue = int(frequency / freq_range[1] * 360) if frequency > 0 else hue

            # Beat detection
            if is_beat(volume):
                # Flash on beat
                brightness = MAX_BRIGHTNESS
                saturation = MAX_SATURATION
            
                # Schedule return to rhythm-based brightness
                asyncio.create_task(fade_back(d, flash_duration))
            else:
                # Base rhythm mode
                brightness = int(np.clip(volume * 10, 0, 1000))  # Map volume to brightness
                saturation = 1000

            value = generate_dp27_payload(0, hue, saturation, brightness)  # Full brightness
            logging.info(f"Sending {value} (" + \
                         f"H: {hue:03d} " + \
                         f"S: {saturation:04d} " + \
                         f"V: {brightness:04d} " + \
                         f"vol: {volume:10.2f} dB " + \
                         f"freq: {frequency:10.2f} Hz) " + \
                         f"to {device_name}")
            payload = d.generate_payload(tinytuya.CONTROL, {"27": value})
            d.send(payload)

    except Exception as e:
        logging.error(f"Error controlling {device_name or 'unknown device'}: {e}")
        d.set_white()
        raise

async def music_mode(request_data):
    global stop_event

    stop = request_data.get('stop', False)
    all_devices = request_data.get('all', False)
    devices_names = request_data.get('devices', [])
    
    if stop:
        stop_event.set()
        return jsonify({"status": "success", "message": "Music mode stopped"})
    
    stop_event.clear()
    selected_devices = [d for d in devices if all_devices or d.get('name') in devices_names]
    if not selected_devices:
        return jsonify({"status": "error", "message": "No matching devices found"}), 404
    
    minf = 10
    maxf = 20000
    step = (maxf - minf) // len(selected_devices)
    frequency_ranges = [(minf + i * step, minf + (i + 1) * step) for i in range(len(selected_devices))]
    
    asyncio.create_task(audio_reader())

    tasks = []
    for device, freq_range in zip(selected_devices, frequency_ranges):
        task = asyncio.create_task(audio_consumer(device, freq_range))
        tasks.append(task)
    
    return jsonify({"status": "success", "message": "Music mode started"})

@app.route('/list', methods=['GET'])
async def device_list():
    await load_devices()
    return jsonify([{ 'name': d.get('name'), 'id': d['id'], 'ip': d['ip'], 'version': d["ver"] } for d in devices])

@app.route('/turn_on', methods=['POST'])
async def turn_on():
    request_data = await request.get_json()
    return await handle_action_over_devices('turn_on', request_data)

@app.route('/turn_off', methods=['POST'])
async def turn_off():
    request_data = await request.get_json()
    return await handle_action_over_devices('turn_off', request_data)

@app.route('/set_mode', methods=['POST'])
async def set_mode():
    request_data = await request.get_json()
    mode = request_data.get('mode')
    return await handle_action_over_devices('set_mode', request_data, mode)

@app.route('/set_brightness', methods=['POST'])
async def set_brightness():
    request_data = await request.get_json()
    brightness = request_data.get('brightness')
    return await handle_action_over_devices('set_brightness', request_data, brightness)

@app.route('/set_temperature', methods=['POST'])
async def set_temperature():
    request_data = await request.get_json()
    temperature = request_data.get('temperature')
    return await handle_action_over_devices('set_colourtemp', request_data, temperature)

@app.route('/set_color', methods=['POST'])
async def set_color():
    request_data = await request.get_json()
    color_input = request_data.get('color')
    r, g, b = Color(color_input).rgb
    rgb = int(255 * r), int(255 * g), int(255 * b)
    return await handle_action_over_devices('set_colour', request_data, *rgb)

@app.route('/music', methods=['POST'])
async def music():
    request_data = await request.get_json()
    return await music_mode(request_data)

def main():
    asyncio.run(load_devices())
    logging.info("Daemon started")
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == '__main__':
    main()
