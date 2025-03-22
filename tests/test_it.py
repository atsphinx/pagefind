"""Standard tests."""

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html")
def test__it(app: SphinxTestApp):
    """Test to pass."""
    app.build()
    assert (app.outdir / "_pagefind").exists()
    assert not (app.outdir / "searchindex.js").exists()
    soup = BeautifulSoup((app.outdir / "search.html").read_text(), "html.parser")
    assert [
        e
        for e in soup.find_all("script")
        if "src" in e.attrs and e["src"].startswith("_pagefind")  # type: ignore[index,union-attr]
    ]
    assert [
        e
        for e in soup.find_all("link")
        if "href" in e.attrs and e["href"].startswith("_pagefind")  # type: ignore[index,union-attr]
    ]
