from lib import g
from lib import components

def header_light():
    html = f'''
        <header class="header-light">
            <div class="container-xl header-light-container">
                <div class="header-light-menu">
                    <a class="header-light-menu-logo" href="/">Ozonogroup</a>
                    <nav class="header-light-menu-nav">
                        <a href="/">Home</a>
                        <a href="/prodotti.html">Prodotti</a>
                        <a href="/servizi.html">Servizi</a>
                        <a href="/settori.html">Settori</a>
                        <a href="/chi-siamo.html">Chi Siamo</a>
                        <a href="/contatti.html">Contatti</a>
                    </nav>
                </div>
                {components.link_fill()}
            </div>
        </header>
    '''
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    class_name = '.header-light'
    if class_name not in css:
        css += f'''
            {class_name} {{
                background-color: {g.color_white};
                padding-top: 16px;
                padding-bottom: 16px;
            }}
        '''
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
    class_name = '.header-light-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                justify-content: space-between;
                align-items: center;
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
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    return html

def header_dark():
    html = f'''
        <header class="header-dark">
            <div class="container-xl header-dark-container">
                <div class="header-dark-menu">
                    <a class="header-dark-menu-logo" href="/">Ozonogroup</a>
                    <nav class="header-dark-menu-nav">
                        <a href="/">Home</a>
                        <a href="/prodotti.html">Prodotti</a>
                        <a href="/servizi.html">Servizi</a>
                        <a href="/settori.html">Settori</a>
                        <a href="/chi-siamo.html">Chi Siamo</a>
                        <a href="/contatti.html">Contatti</a>
                    </nav>
                </div>
                {components.link_fill_reverse()}
            </div>
        </header>
    '''
    with open('styles/tmp/pag-home.css') as f: css = f.read()
    class_name = '.header-dark'
    if class_name not in css:
        css += f'''
            {class_name} {{
                background-color: {g.color_black_pearl};
                padding-top: 16px;
                padding-bottom: 16px;
            }}
        '''
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
    class_name = '.header-dark-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
        '''
    class_name = '.header-dark-menu'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 32px;
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
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    return html

def home_hero():
    html = f'''
        <section class="home-hero-section">
            <div class="container-xl" style="height: 100%;">
                <div class="home-hero-container">
                    <div class="home-hero-title-container">
                        <div style="flex: 2;">
                            <h1 class="home-hero-title-text">Sanificazione
                                ozono per l'industria alimentare
                            </h1>
                        </div>
                        <div style="flex: 1;"></div>
                    </div>
                    <div class="home-hero-content-container">
                        <div style="flex: 2;"></div>
                        <div style="flex: 1;">
                            <p style="color: #ffffff; font-size: 16px; line-height: 24px; margin-bottom: 24px;">Progettiamo
                                sistemi di sanificazione con ozono per ambienti di produzione alimentari pi&#249;
                                sicuri e igienici (senza l'uso di sostanze chimiche).</p>
                            <div style="display: flex; gap: 24px;">
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
    class_name = '.home-hero-title-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
                margin-bottom: 64px;
                gap: 64px;
            }}
        '''
    class_name = '.home-hero-title-text'
    if class_name not in css:
        css += f'''
            {class_name} {{
                font-size: {g.typography_size_xxxl};
                color: white;
                line-height: 1;
                font-weight: normal;
            }}
        '''
    class_name = '.home-hero-content-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                display: flex;
            }}
        '''
    class_name = '.home-hero-content-container a'
    if class_name not in css:
        css += f'''
            {class_name} {{
                text-decoration-line: none;
                display: inline-block;
            }}
        '''
    class_name = '.home-hero-content-button'
    if class_name not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                background-color: {g.color_white};
                border: 1px solid {g.color_white};
                border-radius: 9999px;
                padding: 8px 16px;
                text-decoration-line: none;
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
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
    class_name = '.home-proof-section img'
    if class_name not in css:
        css += f'''
            {class_name} {{
                flex: 1;
                opacity: 66%;
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
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
    html_paragraph = components.paragraph_default(
        paragraph_text = f'''
            Il sistema progettato da Ozonogroup offre numerosi vantaggi in termini di sicurezza, efficacia e sostenibilità, migliorando ogni fase del processo produttivo.
        '''
    )
    html_header = f'''
        <div class="home-benefits-intro-container">
            <div style="flex: 3;">
                <p class="home-benefits-intro-title">
                    Vantaggi del sistema ad ozono per gli operatori alimentari
                </p>
            </div>
            <div style="flex: 2;">
                {html_paragraph}
            </div>
        </div>
    '''
    html_paragraph = components.paragraph_default(
        paragraph_text = f'''
            L'ozono è riconosciuto a livello normativo come agente sanificante efficace e sicuro. L'automazione dei cicli di disinfezione garantisce la ripetibilità e tracciabilità dei processi, requisito fondamentale nei piani HACCP.
        '''
    )
    html_card_1 = f'''
        <div class="home-benefits-card-container">
            <p style="margin-bottom: 16px; color: #53BED6;">01 - Sicurezza</p>
            <h3 class="home-benefits-card-title">Rispetta gli standard HACCP per la sicurezza alimentare</h3>
            {html_paragraph}
            <div style="margin-bottom: 64px;"></div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                    fill="#1f1f1f">
                    <path
                        d="M420-340h120v-100h100v-120H540v-100H420v100H320v120h100v100Zm60 260q-139-35-229.5-159.5T160-516v-244l320-120 320 120v244q0 152-90.5 276.5T480-80Zm0-84q104-33 172-132t68-220v-189l-240-90-240 90v189q0 121 68 220t172 132Zm0-316Z" />
                </svg>
                <!-- <div style="display: flex; gap: 8px;">
                    <a class="home-benefits-card-link" href="#">Learn more</a>
                    <svg class="home-benefits-card-icon" xmlns="http://www.w3.org/2000/svg" fill="none"
                        viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
                    </svg>
                </div> -->
            </div>
        </div>
    '''
    html_paragraph = components.paragraph_default(
        paragraph_text = f'''
            L'ozono garantisce un'azione biocida completa, su aria, acqua e superfici. Riduce fino al 99,9% della carica microbica, inclusa Listeria monocytogenes, Salmonella spp., E. coli, Botrytis, e molti altri patogeni critici.
        '''
    )
    html_card_2 = f'''
        <div class="home-benefits-card-container">
            <div class="home-benefits-card-container">
                <p style="margin-bottom: 16px; color: #53BED6;">02 - Efficacia</p>
                <h3 class="home-benefits-card-title">
                    Efficace su batteri, virus, muffe, odori e altri microrganismi.</h3>
                {html_paragraph}
                <div style="margin-bottom: 64px;"></div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                        fill="#1f1f1f">
                        <path
                            d="M450-80q-12 0-21-9t-9-21q0-12 9-21t21-9v-62q-42-5-79-20t-67-40l-43 44q9 9 9 21t-9 21q-9 9-21 9t-21-9l-43-42q-9-9-9-21.5t9-21.5q9-9 21-8.5t21 8.5l44-44q-25-31-40-67t-20-78h-62q0 12-9 21t-21 9q-12 0-21-9t-9-21v-60q0-12 9-21t21-9q12 0 21 9t9 21h62q5-42 20.5-78t39.5-67l-44-44q-9 8-21 8.5t-21-8.5q-9-9-9-21.5t9-21.5l42-42q9-9 21.5-9t21.5 9q9 9 9 21.5t-9 21.5l43 43q31-25 67-40t78-20v-62q-12 0-20.5-9t-8.5-21q0-12 9-21t21-9h60q12 0 21 9t9 21q0 12-9 21t-21 9v62q42 5 78 20t67 40l44-44q-9-9-9-21t9-21q9-9 21.5-9t21.5 9l42 43q9 9 9 21t-9 21q-9 9-21.5 9t-21.5-9l-43 43q25 31 40 67.5t20 78.5h62q0-12 9-21t21-9q12 0 21 9t9 21v60q0 12-9 21t-21 9q-12 0-21-9t-9-21h-62q-5 42-20 78.5T698-304l43 43q9-9 21.5-9t21.5 9q9 9 9 21.5t-9 21.5l-42 42q-9 9-21.5 9t-21.5-9q-9-9-8.5-21t8.5-21l-44-44q-31 25-67 40.5T510-201v61q12 0 21 9t9 21q0 12-9 21t-21 9h-60Zm30-200q83 0 141.5-58.5T680-480q0-83-58.5-141.5T480-680q-83 0-141.5 58.5T280-480q0 83 58.5 141.5T480-280Zm-70-40q17 0 28.5-11.5T450-360q0-17-11.5-28.5T410-400q-17 0-28.5 11.5T370-360q0 17 11.5 28.5T410-320Zm140 0q17 0 28.5-11.5T590-360q0-17-11.5-28.5T550-400q-17 0-28.5 11.5T510-360q0 17 11.5 28.5T550-320ZM340-440q17 0 28.5-11.5T380-480q0-17-11.5-28.5T340-520q-17 0-28.5 11.5T300-480q0 17 11.5 28.5T340-440Zm140 0q17 0 28.5-11.5T520-480q0-17-11.5-28.5T480-520q-17 0-28.5 11.5T440-480q0 17 11.5 28.5T480-440Zm140 0q17 0 28.5-11.5T660-480q0-17-11.5-28.5T620-520q-17 0-28.5 11.5T580-480q0 17 11.5 28.5T620-440ZM410-560q17 0 28.5-11.5T450-600q0-17-11.5-28.5T410-640q-17 0-28.5 11.5T370-600q0 17 11.5 28.5T410-560Zm140 0q17 0 28.5-11.5T590-600q0-17-11.5-28.5T550-640q-17 0-28.5 11.5T510-600q0 17 11.5 28.5T550-560Zm-70 80Z" />
                    </svg>
                    <!-- <div style="display: flex; gap: 8px;">
                        <a class="home-benefits-card-link" href="#">Learn more</a>
                        <svg class="home-benefits-card-icon" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
                        </svg>
                    </div> -->
                </div>
            </div>
        </div>
    '''
    html_paragraph = components.paragraph_default(
        paragraph_text = f'''
            L'ozono è un gas naturale che si decompone in ossigeno, senza lasciare residui. Elimina microrganismi patogeni senza generare rifiuti pericolosi o sostanze tossiche. Riduce l'uso di acqua, detersivi, e sanificanti convenzionali.
        '''
    )
    html_card_3 = f'''
        <div class="home-benefits-card-container">
            <div class="home-benefits-card-container">
                <p style="margin-bottom: 16px; color: #53BED6;">03 - Sostenibilità</p>
                <h3 class="home-benefits-card-title">
                    Sanifica in modo ecologico, senza uso di sostanze chimiche</h3>
                {html_paragraph}
                <div style="margin-bottom: 64px;"></div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                        fill="#1f1f1f">
                        <path
                            d="M216-176q-45-45-70.5-104T120-402q0-63 24-124.5T222-642q35-35 86.5-60t122-39.5Q501-756 591.5-759t202.5 7q8 106 5 195t-16.5 160.5q-13.5 71.5-38 125T684-182q-53 53-112.5 77.5T450-80q-65 0-127-25.5T216-176Zm112-16q29 17 59.5 24.5T450-160q46 0 91-18.5t86-59.5q18-18 36.5-50.5t32-85Q709-426 716-500.5t2-177.5q-49-2-110.5-1.5T485-670q-61 9-116 29t-90 55q-45 45-62 89t-17 85q0 59 22.5 103.5T262-246q42-80 111-153.5T534-520q-72 63-125.5 142.5T328-192Zm0 0Zm0 0Z" />
                    </svg>
                    <!-- <div style="display: flex; gap: 8px;">
                        <a class="home-benefits-card-link" href="#">Learn more</a>
                        <svg class="home-benefits-card-icon" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M17.25 8.25 21 12m0 0-3.75 3.75M21 12H3" />
                        </svg>
                    </div> -->
                </div>
            </div>
        </div>
    '''

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
    with open('styles/tmp/pag-home.css') as f: css = f.read()
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
    class_name = '.home-benefits-intro-title'
    if class_name not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                font-size: {g.typography_size_xl};
                line-height: {g.typography_line_height_xl};
                font-weight: normal;
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
    class_name = '.home-benefits-card-container'
    if class_name not in css:
        css += f'''
            {class_name} {{
                background-color: {g.color_gray_extralight};
                border-radius: {g.border_radius_xl};
                padding: 16px;
            }}
        '''
    class_name = '.home-benefits-card-title'
    if class_name not in css:
        css += f'''
            {class_name} {{
                margin-bottom: 16px;
                color: {g.color_black_pearl};
                font-size: {g.typography_size_lg};
                line-height: 1.2;
                font-weight: normal;
            }}
        '''
    class_name = '.home-benefits-card-link'
    if class_name not in css:
        css += f'''
            {class_name} {{
                color: {g.color_black_pearl};
                text-decoration-line: none;
            }}
        '''
    class_name = '.home-benefits-card-icon'
    if class_name not in css:
        css += f'''
            {class_name} {{
                height: 24px;
            }}
        '''
    with open('styles/tmp/pag-home.css', 'w') as f: f.write(css)
    return html