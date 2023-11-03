#!/usr/bin/env python3
"""A module for log filtering
"""

import re
import os
import logging
from typing import List

patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str) -> str:
    extract, replace = patterns["extract"], patterns["replace"]
    return re.sub(extract(fields, separator), replace(redaction), message)
def get_logger() -> logging.Logger:
    """new logger for user data.
    """
    logger = logging.getLogger("user_data")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.setLevel(logging.INFO)
    logger.Propagate = False
    logger.addHandler(stream_handler)
    return logger