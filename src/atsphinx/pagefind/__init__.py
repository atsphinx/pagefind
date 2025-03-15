"""Pagefind search component for Sphinx.."""

import subprocess
from typing import Optional

from pagefind_bin import get_executable  # type: ignore[import-untyped]
from sphinx.application import Sphinx

__version__ = "0.0.0"


def create_all_index(app: Sphinx, exc: Optional[Exception]):
    """Create index of pagefind.

    This uses generated html, therefore run after build.
    """
    try:
        bin = get_executable()
    except FileNotFoundError:
        raise
    cmd = [
        # NOTE: Currentry, works for default theme.
        str(bin),
        "--silent",
        "--site",
        str(app.outdir),
        "--root-selector",
        app.config.pagefind_root_selector,
    ]
    subprocess.run(cmd)


def setup(app: Sphinx):  # noqa: D103
    app.connect("build-finished", create_all_index)
    app.add_config_value("pagefind_root_selector", ".body", "html", str)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
