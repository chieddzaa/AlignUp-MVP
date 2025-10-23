"""
AlignUp App Package
-------------------
This file marks `alignup_app` as a Python package.

It also initializes shared resources like logging and versioning,
so that every module (services, models, etc.) uses consistent settings.
"""

import logging

# ----------------------------------------------------------------------
# Package Metadata
# ----------------------------------------------------------------------
__appname__ = "AlignUp"
__version__ = "1.0.0"
__author__ = "Natasha Matare"
__email__ = "chiedzanatasha26@gmail.com"

# ----------------------------------------------------------------------
# Logging Configuration
# ----------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger(__appname__)

# Example: logger.info("AlignUp package initialized successfully.")
