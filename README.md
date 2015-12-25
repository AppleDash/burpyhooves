BuhIRC
================

##### Every other Python IRC bot framework I've found has been slow, badly-written, hard to use, or otherwise unsuitable for my needs. BuhIRC aims to solve that.

BuhIRC runs on Python 3, and has the following dependancies, obtainable through pip:

- `requests`: HTTP library
- `beautifulsoup4`: HTML parsing library
- `lxml`: Fast HTML parser

If you want to run this for some reason, you probably want to copy `doc/buhirc.json.example` and `doc/permissions.json.example` to `etc/buhirc.json` and `etc/permissions.json` and edit them to your liking.
You will then want to run `./buhirc.py`

