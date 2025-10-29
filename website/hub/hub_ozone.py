import os

import markdown

from lib import g
from lib import components
from lib import blocks
from lib import sections

def ozono_article_gen(article_url_slug):
    with open('styles/tmp/hub-ozone.css') as f: css = f.read()
    with open('styles/tmp-mobile/hub-ozone-mobile.css') as f: css_mobile = f.read()

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
                margin-top: 4rem;
            }}
        '''
    class_name = '.article-h3'
    if class_name not in css:
        css += f'''
            {class_name} {{
                color: #202124;
                font-size: {g.typography_size_md};
                line-height: {g.typography_line_height_md};
                font-weight: bold;
                margin-bottom: 16px;
                margin-top: 2rem;
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
    class_name = '.article-ol'
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
                margin-bottom: 0.25rem;
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

    with open('styles/tmp/hub-ozone.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/hub-ozone-mobile.css', 'w') as f: f.write(css_mobile)
    
    article_folderpath = '/'.join(article_url_slug.split('/')[:-1])
    try: os.makedirs(article_folderpath)
    except: pass
    html_article = ''

    with open(f'database/hubs/{article_url_slug}.txt', encoding='utf-8', errors='ignore') as f: 
        markdown_text = f.read()
    lines = []
    for line in markdown_text.split('\n'):
        line = line.strip()
        line = line.replace('**', '')
        line = line.replace('—', '-')
        line = line.replace('–', '-')
        if line.startswith('---'): continue 
        if line.startswith('### '): 
            line = line.replace('### ', '')
            line = line.capitalize()
            line = f'### {line}'
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
    html_article = html_article.replace('<h3', '<h3 class="container-md article-h3"')
    html_article = html_article.replace('<ul', '<ul class="container-md article-ul"')
    html_article = html_article.replace('<ol', '<ol class="container-md article-ol"')
    html_article = html_article.replace('<li', '<li class="article-li"')
    html_article = html_article.replace('<p>', '<p class="container-md article-p"">')
    
    html_article = html_article.replace('/h1>', '/h1>\n<p class="container-md article-date">6 October 2025</p>\n<p class="container-sd article-author">Staff Tecnico Ozonogroup</p>')

    breadcrumbs = article_url_slug.split('/')
    breadcrumbs_html = f''
    breadcrumbs_html += f'''<div class="container-xl">'''
    breadcrumbs_html += f'''<a style="color: #5f6368; text-decoration: none; font-size: {g.typography_size_xs};" href="/">HOME</a><span> > </span>'''
    chunk = '/'
    for item in breadcrumbs[:-1]:
        chunk += item
        breadcrumbs_html += f'''<a style="color: #5f6368; text-decoration: none; font-size: {g.typography_size_xs};" href="{chunk}.html">{item.upper()}</a><span> > </span>'''
        chunk += '/'
    breadcrumbs_html += f'''<span style="color: #5f6368; text-decoration: none; font-size: {g.typography_size_xs};">{breadcrumbs[-1].upper()}</span>'''
    breadcrumbs_html += f'''</div>'''

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
            {breadcrumbs_html}
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
    html_filepath = f'public/{article_url_slug}.html'
    print(html_filepath)
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html_index)
    
def ozono_gen():
    html_article = ''
    html_heading = components.h2_default(
        text= f'''Ozono''',
    )
    image_h = '15rem'
    border_radius = '0.5rem'
    border_color = '#cdcdcd'
    card_bg_color = g.color_gray_extralight
    card_bg_color = '#ffffff'
    card_style_h3 = f'''
        style="
            margin-bottom: 1rem; 
            font-weight: normal;
            font-size: {g.typography_size_lg};
        "
    '''
    html_cards = ''
    html_cards += f'''
        <a href="/ozono/chimica.html" style="text-decoration: none; color: #222222;">
            <div style="background-color: {card_bg_color}; border: 1px solid {border_color}; border-radius: {border_radius};">
                <img src='/immagini/home/sanificazione-ozono.png' style="height: {image_h}; object-fit: cover; border-top-left-radius: {border_radius}; border-top-right-radius: {border_radius};">
                <div style="padding: 1rem 2rem;">
                    <h3 {card_style_h3}>Chimica</h3>
                    <p>Articolo sulla chimica dell'ozono.</p>
                </div>
            </div>
        </a>
    '''
    html_cards += f'''
        <a href="/ozono/ambiente.html" style="text-decoration: none; color: #222222;">
            <div style="background-color: {card_bg_color}; border: 1px solid {border_color}; border-radius: {border_radius};">
                <img src='/ozono.jpg' style="height: {image_h}; object-fit: cover; border-top-left-radius: {border_radius}; border-top-right-radius: {border_radius};">
                <div style="padding: 1rem 2rem;">
                    <h3 {card_style_h3}>Ambiente</h3>
                    <p>Articolo sull'ozono ambientale.</p>
                </div>
            </div>
        </a>
    '''
    html_cards += f'''
        <a href="/ozono/sanificazione.html" style="text-decoration: none; color: #222222;">
            <div style="background-color: {card_bg_color}; border: 1px solid {border_color}; border-radius: {border_radius};">
                <img src='/ozono-sanificazione.jpg' style="height: {image_h}; object-fit: cover; border-top-left-radius: {border_radius}; border-top-right-radius: {border_radius};">
                <div style="padding: 1rem 2rem;">
                    <h3 {card_style_h3}>Sanificazione</h3>
                    <p>Articolo sulla sanificazione ad ozono.</p>
                </div>
            </div>
        </a>
    '''
    html_cards += f'''
        <a href="/ozono/terapia.html" style="text-decoration: none; color: #222222;">
            <div style="background-color: {card_bg_color}; border: 1px solid {border_color}; border-radius: {border_radius};">
                <img src='/ozono-terapia.jpg' style="height: {image_h}; object-fit: cover; border-top-left-radius: {border_radius}; border-top-right-radius: {border_radius};">
                <div style="padding: 1rem 2rem;">
                    <h3 {card_style_h3}">Ozonoterapia</h3>
                    <p>Articolo sulla ozonoterapia.</p>
                </div>
            </div>
        </a>
    '''
    html_article = sections.grid_1_default(html_heading, html_cards, html_buttons='')
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

def gen():
    # reset tmp css
    with open('styles/tmp/hub-ozone.css', 'w') as f: f.write('')
    with open('styles/tmp-mobile/hub-ozone-mobile.css', 'w') as f: f.write('')

    ozono_article_gen(article_url_slug=f'ozono/chimica')
    ozono_article_gen(article_url_slug=f'ozono/ambiente')
    ozono_article_gen(article_url_slug=f'ozono/terapia')
    ozono_article_gen(article_url_slug=f'ozono/sanificazione')
    ozono_article_gen(article_url_slug=f'ozono/sanificazione/applicazioni/caseificio')
    ozono_article_gen(article_url_slug=f'ozono/sanificazione/applicazioni/disinfestazione')
    
    ozono_gen()
