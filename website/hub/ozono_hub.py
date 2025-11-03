import os

import markdown

from lib import g
from lib import components

def ozono_article_gen(article_url_slug):
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
    html_article += markdown.markdown(markdown_text, extensions=['tables'])

    html_article = html_article.replace('<p><img', '<p class="container-lg"><img class="article-img"')
    html_article = html_article.replace('<h1', '<h1 class="container-lg article-h1"')
    html_article = html_article.replace('<h2', '<h2 class="container-md article-h2"')
    html_article = html_article.replace('<h3', '<h3 class="container-md article-h3"')
    html_article = html_article.replace('<ul', '<ul class="container-md article-ul"')
    html_article = html_article.replace('<ol', '<ol class="container-md article-ol"')
    html_article = html_article.replace('<li', '<li class="article-li"')
    html_article = html_article.replace('<p>', '<p class="container-md article-p"">')
    html_article = html_article.replace('<table>', '<table class="container-md article-table"">')
    
    html_article = html_article.replace('/h1>', '/h1>\n<p class="container-md article-date">6 October 2025</p>\n<p class="container-sd article-author">Staff Tecnico Ozonogroup</p>')

    breadcrumbs_text_size = '0.75rem'
    breadcrumbs = article_url_slug.split('/')
    breadcrumbs_html = f''
    breadcrumbs_html += f'''<div class="container-xl">'''
    breadcrumbs_html += f'''<a style="color: #5f6368; text-decoration: none; font-size: {breadcrumbs_text_size};" href="/">HOME</a><span> > </span>'''
    chunk = '/'
    for item in breadcrumbs[:-1]:
        chunk += item
        breadcrumbs_html += f'''<a style="color: #5f6368; text-decoration: none; font-size: {breadcrumbs_text_size};" href="{chunk}.html">{item.upper()}</a><span> > </span>'''
        chunk += '/'
    breadcrumbs_html += f'''<span style="color: #5f6368; text-decoration: none; font-size: {breadcrumbs_text_size};">{breadcrumbs[-1].upper()}</span>'''
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
            {components.header_light()}
            {breadcrumbs_html}
            <main>
                {html_article}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    try: os.makedirs(f'{g.website_folderpath}/{article_folderpath}')
    except: pass
    html_filepath = f'{g.website_folderpath}/{article_url_slug}.html'
    print(html_filepath)
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html_index)
    
def ozono_gen():
    html_article = ''
    html_article += f'''
        <div class="container-xl" style="margin-top: 5rem; margin-bottom: 5rem;">
            <h1 style="color: #222222; font-size: 3.0rem; line-height: 1; font-weight: normal; text-align: center; margin-bottom: 1rem;">Ozono</h1>
            <p style="color: #555555; font-size: 1.25rem; line-height: 1; font-weight: normal; text-align: center;">Tutto quello che c'è da sapere sull'ozono.</p>
        </div>
    '''
    html_heading = f'''
        <div class="container-xl" style="margin-bottom: 3rem;">
            <div style="display: flex; justify-content: space-between;">
                <div>
                    <h2 style="color: #222222; font-size: 2.25rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">Articoli principali</h1>
                    <p style="color: #555555; font-size: 1.125rem; line-height: 1; font-weight: normal;">Scopri i principali argomenti di intersse sull'ozono.</p>
                </div>
                <div>
                    <a style="display: inline-block; text-decoration: none; color: blue; margin-top: 0.5rem;" href="#">Visualizza tutti gli articoli</a>
                </div>
            </div>
        </div>
    '''

    image_h = '15rem'
    border_radius = '0.5rem'
    border_color = '#cdcdcd'
    card_bg_color = '#f8f9fB'
    card_bg_color = '#ffffff'
    card_style_h3 = f'''
        style="
            margin-bottom: 1rem; 
            font-weight: normal;
            font-size: 1.5rem;
        "
    '''
    data = [
        {
            'href': '''/ozono/chimica.html''',
            'image_src': '/immagini/ozono-chimica.jpg',
            'category': 'CHIMICA',
            'title': '''Chimica dell'ozono: reazioni, meccanismi e implicazioni atmosferiche''',
            'description': '''La molecola di ozono, O₃, presenta una struttura piegata con un angolo di circa 117°, dovuto all'ibridazione sp² degli atomi di ossigeno...''',
            'date': '''6 OTTOBRE 2025''',
            'datetime': '''2025-10-06''',
        },
        {
            'href': '''/ozono/ambiente.html''',
            'image_src': '/immagini/ozono-ambiente.jpg',
            'category': 'AMBIENTE',
            'title': '''Ozono nell'ambiente: cos'è, dove si trova e quali sono i suoi effetti sull'atmosfera''',
            'description': '''L'ozono è una delle molecole più affascinanti e controverse dell'atmosfera terrestre. Può essere allo stesso tempo un prezioso alleato contro i raggi ultravioletti e un pericoloso inquinante se presente nei bassi strati dell'aria.''',
            'date': '''6 OTTOBRE 2025''',
            'datetime': '''2025-10-06''',
        },
        {
            'href': '''/ozono/sanificazione.html''',
            'image_src': '/immagini/ozono-sanificazione.jpg',
            'category': 'SANIFICAZIONE',
            'title': '''Sanificazione a ozono: la soluzione naturale per igiene, sicurezza e benessere''',
            'description': '''La sanificazione a ozono sta diventando una delle soluzioni più efficaci ed ecologiche per garantire la pulizia, la disinfezione e l'igiene di ambienti domestici, professionali e agricoli.''',
            'date': '''6 OTTOBRE 2025''',
            'datetime': '''2025-10-06''',
        },
        {
            'href': '''/ozono/terapia.html''',
            'image_src': '/immagini/ozono-terapia.jpg',
            'category': 'OZONOTERAPIA',
            'title': '''Ozonoterapia: applicazioni, meccanismi e prospettive della terapia con ozono''',
            'description': '''Negli ultimi anni l’ozonoterapia ha guadagnato un ruolo crescente all’interno della medicina rigenerativa e funzionale.''',
            'date': '''6 OTTOBRE 2025''',
            'datetime': '''2025-10-06''',
        },
    ]
    html_cards = ''
    for item in data:
        description = ''
        for word in item['description'].split():
            description += f'{word} '
            if len(description) > 60:
                break
        description = description.strip() + '...'
        html_cards += f'''
            <a href="{item['href']}" style="text-decoration: none; color: #222222;">
                <div style="background-color: {card_bg_color}; border: 1px solid {border_color}; border-radius: {border_radius};">
                    <img src="{item['image_src']}" style="height: {image_h}; object-fit: cover; border-top-left-radius: {border_radius}; border-top-right-radius: {border_radius};">
                    <div style="padding: 1rem 2rem;">
                        <p style="color: #777777; font-size: 0.75rem; line-height: 1; font-weight: bold; letter-spacing: 1px; margin-bottom: 0.75rem;">{item['category']}</p>
                        <h3 style="color: #333333; font-size: 1.5rem; line-height: 1.2; font-weight: normal; margin-bottom: 0.75rem;">{item['title']}</h3>
                        <p style="color: #555555; font-size: 1rem; line-height: 1.375rem; font-weight: normal; margin-bottom: 5rem;">{description}</p>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <time datetime="{item['datetime']}" style="color: #777777; font-size: 0.75rem; line-height: 1; font-weight: bold; letter-spacing: 1px;">{item['date']}</time>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="blue"><path d="m560-240-56-58 142-142H160v-80h486L504-662l56-58 240 240-240 240Z"/></svg>
                        </div>
                    </div>
                </div>
            </a>
        '''
    html_article += html_heading
    html_article += f'''
        <section class="container-xl" style="margin-bottom: 6.4rem;">
            <div class="grid-3">
                {html_cards}
            </div>
        </section>
    '''
    html_index = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/style.css">
            </head>
        <body>
            {components.header_light()}
            <main>
                {html_article}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_index_filepath = f'{g.website_folderpath}/ozono.html'
    with open(html_index_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html_index)

def gen():
    ozono_article_gen(article_url_slug=f'ozono/chimica')
    ozono_article_gen(article_url_slug=f'ozono/ambiente')
    ozono_article_gen(article_url_slug=f'ozono/terapia')
    ozono_article_gen(article_url_slug=f'ozono/sanificazione')
    ozono_article_gen(article_url_slug=f'ozono/sanificazione/applicazioni/caseificio')
    ozono_article_gen(article_url_slug=f'ozono/sanificazione/applicazioni/disinfestazione')
    
    ozono_gen()
