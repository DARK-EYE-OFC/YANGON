import time

START_TIME = time.time()


def runtime():
    seconds = int(time.time() - START_TIME)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    parts = []
    if days:
        parts.append(f"{days}d")
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    parts.append(f"{seconds}s")

    return " ".join(parts)


class Runtime:
    name = "runtime"
    aliases = ["uptime"]

    @staticmethod
    def execute(ctx):
        ctx["client"].reply_message(
            f"⏱️ *YANGON Runtime*\n\n{runtime()}",
            ctx["event"],
        )


command = Runtime()
