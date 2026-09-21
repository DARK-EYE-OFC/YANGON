class Owner:
    name = "owner"
    aliases = ["creator"]

    @staticmethod
    def execute(ctx):
        config = ctx["config"]
        text = (
            f"👑 *OWNER*\n\n"
            f"Name: {config.owner_name}\n"
            f"Number: +{config.owner_number}"
        )
        ctx["client"].reply_message(text, ctx["event"])


command = Owner()
