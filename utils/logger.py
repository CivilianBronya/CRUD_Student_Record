import logging
import os

LOG_DIR = "logs"
LOG_FILE = "logs/app.log"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

def log_action(message: str):
    logging.info(message)

