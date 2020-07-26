import configparser
from os import path, remove
from pathlib import Path

from utils.conf import check_if_arch_linux


def create_default_config(clean: bool = False) -> bool:
    base_config_path = f"{str(Path.home())}/.config/paur"
    if not path.exists(base_config_path):
        Path(base_config_path).mkdir(mode=0o777, parents=True, exist_ok=False)
    config_path = f"{base_config_path}/config.ini"
    if path.exists(base_config_path):
        if not clean:
            raise Exception(
                "Config already exist! To reset config run paur init clean "
            )
        remove(config_path)
    config = configparser.ConfigParser()
    config["configs"] = {
        "path_to_db": f"{base_config_path}/paur.db",
        "is_arch": str(check_if_arch_linux()),
        "enable_logging": "False",
        "log_in_file": "False",
        "path_to_log_file": f"{base_config_path}/log.txt",
    }
    with open(config_path, "w") as configfile:
        config.write(configfile)
    return True
