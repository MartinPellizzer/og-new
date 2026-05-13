
import os
import markdown

from lib import g
from lib import io
from lib import components


def settori_vino():
    with open(f'./articoli/settori/settori-vino.md', encoding='utf-8') as f: markdown_text = f.read()

    article_html = markdown.markdown(markdown_text, extensions=["tables", "fenced_code"])
    html_breadcrumbs = components.breadcrumbs_new('settori/vino')

    title = ''
    for line in markdown_text.split('\n'):
        if line.startswith('# '):
            title = line.replace('# ', '').strip()
            break
    print(title)

    html_article = f'''
        <div class="article container-md" style="margin-top: 5rem;">
            {html_breadcrumbs}
            <p>
                Maggio 6, 2026 <span>•</span> Staff Tecnico Ozonogroup
            </p>
            {article_html}
        </div>
    '''
    html_article = html_article.replace('’', "'")

    html = f'''
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="/styles.css">
            <title>{title}</title>
            <meta name="description" content="">
        </head>
        <body>
            {components.header_default()}
            <main style="margin-bottom: 5rem;">
                {html_article}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''

    html_folderpath = f'{g.WEBSITE_FOLDERPATH}/settori/vino'
    os.makedirs(html_folderpath, exist_ok=True)
    html_filepath = f'{html_folderpath}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)

def settori():
    with open(f'./articoli/settori/settori.md', encoding='utf-8') as f: markdown_text = f.read()

    article_html = markdown.markdown(markdown_text, extensions=["tables", "fenced_code"])
    html_breadcrumbs = components.breadcrumbs_new('settori')

    title = ''
    for line in markdown_text.split('\n'):
        if line.startswith('# '):
            title = line.replace('# ', '').strip()
            break
    print(title)

    html_article = f'''
        <div class="article container-md" style="margin-top: 5rem;">
            {html_breadcrumbs}
            <p>
                Maggio 6, 2026 <span>•</span> Staff Tecnico Ozonogroup
            </p>
            {article_html}
        </div>
    '''
    html_article = html_article.replace('’', "'")

    html = f'''
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="/styles.css">
            <title>{title}</title>
            <meta name="description" content="">
        </head>
        <body>
            {components.header_default()}
            <main style="margin-bottom: 5rem;">
                {html_article}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''

    html_folderpath = f'{g.WEBSITE_FOLDERPATH}/settori'
    os.makedirs(html_folderpath, exist_ok=True)
    html_filepath = f'{html_folderpath}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)

def main():
    settori()
    settori_vino()