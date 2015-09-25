burpyhooves
================

##### This is a rewrite/clone of another IRC bot by the same name from a channel on Canternet. It is, however, slowly morphing into its own generic bot framework.

BurpyHooves runs on Python 3, and has the following dependancies, obtainable through pip:

- `requests`: HTTP library
- `beautifulsoup4`: HTML parsing library
- `lxml`: Fast HTML parser

If you want to run this for some reason, you probably want to copy `doc/burpyhooves.json.example` and `doc/permissions.json.example` to `etc/burpyhooves.json` and `etc/permissions.json` and edit them to your liking.
You will then want to run `python3 burpyhooves.py`
