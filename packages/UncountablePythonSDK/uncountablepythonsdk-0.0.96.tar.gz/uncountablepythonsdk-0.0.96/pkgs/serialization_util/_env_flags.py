import os

USE_FASTJSON: bool = os.environ.get("USE_FASTJSON", "false").lower() == "true"
