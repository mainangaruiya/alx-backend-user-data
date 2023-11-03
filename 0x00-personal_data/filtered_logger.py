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
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    extract, replace = patterns["extract"], patterns["replace"]
    return re.sub(extract(fields, separator), replace(redaction), message)
