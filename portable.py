"""
Methods to facilitate portability across platforms, architectures, and
build systems.
"""
import os


def fs_path(path):
    """
    Returns a usable filesystem path to `path`, accounting for packers
    and relocation.
    """
    # PyInstaller's one-file (--one-file) mode expands into a temporary
    # directory on first run. It copies data files into this new directory
    # and sets the path in _MEIPASS2. This is not required for py2app
    # or py2exe.
    return os.path.join(
        os.environ.get("_MEIPASS2", os.path.abspath(".")),
        path
    )
