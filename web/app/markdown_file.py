from markdown import markdown

def convert(md_file):
    config = {
        'toc': {
            'permalink': '',
            'permalink_class': 'anchor',
            'title': 'Table of Contents',
            'toc_depth': '3'
        }
    }
    TOC = "<div markdown='1' id='toc-holder'>[TOC]</div>"
    md_content = markdown(TOC + md_file.read_text(),
        extensions=[
            'extra',
            'codehilite',
            'mdx_truly_sane_lists', # 'sane_lists',
            'pymdownx.tasklist',
            'toc'
        ],
        extension_configs=config
    )
    return md_content

