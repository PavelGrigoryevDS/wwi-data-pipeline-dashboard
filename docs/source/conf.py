# Configuration file for the Sphinx documentation builder.
from datetime import datetime

# -- Project information -----------------------------------------------------
project = "wwi-data-pipeline-dashboard"
copyright = f"{datetime.now().year}, Pavel Grigoryev"
author = "Pavel Grigoryev"
language = "en"
# -- General configuration ---------------------------------------------------
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "myst-markdown",
    ".ipynb": "myst-nb",
}

extensions = [
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx.ext.intersphinx",
]

# MyST-NB configuration for Jupyter notebooks
nb_execution_mode = "off"
nb_execution_timeout = -1
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
]


templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
    "_pre_run.ipynb",
    "_post_run.ipynb",
]

html_sidebars = {}

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_title = "#🌐 WWI Data Pipeline and Dashboard"
html_short_title = "#🌐 WWI Data Pipeline and Dashboard"
# Theme options

html_theme_options = {
    "use_edit_page_button": False,
    "show_navbar_depth": 2,
    "show_toc_level": 2,
    "home_page_in_toc": True,
    "use_fullscreen_button": True,
    "use_download_button": True,
    "use_repository_button": True,
    "path_to_docs": "",
    "repository_url": "https://github.com/PavelGrigoryevDS/wwi-data-pipeline-dashboard",
    "logo": {
        "image_light": "_static/logo-light.jpg",
        "image_dark": "_static/logo-dark.jpg",
    },
    "toc_title": "On this page",
    "pygments_light_style": "tango",
    "pygments_dark_style": "monokai",
}


def setup(app):
    app.add_css_file("custom.css")
    app.add_js_file("custom.js")
