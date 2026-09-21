class Alive:
    name = "alive"
    aliases = ["online"]

    @staticmethod
    def execute(ctx):
        config = ctx["config"]
        text = (
            f"╭───❒ *{config.bot_name}* ❒───╮\n"
            f"│ 🟢 Bot is online\n"
            f"│ 📦 Version: {config.version}\n"
            f"│ ⚙️ Mode: {config.mode}\n"
            f"╰────────────────────❒\n\n"
            f"{config.watermark}"
        )
        ctx["client"].reply_message(text, ctx["event"])


command = Alive()
