#!/usr/bin/env python3
"""
module for filtering loggers
"""

import re

def filter_datum(fields, redaction, message, separator):
    pattern = '|'.join(map(re.escape, fields))
    return re.sub(rf'({pattern})=[^{separator}]+', rf'\1={redaction}', message)


