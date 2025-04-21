import re

def validate_phone(number):
    # ایران: 912XXXXXXX, یعنی ده رقمی بدون +98
    return bool(re.fullmatch(r"9\d{9}", number))

def validate_config(config):
    if not isinstance(config, dict):
        return False
    for k, v in config.items():
        if not hasattr(v, 'send'):
            return False
    return True
