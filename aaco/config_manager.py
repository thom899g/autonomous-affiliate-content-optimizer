"""
 Configuration Management Module for AACO
 Manages configuration parameters and settings.
"""

from typing import Dict, Any
import logging
import yaml
from pathlib import Path

logger = logging.getLogger(__name__)

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Loads configuration from a YAML file.
    Args:
        config_path: Path to the