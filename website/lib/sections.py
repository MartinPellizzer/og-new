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

