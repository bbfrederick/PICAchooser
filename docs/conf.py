# Configuration file for the Sphinx documentation builder.
# -*- coding: utf-8 -*-
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime
from distutils.version import LooseVersion

import sphinx
from m2r import MdInclude

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("sphinxext"))
sys.path.insert(0, os.path.abspath("../picachooser"))
from github_link import make_linkcode_resolve

# -- Project information -----------------------------------------------------

project = "picachooser"
copyright = "2021, Blaise Frederick"
author = "Blaise Frederick"

# The master toctree document.
master_doc = "index"

# The suffix(es) of source filenames.
source_suffix = ".rst"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",  # standard
    "sphinx.ext.autosummary",  # standard
    "sphinx.ext.coverage",  # collect doc coverage stats
    "sphinx.ext.doctest",  # runs doctests
    "sphinx.ext.ifconfig",  # includes content based on configuration
    "sphinx.ext.intersphinx",  # links code to other packages
    "sphinx.ext.linkcode",  # links to code from api
    "sphinx.ext.napoleon",  # alternative to numpydoc
    "sphinx.ext.todo",  # support for todo items
    "sphinx_gallery.gen_gallery",  # example gallery
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# -----------------------------------------------------------------------------
# sphinx.ext.autosummary settings
# -----------------------------------------------------------------------------
# generate autosummary even if no references
autosummary_generate = True

# -----------------------------------------------------------------------------
# sphinx.ext.todo settings
# -----------------------------------------------------------------------------
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -----------------------------------------------------------------------------
# sphinx.ext.napoleon settings
# -----------------------------------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = False
napoleon_use_keyword = True
napoleon_use_rtype = False

# -----------------------------------------------------------------------------
# LaTeX output
# -----------------------------------------------------------------------------
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
#latex_documents = [
#    (
#        master_doc,
#        "picachooser.tex",
#        "picachooser Documentation",
#        "Blaise Frederick",
#        "manual",
#    ),
#]

# -----------------------------------------------------------------------------
# Manual page output
# -----------------------------------------------------------------------------
# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "picachooser", "picachooser Documentation", [author], 1)]

# -----------------------------------------------------------------------------
# Texinfo output
# -----------------------------------------------------------------------------
# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "picachooser",
        "picachooser Documentation",
        author,
        "picachooser",
        "A set of GUI tools for examining and comparing independent component files.",
        "Miscellaneous",
    ),
]

#------------------------------------------------------------------------------
# PDF output
#------------------------------------------------------------------------------
extensions += ['rst2pdf.pdfbuilder']
pdf_documents = [
    (
        'index',
         u'rst2pdf',
         u'picachooser doc',
         u'Blaise Frederick',
    ),
]

# -----------------------------------------------------------------------------
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -----------------------------------------------------------------------------
# HTMLHelp output
# -----------------------------------------------------------------------------
# Output file base name for HTML help builder.
htmlhelp_basename = "picachooserdoc"

# The following is used by sphinx.ext.linkcode to provide links to github
linkcode_resolve = make_linkcode_resolve(
    "picachooser",
    "https://github.com/bbfrederick/" "picachooser/blob/{revision}/" "{package}/{path}#L{lineno}",
)

# -----------------------------------------------------------------------------
# Setup functions
# -----------------------------------------------------------------------------


# https://github.com/rtfd/sphinx_rtd_theme/issues/117
def setup(app):
    app.add_css_file("theme_overrides.css")
    app.connect("autodoc-process-docstring", generate_example_rst)
    # Fix to https://github.com/sphinx-doc/sphinx/issues/7420
    # from https://github.com/life4/deal/commit/7f33cbc595ed31519cefdfaaf6f415dada5acd94
    # from m2r to make `mdinclude` work
    app.add_config_value("no_underscore_emphasis", False, "env")
    app.add_config_value("m2r_parse_relative_links", False, "env")
    app.add_config_value("m2r_anonymous_references", False, "env")
    app.add_config_value("m2r_disable_inline_math", False, "env")
    app.add_directive("mdinclude", MdInclude)


def generate_example_rst(app, what, name, obj, options, lines):
    # generate empty examples files, so that we don't get
    # inclusion errors if there are no examples for a class / module
    folder = os.path.join(app.srcdir, "generated")
    if not os.path.isdir(folder):
        os.makedirs(folder)
    examples_path = os.path.join(app.srcdir, "generated", "%s.examples" % name)
    if not os.path.exists(examples_path):
        # touch file
        open(examples_path, "w").close()
