#!/usr/bin/env python
import requests
import json
import sys
import argparse

BASE_URL = 'http://localhost:5000'

def send_command(command, parameters=None):
    url = f'{BASE_URL}/{command}'
    headers = {'Content-type': 'application/json'}
    try:
        if parameters:
            print(f"Sending command: {url} with parameters {parameters}")
            response = requests.post(url, headers=headers, data=json.dumps(parameters))
        else:
            print(f"Sending command: {url}")
            response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return {"status": "error", "message": str(e)}

def main():
    parser = argparse.ArgumentParser(description='Control Tuya devices.')
    subparsers = parser.add_subparsers(title='commands', dest='command', help='Available commands')

    # Device list command
    device_list_parser = subparsers.add_parser('list', help='List all devices')

    # Turn on command
    on_parser = subparsers.add_parser('on', help='Turn on a device')
    on_parser.add_argument('devices', type=str, nargs='*', help='Device(s) name(s)')
    on_parser.add_argument('--all',   action='store_true', help='Turn on all devices')

    # Turn off command
    off_parser = subparsers.add_parser('off', help='Turn off a device')
    off_parser.add_argument('devices', type=str, nargs='*', help='Device(s) name(s)')
    off_parser.add_argument('--all',   action='store_true', help='Turn off all devices')

    # Set color command
    color_parser = subparsers.add_parser('color', help='Set the color of a device')
    color_parser.add_argument('color',   type=str, help='Color value')
    color_parser.add_argument('devices', type=str, nargs='*', help='Device(s) name(s)')
    color_parser.add_argument('--all',   action='store_true', help='Set color for all devices')

    # Set brightness command
    brightness_parser = subparsers.add_parser('brightness', help='Set the brightness of a device')
    brightness_parser.add_argument('brightness', type=int, help='Brightness value')
    brightness_parser.add_argument('devices', nargs='*', type=str, help='Device(s) name(s)')
    brightness_parser.add_argument('--all',   action='store_true', help='Set brightness for all devices')

    # Set colour temperature command
    colourtemp_parser = subparsers.add_parser('temperature', help='Set the colour temperature of a device')
    colourtemp_parser.add_argument('temperature', type=int,  help='Colour temperature value')
    colourtemp_parser.add_argument('devices', nargs='*', type=str, help='Device(s) name(s)')
    colourtemp_parser.add_argument('--all',   action='store_true', help='Set colour temperature for all devices')

    # Set mode command
    mode_parser = subparsers.add_parser('mode', help='Set the mode of a device')
    mode_parser.add_argument('mode', type=str, choices=['white', 'colour', 'scene', 'music'], help='Mode value')
    mode_parser.add_argument('devices', nargs='*', type=str, help='Device(s) name(s)')
    mode_parser.add_argument('--all',   action='store_true', help='Set mode for all devices')

    # Music sim command
    music_parser = subparsers.add_parser('music', help='Simulate music mode for a device')
    music_parser.add_argument('devices', nargs='*', type=str, help='Device(s) name(s)')
    music_parser.add_argument('--all',   action='store_true', help='Music mode using all devices')
    music_parser.add_argument('--stop',  action='store_true', help='Stop music mode for selected devices')

    args = parser.parse_args()

    parameters = {}
    endpoint = args.command
    if args.command == 'on':
        endpoint = 'turn_on'
        if args.all:
            parameters["all"] = True
        elif args.devices:
            parameters["devices"] = args.devices
        else:
            print("Error: Device(s) name(s) required when not using --all")
            sys.exit(1)

    elif args.command == 'off':
        endpoint = 'turn_off'
        if args.all:
            parameters["all"] = True
        elif args.devices:
            parameters["devices"] = args.devices
        else:
            print("Error: Device(s) name(s) required when not using --all")
            sys.exit(1)

    elif args.command == 'color':
        endpoint = 'set_color'
        if args.all:
            parameters["all"] = True
        elif args.devices:
            parameters["devices"] = args.devices
        if args.color:
            parameters["color"] = args.color

    elif args.command == 'brightness':
        endpoint = 'set_brightness'
        if args.all:
            parameters["all"] = True
        elif args.devices:
            parameters["devices"] = args.devices
        if args.brightness:
            parameters["brightness"] = args.brightness

    elif args.command == 'temperature':
        endpoint = 'set_temperature'
        if args.all:
            parameters["all"] = True
        elif args.devices:
            parameters["devices"] = args.devices
        if args.temperature:
            parameters["temperature"] = args.temperature

    elif args.command == 'mode':
        endpoint = 'set_mode'
        if args.all:
            parameters["all"] = True
        elif args.devices:
            parameters["devices"] = args.devices
        if args.mode:
            parameters["mode"] = args.mode

    elif args.command == 'music':
        if args.all:
            parameters["all"] = True
        elif args.devices:
            parameters["devices"] = args.devices
        if args.stop:
            parameters["stop"] = args.stop 

    elif endpoint:
        print("Error: Invalid command")

    if endpoint:
        result = send_command(endpoint, parameters if parameters else None)
        if endpoint == 'list':
            for device in result:
                print(device)
            return
        print(json.dumps(result))
        return

    parser.print_help()

if __name__ == '__main__':
    main()
