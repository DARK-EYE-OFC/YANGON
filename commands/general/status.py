import platform
import sys


class Status:
    name = "status"
    aliases = ["info"]

    @staticmethod
    def execute(ctx):
        config = ctx["config"]

        text = (
            f"╭───❒ *{config.bot_name} STATUS* ❒───╮\n"
            f"│ 🟢 Status: Online\n"
            f"│ 📦 Version: {config.version}\n"
            f"│ 🐍 Python: {platform.python_version()}\n"
            f"│ 💻 Platform: {platform.system()}\n"
            f"│ ⚙️ Mode: {config.mode}\n"
            f"╰──────────────────────────❒"
        )

        ctx["client"].reply_message(text, ctx["event"])


command = Status()
