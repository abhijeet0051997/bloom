from typing import List

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config(".env")
PROJECT_NAME: str = config("PROJECT_NAME", default="Bloom")
VERSION = "0.0.1"
DEBUG: str = config("DEBUG", cast=bool, default=True)
ALLOWED_HOSTS: List[str] = config("ALLOWED_HOSTS", cast=CommaSeparatedStrings, default="*")
