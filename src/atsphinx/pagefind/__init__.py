"""Pagefind search component for Sphinx.."""

import subprocess
from pathlib import Path
from typing import Any, Optional

from docutils import nodes
from pagefind_bin import get_executable  # type: ignore[import-untyped]
from sphinx.application import Sphinx
from sphinx.config import Config

__version__ = "0.1.2"

root = Path(__file__).resolve().parent


def update_config(app: Sphinx, config: Config):
    """Update configuration values to run pagefind."""
    config.templates_path.insert(0, str(root / "_templates"))
    config.html_static_path.append(str(root / "_static"))


def disable_builtin_search(app: Sphinx):
    """Override builder's property to disable search features."""
    if hasattr(app.builder, "search"):
        app.builder.search = False


def append_search_html(app: Sphinx):
    """Re-append search page.

    This is to create page when builtin search is disabled.
    """
    yield ("search", {}, "search.html")


def configure_page_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Optional[nodes.document],
):
    context["pagefind"] = {
        "directory": app.config.pagefind_directory,
    }


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
        "--output-subdir",
        app.config.pagefind_directory,
        "--force-language",
        app.config.language,
        "--root-selector",
        app.config.pagefind_root_selector,
    ]
    subprocess.run(cmd)


def setup(app: Sphinx):  # noqa: D103
    app.add_config_value("pagefind_directory", "_pagefind", "html", str)
    app.connect("config-inited", update_config)
    app.connect("builder-inited", disable_builtin_search)
    app.connect("build-finished", create_all_index)
    app.connect("html-collect-pages", append_search_html)
    app.connect("html-page-context", configure_page_context)
    app.add_config_value("pagefind_root_selector", ".body", "html", str)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
