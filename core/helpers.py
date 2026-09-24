import re
import time


def normalize_phone(phone):
    """Remove spaces and symbols from an international phone number."""
    phone = re.sub(r"\D", "", phone)

    if not phone:
        return None

    return phone


def banner(config):
    print()
    print("╭──────────────────────────────╮")
    print(f"│          {config.bot_name:<12}        │")
    print("├──────────────────────────────┤")
    print(f"│ Version: {config.version:<17} │")
    print(f"│ Mode:    {config.mode:<17} │")
    print("╰──────────────────────────────╯")
    print()


def uptime(start_time):
    seconds = int(time.time() - start_time)

    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    return f"{days}d {hours}h {minutes}m {seconds}s"
