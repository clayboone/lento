"""App instance configuration."""
import dotenv
import os
import sys
from pathlib import Path


def get_data_file_path(relative_path):
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath('.')

    return os.path.join(base, relative_path)


dotenv.load_dotenv(dotenv_path=get_data_file_path('.env'), override=True)  # noqa: E501


class Config:
    TEST_VAR = os.getenv('TEST_VAR')
    MACOS_APPLICATION_FOLDER = Path("/Applications/")
    DRIVE_LETTER = "C:\\"
