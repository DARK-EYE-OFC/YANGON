class Menu:
    name = "menu"
    aliases = ["help", "commands"]

    @staticmethod
    def execute(ctx):
        config = ctx["config"]
        p = config.prefix

        text = (
            f"╭───❒ *{config.bot_name} MENU* ❒───╮\n"
            f"│\n"
            f"│ *GENERAL*\n"
            f"│ {p}ping\n"
            f"│ {p}alive\n"
            f"│ {p}status\n"
            f"│ {p}runtime\n"
            f"│ {p}owner\n"
            f"│ {p}menu\n"
            f"│\n"
            f"│ *YANGON v{config.version}*\n"
            f"╰──────────────────────────❒\n\n"
            f"{config.watermark}"
        )

        ctx["client"].reply_message(text, ctx["event"])


command = Menu()
