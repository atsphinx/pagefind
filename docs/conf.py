import os

from atsphinx.mini18n import get_template_dir as get_mini18n_template_dir
from atsphinx.pagefind import __version__ as version

# -- Project information
project = "atsphinx-pagefind"
copyright = "2025, Kazuya Takei"
author = "Kazuya Takei"
release = version

# -- General configuration
extensions = [
    # Bundled extensions
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    # Third-party extensions
    "sphinx_toolbox.confval",
    # atsphinx group
    "atsphinx.footnotes",
    "atsphinx.mini18n",
    "atsphinx.pagefind",
]
templates_path = ["_templates", get_mini18n_template_dir()]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for i18n
language = "en"
gettext_compact = False
locale_dirs = ["_locales"]

# -- Options for HTML output
html_theme = "bulma-basic"
html_static_path = ["_static"]
html_title = f"{project} v{release}"
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
    "custom.css",
]
html_theme_options = {
    "color_mode": "light",
    "bulmaswatch": "pulse",
    "logo_description": "This is documentation of atsphinx-pagefind.",
    "sidebar_position": "right",
    "sidebar_size": 3,
    "navbar_icons": [
        {
            "label": "",
            "icon": "fa-brands fa-solid fa-github fa-2x",
            "url": "https://github.com/atsphinx/pagefind",
        },
    ],
}
html_sidebars = {
    "**": [
        "select-lang.html",
        "sidebar/logo.html",
        "sidebar/line.html",
        "sidebar/searchbox.html",
        "sidebar/localtoc.html",
    ]
}

# -- Options for extensions
# sphinx.ext.intersphinx
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}
# sphinx.ext.todo
todo_include_todos = True
# atsphinx.mini18n
mini18n_default_language = "en"
mini18n_support_languages = ["en", "ja"]
mini18n_select_lang_label = "Languages"
mini18n_basepath = os.environ.get("ATSPHINX_MINI18N_BASEPATH", "/")
# atsphinx.pagefind
pagefind_root_selector = "main"
