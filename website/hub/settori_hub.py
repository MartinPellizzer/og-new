import os
import markdown

from lib import g
from lib import io
from lib import components


def settori_vino():
    with open(f'./articoli/settori/settori-vino.md', encoding='utf-8') as f: markdown_text = f.read()

    article_html = markdown.markdown(markdown_text)
    
    article_title_html = ''
    article_first_paragraph_html = ''
    article_content_html = ''
    for line in article_html.split('\n'):
        if line.strip().startswith('<h1'):
            article_title_html += line
        elif article_first_paragraph_html == '':
            line = line.replace('<p', '<p style="font-size: 1.75rem; line-height: 1.3; color: #202124; margin-bottom: 2rem;"')
            article_first_paragraph_html += line
        else:
            article_content_html += line

    print(article_html)
    # quit()

    html_breadcrumbs = components.breadcrumbs_new('')
    hero_html = f'''
        <section class="article" style="background-color: #000; padding-top: 5rem; padding-bottom: 5rem; margin-bottom: 5rem;">
            <div class="container-xl">
                <div class="m-flex" style="align-items: center; gap: 1rem;">
                    <div style="flex: 2;">
                        {html_breadcrumbs}
                        {article_title_html}
                        <p style="color: #fff;">
                            Maggio 6, 2026 <span>•</span> Staff Tecnico Ozonogroup
                        </p>
                    </div>
                    <div style="flex: 1;">
                    </div>
                </div>
            </div>
        </section>
    '''

    html_article = f'''
        <div class="container-xl">
            <div class="m-flex" style="align-items: center;">
                <div style="flex: 3;" class="article">
                    {article_first_paragraph_html}
                    {article_content_html}
                </div>
                <div style="flex: 1;">
                </div>
            </div>
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
            <title>Tecnologia dell'ozono nei sistemi industriali </title>
            <meta name="description" content="">
        </head>
        <body>
            {components.header_default()}
            <main style="margin-bottom: 5rem;">
                {hero_html}
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
    markdown_text = io.file_read(f'./articoli/settori/settori.md')

    article_html = markdown.markdown(markdown_text)
    article_title_html = ''
    article_content_html = ''
    for line in article_html.split('\n'):
        if line.strip().startswith('<h1'):
            article_title_html += line
        else:
            article_content_html += line

    print(article_html)
    # quit()

    html_breadcrumbs = components.breadcrumbs_new('')
    hero_html = f'''
        <section class="article" style="background-color: #000; padding-top: 5rem; padding-bottom: 5rem; margin-bottom: 5rem;">
            <div class="container-xl">
                <div class="m-flex" style="align-items: center; gap: 1rem;">
                    <div style="flex: 2;">
                        {html_breadcrumbs}
                        {article_title_html}
                        <p style="color: #fff;">
                            Maggio 6, 2026 <span>•</span> Staff Tecnico Ozonogroup
                        </p>
                    </div>
                    <div style="flex: 1;">
                    </div>
                </div>
            </div>
        </section>
    '''

    html_article = f'''
        <div class="container-xl">
            <div class="m-flex" style="align-items: center;">
                <div style="flex: 3;">
                    {article_content_html}
                </div>
                <div style="flex: 1;">
                </div>
            </div>
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
            <title>Tecnologia dell'ozono nei sistemi industriali </title>
            <meta name="description" content="">
        </head>
        <body>
            {components.header_default()}
            <main>
                {hero_html}
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