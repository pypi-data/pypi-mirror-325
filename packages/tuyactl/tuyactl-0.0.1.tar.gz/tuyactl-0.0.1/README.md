# tuyactl - A CLI tool for managing Tuya devices

## Please note this is just a experimental and unstable project.

So far the daemon and client program controls rgb light bulbs using [tinytuya](https://github.com/jasonacox/tinytuya) library,
which involves some previous setup follow the tutorial [here](https://github.com/jasonacox/tinytuya#setup-wizard---getting-local-keys).
Once you generated your `snapshot.json` place it in your home directory.
There are ways of configure the snapshot.json location using environment variables (look the head of tuyad script)
