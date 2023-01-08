# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'TanukiCraft'
copyright = '2023, Drac, Insert, Tom, Shiro, Jura, Kobe, Kai, Jura\'s foot, Jura foot\'s toe'
author = 'Drac'

release = '0.3a'
version = '0.3.0a'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'furo'

# -- Options for EPUB output
epub_show_urls = 'footnote'
