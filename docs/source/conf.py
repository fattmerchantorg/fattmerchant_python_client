# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import guzzle_sphinx_theme

print(os.path.abspath(__file__))

sys.path.insert(0, os.path.abspath("../../"))
sys.path.insert(0, os.path.abspath("../../../../"))

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = "guzzle_sphinx_theme"
pygments_style = "sphinx"

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the sidebar
    "project_nav_name": "fattmerchant client"
}
# -- Project information -----------------------------------------------------

project = "fattmerchant"
copyright = "2019, Austin Burns"
author = "Austin Burns"

# The full version, including alpha/beta/rc tags
release = "1.1.5"

# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc", "sphinx.ext.coverage", "sphinx.ext.napoleon"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The document name of the “master” document, that is, the document that
# contains the root toctree directive.
master_doc = 'index'

# Do not change the member order for classes
autodoc_member_order = 'bysource'

# -- Options for HTML output -------------------------------------------------

    # The theme to use for HTML and HTML Help pages.  See the documentation for
    # a list of builtin themes.
    #

    # Add any paths that contain custom static files (such as style sheets) here,
    # relative to this directory. They are copied after the builtin static files,
    # so a file named "default.css" will overwrite the builtin "default.css".
    # html_static_path = ["_static"]
