import importlib
from pathlib import Path

from phringe.core.base_entity import BaseEntity
from phringe.io.utils import load_config


class Configuration(BaseEntity):
    path: str = None
    config_dict: dict = None

    def __init__(self, path):
        super().__init__()
        self.config_dict = load_config(path)

    def load_config(path: Path):
        spec = importlib.util.spec_from_file_location("config", path)
        config_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config_module)
        return config_module.config
