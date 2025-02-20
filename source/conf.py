# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'NI Linux RT Security Documentation With SNAC Configuration'
author = r'Emerson T\&M'
copyright = f'2024-%Y, {author}'
version = '1.1'
release = version  # release does not need a patch number for documentation
nist_rev = '3'  # NIST 800-171 Revision number

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []
primary_domain = None
source_encoding = 'utf-8'

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['media']

# -- Options for LaTeX/PDF output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-pdf-output
latex_engine = 'xelatex'

latex_documents = [
    ('index', 'SNAC.tex', project, author, 'manual', False),
]

# Needed so file is copied to build location
latex_logo = 'media/logo.png'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    # \setcounter{secnumdepth}{0} Disables section numbering
    'preamble': r'''
        \usepackage{scalefnt }
        \setlength{\headheight}{14.5pt}
        \setcounter{secnumdepth}{0}
    ''',

    # Custom title page
    'maketitle': r'''
        \begin{titlepage}
            \centering
            \vspace*{2cm}
            {\Huge \textbf{%s}\par}
            \vspace{1.5cm}
            {\Large \textbf{Based on NIST 800-171 Rev%s}\par}
            \vspace{1.5cm}
            {\Large \textbf{%s}\par}
            \vspace{1.5cm}
            {\Large Release: %s\par}
            \vfill
            {\Large \today\par}
            \vspace*{2cm}
            \includegraphics[width=0.25\textwidth]{logo.png}
        \end{titlepage}
    ''' % (project, nist_rev, author, release)
}
