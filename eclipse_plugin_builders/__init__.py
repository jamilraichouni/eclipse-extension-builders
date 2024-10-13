"""The eclipse_plugin_builders package."""

from importlib import metadata

try:
    __version__ = metadata.version("eclipse_plugin_builders")
except metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0+unknown"
del metadata
