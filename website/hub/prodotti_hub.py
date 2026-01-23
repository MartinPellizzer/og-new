import os

import lorem

from lib import g
from lib import io
from lib import components

# products_data = io.csv_to_dict(f'{g.SSOT_FOLDERPATH}/products/data.csv', delimiter=',')
products_data = io.json_read(f'{g.SSOT_FOLDERPATH}/products/data.json')

categories_data = [
    {
        'category_name': 'Tutti', 
        'category_href': '/prodotti.html', 
    },
    {
        'category_name': 'Generatori', 
        'category_href': '/prodotti/generatori.html', 
    },
    {
        'category_name': 'Generatori Piccoli', 
        'category_href': '/prodotti/generatori/piccoli.html', 
    },
    {
        'category_name': 'Generatori Medi', 
        'category_href': '/prodotti/generatori/medi.html', 
    },
    {
        'category_name': 'Generatori Grandi', 
        'category_href': '/prodotti/generatori/grandi.html', 
    },
    {
        'category_name': 'Generatori Gas', 
        'category_href': '/prodotti/generatori/gas.html', 
    },
    {
        'category_name': 'Generatori Acqua', 
        'category_href': '/prodotti/generatori/acqua.html', 
    },
    {
        'category_name': 'Accessori', 
        'category_href': '/prodotti/accessori.html', 
    },
]

def hero_html_gen(category=''):
    section_hero_py = '5rem'
    section_py = '8rem'
    hero_button = f'''
        <div style="flex: 1; display: flex; justify-content: end; margin-top: 0.25rem;">
            <div style="display: inline-block;">
                <a class="button-default-1" href="/contatti.html">
                    <span>Prenota Consulenza Gratuita</span>
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                </a>
            </div>
        </div>
    '''
    if category == '':
        title = '''Generatori e sistemi professionali ad ozono per l'industria'''
    else: 
        category_name = category['category_name']
        category_href = category['category_href']
        title = category_name
    ########################################
    # hero
    ########################################
    hero_html = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_hero_py};">
            <div style="display: flex; justify-content: space-between; center;">
                <div style="flex: 2;">
                    <h1 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
                        {title}
                    </h1>
                </div>
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    return hero_html

def group_products_by_name_old():
    groups = []
    for item in products_data:
        found = False
        for group in groups:
            if group['nome'] == item['nome']:
                found = True
                group['data'].append(item)
                break
        if not found:
            _item = {
                'nome': item['nome'],
                'data': [item],
            }
            groups.append(_item)
    return groups

def group_products_by_name():
    groups = []
    for item in products_data:
        found = False
        for group in groups:
            if group['name'] == item['name']:
                found = True
                group['data'].append(item)
                break
        if not found:
            _item = {
                'name': item['name'],
                'data': [item],
            }
            groups.append(_item)
    return groups

def cta():
    html = f'''
        <section class="container-xl" style="margin-top: 6rem; margin-bottom: 6rem;">
            <div style="display: flex; align-items: center; gap: 3rem; margin-bottom: 2rem;">
                <h2 style="color: {g.color_black_pearl}; font-size: 1.25rem; font-weight: normal;">Contattaci</h2>
                <div style="display: flex; align-items: center; gap: 1.5rem;">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="{g.color_black_pearl}">
                            <path
                                d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm320-280L160-640v400h640v-400L480-440Zm0-80 320-200H160l320 200ZM160-640v-80 480-400Z" />
                        </svg>
                        <span>Email: info@ozonogroup.it</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="{g.color_black_pearl}">
                            <path
                                d="M798-120q-125 0-247-54.5T329-329Q229-429 174.5-551T120-798q0-18 12-30t30-12h162q14 0 25 9.5t13 22.5l26 140q2 16-1 27t-11 19l-97 98q20 37 47.5 71.5T387-386q31 31 65 57.5t72 48.5l94-94q9-9 23.5-13.5T670-390l138 28q14 4 23 14.5t9 23.5v162q0 18-12 30t-30 12ZM241-600l66-66-17-94h-89q5 41 14 81t26 79Zm358 358q39 17 79.5 27t81.5 13v-88l-94-19-67 67ZM241-600Zm358 358Z" />
                        </svg>
                        <span>Telefono: +39 0423 952833</span>
                    </div>
                </div>
            </div>
            <div style="">
                <div style="display: inline-block;">
                    <a class="button-default-3" href="/contatti.html">
                        <span>Prenota Consulenza Gratuita</span>
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#ffffff"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                    </a>
                </div>
            </div>
        </section>
    '''
    return html


def sidebar_gen():
    categories_html = ''
    for item in categories_data:
        card_html = f'''
            <a class="font-inter-medium" 
                style="
                display: block; 
                font-size: 0.875rem; color: #666666; text-decoration: none; 
                line-height: 1; margin-bottom: 0.875rem; 
                padding-bottom: 0.875rem; border-bottom: 1px solid #e7e7e7;
                padding-left: 1rem;
                padding-rignt: 1rem;
                "
                href="{item['category_href']}">
                > {item['category_name'].title()}
            </a>
        '''
        categories_html += card_html
        
    product_1 = products_data[0]
    product_2 = products_data[1]
    product_3 = products_data[2]
    products_popular_data = [product_1, product_2, product_3, ]
    popular_cards_html = ''
    for item in products_popular_data:
        product_name = item['name']
        product_slug = product_name.lower().strip().replace(' ', '-')
        item = item['versions'][0]
        popular_card_html = f'''
            <div style="display: flex; gap: 1rem;">
                <div style="flex: 2;">
                <a style="
                        color: #222222; text-decoration: none;
                    "
                    href="/prodotti/{product_slug}.html"
                >
                    <div style="background-color: #f7f7f7; padding: 1rem; margin-bottom: 1rem;">
                        <img src="/immagini/{item['image_filename']}" style="height: 4rem; object-fit: contain;">
                    </div>
                </a>
                </div>
                <div style="flex: 3;">
                    <p class="font-inter-regular" style="font-size: 0.675rem; color: #666666; line-height: 1; margin-bottom: 0.5rem;">{item['output'].upper()}</p>
                    <a style="
                            color: #222222; text-decoration: none;
                        "
                        href="/prodotti/{product_slug}.html"
                    >
                        <h2 class="font-inter-medium" style="font-size: 1rem; color: #222222; line-height: 1; margin-bottom: 0.5rem;">{item['name']}</h2>
                    </a>
                </div>
            </div>
        '''
        popular_cards_html += popular_card_html
    sidebar_html = f'''
        <h2 class="font-inter-medium" 
            style="font-size: 0.875rem; color: #222222; line-height: 1; 
            margin-bottom: 1.5rem;">
            CATEGORIE
        </h2>
        {categories_html}
        <h2 class="font-inter-medium" 
            style="font-size: 0.875rem; color: #222222; line-height: 1; 
            margin-bottom: 1.5rem; margin-top: 3rem;">
            PRODOTTI POPOLARI
        </h2>
        {popular_cards_html}
    '''
    return sidebar_html

def sidebar_gen_old():
    categories_data = [
        {
            'category_name': 'piccole', 
            'category_href': '/prodotti/generatori-dimensioni-piccole.html', 
        },
        {
            'category_name': 'medie', 
            'category_href': '/prodotti/generatori-dimensioni-medie.html', 
        },
        {
            'category_name': 'grandi', 
            'category_href': '/prodotti/generatori-dimensioni-grandi.html', 
        },
        {
            'category_name': 'gas', 
            'category_href': '/prodotti/generatori-gas.html', 
        },
        {
            'category_name': 'acqua', 
            'category_href': '/prodotti/generatori-acqua.html', 
        },
        {
            'category_name': 'accessori', 
            'category_href': '/prodotti/accessori.html', 
        },
    ]
    categories_html = ''
    for item in categories_data:
        card_html = f'''
            <a class="font-inter-medium" 
                style="
                display: block; 
                font-size: 0.875rem; color: #666666; text-decoration: none; 
                line-height: 1; margin-bottom: 0.875rem; 
                padding-bottom: 0.875rem; border-bottom: 1px solid #e7e7e7;
                padding-left: 1rem;
                padding-rignt: 1rem;
                "
                href="{item['category_href']}">
                > {item['category_name'].title()}
            </a>
        '''
        categories_html += card_html
        
    groups = group_products_by_name()
    group_1_data = groups[0]['data']
    group_2_data = groups[1]['data']
    group_3_data = groups[2]['data']
    products_popular_data = [group_1_data, group_2_data, group_3_data, ]
    popular_cards_html = ''
    for item in products_popular_data:
        item = item[0]
        print(item)
        popular_card_html = f'''
            <div style="display: flex; gap: 1rem;">
                <div style="flex: 2;">
                    <div style="background-color: #f7f7f7; padding: 1rem; margin-bottom: 1rem;">
                        <img src="/immagini/{item['image_filename']}" style="height: 4rem; object-fit: contain;">
                    </div>
                </div>
                <div style="flex: 3;">
                    <p class="font-inter-regular" style="font-size: 0.675rem; color: #666666; line-height: 1; margin-bottom: 0.5rem;">{item['output'].upper()}</p>
                    <h2 class="font-inter-medium" style="font-size: 1rem; color: #222222; line-height: 1; margin-bottom: 0.5rem;">{item['name']}</h2>
                    <p class="font-inter-bold" style="font-size: 0.875rem; color: #222222; line-height: 1;">{item['price']}</p>
                </div>
            </div>
        '''
        popular_cards_html += popular_card_html
    sidebar_html = f'''
        <h2 class="font-inter-medium" 
            style="font-size: 0.875rem; color: #222222; line-height: 1; 
            margin-bottom: 1.5rem;">
            CATEGORIE
        </h2>
        {categories_html}
        <h2 class="font-inter-medium" 
            style="font-size: 0.875rem; color: #222222; line-height: 1; 
            margin-bottom: 1.5rem; margin-top: 3rem;">
            PRODOTTI POPOLARI
        </h2>
        {popular_cards_html}
    '''
    return sidebar_html

def products_gen():
    hero = hero_html_gen()

    ########################################
    # NEW html
    ########################################
    cards_html = ''
    for group in products_data:
        product_name = group['name']
        product_slug = product_name.lower().strip().replace(' ', '-')
        item = group['versions'][0]
        # product_versions_html = product_versions_html_gen(group)
        card_html = f'''
            <div>
                <a style="
                        color: #222222; text-decoration: none;
                    "
                    href="/prodotti/{product_slug}.html"
                >
                    <div style="background-color: #f7f7f7; padding: 3rem; margin-bottom: 1rem;">
                        <img src="/immagini/{item['image_filename']}" style="height: 10rem; object-fit: contain;">
                    </div>
                </a>
                <p class="font-inter-regular" style="font-size: 0.675rem; color: #666666; line-height: 1; margin-bottom: 0.5rem;">{item['output'].upper()}</p>
                <h2 class="font-inter-medium" style="font-size: 1rem; color: #222222; line-height: 1; margin-bottom: 0.5rem;">
                    <a style="
                            color: #222222; text-decoration: none;
                        "
                        href="/prodotti/{product_slug}.html"
                    >
                        {product_name}
                    </a>
                </h2>
            </div>
        '''
        cards_html += card_html
    sidebar_html = sidebar_gen()

    prodotti = f'''
        <section class="container-xl" style="margin-top: 2rem;">
            <div class="flex-d" style="gap: 2rem;">
                <div class="hide-m" style="flex: 1;">
                {sidebar_html}
                </div>
                <div style="flex: 3;">
                    <div class="grid-3" style="gap: 1.6rem;">
                        {cards_html}
                    </div>
                </div>
            </div>
        </section>
    '''

    ########################################
    # html
    ########################################
    html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/style.css">
        </head>
        <body>
            {components.header_light()}
            <main style="margin-bottom: 4.8rem;">
                {hero}
                {prodotti}
            </main>
                
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_filepath = f'{g.website_folderpath}/prodotti.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)

def product_versions_html_gen(product):
    product_versions = [item['version'] for item in product['versions']]
    product_versions_html = ''
    for product_version in product_versions:
        _html = f'''
            <span class="font-inter-bold" 
                style="
                white-space: nowrap;
                padding: 6px 12px;
                border: 1px solid #e7e7e7;
                color: #222222;
                font-size: 0.75rem;
            ">
                {product_version}
            </span>
        '''
        product_versions_html += _html
    product_versions_html = f'''
        <p class="font-inter-medium" 
            style="font-size: 0.75rem; color: #777777; 
            line-height: 1; margin-bottom: 0.625rem;
            letter-spacing: 0.5px;
        ">
            VERSIONI:
        </p>
        <div style="
            display: flex; flex-wrap: wrap; gap: 0.5rem;
            margin-bottom: 1rem;
        ">
        {product_versions_html}
        </div>
    '''
    return product_versions_html

def products_product_gen():
    try: os.makedirs(f'{g.website_folderpath}/prodotti')
    except: pass
    ### group by name
    # groups = group_products_by_name()

    for product in products_data:
        product_name = product['name']
        product_slug = product_name.lower().strip().replace(' ', '-')
        html_filepath = f'{g.website_folderpath}/prodotti/{product_slug}.html'
        item = product['versions'][0]
        models_num = len(product['versions'])
        product_description = product['description']
        ###
        product_versions_html = product_versions_html_gen(product)
        
        ###
        versions_details_html = ''
        for item_i, item in enumerate(product['versions']):
            # product_desc = lorem.paragraph()
            product_desc = item['description']
            product_code = item['code']
            product_producion_nominal = item['production_nominal']
            product_weight = item['weight'].replace('.', ',')
            product_size = item['size']
            product_voltage = item['voltage']
            product_frequency = item['frequency']
            product_power = item['power']
            version_details_html = f'''
                <div style="margin-top: 2rem;">
                    <h2 class="font-inter-bold" 
                        style="color: #222222; font-size: 1.25rem; 
                        line-height: 1; margin-bottom: 1rem;
                    ">
                        Versione {item['version']}
                    </h2>
                    <div class="tabs">
                        <!-- Radio buttons -->
                        <input type="radio" name="tab{item_i}" id="tabs{item_i}-a" checked>
                        <input type="radio" name="tab{item_i}" id="tabs{item_i}-b">
                        <!-- Tab labels -->
                        <div class="tab-labels">
                            <label for="tabs{item_i}-a">Descrizione</label>
                            <label for="tabs{item_i}-b">Informazioni Tecniche</label>
                        </div>
                        <!-- Tab content -->
                        <div class="tab-content">
                            <div class="content a">
                                <p class="font-inter-regular" 
                                    style="font-size: 1rem; color: #777777; 
                                    margin-bottom: 1rem; line-height: 1.625rem;
                                ">
                                    {product_desc}
                                </p>
                            </div>
                            <div class="content b">
                                <p class="font-inter-regular" 
                                    style="font-size: 1rem; color: #777777; 
                                    margin-bottom: 1rem; line-height: 1.625rem;
                                ">
                                    Codice: {product_code} 
                                </p>
                                <p class="font-inter-regular" 
                                    style="font-size: 1rem; color: #777777; 
                                    margin-bottom: 1rem; line-height: 1.625rem;
                                ">
                                    Produzione (Nominale): {product_producion_nominal}  g/h 
                                </p>
                                <p class="font-inter-regular" 
                                    style="font-size: 1rem; color: #777777; 
                                    margin-bottom: 1rem; line-height: 1.625rem;
                                ">
                                    Peso: {product_weight} kg 
                                </p>
                                <p class="font-inter-regular" 
                                    style="font-size: 1rem; color: #777777; 
                                    margin-bottom: 1rem; line-height: 1.625rem;
                                ">
                                    Dimensioni: {product_size} mm
                                </p>
                                <p class="font-inter-regular" 
                                    style="font-size: 1rem; color: #777777; 
                                    margin-bottom: 1rem; line-height: 1.625rem;
                                ">
                                    Tensione Alimentazione: {product_voltage} V
                                </p>
                                <p class="font-inter-regular" 
                                    style="font-size: 1rem; color: #777777; 
                                    margin-bottom: 1rem; line-height: 1.625rem;
                                ">
                                    Frequenza Alimentazione: {product_frequency} Hz
                                </p>
                                <p class="font-inter-regular" 
                                    style="font-size: 1rem; color: #777777; 
                                    margin-bottom: 1rem; line-height: 1.625rem;
                                ">
                                    Potenza: {product_power} Watt
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            '''
            versions_details_html += version_details_html
            # break
        
        ########################################
        # html
        ########################################
        # product_preview = lorem.paragraph()
        # product_desc = lorem.paragraph()

        '''
        <p class="font-inter-bold" 
            style="font-size: 1.375rem; color: #222222; 
            line-height: 1; margin-bottom: 1rem;
        ">€
            {item['price']}
        </p>
        '''

        sidebar_html = sidebar_gen()
        product_html = f'''
            <div class="flex-d" style="gap: 2rem; margin-bottom: 0rem;">
                <div style="flex: 1;">
                    <div style="background-color: #f7f7f7; padding: 3rem; margin-bottom: 1rem;">
                        <img src="/immagini/{item['image_filename']}" style="height: 20rem; object-fit: contain;">
                    </div>
                </div>
                <div style="flex: 1;">
                    <h1 class="font-inter-bold" 
                        style="color: #222222; font-size: 2rem; 
                        line-height: 1; margin-bottom: 1rem;
                    ">
                        {item['name']}
                    </h1>
                    <p class="font-inter-regular" 
                        style="font-size: 1rem; color: #777777; 
                         margin-bottom: 1rem;
                    ">
                        {product_description}
                    </p>
                    <p class="font-inter-medium" 
                        style="font-size: 0.75rem; color: #777777; 
                        line-height: 1; margin-bottom: 1rem;
                        letter-spacing: 0.5px;
                    ">
                        OUTPUT: 
                        <span class="font-inter-bold"
                            style="font-size: 0.75rem; color: #222222;
                        ">
                            {item['output'].upper()}
                        </span>
                    </p>
                    
                    {product_versions_html}
                    <div style="
                        display: inline-block;
                        padding: 12px 24px;
                        background-color: #222222;
                        font-size: 0.75rem;
                        letter-spacing: 0.5px;
                    ">
                        <a href="#"
                            style="
                            color: #ffffff;
                            text-decoration: none;
                        ">
                            RICHIEDI PREVENTIVO
                        </a>
                    </div>
                </div>
            </div>
            {versions_details_html}

        '''

        content_html = f'''
            <section class="container-xl" style="margin-top: 2rem; margin-bottom: 4rem;">
                <div class="flex-d" style="gap: 2rem;">
                    <div class="hide-m" style="flex: 1;">
                    {sidebar_html}
                    </div>
                    <div style="flex: 3;">
                        {product_html}
                    </div>
                </div>
            </section>
        '''
    
        html = f'''
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
                    {content_html}
                </main>
                {components.footer_dark()}
            </body>
            </html>
        '''
        with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
            f.write(html)

def products_category_gen(category):
    hero_html = hero_html_gen(category)
    category_name = category['category_name']
    category_href = category['category_href']
    ########################################
    # NEW html
    ########################################
    cards_html = ''
    for product in products_data:
        product_name = product['name']
        product_slug = product_name.lower().strip().replace(' ', '-')
        version = product['versions'][0]
        product_categories = [category.lower().strip() for category in version['categories']]
        if category_name.lower().strip() != 'tutti':
            if category_name.lower().strip() not in product_categories: continue
        card_html = f'''
            <div>
                <a style="
                        color: #222222; text-decoration: none;
                    "
                    href="/prodotti/{product_slug}.html"
                >
                    <div style="background-color: #f7f7f7; padding: 3rem; margin-bottom: 1rem;">
                        <img src="/immagini/{version['image_filename']}" style="height: 10rem; object-fit: contain;">
                    </div>
                </a>
                <p class="font-inter-regular" style="font-size: 0.675rem; color: #666666; line-height: 1; margin-bottom: 0.5rem;">{version['output'].upper()}</p>
                <h2 class="font-inter-medium" style="font-size: 1rem; color: #222222; line-height: 1; margin-bottom: 0.5rem;">
                    <a style="
                            color: #222222; text-decoration: none;
                        "
                        href="/prodotti/{product_slug}.html"
                    >
                        {product_name}
                    </a>
                </h2>
            </div>
        '''
        cards_html += card_html
    sidebar_html = sidebar_gen()
    prodotti = f'''
        <section class="container-xl" style="margin-top: 2rem;">
            <div class="flex-d" style="gap: 2rem;">
                <div class="hide-m" style="flex: 1;">
                {sidebar_html}
                </div>
                <div style="flex: 3;">
                    <div class="grid-3" style="gap: 1.6rem;">
                        {cards_html}
                    </div>
                </div>
            </div>
        </section>
    '''
    ###
    html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="/style.css">
        </head>
        <body>
            {components.header_light()}
            <main style="margin-bottom: 4.8rem;">
                {hero_html}
                {prodotti}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_filepath = f'{g.website_folderpath}/{category_href}'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)

def gen():
    products_product_gen()
    for category in categories_data:
        products_category_gen(category)
    products_gen()
