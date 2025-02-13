# -*- coding: utf-8 -*-

import espm

extensions = [
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.inheritance_diagram',
    'nbsphinx',
    'sphinx_gallery.load_style',
    'IPython.sphinxext.ipython_console_highlighting',
]

extensions.append('sphinx.ext.autodoc')
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'member-order': 'groupwise',  # alphabetical, groupwise, bysource
}

extensions.append('sphinx.ext.intersphinx')
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
    'matplotlib': ('https://matplotlib.org/stable', None),
    'hyperspy': ('https://hyperspy.readthedocs.io/en/stable', None),
}

extensions.append('numpydoc')
numpydoc_show_class_members = False
numpydoc_use_plots = True  # Add the plot directive whenever mpl is imported.

extensions.append('matplotlib.sphinxext.plot_directive')
plot_include_source = True
plot_html_show_source_link = False
plot_html_show_formats = False
plot_working_directory = '.'
plot_rcparams = {
    'figure.figsize': (10, 4)
}
plot_pre_code = """
import numpy as np
import matplotlib.pyplot as plt
import espm
import hyperspy.api as hs
"""


extensions.append('sphinx_copybutton')
copybutton_prompt_text = ">>> "

extensions.append('sphinxcontrib.bibtex')
bibtex_bibfiles = ['references.bib']

exclude_patterns = ['_build']
source_suffix = '.rst'
master_doc = 'index'

project = 'espm'
version = espm.__version__
release = espm.__version__
copyright = 'Adrien Teurtrie and Nathanael Perraudin'

pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 2,
}
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
}
latex_documents = [
    ('index', 'espm.tex', 'espm documentation',
     'Adrien Teurtrie and Nathanael Perraudin', 'manual'),
]
