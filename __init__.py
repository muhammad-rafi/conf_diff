import importlib.metadata

try:
    __author__ = """Muhammad Rafi"""
    __version__ = importlib.metadata.version(__package__ or __name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.6.1"
