try:
    from {{ cookiecutter.package_name }}._version import version as __version__
except ImportError:  # pragma: no cover
    __version__ = "unknown"
