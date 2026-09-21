import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    bot_name: str = os.getenv("BOT_NAME", "YANGON")
    version: str = os.getenv("BOT_VERSION", "1.0.0")
    owner_name: str = os.getenv("OWNER_NAME", "DARK-EYE OFC DEV")
    owner_number: str = os.getenv("OWNER_NUMBER", "263783546271")
    prefix: str = os.getenv("PREFIX", ".")
    mode: str = os.getenv("MODE", "public")
    watermark: str = os.getenv(
        "WATERMARK",
        "> *♤powered by DARK-EYE OFC DEV*",
    )


config = Config()
