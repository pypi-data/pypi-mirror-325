# ANSI escape codes for colors (most terminals support these)
_COLOR_CODES = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'black': '\033[30m',  # Regular black, not bright black
    'reset': '\033[0m',
}

def _colorize(text, color_name):
    """Applies a color to the text using ANSI escape codes."""
    if color_name not in _COLOR_CODES:
        raise ValueError(f"Invalid color name: {color_name}")
    return f"{_COLOR_CODES[color_name]}{text}{_COLOR_CODES['reset']}"

def to_red(text):
    return _colorize(text, 'red')

def to_green(text):
    return _colorize(text, 'green')

def to_blue(text):
    return _colorize(text, 'blue')

def to_yellow(text):
    return _colorize(text, 'yellow')

def to_cyan(text):
    return _colorize(text, 'cyan')

def to_magenta(text):
    return _colorize(text, 'magenta')

def to_white(text):
    return _colorize(text, 'white')

def to_black(text):
    return _colorize(text, 'black')

# Add more color functions as needed!
