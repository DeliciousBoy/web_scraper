from pathlib import Path
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

PROJ_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJ_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

logger.info(f"PROJ_ROOT path is: {PROJ_DIR}")


try:
    from tqdm import tqdm
    logger.remove(0)
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    pass
