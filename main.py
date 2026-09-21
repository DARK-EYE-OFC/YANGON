import argparse
import sys
from pathlib import Path

from neonize.client import NewClient
from neonize.events import ConnectedEv, MessageEv
from neonize.utils.message import extract_text

from config import config
from core.router import Router
from core.database import Database
from core.helpers import banner, normalize_phone


ROOT = Path(__file__).resolve().parent
SESSION_DB = ROOT / "session" / "yangon.db"


def build_client():
    SESSION_DB.parent.mkdir(parents=True, exist_ok=True)
    return NewClient(str(SESSION_DB))


def install_events(client, router):
    @client.event(ConnectedEv)
    def on_connected(client, _):
        print()
        print("╭──────────────────────────────╮")
        print("│        YANGON CONNECTED      │")
        print("├──────────────────────────────┤")
        print(f"│ Version: {config.version:<17} │")
        print(f"│ Mode: {config.mode:<20}│")
        print("╰──────────────────────────────╯")
        print()

    @client.event(MessageEv)
    def on_message(client, event):
        try:
            text = extract_text(event.Message) or ""
            router.handle(client, event, text)
        except Exception as exc:
            print(f"[MESSAGE ERROR] {exc}")


def pair_phone(client, phone):
    from neonize.proto.waCommon_pb2 import ClientName

    phone = normalize_phone(phone)
    if not phone:
        raise ValueError("Enter a valid international phone number, e.g. 263783546271")

    print()
    print("╭──────────────────────────────╮")
    print("│       YANGON PAIRING         │")
    print("├──────────────────────────────┤")
    print(f"│ Number: {phone}")
    print("│ Requesting link code...")
    print("╰──────────────────────────────╯")

    code = client.PairPhone(
        phone,
        show_push_notification=True,
        client_name=ClientName.LINUX,
    )

    print()
    print("╭──────────────────────────────╮")
    print("│      YOUR YANGON CODE        │")
    print("├──────────────────────────────┤")
    print(f"│        {code}")
    print("╰──────────────────────────────╯")
    print()
    print("On WhatsApp:")
    print("Settings → Linked Devices → Link a Device")
    print("→ Link with phone number instead")
    print(f"→ Enter {code}")
    print()


def main():
    parser = argparse.ArgumentParser(description="YANGON WhatsApp Bot")
    parser.add_argument(
        "--pair",
        metavar="PHONE",
        help="Pair a new WhatsApp account using an international phone number",
    )
    args = parser.parse_args()

    banner(config)

    db = Database(ROOT / "database")
    router = Router(config=config, database=db)

    client = build_client()
    install_events(client, router)

    if args.pair:
        pair_phone(client, args.pair)

    print("⏳ Connecting to WhatsApp...")
    try:
        client.connect()
    except KeyboardInterrupt:
        print("\nYANGON stopped.")
    except Exception as exc:
        print(f"[FATAL] WhatsApp connection failed: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
