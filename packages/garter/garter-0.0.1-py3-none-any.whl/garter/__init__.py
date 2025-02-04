"""
garter.__init__

Initialization script for the Garter package and its core dependencies.
"""
import os
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, TypeVar, Union

from dotenv import load_dotenv

# Get environment variables
try:
    load_dotenv()
except Exception as e:
    print(e)


@dataclass
class Constants(Enum):
    """
    Constants

    Package-level constants.
    """
    DATA_DIR = os.getenv("GARTER_DATA_DIR") or Path("~/Garter").expanduser()
    IMAGES_DIR = os.getenv("GARTER_IMAGES_DIR") or Path("~/Garter/Images").expanduser()
    try:
        # Ensure data directories exist
        if not Path(DATA_DIR).exists():
            Path(DATA_DIR).mkdir(parents=True, exist_ok=True)

        if not Path(IMAGES_DIR).exists():
            Path(IMAGES_DIR).mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(e)


# Export package-level constants
DATA_DIR = Constants.DATA_DIR
IMAGES_DIR = Constants.IMAGES_DIR

