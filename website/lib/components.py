from lib import g

def html_header_light():
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
                <div>
                    <a class="header-light-button" href="/contatti.html">Prenota consulenza</a>
                </div>
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
    class_name = '.header-light-button'
    if class_name not in css:
        css += f'''
            {class_name} {{
                color: {g.color_white};
                background-color: {g.color_black_pearl};
                border: 1px solid {g.color_black_pearl};
                border-radius: 9999px;
                padding: 8px 16px;
                text-decoration-line: none;
            }}
        '''

    with open('styles/tmp/pag-home.css', 'a') as f: f.write(css)
    return html

def html_header_dark():
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
                <div>
                    <a class="header-dark-button" href="/contatti.html">Prenota consulenza</a>
                </div>
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
    class_name = '.header-dark-button'
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

    with open('styles/tmp/pag-home.css', 'a') as f: f.write(css)
    return html