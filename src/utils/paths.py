from pathlib import Path

# Root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Data folders
DATA_DIR = BASE_DIR / "Data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"