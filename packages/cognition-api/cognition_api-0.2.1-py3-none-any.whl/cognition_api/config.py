from pydantic import BaseSettings
from pathlib import Path
import yaml


class Settings(BaseSettings):
    def __init__(self):
        super().__init__()
        config_path = Path(__file__).parent / "api.yaml"
        with open(config_path) as f:
            self.__dict__.update(yaml.safe_load(f))
