# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Script to anaylze disk usage and report to computer manger.

"""

import tornado
import json
import logging
import subprocess
from decimal import Decimal
from enum import Enum
from pathlib import Path
from typing import Any, Optional, Union

from qbraid_core import QbraidException, QbraidSession

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)


class Unit(str, Enum):
    """Enum to represent the units of disk usage."""

    @tornado.web.authenticated
    def get(self):
        """Get user's qBraid credentials."""
        try:
            usage = get_disk_usage_gb()
            self.finish(json.dumps(usage))
        except e:
            logger.error("Error getting disk usage: %s", e)
            self.set_status(500)
            self.finish(json.dumps({"error": "Error getting disk usage"}))

    KB = "KB"
    MB = "MB"
    GB = "GB"

    @classmethod
    def from_str(cls, unit: str) -> "Unit":
        """Create a Unit from a string."""
        try:
            return cls(unit.upper())
        except ValueError as e:
            raise ValueError(f"Invalid unit: {unit}") from e


CONVERSION_FACTORS = {
    Unit.KB: Decimal("1000000"),
    Unit.MB: Decimal("1000"),
    Unit.GB: Decimal("1"),
}


def convert_to_gb(size: Decimal, unit: Unit) -> Decimal:
    """
    Converts a size in a given unit to GB.

    Args:
        size (Decimal): The size value to convert.
        unit (Unit): The unit of the size.

    Returns:
        Decimal: The size in GB.

    Raises:
        ValueError: If the unit is not recognized.
    """
    if unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unknown unit: {unit}")
    return size / CONVERSION_FACTORS[unit]


def get_disk_usage_gb(filepath: Optional[Union[str, Path]] = None) -> Decimal:
    """
    Get the disk usage of a file or directory in GB.

    Args:
        filepath (Optional[Union[str, Path]]): The file or directory path to measure.

    Returns:
        Decimal: The disk usage in GB.

    Raises:
        RuntimeError: If there are errors executing or parsing the command output.
        FileNotFoundError: If the file or directory does not exist.
    """
    try:
        command = ["gdu", "-p", "-n", "-s", "--si"]

        if filepath:
            filepath = Path(filepath)
            if not filepath.exists():
                raise FileNotFoundError(f"File or directory does not exist: {filepath}")

            command.append(str(filepath))

        result = subprocess.run(command, capture_output=True, text=True, check=True)

        value, unit_str = result.stdout.strip().split()[:2]

        unit = Unit.from_str(unit_str)

        gb = convert_to_gb(Decimal(value), unit)

        gb_rounded = gb.quantize(Decimal("0.01"))

        return gb_rounded
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error executing gdu: {e}") from e
    except (ValueError, IndexError) as e:
        raise RuntimeError(f"Error processing gdu output: {e}") from e

# du -h .