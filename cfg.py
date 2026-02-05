from environs import Env
from loguru import logger

env = Env()
try:
    env.read_env()
except FileNotFoundError:
    logger.debug("NO ENV.")

# Ссылки
URL = env.str("URL", default="")
