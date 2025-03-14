"""Pagefind search component for Sphinx.."""

import subprocess
from typing import Optional

from pagefind_bin import get_candidate_paths  # type: ignore[import-untyped]
from sphinx.application import Sphinx

__version__ = "0.0.0"


def create_all_index(app: Sphinx, exc: Optional[Exception]):
    """Create index of pagefind.

    This uses generated html, therefore run after build.
    """
    bin = [p for p in get_candidate_paths() if p.exists()]
    cmd = [
        str(bin[0]),
        "--silent",
        "--site",
        str(app.outdir),
        "--root-selector",
        ".body",
    ]
    subprocess.run(cmd)


def setup(app: Sphinx):  # noqa: D103
    app.connect("build-finished", create_all_index)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
