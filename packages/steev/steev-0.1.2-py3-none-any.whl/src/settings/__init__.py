import os
from importlib import import_module
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR.parent / ".env")


def _get_environment():
    env = os.environ.get("STEEV_ENV", "prod")

    # local 설정 파일이 없으면 prod로 폴백
    if env == "dev":
        local_settings = Path(__file__).parent / "dev.py"
        if not local_settings.exists():
            env = "prod"

    return env


env = _get_environment()

settings_module = import_module(f"src.settings.{env}")

BASE_URL = settings_module.BASE_URL
API_BASE_URL = f"https://{BASE_URL}"
WS_BASE_URL = f"wss://{BASE_URL}/ws"

DEBUG = settings_module.DEBUG

LOCAL_DIR = Path.home() / ".steev"
CREDENTIALS_FILE = LOCAL_DIR / "credentials.json"
CACHE_FILE = LOCAL_DIR / ".cache"
