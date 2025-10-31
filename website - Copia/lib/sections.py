from lib import g
from lib import utils
from lib import blocks
from lib import components

def header_light():
    html_nav_link_list = ''
    for nav_link in g.header_nav_link_list:
        html_nav_link_list += f'<a href="{nav_link["link_href"]}">{nav_link["link_name"].title()}</a>\n'
    html = f'''
        <header class="header-light">
            <div class="container-xl header-light-container">
                <div class="header-light-menu">
                    <a class="header-light-menu-logo" href="/">Ozonogroup</a>
                    <nav class="header-light-menu-nav">
                        {html_nav_link_list}
                    </nav>
                </div>
                <div class="home-hero-header-button">
                    {components.link_fill()}
                </div>
            </div>
        </header>
    '''
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.header-light'
    if class_name not in css:
        css += f'''
            {class_name} {{
                background-color: {g.color_white};
                padding-top: 2.4rem;
                padding-bottom: 2.4rem;
            }}
        '''
    class_name = '.header-light-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
        '''
    class_name = '.header-light-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                    text-align: center;
                }}
            }}
        '''
    class_name = '.header-light-menu'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 32px;
            }}
        '''
    class_name = '.header-light-menu'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                    text-align: center;
                }}
            }}
        '''
    class_name = '.header-light-menu-logo'
    if class_name not in css:
        css += f'''
            {class_name} {{
                font-size: {g.typography_size_lg};
                color: {g.color_black_pearl};
                text-decoration-line: none;
            }}
        '''
    class_name = '.header-light-menu-nav'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                align-items: center;
                gap: 16px;
            }}
        '''
    class_name = '.header-light-menu-nav a'
    if class_name not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                text-decoration-line: none;
            }}
        '''
    class_name = '.home-hero-header-button'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    display: none;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def header_dark():
    html_nav_link_list = ''
    for nav_link in g.header_nav_link_list:
        html_nav_link_list += f'<a href="{nav_link["link_href"]}">{nav_link["link_name"].title()}</a>\n'
    html = f'''
        <header class="header-dark">
            <div class="container-xl header-dark-container">
                <div class="header-dark-menu">
                    <a class="header-dark-menu-logo" href="/">Ozonogroup</a>
                    <nav class="header-dark-menu-nav">
                        {html_nav_link_list}
                    </nav>
                </div>
                <div class="home-hero-header-button">
                    {components.link_fill_reverse()}
                </div>
            </div>
        </header>
    '''
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.header-dark'
    if class_name not in css:
        css += f'''
            {class_name} {{
                background-color: {g.color_black_pearl};
                padding-top: 2.4rem;
                padding-bottom: 2.4rem;
            }}
        '''
    class_name = '.header-dark-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 1.6rem;
            }}
        '''
    class_name = '.header-dark-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                    text-align: center;
                }}
            }}
        '''
    class_name = '.header-dark-menu'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 1.6rem;
            }}
        '''
    class_name = '.header-dark-menu'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                    text-align: center;
                }}
            }}
        '''
    class_name = '.header-dark-menu-logo'
    if class_name not in css:
        css += f'''
            {class_name} {{
                font-size: {g.typography_size_lg};
                color: {g.color_white};
                text-decoration-line: none;
            }}
        '''
    class_name = '.header-dark-menu-nav'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                align-items: center;
                gap: 16px;
            }}
        '''
    class_name = '.header-dark-menu-nav a'
    if class_name not in css:
        css += f'''
            {class_name} {{
                color: {g.color_white};
                text-decoration-line: none;
            }}
        '''
    class_name = '.home-hero-header-button'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    display: none;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def footer_default():
    html_contatti_heading = components.h2_reverse(
        text = f'''Contatti''',
    )
    html_address_paragraph = components.paragraph_reverse(
        text = f'''Via dell'Artigianato, 23, 31011 Asolo TV''',
        margin_bottom = '0.8rem',
    )
    html_phone_paragraph = components.paragraph_reverse(
        text = f'''+39 0423 952833''',
        margin_bottom = '0',
    )
    html_email_paragraph = components.paragraph_reverse(
        text = f'''info@ozonogroup.it''',
        margin_bottom = '0',
    )
    html_links_heading = components.h2_reverse(
        text = f'''Risorse''',
    )
    html_paragraph_reverse = components.paragraph_reverse(
        text = f'''Copyright © Ozonogroup | Tutti i diritti riservati''',
        margin_bottom = '0',
    )
    html_nav_link_list = ''
    for nav_link in g.footer_nav_link_list:
        html_link = components.link_reverse(
            nav_link["link_name"].title(), 
            nav_link["link_href"],
        )
        html_nav_link_list += html_link
    html = f'''
        <footer class="home-footer-container">
            <div class="container-xl">
                <div class="home-footer-intro-container">
                    <div>
                        {html_contatti_heading}
                        {html_address_paragraph}
                        <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 8px;">
                            <svg xmlns="http://www.w3.org/2000/svg" height="16px" viewBox="0 -960 960 960" width="16px" fill="#ffffff">
                                <path d="M798-120q-125 0-247-54.5T329-329Q229-429 174.5-551T120-798q0-18 12-30t30-12h162q14 0 25 9.5t13 22.5l26 140q2 16-1 27t-11 19l-97 98q20 37 47.5 71.5T387-386q31 31 65 57.5t72 48.5l94-94q9-9 23.5-13.5T670-390l138 28q14 4 23 14.5t9 23.5v162q0 18-12 30t-30 12ZM241-600l66-66-17-94h-89q5 41 14 81t26 79Zm358 358q39 17 79.5 27t81.5 13v-88l-94-19-67 67ZM241-600Zm358 358Z" />
                            </svg>
                            {html_phone_paragraph}
                        </div>
                        <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 8px;">
                            <svg xmlns="http://www.w3.org/2000/svg" height="16px" viewBox="0 -960 960 960" width="16px" fill="#ffffff">
                                <path d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm320-280L160-640v400h640v-400L480-440Zm0-80 320-200H160l320 200ZM160-640v-80 480-400Z" />
                            </svg>
                            {html_email_paragraph}
                        </div>
                    </div>
                    <div>
                        {html_links_heading}
                        <div class="home-footer-nav">
                            {html_nav_link_list}
                        </div>
                    </div>
                </div>
                <div class="home-footer-copyright-container">
                    <a style="font-size: 24px; color: #ffffff; text-decoration-line: none;" href="#">Ozonogroup</a>
                    {html_paragraph_reverse}
                </div>
            </div>
        </footer>
    '''
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.home-footer-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                background-color: {g.color_black_pearl};
                padding-top: 96px;
                padding-bottom: 96px;
            }}
        '''
    class_name = '.home-footer-intro-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                justify-content: space-between;
                margin-bottom: 64px;
            }}
        '''
    class_name = '.home-footer-nav'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                flex-direction: column;
                gap: 0.8rem;
            }}
        '''
    class_name = '.home-footer-copyright-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
        '''
    class_name = '.home-footer-intro-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                    gap: 32px;
                }}
            }}
        '''
    class_name = '.home-footer-copyright-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                    gap: 16px;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

##########################################################

def home_hero():
    title = components.h1_reverse(
        text = f'''Sanificazione ozono per l'industria alimentare''',
        align_mobile = 'center',
    )
    html = f'''
        <section class="home-hero-section">
            <div class="container-xl" style="height: 100%;">
                <div class="home-hero-container">
                    <div class="home-hero-title-container">
                        <div style="flex: 2;">
                            {title}
                        </div>
                        <div style="flex: 1;"></div>
                    </div>
                    <div class="home-hero-content-container">
                        <div style="flex: 2;"></div>
                        <div style="flex: 1;">
                            <p style="color: #ffffff; font-size: 16px; line-height: 24px; margin-bottom: 24px;">Progettiamo
                                sistemi di sanificazione con ozono per ambienti di produzione alimentari pi&#249;
                                sicuri e igienici (senza l'uso di sostanze chimiche).</p>
                            <div class="home-hero-buttons-container">
                                {components.link_fill_reverse()}
                                {components.link_ghost_reverse()}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    '''
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.home-hero-section'
    if class_name not in css:
        css += f'''
            {class_name} {{
                background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/immagini/home/sanificazione-ozono.png');
                background-size: cover;
                background-position: center;
                margin-bottom: 96px;
                border-bottom-left-radius: {g.border_radius_xl};
                border-bottom-right-radius: {g.border_radius_xl};
            }}
        '''
    class_name = '.home-hero-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                padding-top: 128px;
                display: flex;
                padding-bottom: 128px;
                flex-direction: column;
                justify-content: center;
                height: 80%;
            }}
        '''
    class_name = '.home-hero-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    padding-top: 96px;
                    padding-bottom: 96px;
                    height: auto;
                }}
            }}
        '''
    class_name = '.home-hero-title-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                margin-bottom: 64px;
                gap: 64px;
            }}
        '''
    class_name = '.home-hero-title-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                    margin-bottom: 0px;
                    gap: 16px;
                }}
            }}
        '''
    class_name = '.home-hero-content-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
            }}
        '''
    class_name = '.home-hero-content-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                    text-align: center;
                }}
            }}
        '''
    class_name = '.home-hero-buttons-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                gap: 24px;
            }}
        '''
    class_name = '.home-hero-buttons-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def home_proof():
    html = f'''
        <section>
            <div class="container-xl home-proof-section">
                <img src="/immagini/home/ministero-salute-italia-logo-grayscale.png" alt="">
                <img style="margin-bottom: 16px;" src="/immagini/home/commissione-europea-logo-grayscale.png" alt="">
                <img src="/immagini/home/food-drug-administration-usa-logo-grayscale.png" alt="">
                <img src="/immagini/home/ministero-salute-italia-logo-grayscale.png" alt="">
                <img style="margin-bottom: 16px;" src="/immagini/home/commissione-europea-logo-grayscale.png" alt="">
                <img src="/immagini/home/food-drug-administration-usa-logo-grayscale.png" alt="">
            </div>
        </section>
    '''
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.home-proof-section'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                gap: 24px;
                align-items: center;
            }}
        '''
    class_name = '.home-proof-section'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                    gap: 16px;
                }}
            }}
        '''
    class_name = '.home-proof-section img'
    if class_name not in css:
        css += f'''
            {class_name} {{
                flex: 1;
                opacity: 66%;
            }}
        '''
    class_name = '.home-proof-section img'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    width: 240px;
                    opacity: 50%;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def separator(text):
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    class_name = '.separator-section'
    if class_name not in css:
        css += f'''
            {class_name} {{
                margin-top: 96px;
                margin-bottom: 96px;
            }}
        '''
    class_name = '.separator-layout'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                align-items: center;
            }}
        '''
    class_name = '.separator-text'
    if class_name not in css:
        css += f'''
            {class_name} {{
                font-size: {g.typography_size_md};
                font-weight: normal;
                line-height: 24px;
                color: {g.color_light_gray};
                padding: 6px 12px;
                border-radius: 9999px;
                border: 1px solid {g.color_light_gray};
            }}
        '''
    class_name = '.separator-line'
    if class_name not in css:
        css += f'''
            {class_name} {{
                border-bottom: 1px solid {g.color_light_gray};
                width: 90%;
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    ###
    html = f'''
        <section class="container-xl separator-section">
            <div class="separator-layout">
                <h2 class="separator-text">{text}</h2>
                <div class="separator-line"></div>
            </div>
        </section>
    '''
    return html

def home_benefits():
    html_header = blocks.heading_default_1(
        title = components.h2_default(
            text = f'''Vantaggi del sistema ad ozono per gli operatori alimentari''',
            align = f'''left''',
        ),
        paragraph = components.paragraph_default(
            text = f'''Il sistema progettato da Ozonogroup offre numerosi vantaggi in termini di sicurezza, efficacia e sostenibilità, migliorando ogni fase del processo produttivo.''',
        ),
    )
    ###
    html_card_1 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'''01 - Sicurezza''',
        ),
        title = components.h3_default(
            text = f'Rispetta gli standard HACCP per la sicurezza alimentare',
        ),
        paragraph = components.paragraph_default(
            text = f'''L'ozono è riconosciuto a livello normativo come agente sanificante efficace e sicuro. L'automazione dei cicli di disinfezione garantisce la ripetibilità e tracciabilità dei processi, requisito fondamentale nei piani HACCP.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" viewBox="0 -960 960 960" fill="#1f1f1f">
                    <path d="M420-340h120v-100h100v-120H540v-100H420v100H320v120h100v100Zm60 260q-139-35-229.5-159.5T160-516v-244l320-120 320 120v244q0 152-90.5 276.5T480-80Zm0-84q104-33 172-132t68-220v-189l-240-90-240 90v189q0 121 68 220t172 132Zm0-316Z" />
                </svg>
            ''',
        ),
        link = components.link_default(
            link_text = f'''Learn more''',
            link_href = f'''#''',
        ),
    )
    html_card_2 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'''02 - Efficacia''',
        ),
        title = components.h3_default(
            text = f'Efficace su batteri, virus, muffe, odori e altri microrganismi',
        ),
        paragraph = components.paragraph_default(
            text = f'''L'ozono garantisce un'azione biocida completa, su aria, acqua e superfici. Riduce fino al 99,9% della carica microbica, inclusa Listeria monocytogenes, Salmonella spp., E. coli, Botrytis, e molti altri patogeni critici.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M450-80q-12 0-21-9t-9-21q0-12 9-21t21-9v-62q-42-5-79-20t-67-40l-43 44q9 9 9 21t-9 21q-9 9-21 9t-21-9l-43-42q-9-9-9-21.5t9-21.5q9-9 21-8.5t21 8.5l44-44q-25-31-40-67t-20-78h-62q0 12-9 21t-21 9q-12 0-21-9t-9-21v-60q0-12 9-21t21-9q12 0 21 9t9 21h62q5-42 20.5-78t39.5-67l-44-44q-9 8-21 8.5t-21-8.5q-9-9-9-21.5t9-21.5l42-42q9-9 21.5-9t21.5 9q9 9 9 21.5t-9 21.5l43 43q31-25 67-40t78-20v-62q-12 0-20.5-9t-8.5-21q0-12 9-21t21-9h60q12 0 21 9t9 21q0 12-9 21t-21 9v62q42 5 78 20t67 40l44-44q-9-9-9-21t9-21q9-9 21.5-9t21.5 9l42 43q9 9 9 21t-9 21q-9 9-21.5 9t-21.5-9l-43 43q25 31 40 67.5t20 78.5h62q0-12 9-21t21-9q12 0 21 9t9 21v60q0 12-9 21t-21 9q-12 0-21-9t-9-21h-62q-5 42-20 78.5T698-304l43 43q9-9 21.5-9t21.5 9q9 9 9 21.5t-9 21.5l-42 42q-9 9-21.5 9t-21.5-9q-9-9-8.5-21t8.5-21l-44-44q-31 25-67 40.5T510-201v61q12 0 21 9t9 21q0 12-9 21t-21 9h-60Zm30-200q83 0 141.5-58.5T680-480q0-83-58.5-141.5T480-680q-83 0-141.5 58.5T280-480q0 83 58.5 141.5T480-280Zm-70-40q17 0 28.5-11.5T450-360q0-17-11.5-28.5T410-400q-17 0-28.5 11.5T370-360q0 17 11.5 28.5T410-320Zm140 0q17 0 28.5-11.5T590-360q0-17-11.5-28.5T550-400q-17 0-28.5 11.5T510-360q0 17 11.5 28.5T550-320ZM340-440q17 0 28.5-11.5T380-480q0-17-11.5-28.5T340-520q-17 0-28.5 11.5T300-480q0 17 11.5 28.5T340-440Zm140 0q17 0 28.5-11.5T520-480q0-17-11.5-28.5T480-520q-17 0-28.5 11.5T440-480q0 17 11.5 28.5T480-440Zm140 0q17 0 28.5-11.5T660-480q0-17-11.5-28.5T620-520q-17 0-28.5 11.5T580-480q0 17 11.5 28.5T620-440ZM410-560q17 0 28.5-11.5T450-600q0-17-11.5-28.5T410-640q-17 0-28.5 11.5T370-600q0 17 11.5 28.5T410-560Zm140 0q17 0 28.5-11.5T590-600q0-17-11.5-28.5T550-640q-17 0-28.5 11.5T510-600q0 17 11.5 28.5T550-560Zm-70 80Z" />
                </svg>
            ''',
        ),
        link = components.link_default(
            link_text = f'''Learn more''',
            link_href = f'''#''',
        ),
    )
    html_card_3 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'''03 - Sostenibilità''',
        ),
        title = components.h3_default(
            text = f'Sanifica in modo ecologico, senza uso di sostanze chimiche',
        ),
        paragraph = components.paragraph_default(
            text = f'''L'ozono è un gas naturale che si decompone in ossigeno, senza lasciare residui. Elimina microrganismi patogeni senza generare rifiuti pericolosi o sostanze tossiche. Riduce l'uso di acqua, detersivi, e sanificanti convenzionali.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M216-176q-45-45-70.5-104T120-402q0-63 24-124.5T222-642q35-35 86.5-60t122-39.5Q501-756 591.5-759t202.5 7q8 106 5 195t-16.5 160.5q-13.5 71.5-38 125T684-182q-53 53-112.5 77.5T450-80q-65 0-127-25.5T216-176Zm112-16q29 17 59.5 24.5T450-160q46 0 91-18.5t86-59.5q18-18 36.5-50.5t32-85Q709-426 716-500.5t2-177.5q-49-2-110.5-1.5T485-670q-61 9-116 29t-90 55q-45 45-62 89t-17 85q0 59 22.5 103.5T262-246q42-80 111-153.5T534-520q-72 63-125.5 142.5T328-192Zm0 0Zm0 0Z" />
                </svg>
            ''',
        ),
        link = components.link_default(
            link_text = f'''Learn more''',
            link_href = f'''#''',
        ),
    )
    html = f'''
        <section class="container-xl">
            {html_header}
            <div class="home-benefits-cards-container">
                <div style="flex: 1;">
                    {html_card_1}
                </div>
                <div style="flex: 1;">
                    {html_card_2}
                </div>
                <div style="flex: 1;">
                    {html_card_3}
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.home-benefits-intro-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                align-items: center;
                gap: 48px;
                margin-bottom: 32px;
            }}
        '''
    class_name = '.home-benefits-cards-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                gap: 24px;
            }}
        '''
    class_name = '.home-benefits-cards-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                }}
            }}
        '''
    class_name = '.home-benefits-cards-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def home_services():
    html_heading = blocks.heading_default_2(
        title = components.h2_default(
            text = f'''Tecnologia personalizzata per ogni esigenza dell'industria alimentare''',
            align = f'''center''',
            align_mobile = f'''left''',
        ),
        paragraph = components.paragraph_default(
            text = f'''I nostri sistemi di sanificazione all'ozono sono progettati su misura per adattarsi a ogni fase del processo produttivo. Che tu operi nella trasformazione, nel confezionamento o nella logistica, Ozonogroup ha una soluzione efficace, sicura e automatizzata.''',
            align = f'''center''',
            align_mobile = f'''left''',
        ),
    )
    html_card_1 = blocks.card_default_2(
        icon = components.icon_default(
            svg = f'''
                <svg style="margin-bottom: 16px;" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M784-120 532-372q-30 24-69 38t-83 14q-109 0-184.5-75.5T120-580q0-109 75.5-184.5T380-840q109 0 184.5 75.5T640-580q0 44-14 83t-38 69l252 252-56 56ZM380-400q75 0 127.5-52.5T560-580q0-75-52.5-127.5T380-760q-75 0-127.5 52.5T200-580q0 75 52.5 127.5T380-400Z" />
                </svg>
            ''',
        ),
        title = components.h3_default(
            text = f'''1. Analisi e Valutazione''',
        ),
        paragraph = components.paragraph_default(
            text = f'''Analizziamo il tuo ambiente produttivo, i rischi biologici specifici e le necessita operative per proporre una soluzione su misura basata sull'ozono.''',
        ),
    )
    html_card_2 = blocks.card_default_2(
        icon = components.icon_default(
            svg = f'''
                <svg style="margin-bottom: 16px;" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="m352-522 86-87-56-57-44 44-56-56 43-44-45-45-87 87 159 158Zm328 329 87-87-45-45-44 43-56-56 43-44-57-56-86 86 158 159Zm24-567 57 57-57-57ZM290-120H120v-170l175-175L80-680l200-200 216 216 151-152q12-12 27-18t31-6q16 0 31 6t27 18l53 54q12 12 18 27t6 31q0 16-6 30.5T816-647L665-495l215 215L680-80 465-295 290-120Zm-90-80h56l392-391-57-57-391 392v56Zm420-419-29-29 57 57-28-28Z" />
                </svg>
            ''',
        ),
        title = components.h3_default(
            text = f'''2. Progettazione e Realizzazione''',
        ),
        paragraph = components.paragraph_default(
            text = f'''Sviluppiamo una soluzione su misura, combinando le migliori tecnologie a ozono con un design personalizzato per otimizzare igiene, efficienza e sostenibilita.''',
        ),
    )
    html_card_3 = blocks.card_default_2(
        icon = components.icon_default(
            svg = f'''
                <svg style="margin-bottom: 16px;" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M686-132 444-376q-20 8-40.5 12t-43.5 4q-100 0-170-70t-70-170q0-36 10-68.5t28-61.5l146 146 72-72-146-146q29-18 61.5-28t68.5-10q100 0 170 70t70 170q0 23-4 43.5T584-516l244 242q12 12 12 29t-12 29l-84 84q-12 12-29 12t-29-12Zm29-85 27-27-256-256q18-20 26-46.5t8-53.5q0-60-38.5-104.5T386-758l74 74q12 12 12 28t-12 28L332-500q-12 12-28 12t-28-12l-74-74q9 57 53.5 95.5T360-440q26 0 52-8t47-25l256 256ZM472-488Z" />
                </svg>
            ''',
        ),
        title = components.h3_default(
            text = f'''3. Installazione e Formazione''',
        ),
        paragraph = components.paragraph_default(
            text = f'''Il nostro team tecnico si occupa dell'installazione e forma il tuo personale sull'utilizzo sicuro e ottimale del sistema.''',
        ),
    )
    html_card_4 = blocks.card_default_2(
        icon = components.icon_default(
            svg = f'''
                <svg style="margin-bottom: 16px;" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M240-400h320v-80H240v80Zm0-120h480v-80H240v80Zm0-120h480v-80H240v80ZM80-80v-720q0-33 23.5-56.5T160-880h640q33 0 56.5 23.5T880-800v480q0 33-23.5 56.5T800-240H240L80-80Zm126-240h594v-480H160v525l46-45Zm-46 0v-480 480Z" />
                </svg>
            ''',
        ),
        title = components.h3_default(
            text = f'''4. Assistenza e Manutenzione''',
        ),
        paragraph = components.paragraph_default(
            text = f'''Forniamo supporto tecnico continuo e piano di manutenzione preventiva per assicurare performance costanti e conformita normativa nel tempo.''',
        ),
    )
    html_cards = f'''
        <div class="home-services-cards-container">
            <div style="flex: 1;">
                <div style="display: flex; flex-direction: column; gap: 24px;">
                    {html_card_1}
                    {html_card_2}
                </div>
            </div>
            <div style="flex: 1;">
                <div class="home-services-card-offset">
                    {html_card_3}
                    {html_card_4}
                </div>
            </div>
        </div>
    '''
    html = f'''
        <section class="container-xl">
            {html_heading}
            {html_cards}
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.home-services-intro-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 768px;
                margin-right: auto;
                margin-left: auto;
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-bottom: 32px;
            }}
        '''
    class_name = '.home-services-cards-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                gap: 24px;
                margin-bottom: 32px;
            }}
        '''
    class_name = '.home-services-cards-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                }}
            }}
        '''
    class_name = '.home-services-card-offset'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                flex-direction: column;
                gap: 24px;
                margin-top: 48px;
            }}
        '''
    class_name = '.home-services-card-offset'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    margin-top: 0;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html
    
def home_sectors():
    html_heading = blocks.heading_default_2(
        title = components.h2_default(
            text = f'''Soluzioni specifiche per ogni filiera alimentare''',
        ),
        paragraph = components.paragraph_default(
            text = f'''Ogni settore dell'industria alimentare ha esigenze diverse in termini di igiene, normativa e tipo di contaminazione microbiologica. I sistemi di sanificazione all'ozono di Ozonogroup sono progettati per adattarsi perfettamente a questi contesti, garantendo efficacia microbiologica, sostenibilità ambientale e conformità normativa.''',
        ),
    )
    html_card_1 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'''01''',
        ),
        title = components.h3_default(
            text = f'Carne e Pollame',
        ),
        paragraph = components.paragraph_default(
            text = f'''Sanificazione profonda in ambienti ad alto rischio microbiologico. Eliminazione di patogeni come Salmonella, Listeria e E. coli da superfici, macchinari e ambienti. Sistemi integrati nelle linee di disosso, sezionamento e confezionamento. Controllo degli odori e prevenzione della formazione di biofilm.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M250-40v-160h-30q-42 0-71-29t-29-71q0-42 29-71t71-29h30v-40H120v-200h130v-40h-30q-42 0-71-29t-29-71q0-42 29-71t71-29h30v-40h60v40h30q42 0 71 29t29 71q0 42-29 71t-71 29h-30v40h130v200H310v40h30q42 0 71 29t29 71q0 42-29 71t-71 29h-30v160h-60Zm400 0v-160h-30q-42 0-71-29t-29-71q0-42 29-71t71-29h30v-40H520v-200h130v-40h-30q-42 0-71-29t-29-71q0-42 29-71t71-29h30v-40h60v40h30q42 0 71 29t29 71q0 42-29 71t-71 29h-30v40h130v200H710v40h30q42 0 71 29t29 71q0 42-29 71t-71 29h-30v160h-60ZM220-760h120q8 0 14-6t6-14q0-8-6-14t-14-6H220q-8 0-14 6t-6 14q0 8 6 14t14 6Zm400 0h120q8 0 14-6t6-14q0-8-6-14t-14-6H620q-8 0-14 6t-6 14q0 8 6 14t14 6ZM200-520h160v-40H200v40Zm400 0h160v-40H600v40ZM220-280h120q8 0 14-6t6-14q0-8-6-14t-14-6H220q-8 0-14 6t-6 14q0 8 6 14t14 6Zm400 0h120q8 0 14-6t6-14q0-8-6-14t-14-6H620q-8 0-14 6t-6 14q0 8 6 14t14 6ZM200-760v-40 40Zm400 0v-40 40ZM200-520v-40 40Zm400 0v-40 40ZM200-280v-40 40Zm400 0v-40 40Z" />
                </svg>
            ''',
        ),
        link = components.link_default(
            link_text = f'''Scopri Settori''',
            link_href = f'''/settori.html''',
        ),
    )
    html_card_2 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'''02''',
        ),
        title = components.h3_default(
            text = f'Pesce e Frutti di Mare',
        ),
        paragraph = components.paragraph_default(
            text = f'''Igiene in ambienti umidi, a bassa temperatura e ad alto carico organico. Ozono efficace anche in ambienti freddi (5°C), ideale per celle e zone di lavorazione pesce. Riduzione della carica batterica su filetti, crostacei, superfici e nastri trasportatori. Prolungamento della shelf-life senza additivi chimici.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M440-120q-100 0-170-70t-70-170v-240l200 200-56 57-64-64v47q0 66 47 113t113 47q66 0 113-47t47-113v-127q-36-14-58-44.5T520-600q0-38 22-68.5t58-44.5v-167h80v167q36 14 58 44.5t22 68.5q0 38-22 69t-58 44v127q0 100-70 170t-170 70Zm200-440q17 0 28.5-11.5T680-600q0-17-11.5-28.5T640-640q-17 0-28.5 11.5T600-600q0 17 11.5 28.5T640-560Zm0-40Z" />
                </svg>
            ''',
        ),
        link = components.link_default(
            link_text = f'''Scopri Settori''',
            link_href = f'''/settori.html''',
        ),
    )
    html_card_3 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'''03''',
        ),
        title = components.h3_default(
            text = f'Ortofrutta',
        ),
        paragraph = components.paragraph_default(
            text = f'''Sanificazione post-raccolta, durante lo stoccaggio e nel confezionamento. Rimozione di muffe e lieviti (Botrytis, Penicillium) responsabili del deterioramento precoce. Disinfezione di casse, nastri, vasche di lavaggio e aria nelle aree di confezionamento.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M480-120q-117 0-198.5-81.5T200-400q0-94 55.5-168.5T401-669q-20-5-39-14.5T328-708q-33-33-42.5-78.5T281-879q47-5 92.5 4.5T452-832q23 23 33.5 52t13.5 61q13-31 31.5-58.5T572-828q11-11 28-11t28 11q11 11 11 28t-11 28q-22 22-39 48.5T564-667q88 28 142 101.5T760-400q0 117-81.5 198.5T480-120Zm0-80q83 0 141.5-58.5T680-400q0-83-58.5-141.5T480-600q-83 0-141.5 58.5T280-400q0 83 58.5 141.5T480-200Zm0-200Z" />
                </svg>
            ''',
        ),
        link = components.link_default(
            link_text = f'''Scopri Settori''',
            link_href = f'''/settori.html''',
        ),
    )
    html_card_4 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'''04''',
        ),
        title = components.h3_default(
            text = f'Latticini e Derivati del Latte',
        ),
        paragraph = components.paragraph_default(
            text = f'''Controllo microbiologico in ambienti sensibili alla contaminazione crociata. Rimozione di Listeria monocytogenes in vasche, superfici e impianti CIP. Disinfezione di aria e superfici nelle aree di fermentazione e maturazione. Sistemi compatibili con ambienti ad alta umidità e carico proteico.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M482-40 294-400q-71 3-122.5-41T120-560q0-51 29.5-92t74.5-58q18-91 89.5-150.5T480-920q95 0 166.5 59.5T736-710q45 17 74.5 58t29.5 92q0 75-53 119t-119 41L482-40ZM280-480q15 0 29.5-5t26.5-17l22-22 26 16q21 14 45.5 21t50.5 7q26 0 50.5-7t45.5-21l26-16 22 22q12 12 26.5 17t29.5 5q33 0 56.5-23.5T760-560q0-30-19-52.5T692-640l-30-4-2-32q-5-69-57-116.5T480-840q-71 0-123 47.5T300-676l-2 32-30 6q-30 6-49 27t-19 51q0 33 23.5 56.5T280-480Zm202 266 108-210q-24 12-52 18t-58 6q-27 0-54.5-6T372-424l110 210Zm-2-446Z" />
                </svg>
            ''',
        ),
        link = components.link_default(
            link_text = f'''Scopri Settori''',
            link_href = f'''/settori.html''',
        ),
    )
    html_card_5 = blocks.card_default_1(
        suptitle = components.suptitle_default(
            text = f'''05''',
        ),
        title = components.h3_default(
            text = f'Bevande e Imbottigliamento',
        ),
        paragraph = components.paragraph_default(
            text = f'''Igienizzazione delle linee e prevenzione di alterazioni microbiologiche nei liquidi. Ozono in forma gassosa e acquosa per la sanificazione di serbatoi, tubazioni, riempitrici. Sistemi integrati nei processi CIP e SIP. Nessun residuo chimico: ideale per produzione biologica o senza conservanti.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M491-200q12-1 20.5-9.5T520-230q0-14-9-22.5t-23-7.5q-41 3-87-22.5T343-375q-2-11-10.5-18t-19.5-7q-14 0-23 10.5t-6 24.5q17 91 80 130t127 35ZM480-80q-137 0-228.5-94T160-408q0-100 79.5-217.5T480-880q161 137 240.5 254.5T800-408q0 140-91.5 234T480-80Zm0-80q104 0 172-70.5T720-408q0-73-60.5-165T480-774Q361-665 300.5-573T240-408q0 107 68 177.5T480-160Zm0-320Z" />
                </svg>
            ''',
        ),
        link = components.link_default(
            link_text = f'''Scopri Settori''',
            link_href = f'''/settori.html''',
        ),
    )
    html = f'''
        <section class="container-xl">
            <div class="home-industries-cards-container">
                <div style="flex: 1;">
                    {html_heading}
                    <!-- <a style="display: inline-block; color: #0f1f2e; padding: 8px 16px; border-radius: 9999px; border: 1px solid #0f1f2e; text-decoration-line: none;"
                    href="#">Come funziona</a> -->
                </div>
                <div style="flex: 1;">
                    {html_card_1}
                </div>
                <div style="flex: 1;">
                    {html_card_2}
                </div>
            </div>
            <div class="home-industries-cards-container">
                <div style="flex: 1;">
                    {html_card_3}
                </div>
                <div style="flex: 1;">
                    {html_card_4}
                </div>
                <div style="flex: 1;">
                    {html_card_5}
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.home-industries-cards-container'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                display: flex;
                gap: 24px;
                margin-bottom: 24px;
            }}
        '''
    class_name = '.home-industries-cards-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def home_about():
    html_heading = blocks.heading_default_2(
        title = components.h2_default(
            text = f'''Perché scegliere Ozonogroup?''',
        ),
        paragraph = components.paragraph_default(
            text = f'''Ozonogroup progetta sistemi di sanificazione all'ozono su misura per l'industria alimentare, garantendo igiene, sicurezza e conformità normativa. Con esperienza pluriennale e un reparto R&D interno, offriamo soluzioni affidabili, supporto tecnico continuo e formazione. Riduci l'uso di chimici e migliora la qualità produttiva con una tecnologia sicura e sostenibile.''',
        ),
    )
    html = f'''
        <section class="container-xl">
            <div style="display: flex; flex-direction: column; gap: 32px;">
                <div class="home-about-intro-container">
                    <div style="flex: 1;">
                        <img style="height: 400px; object-fit: cover; border-radius: 16px;"
                            src="/immagini/home/batteri.webp" alt="">
                    </div>
                    <div style="flex: 1;">
                        {html_heading}
                    </div>
                </div>
                <div class="home-about-images-container">
                    <div style="flex: 1;">
                        <img style="height: 400px; object-fit: cover; border-radius: 16px;"
                            src="/immagini/home/odori.webp" alt="">
                    </div>
                    <div style="flex: 2;">
                        <img style="height: 400px; object-fit: cover; border-radius: 16px;"
                            src="/immagini/home/muffe.webp" alt="">
                    </div>
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.home-about-intro-container'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                display: flex;
                align-items: center;
                gap: 32px;
            }}
        '''
    class_name = '.home-about-intro-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                }}
            }}
        '''
    class_name = '.home-about-images-container'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                display: flex;
                align-items: center;
                gap: 32px;
            }}
        '''
    class_name = '.home-about-images-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def home_contact():
    html_h2_reverse = components.h2_reverse(
        text = f'''
            Pronto a rivoluzionare la sicurezza del tuo impianto alimentare?
        ''',
        align = f'''left''',
        align_mobile = f'''center''',
    )
    html_paragraph_reverse = components.paragraph_reverse(
        text = f'''
            Che tu stia cercando un sistema completo di sanificazione all'ozono, un audit tecnico, o semplicemente vuoi capire come integrare l'ozono nei tuoi processi, Ozonogroup è il partner giusto per te.
        '''
    )
    html_button_fill_reverse = components.button_fill_reverse('Conoscici meglio', '/contatti.html')
    html_button_ghost_reverse = components.button_ghost_reverse('Come funziona', '/contatti.html')
    html_email = blocks.contact_reverse(
        icon = f'''
            <svg xmlns="http://www.w3.org/2000/svg" height="32px" viewBox="0 -960 960 960" width="32px" fill="#ffffff">
                <path
                    d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm320-280L160-640v400h640v-400L480-440Zm0-80 320-200H160l320 200ZM160-640v-80 480-400Z" />
            </svg>
        ''',
        cta = f'''
            Mandaci una email
        ''',
        contact = f'''
            info@ozonogroup.it
        ''',
    )
    html_phone = blocks.contact_reverse(
        icon = f'''
            <svg xmlns="http://www.w3.org/2000/svg" height="32px" viewBox="0 -960 960 960" width="32px" fill="#ffffff">
                <path
                    d="M798-120q-125 0-247-54.5T329-329Q229-429 174.5-551T120-798q0-18 12-30t30-12h162q14 0 25 9.5t13 22.5l26 140q2 16-1 27t-11 19l-97 98q20 37 47.5 71.5T387-386q31 31 65 57.5t72 48.5l94-94q9-9 23.5-13.5T670-390l138 28q14 4 23 14.5t9 23.5v162q0 18-12 30t-30 12ZM241-600l66-66-17-94h-89q5 41 14 81t26 79Zm358 358q39 17 79.5 27t81.5 13v-88l-94-19-67 67ZM241-600Zm358 358Z" />
            </svg>
        ''',
        cta = f'''
            Chiamaci
        ''',
        contact = f'''
            +39 0423 952833
        ''',
    )
    html = f'''
        <section class="container-xl" style="margin-bottom: 96px;">
            <div
                style="border-radius: 16px; border-bottom-left-radius: 16px;
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/immagini/home/sanificazione-ozono.png');
            background-size: cover; background-position: center; padding-top: 96px; padding-bottom: 96px; padding-left: 48px; padding-right: 48px;">
                <div class="home-contact-intro-container">
                    <div style="flex: 1;">
                        {html_h2_reverse}
                    </div>
                    <div style="flex: 1;">
                        <div class="home-contact-intro-content">
                            <div style="flex: 1;">
                                {html_email}
                            </div>
                            <div style="flex: 1;">
                                {html_phone}
                            </div>
                        </div>
                    </div>
                </div>
                <hr style="color: rgba(255, 255, 255, 0.33); margin-bottom: 32px;">
                <div class="home-contact-cta-container">
                    <div style="flex: 1;">
                        <div class="home-contact-cta-buttons">
                            {html_button_fill_reverse}
                            {html_button_ghost_reverse}
                        </div>
                    </div>
                    <div style="flex: 1;">
                        {html_paragraph_reverse}
                    </div>
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.home-contact-intro-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                gap: 96px;
                margin-bottom: 32px;
                align-items: center;
            }}
        '''
    class_name = '.home-contact-intro-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                    gap: 0;
                }}
            }}
        '''
    class_name = '.home-contact-intro-title'
    if class_name not in css:
        css += f'''
            {class_name} {{
                font-size: 48px;
                line-height: 56px;
                color: #ffffff;
            }}
        '''
    class_name = '.home-contact-intro-content'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                gap: 24px;
            }}
        '''
    class_name = '.home-contact-intro-content'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                    gap: 0;
                }}
            }}
        '''
    class_name = '.home-contact-cta-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                gap: 96px;
            }}
        '''
    class_name = '.home-contact-cta-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                    gap: 1.6rem;
                }}
            }}
        '''
    class_name = '.home-contact-cta-buttons'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                gap: 8px;
            }}
        '''
    class_name = '.home-contact-cta-buttons'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

##########################################################

def prodotti_hero():
    html_heading = components.h1_reverse(
        text = f'''Prodotti''',
        align_mobile = 'center',
    )
    html_paragraph = components.paragraph_reverse(
        text = f'''I generatori ad ozono di Ozonogroup offrono una soluzione ecologica ed efficace per la sanificazione e il trattamento dell'aria e dell'acqua. Grazie alle loro proprietà ossidanti, garantiscono un'igiene profonda eliminando batteri, virus e odori senza l'utilizzo di agenti chimici.''',
        align_mobile = 'center',
        margin_bottom = '0',
    )
    html = f'''
        <section class="prodotti-hero-section">
            <div class="container-xl">
                {html_heading}
                {html_paragraph}
            </div>
        </section>
    '''
    with open('styles/tmp/pag-prodotti.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-prodotti-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.prodotti-hero-section'
    if class_name not in css:
        css += f'''
            {class_name} {{
                background: {g.color_black_pearl};
                margin-bottom: 96px;
                padding-top: 6.4rem;
                padding-bottom: 6.4rem;
                border-bottom-left-radius: {g.border_radius_xl};
                border-bottom-right-radius: {g.border_radius_xl};
            }}
        '''
    with open('styles/tmp/pag-prodotti.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-prodotti-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def prodotti_piccole():
    html_card_1 = blocks.card_itp_default(
        image = f'''
            <img 
                style="width: 240px; height: 200px; object-fit: cover;"
                src="/immagini/prodotti/ozonogroup-ozonizzatore-mini-transparent.png" 
                alt="ozonizzatore mini di ozonogroup">
        ''', 
        title = components.h3_default(
            text = f'''Mini''',
        ), 
        paragraph = components.paragraph_default(
            text = f'''Generatore compatto e disponibile in diversi modelli, progettato per purificare l'aria in ambienti di dimensioni contenute.''',
        ),
    )
    html_card_2 = blocks.card_itp_default(
        image = f'''
            <img 
                style="width: 240px; height: 200px; object-fit: cover;"
                src="/immagini/prodotti/ozonogroup-ozonizzatore-nymphea-transparent.png" 
                alt="ozonizzatore nymphea di ozonogroup">
        ''', 
        title = components.h3_default(
            text = f'''Nymphea''',
        ), 
        paragraph = components.paragraph_default(
            text = f'''Generatore pratico e funzionale, progettato specificamente per il trattamento dell'acqua in contesti domestici e di piccola scala.''',
        ),
    )
    html = f'''
        <section class="container-xl">
            <div class="prodotti-cards-layout">
                {html_card_1}
                {html_card_2}
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-prodotti.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-prodotti-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.prodotti-cards-layout'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 48px;
            }}
        '''
    with open('styles/tmp/pag-prodotti.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-prodotti-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def prodotti_medie():
    html_card_1 = blocks.card_itp_default(
        image = f'''
            <img 
                style="width: 240px; height: 200px; object-fit: cover;"
                src="/immagini/prodotti/ozonogorup-ozonizzatore-bigpower-transparent.png" 
                alt="ozonizzatore bigpower di ozonogroup">
        ''', 
        title = components.h3_default(
            text = f'''Bigpower''',
        ), 
        paragraph = components.paragraph_default(
            text = f'''Generatore di media potenza è disponibile in più configurazioni e garantisce un'efficace sanificazione dell'aria.''',
        ),
    )
    html_card_2 = blocks.card_itp_default(
        image = f'''
            <img 
                style="width: 240px; height: 200px; object-fit: cover;"
                src="/immagini/prodotti/ozonogroup-ozonizzatore-lympha-transparent.png" 
                alt="ozonizzatore lympha di ozonogroup">
        ''', 
        title = components.h3_default(
            text = f'''Lympha''',
        ), 
        paragraph = components.paragraph_default(
            text = f'''Generatore di media potenza progettato per il trattamento dell'acqua in sistemi di media grandezza.''',
        ),
    )
    html = f'''
        <section class="container-xl">
            <div class="prodotti-cards-layout">
                {html_card_1}
                {html_card_2}
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-prodotti.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-prodotti-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.prodotti-cards-layout'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 48px;
            }}
        '''
    with open('styles/tmp/pag-prodotti.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-prodotti-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def prodotti_grandi():
    html_card_1 = blocks.card_itp_default(
        image = f'''
            <img 
                style="width: 240px; height: 200px; object-fit: cover;"
                src="/immagini/prodotti/ozonogroup-ozonizzatore-greenozone-transparent.png" 
                alt="ozonizzatore greenozone di ozonogroup">
        ''', 
        title = components.h3_default(
            text = f'''Greenozone''',
        ), 
        paragraph = components.paragraph_default(
            text = f'''Generatore ad alta capacità progettato per trattare grandi volumi d'aria in ambienti industriali.''',
        ),
    )
    html_card_2 = blocks.card_itp_default(
        image = f'''
            <img 
                style="width: 240px; height: 200px; object-fit: cover;"
                src="/immagini/prodotti/ozonogroup-ozonizzatore-hydor-transparent.png" 
                alt="ozonizzatore hydor di ozonogroup">
        ''', 
        title = components.h3_default(
            text = f'''Hydor''',
        ), 
        paragraph = components.paragraph_default(
            text = f'''Generatore potente e altamente affidabile, specifico per il trattamento dell'acqua in impianti di grandi dimensioni.''',
        ),
    )
    html_card_3 = blocks.card_itp_default(
        image = f'''
            <img 
                style="width: 240px; height: 200px; object-fit: cover;"
                src="/immagini/prodotti/ozonogorup-ozonizzatore-delta-transparent.png" 
                alt="ozonizzatore delta di ozonogroup">
        ''', 
        title = components.h3_default(
            text = f'''Delta''',
        ), 
        paragraph = components.paragraph_default(
            text = f'''Generatore di ultima generazione, dotato di schermo touch per un controllo avanzato dei parametri.''',
        ),
    )
    html = f'''
        <section class="container-xl">
            <div class="prodotti-cards-layout">
                {html_card_1}
                {html_card_2}
                {html_card_3}
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-prodotti.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-prodotti-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.prodotti-cards-layout'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 48px;
            }}
        '''
    with open('styles/tmp/pag-prodotti.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-prodotti-mobile.css', 'w') as f: f.write(css_mobile)
    return html

##########################################################

def settori_grid():
    html_heading = blocks.heading_default_2(
        title = components.h1_default(
            text = f'''Settori di applicazione della sanificazione ozono''',
            align = f'center',
        ),
        paragraph = components.paragraph_default(
            text = f'''La sanificazione ad ozono viene applicata nel settore lattiero-caseario, carni, ittico, ortofrutticolo, ittico e altri, per eliminare microrganismi patogeni, produrre alimenti sicuri e salvaguardare la salute dei consumatori. Qui sotto trovi una lista dettagliata dei settori dove l'ozono viene impiegato.''',
            align = f'center',
        ),
    )
    html_card_1 = blocks.card_default_1(
        title = components.h3_default(
            text = f'Lattiero-Caseario',
        ),
        paragraph = components.paragraph_default(
            text = f'''La sanificazione ad ozono nel lattiero-caseario elimina microrganismi da ambienti, attrezzature e aria, prolungando la shelf life senza residui chimici.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M482-40 294-400q-71 3-122.5-41T120-560q0-51 29.5-92t74.5-58q18-91 89.5-150.5T480-920q95 0 166.5 59.5T736-710q45 17 74.5 58t29.5 92q0 75-53 119t-119 41L482-40ZM280-480q15 0 29.5-5t26.5-17l22-22 26 16q21 14 45.5 21t50.5 7q26 0 50.5-7t45.5-21l26-16 22 22q12 12 26.5 17t29.5 5q33 0 56.5-23.5T760-560q0-30-19-52.5T692-640l-30-4-2-32q-5-69-57-116.5T480-840q-71 0-123 47.5T300-676l-2 32-30 6q-30 6-49 27t-19 51q0 33 23.5 56.5T280-480Zm202 266 108-210q-24 12-52 18t-58 6q-27 0-54.5-6T372-424l110 210Zm-2-446Z" />
                </svg>
            ''',
        ),
        link = components.link_default(
            link_text = f'''Scopri Applicazioni''',
            link_href = f'''/settori/lattiero-caseario.html''',
        ),
    )
    html_card_2 = blocks.card_default_1(
        title = components.h3_default(
            text = f'Carni',
        ),
        paragraph = components.paragraph_default(
            text = f'''La sanificazione ad ozono elimina batteri, muffe e odori da ambienti, superfici e celle frigorifere, migliorando sicurezza igienica e conservabilità della carne.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M250-40v-160h-30q-42 0-71-29t-29-71q0-42 29-71t71-29h30v-40H120v-200h130v-40h-30q-42 0-71-29t-29-71q0-42 29-71t71-29h30v-40h60v40h30q42 0 71 29t29 71q0 42-29 71t-71 29h-30v40h130v200H310v40h30q42 0 71 29t29 71q0 42-29 71t-71 29h-30v160h-60Zm400 0v-160h-30q-42 0-71-29t-29-71q0-42 29-71t71-29h30v-40H520v-200h130v-40h-30q-42 0-71-29t-29-71q0-42 29-71t71-29h30v-40h60v40h30q42 0 71 29t29 71q0 42-29 71t-71 29h-30v40h130v200H710v40h30q42 0 71 29t29 71q0 42-29 71t-71 29h-30v160h-60ZM220-760h120q8 0 14-6t6-14q0-8-6-14t-14-6H220q-8 0-14 6t-6 14q0 8 6 14t14 6Zm400 0h120q8 0 14-6t6-14q0-8-6-14t-14-6H620q-8 0-14 6t-6 14q0 8 6 14t14 6ZM200-520h160v-40H200v40Zm400 0h160v-40H600v40ZM220-280h120q8 0 14-6t6-14q0-8-6-14t-14-6H220q-8 0-14 6t-6 14q0 8 6 14t14 6Zm400 0h120q8 0 14-6t6-14q0-8-6-14t-14-6H620q-8 0-14 6t-6 14q0 8 6 14t14 6ZM200-760v-40 40Zm400 0v-40 40ZM200-520v-40 40Zm400 0v-40 40ZM200-280v-40 40Zm400 0v-40 40Z" />
                </svg>
            ''',
        ),
    )
        # link = components.link_default(
        #     link_text = f'''Scopri Applicazioni''',
        #     link_href = f'''/settori/carni.html''',
        # ),
    html_card_3 = blocks.card_default_1(
        title = components.h3_default(
            text = f'Ittico',
        ),
        paragraph = components.paragraph_default(
            text = f'''Nel settore ittico, l'ozono sanifica pesce, ambienti e acque, riduce batteri, prolunga la conservazione e migliora l'igiene senza residui chimici.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M440-120q-100 0-170-70t-70-170v-240l200 200-56 57-64-64v47q0 66 47 113t113 47q66 0 113-47t47-113v-127q-36-14-58-44.5T520-600q0-38 22-68.5t58-44.5v-167h80v167q36 14 58 44.5t22 68.5q0 38-22 69t-58 44v127q0 100-70 170t-170 70Zm200-440q17 0 28.5-11.5T680-600q0-17-11.5-28.5T640-640q-17 0-28.5 11.5T600-600q0 17 11.5 28.5T640-560Zm0-40Z" />
                </svg>
            ''',
        ),
    )
        # link = components.link_default(
        #     link_text = f'''Scopri Applicazioni''',
        #     link_href = f'''/settori/ittico.html''',
        # ),
    html_card_4 = blocks.card_default_1(
        title = components.h3_default(
            text = f'Ortofrutticolo',
        ),
        paragraph = components.paragraph_default(
            text = f'''La sanificazione ad ozono nel settore ortofrutticolo igienizza aria, superfici e prodotti, riduce batteri, muffe e odori, prolungando freschezza e sicurezza.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M480-120q-117 0-198.5-81.5T200-400q0-94 55.5-168.5T401-669q-20-5-39-14.5T328-708q-33-33-42.5-78.5T281-879q47-5 92.5 4.5T452-832q23 23 33.5 52t13.5 61q13-31 31.5-58.5T572-828q11-11 28-11t28 11q11 11 11 28t-11 28q-22 22-39 48.5T564-667q88 28 142 101.5T760-400q0 117-81.5 198.5T480-120Zm0-80q83 0 141.5-58.5T680-400q0-83-58.5-141.5T480-600q-83 0-141.5 58.5T280-400q0 83 58.5 141.5T480-200Zm0-200Z" />
                </svg>
            ''',
        ),
    )
        # link = components.link_default(
        #     link_text = f'''Scopri Applicazioni''',
        #     link_href = f'''/settori/ortofrutticolo.html''',
        # ),
    html_card_5 = blocks.card_default_1(
        title = components.h3_default(
            text = f'Vinicolo',
        ),
        paragraph = components.paragraph_default(
            text = f'''La sanificazione ad ozono nel settore vinicolo elimina batteri, muffe e lieviti da attrezzature, bottiglie, uve e ambienti, garantendo qualità e sicurezza.''',
        ),
        icon = components.icon_default(
            svg = f'''
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f">
                    <path d="M320-120v-80h120v-164q-86-14-143-80t-57-156v-240h480v240q0 90-57 156t-143 80v164h120v80H320Zm160-320q56 0 98-34t56-86H326q14 52 56 86t98 34ZM320-640h320v-120H320v120Zm160 200Z" />
                </svg>
            ''',
        ),
    )
    html = f'''
        <section class="container-xl" style="margin-top: 6.4rem; margin-bottom: 6.4rem;">
            {html_heading}
            <div class="home-industries-cards-container">
                <div style="flex: 1;">
                    {html_card_1}
                </div>
                <div style="flex: 1;">
                    {html_card_2}
                </div>
                <div style="flex: 1;">
                    {html_card_3}
                </div>
            </div>
            <div class="home-industries-cards-container">
                <div style="flex: 1;">
                    {html_card_4}
                </div>
                <div style="flex: 1;">
                    {html_card_5}
                </div>
                <div style="flex: 1;">
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.home-industries-cards-container'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                display: flex;
                gap: 24px;
                margin-bottom: 24px;
            }}
        '''
    class_name = '.home-industries-cards-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

##########################################################

def contatti_section_1():
    html_heading = blocks.heading_default_1(
        title = components.h1_default(
            text = f'''Consulta il nostro team di esperti''',
            align = f'center',
            align_mobile = f'left',
        ),
        paragraph = components.paragraph_default(
            text = f'''Se vuoi prenotare una consulenza gratuita o hai bisogno di un'informazione veloce, usa uno dei contatti qui sotto.''',
            align = f'center',
            align_mobile = f'left',
            margin_bottom = '0',
        ),
    )
    html_contact_card_default_1 = blocks.contact_card_default(
        icon = f'''
            <svg style="color: #0f1f2e;" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
                <path d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm320-280L160-640v400h640v-400L480-440Zm0-80 320-200H160l320 200ZM160-640v-80 480-400Z" />
            </svg>
        ''',
        cta = f'''
            Mandaci una email
        ''',
        contact = f'''
            info@ozonogroup.it
        ''',
    )
    html_contact_card_default_2 = blocks.contact_card_default(
        icon = f'''
            <svg style="color: #0f1f2e;" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
                <path d="M798-120q-125 0-247-54.5T329-329Q229-429 174.5-551T120-798q0-18 12-30t30-12h162q14 0 25 9.5t13 22.5l26 140q2 16-1 27t-11 19l-97 98q20 37 47.5 71.5T387-386q31 31 65 57.5t72 48.5l94-94q9-9 23.5-13.5T670-390l138 28q14 4 23 14.5t9 23.5v162q0 18-12 30t-30 12ZM241-600l66-66-17-94h-89q5 41 14 81t26 79Zm358 358q39 17 79.5 27t81.5 13v-88l-94-19-67 67ZM241-600Zm358 358Z" />
            </svg>
        ''',
        cta = f'''
            Chiamaci
        ''',
        contact = f'''
            +39 0423 952833
        ''',
    )
    html = f'''
        <section class="contact-hero-container">
            <div class="container-xl">
                {html_heading}
                <div class="contact-hero-content-container">
                    <div style="flex: 1;">
                        <img style="height: 400px; object-fit: cover; border-radius: 16px;"
                            src="/immagini/home/batteri.webp" alt="">
                    </div>
                    <div style="flex: 1; display: flex; flex-direction: column; gap: 16px;">
                        {html_contact_card_default_1}
                        {html_contact_card_default_2}
                    </div>
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.contact-hero-container'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                margin-top: 6.4rem; 
                margin-bottom: 6.4rem;
            }}
        '''
    class_name = '.contact-hero-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                margin-top: 4.8rem; 
                margin-bottom: 4.8rem;
                }}
            }}
        '''
    class_name = '.contact-hero-content-container'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                display: flex;
                gap: 96px;
            }}
        '''
    class_name = '.contact-hero-content-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                    gap: 16px;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

##########################################################

def chi_siamo_hero():
    html_heading = blocks.heading_default_2(
        title = components.h1_default(
            text = f'''Ozonogroup: Innovatori della Sicurezza Alimentare con la Tecnologia all'Ozono''',
            align = f'center',
            align_mobile = f'left',
        ),
        paragraph = components.paragraph_default(
            text = f'''Utilizziamo la potenza naturale dell'ozono per garantire standard igienico-sanitari elevati e soluzioni sostenibili nella filiera alimentare.''',
            align = f'center',
            align_mobile = f'left',
            margin_bottom = '0',
        ),
    )
    html = f'''
        <section class="chi-siamo-hero-container">
            <div class="container-xl">
                {html_heading}
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.chi-siamo-hero-container'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                margin-top: 6.4rem; 
                margin-bottom: 6.4rem;
            }}
        '''
    class_name = '.chi-siamo-hero-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                margin-top: 4.8rem; 
                margin-bottom: 4.8rem;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def chi_siamo_azienda():
    html_heading = components.h2_default(
        text = f'''Chi Siamo - La nostra azienda''',
    )
    html_storia_paragraph_1 = components.paragraph_default(
        text = f'''Ozonogroup progetta e produce generatori di ozono su misura per l'industria alimentare, con l'obiettivo di garantire sanificazione senza sostanze chimiche, controllo della contaminazione microbica e piena conformità alle normative di sicurezza alimentare.''',
    )
    html_storia_paragraph_2 = components.paragraph_default(
        text = f'''Fondata nel 2007 e con sede ad Asolo, in Veneto, l'azienda serve il mercato B2B italiano offrendo soluzioni integrate, basate su tecnologia a scarica corona, studiate ad hoc per le esigenze igienico-sanitarie di ogni realtà produttiva.''',
    )
    html_storia_paragraph_3 = components.paragraph_default(
        text = f'''Attraverso un approccio orientato all'innovazione sostenibile e alla consulenza specializzata, supportiamo le imprese alimentari nel migliorare la qualità dei processi, ridurre l'uso di sostanze chimiche e aumentare gli standard di sicurezza nella lavorazione, nel confezionamento e nella conservazione degli alimenti.''',
    )
    html = f'''
        <section class="container-xl">
            <div style="display: flex; gap: 64px;">
                <div style="flex: 2;">
                    {html_heading}
                </div>
                <div style="flex: 2;">
                    {html_storia_paragraph_1}
                    {html_storia_paragraph_2}
                    {html_storia_paragraph_3}
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def chi_siamo_storia():
    html_heading = components.h2_default(
        text = f'''La Nostra Storia - Da pionieri locali a innovatori della sanificazione alimentare italiana''',
    )
    html_storia_paragraph_2 = components.paragraph_default(
        text = f'''Ozonogroup nasce nel 2007 dall'iniziativa di un gruppo di imprese con una visione chiara: promuovere l'utilizzo dell'ozono come alternativa ecologica ai sanificanti chimici nell'industria alimentare. Fin dall'inizio, l'obiettivo era risolvere problematiche specifiche che le tecnologie tradizionali non riuscivano a gestire, come la rimozione di muffe e acari nelle celle di stagionatura dei salumi, senza lasciare residui chimici sugli alimenti o negli ambienti di lavorazione.''',
    )
    html_storia_paragraph_3 = components.paragraph_default(
        text = f'''Il nostro primo prodotto (un generatore di ozono compatto per piccole attività alimentari) ha dimostrato risultati eccellenti in contesti critici per l'igiene e la sicurezza alimentare. Da lì,
                    Ozonogroup ha progressivamente ampliato il proprio raggio d'azione, fino a servire aziende di ogni
                    dimensione e settore della filiera alimentare, progettando e realizzando sistemi di sanificazione
                    personalizzati, basati su tecnologie consolidate e soluzioni brevettate di ultima generazione.''',
    )
    html_storia_paragraph_4 = components.paragraph_default(
        text = f'''Nel 2019, un'importante operazione di rebranding ha segnato un
                    nuovo inizio: con l'arrivo del CEO
                    Mauro
                    Dottori, l'azienda ha intrapreso un percorso di trasformazione profonda, evolvendo da semplice
                    fornitore
                    di macchinari a partner strategico per la sanificazione industriale, offrendo consulenza,
                    integrazione e
                    sistemi su misura per ogni esigenza produttiva.''',
    )
    html_storia_paragraph_5 = components.paragraph_default(
        text = f'''Oggi, Ozonogroup collabora attivamente
                    con università e centri di
                    ricerca italiani per sviluppare
                    nuove
                    tecnologie legate all'ozono, rafforzando il proprio impegno verso l'innovazione sostenibile, la
                    sicurezza alimentare e il rigore scientifico. Guardando al futuro, il nostro obiettivo è espandere
                    la
                    presenza internazionale e portare la qualità dei nostri sistemi modulari anche oltre i confini
                    nazionali.''',
    )
    html = f'''
        <section class="container-xl">
            <div style="display: flex; gap: 64px;">
                <div style="flex: 2;">
                    {html_heading}
                </div>
                <div style="flex: 2;">
                    {html_storia_paragraph_2}
                    {html_storia_paragraph_3}
                    {html_storia_paragraph_4}
                    {html_storia_paragraph_5}
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def chi_siamo_missione():
    html_heading = components.h2_default(
        text = f'''La Nostra Missione: Sanificare con ozono per una maggiore sicurezza e sostenibilità nell'industria agroalimentare''',
    )
    html_paragraph_2 = components.paragraph_default(
        text = f'''In Ozonogroup, la nostra missione è rendere la produzione
                    alimentare più sicura, più pulita e più sostenibile attraverso sistemi avanzati di sanificazione a
                    base di ozono, in grado di eliminare agenti patogeni nocivi senza l'utilizzo di sostanze chimiche
                    tossiche. Esistiamo per aiutare i produttori e trasformatori alimentari a rispettare i più alti
                    standard di igiene, tutelando allo stesso tempo la salute pubblica e l'ambiente.''',
    )
    html_paragraph_3 = components.paragraph_default(
        text = f'''Siamo impegnati nella sostenibilità grazie a tecnologie che
                    riducono drasticamente il consumo
                    d'acqua, eliminano i residui chimici e minimizzano l'uso di energia. I nostri sistemi a ozono
                    offrono un controllo microbico efficace, raggiungendo superfici difficili da sanificare e
                    disinfettando aria, acqua e ambienti, senza alterare la qualità degli alimenti o richiedere
                    modifiche strutturali agli impianti.''',
    )
    html_paragraph_4 = components.paragraph_default(
        text = f'''Ozonogroup si distingue per la capacità di fornire soluzioni
                    pratiche, pronte all'uso, pienamente conformi ai principali standard normativi internazionali come
                    HACCP e ISO 22000.''',
    )
    html_paragraph_5 = components.paragraph_default(
        text = f'''La nostra visione a lungo termine è
                    guidare la transizione verso una sanificazione senza agenti
                    chimici in tutta l'industria alimentare globale, eliminando i disinfettanti convenzionali e
                    diventando il punto di riferimento per un'igiene sicura ed ecologica entro il 2030.''',
    )
    html_paragraph_6 = components.paragraph_default(
        text = f'''In ogni fase del nostro lavoro, ci guidano i nostri valori fondamentali: innovazione, conformità
                    normativa e responsabilità ambientale. Questi principi orientano la nostra ricerca, ispirano le
                    nostre soluzioni e rafforzano le collaborazioni con produttori alimentari lungimiranti in tutto il
                    mondo.''',
    )
    html = f'''
        <section class="container-xl">
            <div style="display: flex; gap: 64px;">
                <div style="flex: 2;">
                    {html_heading}
                </div>
                <div style="flex: 2;">
                    {html_paragraph_2}
                    {html_paragraph_3}
                    {html_paragraph_4}
                    {html_paragraph_5}
                    {html_paragraph_6}
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def chi_siamo_tecnologia():
    html_heading = components.h2_default(
        text = f'''La Nostra Tecnologia: Sistemi di sanificazione con ozono automatizzati, efficienti e sicuri''',
    )
    html_paragraph_1 = components.paragraph_default(
        text = f'''La tecnologia di Ozonogroup si basa su generatori di ozono a scarica corona ad alte prestazioni,
                    integrati con concentratori di ossigeno, per garantire un'efficacia massima nella sanificazione. I
                    nostri sistemi sono progettati specificamente per l'industria alimentare e permettono l'applicazione
                    dell'ozono sia in fase gassosa che acquosa, adattandosi a diversi ambienti produttivi come celle
                    frigorifere, superfici di contatto e nastri trasportatori. Alcuni dei nostri impianti sono dotati
                    della nostra Custom Control Unit (CCU), un'unità di controllo intelligente che automatizza il
                    dosaggio dell'ozono e ne regola il flusso in tempo reale, attraverso sensori integrati e
                    un'interfaccia touch intuitiva. Questo permette un monitoraggio continuo e preciso, migliorando la
                    sicurezza operativa e riducendo al minimo l'intervento manuale.''',
    )
    html_paragraph_2 = components.paragraph_default(
        text = f'''A differenza dei disinfettanti tradizionali come il cloro o
                    l'acido peracetico, l'ozono non lascia residui e non richiede risciacquo, contribuendo a un
                    risparmio significativo di acqua e tempo. Inoltre, garantisce una maggiore rapidità d'azione e
                    un'efficacia superiore anche a basse concentrazioni rispetto a sistemi a raggi UV, raggiungendo aree
                    difficili e garantendo una sanificazione completa. La sicurezza è una priorità fondamentale nei
                    nostri impianti: ogni sistema è dotato di sensori ambientali per la rilevazione dell'ozono e
                    dispositivi di spegnimento automatico che proteggono sia gli operatori che i prodotti alimentari.''',
    )
    html_paragraph_3 = components.paragraph_default(
        text = f'''Grazie a una progettazione modulare, i nostri sistemi sono
                    facilmente integrabili
                    con linee CIP, camere frigorifere e macchinari esistenti, rendendo l'adozione semplice e veloce
                    senza modifiche strutturali invasive. I nostri impianti richiedono pochissima manutenzione, limitata
                    a una sola revisione annuale per la pulizia degli elettrodi e la sostituzione dei filtri,
                    contribuendo così a ridurre i costi operativi.''',
    )
    html_paragraph_4 = components.paragraph_default(
        text = f'''Ozonogroup ha inoltre sviluppato un algoritmo proprietario per il controllo modulato del flusso di
                    ozono, che ottimizza l'efficienza della sanificazione riducendo il consumo energetico, con un
                    impatto positivo anche dal punto di vista ambientale. I nostri sistemi sono in grado di eliminare
                    fino al 99,999% (5-log) di agenti patogeni alimentari come Listeria, Salmonella ed Escherichia coli,
                    in tempi significativamente inferiori rispetto ai sanificanti chimici tradizionali. Con una
                    combinazione unica di automazione, sicurezza, sostenibilità e prestazioni microbiologiche
                    comprovate, la tecnologia Ozonogroup rappresenta lo standard più avanzato nella sanificazione
                    industriale a base di ozono.''',
    )
    html = f'''
        <section class="container-xl">
            <div style="display: flex; gap: 64px;">
                <div style="flex: 2;">
                    {html_heading}
                </div>
                <div style="flex: 2;">
                    {html_paragraph_1}
                    {html_paragraph_2}
                    {html_paragraph_3}
                    {html_paragraph_4}
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def chi_siamo_industrie():
    html_heading = components.h2_default(
        text = f'''I Nostri Settori: Soluzioni per l'industria di lavorazione alimentare, imbottigliamento e conservazione''',
    )
    html_paragraph_1 = components.paragraph_default(
        text = f'''Ozonogroup sviluppa sistemi avanzati di sanificazione a ozono pensati per le esigenze specifiche del
                    settore
                    alimentare e delle bevande. Le nostre tecnologie garantiscono elevati standard igienici in ambienti
                    produttivi
                    complessi, aiutando le aziende a rispettare le normative sanitarie, ridurre i costi operativi e
                    migliorare la
                    sicurezza alimentare, senza fare uso di agenti chimici aggressivi.''',
    )
    html_paragraph_2 = components.paragraph_default(
        text = f'''Collaboriamo con birrifici e impianti di imbottigliamento per
                    integrare i nostri sistemi a ozono direttamente nelle
                    linee di produzione e nei cicli CIP (Clean-In-Place). Questo consente una sanificazione efficace di
                    serbatoi,
                    tubazioni e attrezzature senza l'utilizzo di calore o sostanze chimiche, con una riduzione dell'uso
                    di acqua per la
                    disinfezione fino all'80%.''',
    )
    html_paragraph_3 = components.paragraph_default(
        text = f'''Nel settore della lavorazione del pesce, i nostri sistemi
                    risolvono problemi critici come la presenza di listeria
                    e l'accumulo di biofilm sui nastri trasportatori. L'ozono sanifica in tempo reale, senza lasciare
                    residui,
                    garantendo un ambiente più sicuro per gli alimenti e per i lavoratori.''',
    )
    html_paragraph_4 = components.paragraph_default(
        text = f'''Nella lavorazione di carne e pollame, affrontiamo efficacemente la
                    contaminazione da E. coli e Salmonella. I nostri
                    sistemi di sanificazione e trattamento delle superfici raggiungono anche le aree più difficili,
                    come condotti
                    dell'aria e componenti in acciaio inox. I clienti riportano una riduzione della carica microbica
                    fino al 95%,
                    semplificando l'implementazione dei protocolli HACCP e migliorando l'efficienza produttiva.''',
    )
    html_paragraph_5 = components.paragraph_default(
        text = f'''Nel settore lattiero-caseario, integriamo le nostre soluzioni a
                    ozono nei cicli CIP per la sanificazione di impianti
                    di pastorizzazione, serbatoi e ambienti di stagionatura del formaggio. L'ozono sostituisce
                    efficacemente i lavaggi
                    chimici, riduce i residui e garantisce una sanificazione uniforme, lotto dopo lotto.''',
    )
    html_paragraph_6 = components.paragraph_default(
        text = f'''Per quanto riguarda celle frigorifere e centri di distribuzione
                    ortofrutticoli, l'ozono si rivela essenziale per
                    contrastare muffe, etilene e contaminazioni incrociate. I nostri impianti di trattamento dell'aria
                    funzionano in
                    modo continuo senza interrompere le operazioni di stoccaggio, prolungando la shelf life di ortaggi e
                    verdure a
                    foglia, mantenendone freschezza e qualità.''',
    )
    html_paragraph_7 = components.paragraph_default(
        text = f'''Che si
                    tratti di sanificare linee produttive, purificare l'aria o prolungare la conservazione dei prodotti,
                    Ozonogroup
                    fornisce soluzioni su misura, affidabili e sostenibili per ogni settore dell'industria alimentare.''',
    )
    html = f'''
        <section class="container-xl">
            <div style="display: flex; gap: 64px;">
                <div style="flex: 2;">
                    {html_heading}
                </div>
                <div style="flex: 2;">
                    {html_paragraph_1}
                    {html_paragraph_2}
                    {html_paragraph_3}
                    {html_paragraph_4}
                    {html_paragraph_5}
                    {html_paragraph_6}
                    {html_paragraph_7}
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def chi_siamo_sostenibilita():
    html_heading = components.h2_default(
        text = f'''Il Nostro Impegno Per L'Eco-Sostenibilità: Sanificazione ecologica e sostenibile, senza prodotti chimici
                e sprechi''',
    )
    html_paragraph_1 = components.paragraph_default(
        text = f'''In Ozonogroup, la sostenibilità non è un'aggiunta, ma un principio fondamentale integrato in ogni
                    sistema di sanificazione a ozono che progettiamo. Il nostro impegno verso l'ambiente ci rende
                    pionieri nel campo dell'igiene alimentare ecologica, supportando le aziende del settore food nella
                    transizione verso processi più sicuri, puliti e responsabili.''',
    )
    html_paragraph_2 = components.paragraph_default(
        text = f'''I nostri sistemi permettono di ridurre il consumo di acqua di almeno il 40% rispetto ai metodi
                    tradizionali a base di cloro o acqua calda, contribuendo a una gestione più efficiente delle risorse
                    senza compromettere l'efficacia della sanificazione. Utilizziamo aria ambiente per generare ozono in
                    tempo reale, eliminando così la necessità di trasporto, stoccaggio e smaltimento di agenti chimici.
                    A differenza di sostanze come l'acido peracetico o il cloro, l'ozono non lascia residui tossici,
                    rendendo i nostri sistemi più sicuri per gli operatori, per gli alimenti e per l'ambiente.''',
    )
    html_paragraph_3 = components.paragraph_default(
        text = f'''Grazie alla nostra tecnologia, le aziende alimentari possono ridurre fino all'80% i rifiuti legati
                    all'uso di contenitori chimici in plastica. Inoltre, eliminando la sanificazione termica, si riduce
                    il consumo energetico complessivo, aiutando i nostri clienti a raggiungere obiettivi concreti di
                    riduzione delle emissioni di CO2. Un altro beneficio fondamentale è la totale assenza di scarichi
                    chimici, che previene l'inquinamento di falde acquifere e habitat naturali spesso messi a rischio
                    dagli impianti industriali tradizionali.''',
    )
    html_paragraph_4 = components.paragraph_default(
        text = f'''Guardando al futuro, stiamo sviluppando sistemi di nuova generazione dotati di funzioni avanzate per
                    monitorare in tempo reale il risparmio di carbonio, offrendo strumenti concreti per la
                    rendicontazione ESG e il miglioramento continuo delle performance ambientali. In questo modo,
                    Ozonogroup non solo risponde alle sfide di oggi, ma anticipa le esigenze sostenibili di domani.''',
    )
    html = f'''
        <section class="container-xl">
            <div style="display: flex; gap: 64px;">
                <div style="flex: 2;">
                    {html_heading}
                </div>
                <div style="flex: 2;">
                    {html_paragraph_1}
                    {html_paragraph_2}
                    {html_paragraph_3}
                    {html_paragraph_4}
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

##########################################################

def settori_articoli():
    html_heading = components.h1_default(
        text = f'''Sanificazione ozono nel settore lattiero-caseario''',
    )
    html_paragraph_1 = components.paragraph_default(
        text = f'''Sanitation is a non-negotiable pillar of success in dairy operations. With milk and dairy products offering rich media for microbial growth, controlling pathogens and spoilage organisms is essential from raw milk intake to final packaging. Traditional sanitizers like chlorine and peracetic acid have long been used, but these agents often leave residues, require thorough rinsing, and can degrade surfaces over time.''',
    )
    html_paragraph_2 = components.paragraph_default(
        text = f'''Ozone sanitization, a residue-free and highly effective method, is gaining traction across the dairy sector. Unlike general disinfectants, ozone targets common dairy pathogens and biofilms without leaving chemical traces or altering product taste. This article outlines where and how ozone is integrated into dairy operations, the regulatory landscape, safety protocols, ROI implications, and future trends in smart dairy sanitation.''',
    )
    html = f'''
        <section class="container-xl article-container">
            <div style="display: flex; gap: 6.4rem;">
                <div style="flex: 2;">
                    {html_heading}
                    {html_paragraph_1}
                    {html_paragraph_2}
                </div>
                <div style="flex: 1;">
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-settori-articoli.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-settori-articoli-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.article-container'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                margin-top: 6.4rem; 
                margin-bottom: 6.4rem;
            }}
        '''
    class_name = '.article-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    margin-top: 4.8rem; 
                    margin-bottom: 4.8rem;
                }}
            }}
        '''
    with open('styles/tmp/pag-settori-articoli.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-settori-articoli-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def articoli():
    import markdown
    with open('database/article.txt', encoding='utf-8') as f: content = f.read()
    lines = [line.strip() for line in content.split('\n') if line.strip() != '']
    html_article = ''
    html_article = markdown.markdown(content, extensions=['markdown.extensions.tables'])
    html_article = utils.aschii(html_article)

    '''
    ul = False
    for line in lines:
        if line.startswith('# '):
            line = line.replace('# ', '')
            html_article += components.h1_default(
                text = line,
            )
        elif line.startswith('## '):
            line = line.replace('## ', '')
            html_article += components.h2_default(
                text = line,
            )
        elif line.startswith('### '):
            line = line.replace('### ', '')
            html_article += components.h3_default(
                text = line,
            )
        elif line.startswith('- '):
            line = line.replace('- ', '')
            if not ul: 
                html_article += f'<ul>'
            html_article += f'<li>{line}</li>'
        else:
            html_article += components.paragraph_default(
                text = line,
            )
    '''

    html = f'''
        <section class="container-xl article-container">
            <div style="display: flex; gap: 6.4rem;">
                <div style="flex: 2;">
                    <div class="article">
                        {html_article}
                    </div>
                </div>
                <div style="flex: 1;">
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-articoli.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-articoli-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.article-container'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                margin-top: 6.4rem; 
                margin-bottom: 6.4rem;
            }}
        '''
    class_name = '.article-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    margin-top: 4.8rem; 
                    margin-bottom: 4.8rem;
                }}
            }}
        '''
    class_name = '.article h1'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                color: {g.color_black_pearl};
                font-size: {g.typography_size_xxxl};
                line-height: {g.typography_line_height_xxxl};
                font-weight: normal;
                margin-bottom: 16px;
            }}
        '''
    class_name = '.article h2'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                color: {g.color_black_pearl};
                font-size: {g.typography_size_xl};
                line-height: {g.typography_line_height_xl};
                font-weight: normal;
                margin-bottom: 16px;
                margin-top: 4.8rem;
            }}
        '''
    class_name = '.article h3'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                color: {g.color_black_pearl};
                font-size: {g.typography_size_lg};
                line-height: {g.typography_line_height_lg};
                font-weight: normal;
                margin-bottom: 16px;
                margin-top: 2.4rem;
            }}
        '''
    class_name = '.article p'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                color: {g.color_black_pearl};
                font-size: {g.typography_size_md};
                line-height: {g.typography_line_height_md};
                margin-bottom: 1.6rem;
            }}
        '''
    class_name = '.article ul'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                margin-left: 1.6rem;
            }}
        '''
    class_name = '.article li'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                margin-bottom: 0.8rem;
            }}
        '''
    class_name = '.article table'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                border-collapse: collapse; 
                border:1px solid {g.color_black_pearl};
            }}
        '''
    class_name = '.article table td'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                border: 1px solid {g.color_black_pearl};
                padding: 0.8rem;
            }}
        '''
    class_name = '.article table th'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                border: 1px solid {g.color_black_pearl};
                padding: 0.8rem;
            }}
        '''
    with open('styles/tmp/pag-articoli.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-articoli-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def settore():
    '''scrivi un paragrafo di circa 40 parole per ogni una delle seguenti applicazioni dell'ozono nell'industria lattiero-casearia:

        - Sanificazione dei serbatoi di stoccaggio del latte
        - Disinfezione delle attrezzature e delle tubazioni per la lavorazione del latte
        - Sistemi di pulizia in posto (CIP)
        - Sanificazione delle superfici delle macchine di confezionamento e riempimento
        - Trattamento del latte crudo per ridurre il carico microbico
        - Sanificazione di pavimenti e pareti degli stabilimenti caseari
        - Trattamento dell’aria nelle aree di lavorazione e stoccaggio
        - Trattamento delle acque reflue per ridurre il carico organico e patogeni
        - Sanificazione di contenitori riutilizzabili e veicoli di trasporto del latte

        struttura:
        - scrivi un breve paragrafo spiegando cosa e questa applicazione, come si fa, e perche serve.
        - use short words, professional tone, active form sentences.
        - rispondi in italiano.
    '''
    html_applicazioni_h2 = components.h2_default(
        text = 'Applicazioni Principali'
    )
    image = f'''<img src="/immagini/settori/lattiero-caseario/latte.jpg" alt="">'''
    heading = components.h3_default(
        text = f'''Sanificazione dei serbatoi di stoccaggio del latte''',
    )
    lines = [
        'Svuotare completamente il serbatoio dal latte residuo.',
        'Risciacquare il serbatoio con acqua calda per rimuovere residui grossolani.',
        'Generare ozono in concentrazione adeguata e farlo circolare all’interno del serbatoio per almeno 15-20 minuti.',
        'Scaricare l’ozono residuo e risciacquare con acqua sterile.',
        'Asciugare il serbatoio prima di riempirlo.',
    ]
    html_list = components.list_ordered_default(lines)
    html_paragraph = components.paragraph_default(
        text = f''' L’ozono viene usato per sanificare i serbatoi dove si conserva il latte. Si introduce gas ozono all’interno dei serbatoi vuoti dopo lo svuotamento. Questo trattamento elimina batteri e muffe. Serve a prevenire la contaminazione e garantire la qualità del latte.'''
    )
    content = ''
    # content += html_list
    content += html_paragraph
    html_card_1 = blocks.card_ihc_default(
        image = image,
        heading = heading,
        content = content,
    )
    ###
    image = f'''<img src="/immagini/settori/lattiero-caseario/latte-2.jpg" alt="">'''
    heading = components.h3_default(
        text = f'''Disinfezione delle attrezzature e delle tubazioni per la lavorazione del latte''',
    )
    lines = [
        'Scollegare le attrezzature dalla linea di produzione.',
        'Eseguire un pre-risciacquo con acqua calda per eliminare residui di latte.',
        'Far circolare acqua ozonizzata attraverso tubazioni e macchinari per almeno 10-15 minuti.',
        'Risciacquare con acqua sterile per rimuovere residui di ozono.',
        'Asciugare e riconnettere le attrezzature.',
    ]
    html_list = components.list_ordered_default(lines)
    html_paragraph = components.paragraph_default(
        text = f'''  L’ozono sanifica le attrezzature e le tubazioni a contatto col latte. Si immette ozono in forma gassosa o disciolto in acqua. Rimuove biofilm, batteri e residui. Questo evita infezioni crociate e mantiene alto il livello igienico della linea.'''
    )
    content = ''
    # content += html_list
    content += html_paragraph
    html_card_2 = blocks.card_ihc_default(
        image = image,
        heading = heading,
        content = content,
    )
    ###
    image = f'''<img src="/immagini/settori/lattiero-caseario/latte-2.jpg" alt="">'''
    heading = components.h3_default(
        text = f'''Sistemi di pulizia in posto (CIP)''',
    )
    html_paragraph = components.paragraph_default(
        text = f''' Nei sistemi CIP, l’ozono sostituisce o integra detergenti chimici. Si usa acqua ozonizzata per pulire l’interno di impianti chiusi, tubazioni e valvole. Riduce l’uso di prodotti chimici, è sicuro per l’ambiente e migliora l’efficienza dei cicli di lavaggio.'''.strip()
    )
    content = ''
    content += html_paragraph
    html_card_3 = blocks.card_ihc_default(
        image = image,
        heading = heading,
        content = content,
    )
    ###
    image = f'''<img src="/immagini/settori/lattiero-caseario/latte-2.jpg" alt="">'''
    heading = components.h3_default(
        text = f'''Sanificazione delle superfici delle macchine di confezionamento e riempimento''',
    )
    html_paragraph = components.paragraph_default(
        text = f''' L’ozono sanifica le parti esterne delle macchine che confezionano e riempiono i prodotti lattiero-caseari. Si impiega gas ozono o acqua ozonizzata sulle superfici. Elimina germi senza lasciare residui. Garantisce la sicurezza del prodotto confezionato.'''.strip()
    )
    content = ''
    content += html_paragraph
    html_card_4 = blocks.card_ihc_default(
        image = image,
        heading = heading,
        content = content,
    )
    ###
    image = f'''<img src="/immagini/settori/lattiero-caseario/latte-2.jpg" alt="">'''
    heading = components.h3_default(
        text = f'''Trattamento del latte crudo per ridurre il carico microbico''',
    )
    html_paragraph = components.paragraph_default(
        text = f''' L’ozono si può impiegare per trattare il latte crudo prima della lavorazione. Viene diffuso in forma gassosa sotto controllo. Abbatte la carica microbica senza alterare le proprietà del latte. Migliora la sicurezza e prolunga la conservazione.'''.strip()
    )
    content = ''
    content += html_paragraph
    html_card_5 = blocks.card_ihc_default(
        image = image,
        heading = heading,
        content = content,
    )
    ###
    image = f'''<img src="/immagini/settori/lattiero-caseario/latte-2.jpg" alt="">'''
    heading = components.h3_default(
        text = f'''Sanificazione di pavimenti e pareti degli stabilimenti caseari''',
    )
    html_paragraph = components.paragraph_default(
        text = f''' L’ozono in acqua si usa per lavare pavimenti e pareti. Rimuove sporco organico e uccide germi e muffe. Non lascia residui e non richiede risciacquo. Mantiene l’ambiente igienico e conforme alle norme sanitarie.'''.strip()
    )
    content = ''
    content += html_paragraph
    html_card_6 = blocks.card_ihc_default(
        image = image,
        heading = heading,
        content = content,
    )
    ###
    image = f'''<img src="/immagini/settori/lattiero-caseario/latte-2.jpg" alt="">'''
    heading = components.h3_default(
        text = f'''Trattamento dell’aria nelle aree di lavorazione e stoccaggio''',
    )
    html_paragraph = components.paragraph_default(
        text = f''' L’ozono purifica l’aria nei locali di produzione e stoccaggio. Viene diffuso in modo controllato tramite generatori. Abbatte odori, muffe e batteri sospesi. Riduce il rischio di contaminazione crociata e migliora l’igiene ambientale.'''.strip()
    )
    content = ''
    content += html_paragraph
    html_card_7 = blocks.card_ihc_default(
        image = image,
        heading = heading,
        content = content,
    )
    ###
    image = f'''<img src="/immagini/settori/lattiero-caseario/latte-2.jpg" alt="">'''
    heading = components.h3_default(
        text = f'''Trattamento delle acque reflue per ridurre il carico organico e patogeni''',
    )
    html_paragraph = components.paragraph_default(
        text = f''' L’ozono ossida la materia organica e distrugge i patogeni presenti nelle acque reflue. Si inietta nel flusso d’acqua tramite diffusori. Riduce COD, BOD e cariche batteriche. Aiuta a rispettare i limiti ambientali e facilita il riuso dell’acqua.'''.strip()
    )
    content = ''
    content += html_paragraph
    html_card_8 = blocks.card_ihc_default(
        image = image,
        heading = heading,
        content = content,
    )
    ###
    image = f'''<img src="/immagini/settori/lattiero-caseario/latte-2.jpg" alt="">'''
    heading = components.h3_default(
        text = f'''Sanificazione di contenitori riutilizzabili e veicoli di trasporto del latte''',
    )
    html_paragraph = components.paragraph_default(
        text = f''' L’ozono disinfetta contenitori e camion cisterna dopo l’uso. Si applica in forma di gas o acqua ozonizzata sulle superfici interne. Rimuove germi e residui senza agenti chimici. Previene la contaminazione del latte durante il trasporto.'''.strip()
    )
    content = ''
    content += html_paragraph
    html_card_9 = blocks.card_ihc_default(
        image = image,
        heading = heading,
        content = content,
    )
    ###
    html = f'''
        <section class="container-xl settore-applicazione-container">
            {html_applicazioni_h2}
            <div class="settore-applicazione-grid">
                {html_card_1}
                {html_card_2}
                {html_card_3}
                {html_card_4}
                {html_card_5}
                {html_card_6}
                {html_card_7}
                {html_card_8}
                {html_card_9}
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-settori-articoli.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-settori-articoli-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.settore-applicazione-grid'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 1.6rem;
            }}
        '''
    class_name = '.settore-applicazione-grid'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                grid-template-columns: repeat(1, 1fr);
                }}
            }}
        '''
    class_name = '.settore-applicazione-container'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                margin-top: 6.4rem; 
                margin-bottom: 6.4rem;
            }}
        '''
    class_name = '.settore-applicazione-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    margin-top: 4.8rem; 
                    margin-bottom: 4.8rem;
                }}
            }}
        '''
    with open('styles/tmp/pag-settori-articoli.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-settori-articoli-mobile.css', 'w') as f: f.write(css_mobile)
    return html

##########################################################

def hero_1_reverse():
    html_h1 = components.h1_reverse(
        text = 'Sanificazione Ozono Nel Settore Lattiero-Caseario',
        align = 'center',
        align_mobile = 'center',
    )
    html_paragraph = components.paragraph_reverse(
        text = f'''Nell’industria lattiero-casearia, la sanificazione a ozono viene impiegata per igienizzare serbatoi, impianti di lavorazione, ambienti produttivi e confezionamento. È utile anche per il trattamento dell’acqua di lavaggio, garantendo pulizia profonda e riducendo l’uso di detergenti chimici tradizionali.''',
        align = 'center',
        align_mobile = 'center',
        margin_bottom = '0',
    )
    ###
    html = f'''
        <section class="container-xl">
            <div class="hero-1-reverse-container">
                <div class="container-md hero-1-reverse-content-container">
                    {html_h1}
                    {html_paragraph}
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-settori-articoli.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-settori-articoli-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
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
                max-width: {g.container_sm};
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.hero-1-reverse-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                background-color: {g.color_black_pearl};
                border-radius: {g.border_radius_lg};
                margin-top: 16px;
                padding-top: 16px;
                padding-bottom: 16px;
            }}
        '''
    class_name = '.hero-1-reverse-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                }}
            }}
        '''
    class_name = '.hero-1-reverse-content-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                flex-direction: column;
                gap: 1.6rem;
                padding-top: 6.4rem;
                padding-bottom: 6.4rem;
            }}
        '''
    class_name = '.hero-1-reverse-content-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                padding-top: 4.8rem;
                padding-bottom: 4.8rem;
            }}
        '''
    with open('styles/tmp/pag-settori-articoli.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-settori-articoli-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def card_image_1():
    html_heading = components.h1_default(
        text = 'Bacillus spp.',
    )
    html_paragraph = components.paragraph_default(
        text = f'''L’ozono gassoso (50 ppm) in pochi minuti già riduce significativamente il carico (2-4 log10), e dopo 6 h può inattivare completamente le cellule libere''',
        margin_bottom = '0',
    )
    html_card = blocks.card_3_default(
        heading=html_heading, 
        content=html_paragraph,
    )
    html_image = components.image_sm_default(
        src='/immagini/settori/lattiero-caseario/latte.jpg',
        alt='',
    ) 
    ###
    html = f'''
        <section class="container-xl">
            <div class="card-image-1-container">
                <div style="flex: 1; display: flex;">
                    {html_card}
                </div>
                <div style="flex: 1;">
                    {html_image}
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-settori-articoli.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-settori-articoli-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.card-image-1-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                gap: 1.6rem;
            }}
        '''
    class_name = 'card-image-1-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                }}
            }}
        '''
    with open('styles/tmp/pag-settori-articoli.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-settori-articoli-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def card_image_2():
    html_heading = components.h1_default(
        text = 'Bacillus spp.',
    )
    html_paragraph = components.paragraph_default(
        text = f'''L’ozono gassoso (50 ppm) in pochi minuti già riduce significativamente il carico (2-4 log10), e dopo 6 h può inattivare completamente le cellule libere''',
        margin_bottom = '0',
    )
    html_card = blocks.card_3_default(
        heading=html_heading, 
        content=html_paragraph,
    )
    html_image = components.image_sm_default(
        src='/immagini/settori/lattiero-caseario/latte.jpg',
        alt='',
    ) 
    ###
    html = f'''
        <section class="container-xl">
            <div class="card-image-1-container">
                <div style="flex: 1;">
                    {html_image}
                </div>
                <div style="flex: 1; display: flex;">
                    {html_card}
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-settori-articoli.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-settori-articoli-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.card-image-1-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                gap: 1.6rem;
            }}
        '''
    class_name = 'card-image-1-container'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                }}
            }}
        '''
    with open('styles/tmp/pag-settori-articoli.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-settori-articoli-mobile.css', 'w') as f: f.write(css_mobile)
    return html

##########################################################
# ;grids
##########################################################
def grid_1_default(html_heading, html_cards, html_buttons=''):
    if html_buttons.strip() != '': 
        html_buttons = f'''
            <div style="display: flex; justify-content: center; margin-top: 3.2rem;">
                {html_buttons}
            <div>
        '''
    html = f'''
        <section class="container-xl" style="margin-top: 6.4rem; margin-bottom: 6.4rem;">
            {html_heading}
            <div class="grid-3">
                {html_cards}
            </div>
            {html_buttons}
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.grid-3'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 1.6rem;
            }}
        '''
    class_name = '.grid-3'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                grid-template-columns: repeat(1, 1fr);
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

# 2 rows, alternated content + image
def layout_02():
    html_heading = components.h2_default(
        text= f'''A cosa serve la sanificazione con ozono?''', 
    )
    html_row_1_card_1 = blocks.card_3_default(
        heading = components.h3_default(
            text= f'''Contaminazioni biologiche''', 
        ),
        content = components.paragraph_default(
            text= f'''L'ozono elimina le contaminazioni biologiche nell'industria alimentare, neutralizzando batteri, virus, muffe, parassiti e odori.''', 
        ),
    )
    html_row_1_card_2 = components.image_sm_default(
        src = f'/immagini/home/batteri.webp', 
        alt = f'',
    )
    html_row_2_card_1 = blocks.card_3_default(
        heading = components.h3_default(
            text= f'''Contaminazioni chimiche''', 
        ),
        content = components.paragraph_default(
            text= f'''L'ozono elimina le contaminazioni chimiche nell'industria alimentare, riducendo micotossine, pesticidi, fitofarmaci e residui di detergenti.''', 
        ),
    )
    html_row_2_card_2 = components.image_sm_default(
        src = f'/immagini/home/odori.webp', 
        alt = f'',
    )
    html_row_1 = f'''
        <div style="flex: 1;">
            {html_row_1_card_1}
        </div>
        <div style="flex: 1;">
            {html_row_1_card_2}
        </div>
    '''
    html_row_2 = f'''
        <div style="flex: 1;">
            {html_row_2_card_2}
        </div>
        <div style="flex: 1;">
            {html_row_2_card_1}
        </div>
    '''
    html = f'''
        <section class="container-xl" style="margin-top: 6.4rem; margin-bottom: 6.4rem;">
            {html_heading}
            <div style="display: flex; flex-direction: column; gap: 1.6rem;">
                <div class="layout_02_row">
                    {html_row_1}
                </div>
                <div class="layout_02_row">
                    {html_row_2}
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.layout_02_row'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                display: flex;
                gap: 1.6rem;
            }}
        '''
    class_name = '.layout_02_row'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

# 2 rows, alternated content + image
def layout_03():
    html_heading = blocks.heading_default_2(
        components.h2_default(
            text = 'Perché usare l\'ozono?',
            align = 'center',
        ),
        paragraph = components.paragraph_default(
            text = 'L’ozono garantisce una potente attività antimicrobica, penetra superfici complesse, non lascia residui chimici, è compatibile con alimenti biologici e prolunga la shelf-life degli alimenti.',
            align = 'center',
        ),
    )
    length_1 = 10
    length_2 = 9
    html_card_1_heading = components.h3_default(
        text = f'Igiene in Secondi', 
    )
    html_card_1_content = components.paragraph_default(
        text = f'L’ozono è circa 3.000 volte più rapido ed efficace del cloro nel distruggere batteri, virus, muffe e funghi.<br><br>Riduce drasticamente i tempi di sanificazione, permette cicli produttivi più rapidi, minimizza il downtime degli impianti e garantisce igiene efficace in ambienti ad alta rotazione.', 
    )
    html_card_1 = blocks.card_3_default(
        heading = html_card_1_heading, 
        content = html_card_1_content,
    )
    html_card_2_heading = components.h3_default(
        text = f'Zero Residui Chimici', 
    )
    html_card_2_content = components.paragraph_default(
        text = f'L’ozono si decompone rapidamente in ossigeno, senza lasciare residui chimici su superfici o alimenti.<br><br>Garantisce sicurezza alimentare, preserva gusto e freschezza, ed elimina il risciacquo finale, con conseguente risparmio di tempo, acqua e costi produttivi.', 
    )
    html_card_2 = blocks.card_3_default(
        heading = html_card_2_heading, 
        content = html_card_2_content,
    )
    html_row_1 = f'''
        <div style="display: flex; gap: 1.6rem;">
            <div style="flex: {length_1};">
                {html_card_1}
            </div>
            <div style="flex: {length_2};">
                {components.image_xs_default(
                    src = f'/immagini/home/veloce.webp', 
                    alt = '',
                )}
            </div>
        </div>
    '''
    html_row_2 = f'''
        <div style="display: flex; gap: 1.6rem;">
            <div style="flex: {length_2};">
                {components.image_xs_default(
                    src = f'/immagini/home/ecologico.webp', 
                    alt = '',
                )}
            </div>
            <div style="flex: {length_1};">
                {html_card_2}
            </div>
        </div>
    '''
    html = f'''
        <section class="container-xl" style="margin-top: 6.4rem; margin-bottom: 6.4rem;">
            {html_heading}
            {html_row_1}
            <div style="margin-bottom: 1.6rem;"></div>
            {html_row_2}
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

def two_cols():
    html_heading = components.h2_default(
        text = f'''A cosa serve la sanificazione con ozono?''',
        align = 'center',
    )
    html_col_1_paragraph = components.paragraph_default(
        text = f'''L'ozono elimina le contaminazioni biologiche nell'industria alimentare, neutralizzando batteri, virus, muffe, parassiti e odori.''',
        align = 'right',
    )
    html_col_1_image = components.image_sm_default(
        src = f'/immagini/home/batteri.webp', 
        alt = f'',
    )
    html_col_2_paragraph = components.paragraph_default(
        text = f'''L'ozono elimina le contaminazioni chimiche nell'industria alimentare, riducendo micotossine, pesticidi, fitofarmaci e residui di detergenti.'''
    )
    html_col_2_image = components.image_sm_default(
        src = f'/immagini/home/odori.webp', 
        alt = f'',
    )
    html_cols = f'''
        <div>
            <div style="max-width: {g.container_xxs}; margin-left: auto;">
                {html_col_1_paragraph}
            </div>
            {html_col_1_image}
        </div>
        <div>
            <div style="max-width: {g.container_xxs};">
                {html_col_2_paragraph}
            </div>
            {html_col_2_image}
        </div>
    '''
    html = f'''
        <section>
            <div class="container-xs" style="margin-bottom: 1.6rem;">
                {html_heading}
            </div>
            <div class="container-xl">
                <div class="grid-2">
                    {html_cols}
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.container-xs'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: {g.container_xs};
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.grid-2'
    if class_name not in css:
        css += f'''
            {class_name} {{ 
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 1.6rem;
            }}
        '''
    class_name = '.grid-2'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                grid-template-columns: repeat(1, 1fr);
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

##########################################################
# ;layouts
##########################################################
def layout_2col_5x4(html_content, html_contatti):
    html = f'''
        <section class="container-xl">
            <div class="layout-2col-5x4">
                <div style="flex: 5;">
                    {html_content}
                </div>
                <div style="flex: 4;">
                    {html_contatti}
                </div>
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    class_name = '.layout-2col-5x4'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                gap: 4.8rem;
            }}
        '''
    class_name = '.layout-2col-5x4'
    if class_name not in css_mobile:
        css_mobile += f'''
            @media screen and (max-width: 768px) {{
                {class_name} {{
                    flex-direction: column;
                }}
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

##########################################################
# ;hero
##########################################################
def hero_2_reverse(html_heading, image_url):
    html = f'''
        <section class="container-xl">
            <div style="border-radius: 16px; border-bottom-left-radius: 16px;
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url({image_url});
            background-size: cover; 
            background-position: center; 
            padding-top: 96px; padding-bottom: 96px; padding-left: 48px; padding-right: 48px;">
                {html_heading}
            </div>
        </section>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html

##########################################################
# ;spacer
##########################################################

def spacer_1():
    html = f'''
        <div class="spacer_1">
        </div>
    '''
    ###
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    with open('styles/tmp-mobile/pag-home-mobile.css') as f: css_mobile = f.read()
    class_name = '.spacer_1'
    if class_name not in css:
        css += f'''
            {class_name} {{
                margin-bottom: 6.4rem;
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/pag-home-mobile.css', 'w') as f: f.write(css_mobile)
    return html




##########################################################
# ;title
##########################################################

def heading_1():
    html_article_h1 = components.article_h1_default(
        text = f'''Tutto quello che devi sapere sull'ozono''',
        align = f'center',
    )
    html = f'''
        <section class="container-xl">
            {html_article_h1}
        </section>
    '''
    ###
    with open('styles/tmp/hub-ozono.css') as f: css = f.read()
    with open('styles/tmp-mobile/hub-ozono-mobile.css') as f: css_mobile = f.read()
    class_name = '.container-xl'
    if class_name not in css:
        css += f'''
            {class_name} {{
                max-width: 1280px;
                margin-left: auto;
                margin-right: auto;
                padding-left: 16px;
                padding-right: 16px;
            }}
        '''
    with open('styles/tmp/hub-ozono.css', 'w') as f: f.write(css)
    with open('styles/tmp-mobile/hub-ozono-mobile.css', 'w') as f: f.write(css_mobile)
    
    return html

