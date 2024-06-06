try:
    from {{ cookiecutter.package_name }}._version import version as __version__
except ImportError:  # pragma: nocover
    __version__ = "unknown"
