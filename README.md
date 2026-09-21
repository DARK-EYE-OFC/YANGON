# YANGON v1.0.0

A Python WhatsApp Web bot built around Neonize.

## Requirements

- Python 3.10+
- FFmpeg is recommended when you later add audio/video/sticker features.
- A WhatsApp account for linking.

Neonize supports QR authentication and phone-number link codes, stores sessions persistently, and supports Android/Termux among its documented platforms.

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Termux, if `venv` is unavailable:

```bash
pip install -r requirements.txt
```

## Configure

```bash
cp .env.example .env
```

Edit `.env` and set your owner number.

## QR login

```bash
python main.py
```

A QR code is shown by the Neonize client when there is no saved session.

On WhatsApp:
Settings → Linked Devices → Link a Device

## Phone-number pairing

```bash
python main.py --pair 263783546271
```

Enter the displayed 8-character link code in:

WhatsApp → Settings → Linked Devices → Link a Device → Link with phone number instead

The session is stored in `session/yangon.db`, so later runs can reconnect without pairing again.

## Commands

```text
.ping
.alive
.menu
.owner
.status
.runtime
```

## Important

YANGON uses WhatsApp linked-device automation through Neonize. This is not the official WhatsApp Business Cloud API. Use a WhatsApp account you control and follow WhatsApp's applicable terms and policies.

## Project layout

```text
YANGON/
├── main.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── core/
│   ├── database.py
│   ├── helpers.py
│   └── router.py
├── commands/
│   └── general/
│       ├── alive.py
│       ├── menu.py
│       ├── owner.py
│       ├── ping.py
│       ├── runtime.py
│       └── status.py
├── database/
└── session/
```
