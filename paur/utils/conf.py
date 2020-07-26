import configparser
from functools import lru_cache
from os import path
from pathlib import Path
from sys import platform
from typing import List


def check_if_arch_linux() -> bool:
    return True if path.exists("/etc/arch-release") and platform == "linux" else False


@lru_cache
def get_user_config() -> List[str]:
    home = str(Path.home())
    config_path = f"{home}/.config/paur/config.ini"
    if not path.exists(config_path):
        raise Exception("Missing config! Run paur init to create default config.")
    config = configparser.ConfigParser()
    return config.read(config_path)
