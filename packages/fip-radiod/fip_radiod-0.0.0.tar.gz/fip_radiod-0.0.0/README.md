# Fip Radiod
A set of helper functions to play FIP on a vintage radio.

For now, only get what music is currently playing.

You need a `.env` file, containing your Radio France API token:
```bash
RADIOFRANCE_API_TOKEN = "<api-token>"
```

## Simple installation
1. Check that you have Python3.10 or more.
2. Create a dedicated environment.
3. `pip install fip_radiod`
## Build from source (developers)
1. Check that you have Python3.10 or more.
2. `git clone git@github.com:AdrienPlacais/fip_radiod.git`
3. Create a virtual env, e.g. with `cd fip_radiod;pip -m venv venv`
4. Install package with `pip install -e .`
