from lib import g
from lib import io
from lib import components

from lorem_text import lorem

from data import settori_data


def sectors_category_gen():
    ########################################
    # HERO 0001
    ########################################
    opacity = 0.3
    hero_0001_html = f'''
        <section 
            style="
            background-image: linear-gradient(rgba(0, 0, 0, {opacity}), rgba(0, 0, 0, {opacity})), url('/immagini/home/uva-0000.png');   
            background-position: center;
            background-size: cover;
        ">
            {components.header_transparent()}
            <div class="m-flex container-xl" style="flex-direction: column; justify-content: center; gap: 0rem; height: 96vh;">
                <h1 style="color: #fff; text-align: center;">
                    SETTORI DI UTILIZZO DELL'OZONO
                </h1>
                <div style="text-align: center;">
                    <a href="/" class="button-white-ghost-2">
                    Prenota Consulenza
                </a>
                </div>
            </div>
        </section>
    '''

    sectors_cards_html = f''
    sectors_data = io.csv_to_dict('C:\ozonogroup\data\ssot\dataset\manual\settori.csv', delimiter='\\')
    for item in sectors_data:
        sector = item['sector']
        entity = item['entity']
        url_slug = item['url_slug']
        image_src = item['image_src']
        sectors_cards_html += f'''
            <article>
                <a 
                    style="
                    " 
                    href="{url_slug}"
                >
                    <img 
                        style="
                            margin-bottom: 1rem;
                            height: 16rem;
                            object-fit: cover;
                            object-align: center;
                        "
                        src="{image_src}"
                    >
                </a>
                <h3
                    style="
                        font-size: 1rem;
                    "
                >
                    <a 
                        style="
                            color: #111; 
                            text-decoration: none;
                            font-weight: 700;
                            letter-spacing: 0;
                            margin: 0;
                        " 
                        href="{url_slug}"
                    >
                        {entity}
                    </a>
                </h3>
                    <p>
                        {lorem.words(24)}
                    </p>
            </article>
        '''

    sectors_0000_html = f'''
        <section class="container-xl">
            <h2>Settore Agroalimentare</h2>
            <div class="grid-4" style="gap: 2.4rem;">
                {sectors_cards_html}
            </div>
        </section>
    '''

    html = f'''
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="/styles.css">
            <title>Sistemi Industriali a Ozono | Ozonogroup</title>
            <meta name="description" content="Tecnologie e sistemi a ozono per applicazioni industriali, commerciali e civili. Progettazione, applicazioni e guida tecnica sull'ozono.">
        </head>
        <body>
            <main>
                {hero_0001_html}
                {sectors_0000_html}
            </main>
            <!-- =======================================
                 FOOTER
                 Include company info, legal, sitemap, social links
            ======================================== -->
            {components.footer_dark()}
        </body>
        </html>
    '''

    html_filepath = f'{g.WEBSITE_FOLDERPATH}/settori.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)
    print(html)

def sector_gen(item):
    sector = item['sector']
    entity = item['entity']
    url_slug = item['url_slug']
    image_src = item['image_src']
    title = item['title']
    h1 = item['h1']
    ###
    article_html = ''
    article_html += f'''
        <section style="margin-top: 4.8rem;">
            <div class="container-md">
                <h1>{h1}</h1>
            </div>
        </section>
    '''

    demo_hero_html = f'''
        <!-- =========================================================
            HERO — SETTORE LATTIERO-CASEARIO
            URL: /settori/lattiero-caseario/
            ========================================================= -->

        <header
        class="sector-hero"
        aria-labelledby="sector-title"
        style="
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            color: #17202a;
        "
        >

        <!-- Breadcrumb -->
        <section class="breadcrumbs" style="font-size: 0.75rem; margin-bottom: 1rem;">
            {components.breadcrumbs_schema(url_slug)}
        </section>

        {components.breadcrumbs_schema(url_slug)}
        <nav
            aria-label="Percorso di navigazione"
            style="
            padding: 20px 0 16px;
            font-size: 14px;
            line-height: 1.5;
            color: #667085;
            "
        >
            <ol
            itemscope
            itemtype="https://schema.org/BreadcrumbList"
            style="
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
                margin: 0;
                padding: 0;
                list-style: none;
            "
            >

            <li
                itemprop="itemListElement"
                itemscope
                itemtype="https://schema.org/ListItem"
            >
                <a
                itemprop="item"
                href="/"
                style="
                    color: inherit;
                    text-decoration: none;
                "
                >
                <span itemprop="name">Home</span>
                </a>
                <meta itemprop="position" content="1">
            </li>

            <li aria-hidden="true">/</li>

            <li
                itemprop="itemListElement"
                itemscope
                itemtype="https://schema.org/ListItem"
            >
                <a
                itemprop="item"
                href="/settori/"
                style="
                    color: inherit;
                    text-decoration: none;
                "
                >
                <span itemprop="name">Settori</span>
                </a>
                <meta itemprop="position" content="2">
            </li>

            <li aria-hidden="true">/</li>

            <li
                itemprop="itemListElement"
                itemscope
                itemtype="https://schema.org/ListItem"
                aria-current="page"
            >
                <span itemprop="name">Lattiero-caseario</span>
                <meta itemprop="position" content="3">
            </li>

            </ol>
        </nav>


        <!-- Hero Content -->
        <div
            style="
            max-width: 900px;
            padding: 72px 0 88px;
            "
        >

            <!-- Macrosettore -->
            <p
            style="
                margin: 0 0 20px;
                font-size: 13px;
                font-weight: 700;
                line-height: 1.4;
                letter-spacing: 0.12em;
                text-transform: uppercase;
                color: #52606d;
            "
            >
            Settore Agroalimentare
            </p>


            <!-- H1: unica intestazione primaria della pagina -->
            <h1
            id="sector-title"
            style="
                max-width: 850px;
                margin: 0 0 28px;
                font-size: clamp(38px, 6vw, 68px);
                font-weight: 700;
                line-height: 1.05;
                letter-spacing: -0.035em;
                color: #101828;
            "
            >
            Soluzioni per l'industria lattiero-casearia
            </h1>


            <!-- Definizione semantica dell'entità -->
            <p
            style="
                max-width: 760px;
                margin: 0 0 36px;
                font-size: clamp(18px, 2vw, 22px);
                line-height: 1.65;
                color: #475467;
            "
            >
            Esplora processi, applicazioni, problematiche e soluzioni
            per l'impiego dell'ozono nell'industria lattiero-casearia,
            dalla gestione dell'acqua e degli ambienti alla sanificazione
            degli impianti e delle superfici.
            </p>


            <!-- Navigazione semantica interna -->
            <div
            style="
                display: flex;
                flex-wrap: wrap;
                gap: 12px;
                align-items: center;
            "
            >

            <a
                href="/settori/lattiero-caseario/applicazioni/"
                style="
                display: inline-flex;
                align-items: center;
                justify-content: center;
                min-height: 48px;
                padding: 0 22px;
                border-radius: 8px;
                background: #101828;
                color: #ffffff;
                font-size: 15px;
                font-weight: 600;
                line-height: 1;
                text-decoration: none;
                transition: opacity 0.2s ease;
                "
            >
                Esplora le applicazioni
            </a>


            <a
                href="/contatti/"
                style="
                display: inline-flex;
                align-items: center;
                justify-content: center;
                min-height: 48px;
                padding: 0 22px;
                border: 1px solid #d0d5dd;
                border-radius: 8px;
                background: #ffffff;
                color: #344054;
                font-size: 15px;
                font-weight: 600;
                line-height: 1;
                text-decoration: none;
                transition: background 0.2s ease;
                "
            >
                Parla con un esperto
            </a>

            </div>

        </div>

        </header>
    '''
    article_html += f'''
        {demo_hero_html}
    '''

    html = f'''
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="/styles.css">
            <title>{title}</title>
        </head>
        <body>
            <main class="listing">
                {components.header_light_logo()}
                {article_html}
            </main>
            <!-- =======================================
                FOOTER
                Include company info, legal, sitemap, social links
            ======================================== -->
            {components.footer_dark()}
        </body>
        </html>
    '''

    html_filepath = f'{g.WEBSITE_FOLDERPATH}/{url_slug}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)
    print(html)
    quit()

def gen():
    sectors_category_gen()

    sectors_data = io.csv_to_dict('C:\ozonogroup\data\ssot\dataset\manual\settori.csv', delimiter='\\')
    for item in sectors_data:
        sector_gen(item)

    