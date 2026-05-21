# -\*- coding: utf-8 -\*-

from __future__ import unicode_literals
import sys, os

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

sys.path.append(os.path.abspath(os.pardir))

__version__ = '1.0'

# -- General configuration -----------------------------------------------------

source_suffix = '.rst'
master_doc = 'index'
project = 'neusauber'
copyright = '2016, Neusauber.com'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

extlinks = {}

# -- Options for HTML output ---------------------------------------------------

html_theme = 'default'

html_static_path = ['static']

def setup(app):
    # overrides for wide tables in RTD theme
    app.add_css_file('theme_overrides.css') # path relative to static

"""
  You might want to uncomment the “latex_documents = []” if you use CKJ characters in your document.
  Because the pdflatex raises exception when generate Latex documents with CKJ characters.
"""
latex_documents = []

html_show_sourcelink = False
html_copy_source = False

html_theme_options = {
    'collapse_navigation': False,  # 關鍵：不要折疊導覽列，這會讓所有子網頁連結直接展開顯示
    'sticky_navigation': True,    # 滾動時導覽列固定
    'navigation_depth': 1,        # 導覽列顯示的深度
    'includehidden': True,        # 關鍵：即使 toctree 設定了 :hidden:，也強制在左側欄顯示
    'titles_only': True          # 關鍵：只顯示網頁標題（Products、Demo），而不顯示網頁內部的次標題
}

html_sidebars = {
    '**': [
        'globaltoc.html',   # 強制所有頁面（包括首頁）都使用全域目錄，顯示所有子網頁連結
        'searchbox.html'    # 保留搜尋框
    ]
}
