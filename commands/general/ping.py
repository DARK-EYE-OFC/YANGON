class Ping:
    name = "ping"
    aliases = ["p"]

    @staticmethod
    def execute(ctx):
        ctx["client"].reply_message("🏓 Pong!\n\nYANGON v1.0.0", ctx["event"])


command = Ping()
