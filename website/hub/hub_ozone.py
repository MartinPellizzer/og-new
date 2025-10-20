import os

import markdown

from lib import g
from lib import sections

def gen():
    # reset tmp css
    css = ''
    css_mobile = ''
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1200px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.container-lg'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 992px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.container-md'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 768px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.container-sd'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 576px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.article-h1'
    if class_name not in css:
        css += f'''
            {class_name} {{
                color: #202124;
                font-size: {g.typography_size_xxl};
                line-height: {g.typography_line_height_xxl};
                font-weight: normal;
                margin-top: 48px;
                margin-bottom: 16px;
                text-align: center;
            }}
        '''
    class_name = '.article-h2'
    if class_name not in css:
        css += f'''
            {class_name} {{
                color: #202124;
                font-size: {g.typography_size_xl};
                line-height: {g.typography_line_height_xl};
                font-weight: normal;
                margin-bottom: 16px;
                margin-top: 48px;
            }}
        '''
    class_name = '.article-p'
    if class_name not in css:
        css += f'''
            {class_name} {{
                color: #5f6368;
                margin-bottom: 16px;
                font-size: {g.typography_size_md};
                line-height: {g.typography_line_height_md};
            }}
        '''
    class_name = '.article-ul'
    if class_name not in css:
        css += f'''
            {class_name} {{
                padding-left: 32px;
                margin-bottom: 16px;
            }}
        '''
    class_name = '.article-li'
    if class_name not in css:
        css += f'''
            {class_name} {{
                color: #5f6368;
                margin-bottom: 8px;
                font-size: {g.typography_size_md};
                line-height: {g.typography_line_height_md};
            }}
        '''
    class_name = '.article-img'
    if class_name not in css:
        css += f'''
            {class_name} {{
                width: 100%;
                height: 480px;
                object-fit: cover;
                object-position: center;
                border-radius: 8px;
                margin: 0;
                padding: 0;
                margin-bottom: 16px;
            }}
        '''
    class_name = '.article-date'
    if class_name not in css:
        css += f'''
            {class_name} {{
                color: #5f6368;
                margin-bottom: 8px;
                font-size: {g.typography_size_xs};
                line-height: {g.typography_line_height_xs};
                text-transform: uppercase;
                font-weight: bold;
                text-align: center;
            }}
        '''
    class_name = '.article-author'
    if class_name not in css:
        css += f'''
            {class_name} {{
                color: #5f6368;
                margin-bottom: 32px;
                font-size: {g.typography_size_xs};
                line-height: {g.typography_line_height_xs};
                text-transform: uppercase;
                font-weight: bold;
                text-align: center;
            }}
        '''
    with open('styles/tmp/hub-ozono.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/hub-ozono-mobile.css', 'w') as f: f.write(css_mobile)

    html_article = ''

    with open(f'database/hubs/ozono.txt', encoding='utf-8', errors='ignore') as f: 
        markdown_text = f.read()
    lines = []
    for line in markdown_text.split('\n'):
        line = line.strip()
        line = line.replace('**', '')
        line = line.replace('—', '-')
        line = line.replace('–', '-')
        if line.startswith('## '): 
            line = line.replace('## ', '')
            line = line.capitalize()
            line = f'## {line}'
        if line.startswith('# '): 
            line = line.replace('# ', '')
            line = line.capitalize()
            line = f'# {line}'
        lines.append(line)
    markdown_text = '\n'.join(lines)
    html_article += markdown.markdown(markdown_text)

    html_article = html_article.replace('<p><img', '<p class="container-lg"><img class="article-img"')
    html_article = html_article.replace('<h1', '<h1 class="container-lg article-h1"')
    html_article = html_article.replace('<h2', '<h2 class="container-md article-h2"')
    html_article = html_article.replace('<ul', '<ul class="container-md article-ul"')
    html_article = html_article.replace('<li', '<li class="article-li"')
    html_article = html_article.replace('<p>', '<p class="container-md article-p"">')
    
    html_article = html_article.replace('/h1>', '/h1>\n<p class="container-md article-date">6 October 2025</p>\n<p class="container-sd article-author">Staff Tecnico Ozonogroup</p>')


    html_index = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/style.css">
        </head>
        <body>
            {sections.header_light()}
            <main>
                {html_article}
            </main>
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = 'public/ozono.html'
    with open(html_index_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html_index)

    ### subtopics
    article_slug = f'ozono/sanificazione'
    article_folderpath = '/'.join(article_slug.split('/')[:-1])
    try: os.makedirs(article_folderpath)
    except: pass
    html_article = ''

    with open(f'database/hubs/{article_slug}.txt', encoding='utf-8', errors='ignore') as f: 
        markdown_text = f.read()
    lines = []
    for line in markdown_text.split('\n'):
        line = line.strip()
        line = line.replace('**', '')
        line = line.replace('—', '-')
        line = line.replace('–', '-')
        if line.startswith('## '): 
            line = line.replace('## ', '')
            line = line.capitalize()
            line = f'## {line}'
        if line.startswith('# '): 
            line = line.replace('# ', '')
            line = line.capitalize()
            line = f'# {line}'
        lines.append(line)
    markdown_text = '\n'.join(lines)
    html_article += markdown.markdown(markdown_text)

    html_article = html_article.replace('<p><img', '<p class="container-lg"><img class="article-img"')
    html_article = html_article.replace('<h1', '<h1 class="container-lg article-h1"')
    html_article = html_article.replace('<h2', '<h2 class="container-md article-h2"')
    html_article = html_article.replace('<ul', '<ul class="container-md article-ul"')
    html_article = html_article.replace('<li', '<li class="article-li"')
    html_article = html_article.replace('<p>', '<p class="container-md article-p"">')
    
    html_article = html_article.replace('/h1>', '/h1>\n<p class="container-md article-date">6 October 2025</p>\n<p class="container-sd article-author">Staff Tecnico Ozonogroup</p>')


    html_index = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/style.css">
        </head>
        <body>
            {sections.header_light()}
            <main>
                {html_article}
            </main>
            {sections.spacer_1()}
            {sections.footer_default()}
        </body>
        </html>
    '''
    html_index_filepath = f'public/{article_slug}.html'
    with open(html_index_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html_index)


    article_slug = f'ozono/sanificazione/disinfestazione'
    article_folderpath = '/'.join(article_slug.split('/')[:-1])
    try: os.makedirs(article_folderpath)
    except: pass
    html_article = ''

    with open(f'database/hubs/{article_slug}.txt', encoding='utf-8', errors='ignore') as f: 
        markdown_text = f.read()
    lines = []
    for line in markdown_text.split('\n'):
        line = line.strip()
        line = line.replace('**', '')
        line = line.replace('—', '-')
        line = line.replace('–', '-')
        if line.startswith('## '): 
            line = line.replace('## ', '')
            line = line.capitalize()
            line = f'## {line}'
        if line.startswith('# '): 
            line = line.replace('# ', '')
            line = line.capitalize()
            line = f'# {line}'
        lines.append(line)
    markdown_text = '\n'.join(lines)
    html_article += markdown.markdown(markdown_text)

    html_article = html_article.replace('<p><img', '<p class="container-lg"><img class="article-img"')
    html_article = html_article.replace('<h1', '<h1 class="container-lg article-h1"')
    html_article = html_article.replace('<h2', '<h2 class="container-md article-h2"')
    html_article = html_article.replace('<ul', '<ul class="container-md article-ul"')
    html_article = html_article.replace('<li', '<li class="article-li"')
    html_article = html_article.replace('<p>', '<p class="container-md article-p"">')
    
    html_article = html_article.replace('/h1>', '/h1>\n<p class="container-md article-date">6 October 2025</p>\n<p class="container-sd article-author">Staff Tecnico Ozonogroup</p>')


    html_index = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/style.css">
        </head>
        <body>
            {sections.header_light()}
            <main>
                {html_article}
            </main>
            {sections.spacer_1()}
            {sections.footer_default()}
        </body>
        </html>
    '''
    try: os.makedirs(f'public/{article_folderpath}')
    except: pass
    html_filepath = f'public/{article_slug}.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html_index)

