import pathlib

from flask import send_from_directory
from flask import render_template

from app import app
from app.markdown_file import convert

MARKDOWN_PATH = pathlib.Path(app.root_path, '../../markdown')
STATIC_PATH = pathlib.Path(app.root_path, 'static')
CUSTOM_CSS = (MARKDOWN_PATH / 'custom.css').is_file()
CUSTOM_JS = (MARKDOWN_PATH / 'custom.js').is_file()
MATHJAX_CONFIG = (MARKDOWN_PATH / 'mathjax.config.js').is_file()

@app.route('/')
@app.route('/index')
def index():
    return index_page('')


@app.route('/favicon.ico')
def favicon():
    file = MARKDOWN_PATH / 'favicon.ico'
    path = MARKDOWN_PATH if file.exists() else STATIC_PATH
    return send_from_directory(path,
                              'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/<path:url>')
def other_files(url):
    if url.endswith('/'):
        return index_page(url)
    return send_from_directory(MARKDOWN_PATH, url)


@app.route('/<path:url>.md')
def markdown_file(url):
    md_file = MARKDOWN_PATH / (url + ".md")
    if not md_file.is_file():
        return "markdown file: '" + str(md_file) + "' not exist. "

    md_content = convert(md_file)
    template = 'markdown-page.html';
    kwargs = {
        'markdown_content': md_content,
        'custom_css': CUSTOM_CSS,
        'custom_js': CUSTOM_JS,
        'mathjax_config': MATHJAX_CONFIG
    }
    return render_template(template, **kwargs)


def index_page(url):
    path = MARKDOWN_PATH / url
    if not path.is_dir():
        return "Directory [/" + url + "] not exist."

    dirs = url[:-1].split('/')
    crumbs = []
    for i, item in enumerate(dirs):
        crumbs.append((item, '/'.join(dirs[:i+1])))

    template = 'markdown-index.html';
    kwargs = {
        'path': path,
        'crumbs': crumbs
    }
    return render_template(template, **kwargs)

