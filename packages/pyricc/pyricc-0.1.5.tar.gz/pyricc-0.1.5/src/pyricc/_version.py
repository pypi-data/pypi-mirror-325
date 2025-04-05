import importlib.resources

try:
    with importlib.resources.files("pyricc").joinpath("VERSION.txt").open() as f:
        __version__ = f.read().strip()
except FileNotFoundError:
    __version__ = "0.99.43.not_found"  # Fallback version
