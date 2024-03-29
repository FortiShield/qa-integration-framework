"""
Copyright (C) 2024, FortiShield Inc.
Created by FortiShield, Inc. <security@khulnasoft.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
import string
from random import SystemRandom, randint


def get_random_string(string_length: int, digits: bool = True) -> str:
    """Create a random string with specified length.

    Args:
        string_length (int): Random string length.
        digits (boolean): Digits availability for string generation.

    Returns:
        str: Random string.
    """
    character_set = string.ascii_uppercase + string.digits if digits else string.ascii_uppercase

    return ''.join(SystemRandom().choice(character_set) for _ in range(string_length))


def get_random_ip() -> str:
    """Create a random ip address.

    Return:
        str: Random ip address.
    """
    return f"{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}"
