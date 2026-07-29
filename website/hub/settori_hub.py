import json

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
    sectors_data = io.csv_to_dict('C:\ozonogroup\data\ssot\dataset\manual\settori_nuovo.csv', delimiter='\\')
    for item in sectors_data:
        name = item['name']
        url_slug = f'''/settori/{item['slug']}'''
        # image_src = item['image_src']
        image_src = ''
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
                        {name}
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

    html_filepath = f'{g.WEBSITE_FOLDERPATH}/settori/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)
    print(html)

def sector_gen(item):
    name = item['name']
    url_slug = f'''/settori/{item['slug']}'''
    # image_src = item['image_src']
    image_src = ''
    # title = item['title']
    title = 'title'
    # h1 = item['h1']
    h1 = name
    ###
    article_html = ''
    demo_hero_html = f'''
        {components.breadcrumbs_schema(url_slug)}
        <section>
            <h1>
                {h1}
            </h1>
            <p>
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
        </section>
    '''
    article_html += f'''
        {demo_hero_html}    
    '''

    filepath = f'C:\ozonogroup\data\ssot\dataset\manual\settori_table_timeline.csv'
    data = io.csv_to_dict(filepath, delimiter="|")
    # print(json.dumps(data, indent=4))
    # quit()

    cards_html = f''
    for item in data:
        card_html = f'''
            <div
                style="
                    background-color: #fff;
                    border: 1px solid #e2e4e6;
                    border-radius: 10px;
                    padding: 2rem;
                "
            >
                <span
                    aria-hidden="true"
                    style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;margin-bottom:22px;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:18px;font-weight:700;"
                >
                    01
                </span>

                <h3 
                    style="
                        margin-bottom: 1rem;
                    "
                >
                    {item['title']}
                    </h3>
                <p
                    style="
                        color: #626466;
                        font-size: 0.9375rem;
                    "
                >
                    {item['description']}
                </p>
            </div>
        '''
        cards_html += card_html

    article_html += f'''
        <section>
            <div class="grid-3" style="gap: 1rem;">
                {cards_html}
            </div>
        </section>
    '''



    article_html += '''
        <section
  id="industria-lattiero-casearia"
  aria-labelledby="sector-intro-title"
  style="max-width:1180px;margin:0 auto;padding:80px 24px;background:#f7f8f6;color:#17201b;font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;line-height:1.7;"
>

  <!-- Eyebrow / Contesto semantico -->
  <div
    style="display:inline-flex;align-items:center;gap:8px;margin-bottom:18px;padding:6px 10px;border:1px solid #e2e7e3;border-radius:999px;background:#ffffff;color:#1f5c45;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;"
  >
    Settore agroalimentare
  </div>


  <!-- H1 principale della pagina -->
  <h1
    id="sector-intro-title"
    style="max-width:850px;margin:0 0 28px;font-size:clamp(34px,5vw,58px);line-height:1.08;letter-spacing:-.04em;font-weight:750;"
  >
    Industria lattiero-casearia
  </h1>


  <!-- Definizione sintetica dell'entità -->
  <p
    style="max-width:820px;margin:0 0 52px;color:#68736c;font-size:20px;line-height:1.7;"
  >
    L'industria lattiero-casearia comprende la filiera dedicata alla
    trasformazione del latte e alla produzione di alimenti e derivati
    lattiero-caseari. È un settore caratterizzato da processi produttivi
    complessi, rigorosi requisiti igienico-sanitari e specifiche esigenze
    di gestione dell'acqua, degli impianti, delle superfici e degli ambienti.
  </p>


  <!-- Contenuto principale + informazioni strutturate -->
  <div
    style="display:grid;grid-template-columns:minmax(0,1.6fr) minmax(280px,.8fr);gap:56px;align-items:start;"
  >


    <!-- Definizione approfondita -->
    <div>

      <h2
        style="margin:0 0 16px;font-size:28px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
      >
        Che cos'è l'industria lattiero-casearia?
      </h2>

      <p
        style="margin:0 0 20px;color:#3f4943;font-size:17px;"
      >
        La filiera lattiero-casearia comprende le attività industriali
        legate alla raccolta e al trattamento del latte e alla sua
        trasformazione in prodotti come latte alimentare, formaggi,
        yogurt, burro e altri derivati.
      </p>

      <p
        style="margin:0 0 20px;color:#3f4943;font-size:17px;"
      >
        A seconda del prodotto e del processo produttivo, la filiera
        comprende diverse fasi, tra cui ricevimento e stoccaggio delle
        materie prime, trattamento del latte, trasformazione, fermentazione,
        caseificazione, eventuale stagionatura, confezionamento e
        conservazione.
      </p>

      <p
        style="margin:0;color:#3f4943;font-size:17px;"
      >
        L'igiene degli impianti e degli ambienti rappresenta un elemento
        centrale del settore. La gestione della qualità microbiologica
        dell'acqua, delle superfici e degli ambienti produttivi deve essere
        integrata nei processi di controllo e sanificazione adottati
        dall'industria lattiero-casearia.
      </p>

    </div>


    <!-- Informazioni strutturate sul settore -->
    <aside
      aria-label="Panoramica dell'industria lattiero-casearia"
      style="padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;"
    >

      <h2
        style="margin:0 0 22px;font-size:14px;font-weight:750;letter-spacing:.04em;text-transform:uppercase;"
      >
        Panoramica del settore
      </h2>


      <!-- Fact: Macrosettore -->
      <div
        style="padding:0 0 16px;border-top:0;"
      >
        <span
          style="display:block;margin-bottom:4px;color:#68736c;font-size:13px;"
        >
          Macrosettore
        </span>

        <span
          style="display:block;font-size:16px;font-weight:650;"
        >
          Agroalimentare
        </span>
      </div>


      <!-- Fact: Settore -->
      <div
        style="padding:16px 0;border-top:1px solid #e2e7e3;"
      >
        <span
          style="display:block;margin-bottom:4px;color:#68736c;font-size:13px;"
        >
          Settore
        </span>

        <span
          style="display:block;font-size:16px;font-weight:650;"
        >
          Lattiero-caseario
        </span>
      </div>


      <!-- Fact: Prodotti -->
      <div
        style="padding:16px 0;border-top:1px solid #e2e7e3;"
      >
        <span
          style="display:block;margin-bottom:4px;color:#68736c;font-size:13px;"
        >
          Principali prodotti
        </span>

        <span
          style="display:block;font-size:16px;font-weight:650;"
        >
          Latte, formaggi, yogurt, burro e derivati
        </span>
      </div>


      <!-- Fact: Ambiti -->
      <div
        style="padding:16px 0 0;border-top:1px solid #e2e7e3;"
      >
        <span
          style="display:block;margin-bottom:4px;color:#68736c;font-size:13px;"
        >
          Ambiti correlati
        </span>

        <span
          style="display:block;font-size:16px;font-weight:650;"
        >
          Processi, igiene, acqua, sanificazione e conservazione
        </span>
      </div>

    </aside>

  </div>


  <!-- Navigazione semantica verso i cluster della pagina -->
  <nav
    aria-label="Esplora l'industria lattiero-casearia"
    style="display:flex;flex-wrap:wrap;gap:12px;margin-top:48px;padding-top:28px;border-top:1px solid #e2e7e3;"
  >

    <a
      href="#processi"
      style="display:inline-flex;align-items:center;gap:8px;padding:11px 16px;border:1px solid #e2e7e3;border-radius:8px;background:#ffffff;color:#17201b;font-size:14px;font-weight:650;text-decoration:none;"
    >
      Processi del settore
      <span aria-hidden="true">→</span>
    </a>


    <a
      href="#applicazioni"
      style="display:inline-flex;align-items:center;gap:8px;padding:11px 16px;border:1px solid #e2e7e3;border-radius:8px;background:#ffffff;color:#17201b;font-size:14px;font-weight:650;text-decoration:none;"
    >
      Applicazioni dell'ozono
      <span aria-hidden="true">→</span>
    </a>


    <a
      href="#problematiche"
      style="display:inline-flex;align-items:center;gap:8px;padding:11px 16px;border:1px solid #e2e7e3;border-radius:8px;background:#ffffff;color:#17201b;font-size:14px;font-weight:650;text-decoration:none;"
    >
      Problematiche
      <span aria-hidden="true">→</span>
    </a>


    <a
      href="#soluzioni"
      style="display:inline-flex;align-items:center;gap:8px;padding:11px 16px;border:1px solid #e2e7e3;border-radius:8px;background:#ffffff;color:#17201b;font-size:14px;font-weight:650;text-decoration:none;"
    >
      Soluzioni OzonoGroup
      <span aria-hidden="true">→</span>
    </a>

  </nav>

</section>  
    '''

    article_html += '''
    <!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Industria lattiero-casearia: panoramica del settore</title>

  <meta
    name="description"
    content="Panoramica dell'industria lattiero-casearia: prodotti, processi produttivi, applicazioni dell'ozono, problematiche, soluzioni e risorse."
  >
</head>

<body style="margin:0;background:#f7f8f6;color:#17201b;font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;line-height:1.6;">

  <main>

    <!-- =========================================================
         3. PANORAMICA DEL SETTORE
         ========================================================= -->

    <section
      id="panoramica-settore"
      aria-labelledby="panoramica-settore-title"
      style="max-width:1180px;margin:0 auto;padding:80px 24px;"
    >

      <!-- Section header -->

      <div style="max-width:760px;margin-bottom:48px;">

        <p
          style="margin:0 0 12px;color:#1f5c45;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;"
        >
          Esplora il settore
        </p>

        <h2
          id="panoramica-settore-title"
          style="margin:0 0 18px;color:#17201b;font-size:clamp(30px,4vw,46px);line-height:1.12;letter-spacing:-.035em;font-weight:750;"
        >
          Panoramica dell'industria lattiero-casearia
        </h2>

        <p
          style="margin:0;color:#68736c;font-size:18px;line-height:1.7;"
        >
          Esplora i principali elementi dell'industria lattiero-casearia:
          prodotti, processi produttivi, applicazioni dell'ozono,
          problematiche operative, soluzioni tecnologiche e risorse
          di approfondimento.
        </p>

      </div>


      <!-- =======================================================
           KNOWLEDGE MAP
           ======================================================= -->

      <nav
        aria-label="Mappa dell'industria lattiero-casearia"
        style="display:flex;flex-wrap:wrap;gap:16px;"
      >


        <!-- =====================================================
             1. PRODOTTI
             Entità: cosa produce il settore
             ===================================================== -->

        <a
          href="#prodotti"
          style="display:flex;flex:1 1 340px;min-width:280px;min-height:220px;flex-direction:column;justify-content:space-between;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;color:#17201b;text-decoration:none;"
        >

          <div>

            <span
              aria-hidden="true"
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;margin-bottom:22px;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:18px;font-weight:700;"
            >
              01
            </span>

            <h3
              style="margin:0 0 10px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
            >
              Prodotti
            </h3>

            <p
              style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
            >
              Latte, formaggi, yogurt, burro e altri prodotti
              e derivati lattiero-caseari.
            </p>

          </div>

          <span
            style="display:inline-flex;align-items:center;gap:8px;margin-top:24px;color:#1f5c45;font-size:14px;font-weight:700;"
          >
            Esplora i prodotti
            <span aria-hidden="true">→</span>
          </span>

        </a>


        <!-- =====================================================
             2. PROCESSI
             Entità: cosa fa il settore
             ===================================================== -->

        <a
          href="#processi"
          style="display:flex;flex:1 1 340px;min-width:280px;min-height:220px;flex-direction:column;justify-content:space-between;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;color:#17201b;text-decoration:none;"
        >

          <div>

            <span
              aria-hidden="true"
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;margin-bottom:22px;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:18px;font-weight:700;"
            >
              02
            </span>

            <h3
              style="margin:0 0 10px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
            >
              Processi
            </h3>

            <p
              style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
            >
              Dalla raccolta e trattamento del latte alla
              trasformazione, fermentazione, caseificazione,
              stagionatura e confezionamento.
            </p>

          </div>

          <span
            style="display:inline-flex;align-items:center;gap:8px;margin-top:24px;color:#1f5c45;font-size:14px;font-weight:700;"
          >
            Esplora i processi
            <span aria-hidden="true">→</span>
          </span>

        </a>


        <!-- =====================================================
             3. APPLICAZIONI
             Entità: dove applicare la tecnologia
             ===================================================== -->

        <a
          href="#applicazioni"
          style="display:flex;flex:1 1 340px;min-width:280px;min-height:220px;flex-direction:column;justify-content:space-between;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;color:#17201b;text-decoration:none;"
        >

          <div>

            <span
              aria-hidden="true"
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;margin-bottom:22px;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:18px;font-weight:700;"
            >
              03
            </span>

            <h3
              style="margin:0 0 10px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
            >
              Applicazioni dell'ozono
            </h3>

            <p
              style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
            >
              Scopri le applicazioni dell'ozono per acqua,
              aria, superfici, ambienti e specifiche esigenze
              operative della filiera lattiero-casearia.
            </p>

          </div>

          <span
            style="display:inline-flex;align-items:center;gap:8px;margin-top:24px;color:#1f5c45;font-size:14px;font-weight:700;"
          >
            Esplora le applicazioni
            <span aria-hidden="true">→</span>
          </span>

        </a>


        <!-- =====================================================
             4. PROBLEMATICHE
             Entità: cosa deve essere gestito/risolto
             ===================================================== -->

        <a
          href="#problematiche"
          style="display:flex;flex:1 1 340px;min-width:280px;min-height:220px;flex-direction:column;justify-content:space-between;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;color:#17201b;text-decoration:none;"
        >

          <div>

            <span
              aria-hidden="true"
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;margin-bottom:22px;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:18px;font-weight:700;"
            >
              04
            </span>

            <h3
              style="margin:0 0 10px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
            >
              Problematiche
            </h3>

            <p
              style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
            >
              Biofilm, contaminazione microbiologica, muffe,
              qualità dell'acqua, igiene degli impianti,
              sanificazione e gestione degli ambienti produttivi.
            </p>

          </div>

          <span
            style="display:inline-flex;align-items:center;gap:8px;margin-top:24px;color:#1f5c45;font-size:14px;font-weight:700;"
          >
            Esplora le problematiche
            <span aria-hidden="true">→</span>
          </span>

        </a>


        <!-- =====================================================
             5. SOLUZIONI
             Entità: come intervenire
             ===================================================== -->

        <a
          href="#soluzioni"
          style="display:flex;flex:1 1 340px;min-width:280px;min-height:220px;flex-direction:column;justify-content:space-between;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;color:#17201b;text-decoration:none;"
        >

          <div>

            <span
              aria-hidden="true"
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;margin-bottom:22px;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:18px;font-weight:700;"
            >
              05
            </span>

            <h3
              style="margin:0 0 10px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
            >
              Soluzioni
            </h3>

            <p
              style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
            >
              Sistemi e tecnologie a ozono progettati per
              rispondere alle esigenze specifiche dei processi
              e degli ambienti dell'industria lattiero-casearia.
            </p>

          </div>

          <span
            style="display:inline-flex;align-items:center;gap:8px;margin-top:24px;color:#1f5c45;font-size:14px;font-weight:700;"
          >
            Scopri le soluzioni
            <span aria-hidden="true">→</span>
          </span>

        </a>


        <!-- =====================================================
             6. RISORSE
             Entità: conoscenza e approfondimento
             ===================================================== -->

        <a
          href="#risorse"
          style="display:flex;flex:1 1 340px;min-width:280px;min-height:220px;flex-direction:column;justify-content:space-between;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;color:#17201b;text-decoration:none;"
        >

          <div>

            <span
              aria-hidden="true"
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;margin-bottom:22px;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:18px;font-weight:700;"
            >
              06
            </span>

            <h3
              style="margin:0 0 10px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
            >
              Risorse
            </h3>

            <p
              style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
            >
              Guide, approfondimenti tecnici, normative,
              glossario e contenuti dedicati alla conoscenza
              dell'industria lattiero-casearia.
            </p>

          </div>

          <span
            style="display:inline-flex;align-items:center;gap:8px;margin-top:24px;color:#1f5c45;font-size:14px;font-weight:700;"
          >
            Esplora le risorse
            <span aria-hidden="true">→</span>
          </span>

        </a>

      </nav>

    </section>

  </main>


  <!-- =========================================================
       PREVIEW BUTTON
       ========================================================= -->

  <button
    type="button"
    onclick="document.getElementById('panoramica-settore').scrollIntoView({behavior:'smooth'});"
    style="position:fixed;right:24px;bottom:24px;z-index:1000;padding:14px 20px;border:0;border-radius:999px;background:#1f5c45;color:#ffffff;font-family:inherit;font-size:14px;font-weight:700;line-height:1;cursor:pointer;box-shadow:0 8px 24px rgba(0,0,0,.15);"
    aria-label="Visualizza la panoramica del settore"
  >
    Preview
  </button>

</body>
</html>
    '''

    article_html += '''
    <!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Processi dell'industria lattiero-casearia | OzonoGroup</title>

  <meta
    name="description"
    content="Scopri i principali processi dell'industria lattiero-casearia: ricevimento del latte, trattamento, trasformazione, caseificazione, fermentazione, confezionamento e conservazione."
  >
</head>

<body
  style="margin:0;background:#f7f8f6;color:#17201b;font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;line-height:1.6;"
>

  <main>

    <!-- =========================================================
         4. PROCESSI DELLA FILIERA
         ========================================================= -->

    <section
      id="processi"
      aria-labelledby="processi-title"
      style="max-width:1180px;margin:0 auto;padding:80px 24px;"
    >

      <!-- Header della sezione -->

      <div
        style="max-width:780px;margin-bottom:52px;"
      >

        <p
          style="margin:0 0 12px;color:#1f5c45;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;"
        >
          Filiera lattiero-casearia
        </p>

        <h2
          id="processi-title"
          style="margin:0 0 18px;color:#17201b;font-size:clamp(30px,4vw,46px);line-height:1.12;letter-spacing:-.035em;font-weight:750;"
        >
          Processi dell'industria lattiero-casearia
        </h2>

        <p
          style="margin:0;color:#68736c;font-size:18px;line-height:1.7;"
        >
          La filiera lattiero-casearia comprende una sequenza di processi
          che parte dal ricevimento e dalla gestione del latte e prosegue
          attraverso il trattamento, la trasformazione e la produzione
          di diversi derivati, fino al confezionamento e alla conservazione.
          A questi si affiancano processi trasversali dedicati all'igiene,
          alla gestione degli impianti e al controllo delle condizioni
          operative.
        </p>

      </div>


      <!-- =======================================================
           PROCESS FLOW
           ======================================================= -->

      <div
        style="display:flex;flex-wrap:wrap;gap:16px;align-items:stretch;"
      >


        <!-- =====================================================
             01. RICEVIMENTO E RACCOLTA
             ===================================================== -->

        <article
          style="display:flex;flex:1 1 340px;min-width:280px;flex-direction:column;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;"
        >

          <div
            style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;"
          >

            <span
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:16px;font-weight:700;"
              aria-hidden="true"
            >
              01
            </span>

            <span
              style="color:#9aa39d;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;"
            >
              Materia prima
            </span>

          </div>

          <h3
            style="margin:0 0 12px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
          >
            Ricevimento e raccolta del latte
          </h3>

          <p
            style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
          >
            Il latte viene raccolto, trasportato e ricevuto presso
            lo stabilimento lattiero-caseario, dove vengono gestite
            le prime fasi di controllo, accettazione e trasferimento
            verso le successive lavorazioni.
          </p>

        </article>


        <!-- =====================================================
             02. STOCCAGGIO E CONSERVAZIONE DEL LATTE
             ===================================================== -->

        <article
          style="display:flex;flex:1 1 340px;min-width:280px;flex-direction:column;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;"
        >

          <div
            style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;"
          >

            <span
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:16px;font-weight:700;"
              aria-hidden="true"
            >
              02
            </span>

            <span
              style="color:#9aa39d;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;"
            >
              Materia prima
            </span>

          </div>

          <h3
            style="margin:0 0 12px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
          >
            Stoccaggio e conservazione del latte
          </h3>

          <p
            style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
          >
            Il latte viene mantenuto in condizioni controllate prima
            della trasformazione, attraverso sistemi e procedure
            finalizzati alla conservazione delle caratteristiche
            della materia prima.
          </p>

        </article>


        <!-- =====================================================
             03. TRATTAMENTO E STANDARDIZZAZIONE
             ===================================================== -->

        <article
          style="display:flex;flex:1 1 340px;min-width:280px;flex-direction:column;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;"
        >

          <div
            style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;"
          >

            <span
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:16px;font-weight:700;"
              aria-hidden="true"
            >
              03
            </span>

            <span
              style="color:#9aa39d;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;"
            >
              Preparazione
            </span>

          </div>

          <h3
            style="margin:0 0 12px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
          >
            Trattamento e standardizzazione
          </h3>

          <p
            style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
          >
            Il latte può essere sottoposto a processi di trattamento
            e standardizzazione in funzione del prodotto finale,
            compresi processi termici e operazioni di regolazione
            della composizione.
          </p>

        </article>


        <!-- =====================================================
             04. SEPARAZIONE E OMOGENEIZZAZIONE
             ===================================================== -->

        <article
          style="display:flex;flex:1 1 340px;min-width:280px;flex-direction:column;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;"
        >

          <div
            style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;"
          >

            <span
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:16px;font-weight:700;"
              aria-hidden="true"
            >
              04
            </span>

            <span
              style="color:#9aa39d;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;"
            >
              Preparazione
            </span>

          </div>

          <h3
            style="margin:0 0 12px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
          >
            Separazione e omogeneizzazione
          </h3>

          <p
            style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
          >
            In base alla tipologia di prodotto, il latte può essere
            sottoposto a operazioni di separazione delle componenti
            e omogeneizzazione per ottenere caratteristiche fisiche
            e compositive specifiche.
          </p>

        </article>


        <!-- =====================================================
             05. PASTORIZZAZIONE E TRATTAMENTI TERMICI
             ===================================================== -->

        <article
          style="display:flex;flex:1 1 340px;min-width:280px;flex-direction:column;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;"
        >

          <div
            style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;"
          >

            <span
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:16px;font-weight:700;"
              aria-hidden="true"
            >
              05
            </span>

            <span
              style="color:#9aa39d;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;"
            >
              Trattamento
            </span>

          </div>

          <h3
            style="margin:0 0 12px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
          >
            Pastorizzazione e trattamenti termici
          </h3>

          <p
            style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
          >
            I trattamenti termici vengono utilizzati per ottenere
            specifiche caratteristiche igienico-sanitarie e
            tecnologiche del prodotto, in funzione della destinazione
            e del processo produttivo.
          </p>

        </article>


        <!-- =====================================================
             06. FERMENTAZIONE
             ===================================================== -->

        <article
          style="display:flex;flex:1 1 340px;min-width:280px;flex-direction:column;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;"
        >

          <div
            style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;"
          >

            <span
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:16px;font-weight:700;"
              aria-hidden="true"
            >
              06
            </span>

            <span
              style="color:#9aa39d;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;"
            >
              Trasformazione
            </span>

          </div>

          <h3
            style="margin:0 0 12px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
          >
            Fermentazione
          </h3>

          <p
            style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
          >
            La fermentazione è impiegata nella produzione di diversi
            alimenti lattiero-caseari, tra cui yogurt e altri prodotti
            fermentati, attraverso l'impiego di colture selezionate
            e condizioni di processo controllate.
          </p>

        </article>


        <!-- =====================================================
             07. CASEIFICAZIONE
             ===================================================== -->

        <article
          style="display:flex;flex:1 1 340px;min-width:280px;flex-direction:column;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;"
        >

          <div
            style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;"
          >

            <span
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:16px;font-weight:700;"
              aria-hidden="true"
            >
              07
            </span>

            <span
              style="color:#9aa39d;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;"
            >
              Trasformazione
            </span>

          </div>

          <h3
            style="margin:0 0 12px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
          >
            Caseificazione
          </h3>

          <p
            style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
          >
            La produzione dei formaggi comprende operazioni come
            coagulazione, rottura della cagliata, lavorazione,
            eventuale cottura, formatura e salatura, con fasi
            successive determinate dalla tipologia di formaggio.
          </p>

        </article>


        <!-- =====================================================
             08. STAGIONATURA E MATURAZIONE
             ===================================================== -->

        <article
          style="display:flex;flex:1 1 340px;min-width:280px;flex-direction:column;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;"
        >

          <div
            style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;"
          >

            <span
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:16px;font-weight:700;"
              aria-hidden="true"
            >
              08
            </span>

            <span
              style="color:#9aa39d;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;"
            >
              Maturazione
            </span>

          </div>

          <h3
            style="margin:0 0 12px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
          >
            Stagionatura e maturazione
          </h3>

          <p
            style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
          >
            Alcuni prodotti lattiero-caseari, in particolare i formaggi,
            vengono sottoposti a periodi di stagionatura e maturazione
            in condizioni ambientali controllate per sviluppare
            caratteristiche specifiche.
          </p>

        </article>


        <!-- =====================================================
             09. CONFEZIONAMENTO
             ===================================================== -->

        <article
          style="display:flex;flex:1 1 340px;min-width:280px;flex-direction:column;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;"
        >

          <div
            style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;"
          >

            <span
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:16px;font-weight:700;"
              aria-hidden="true"
            >
              09
            </span>

            <span
              style="color:#9aa39d;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;"
            >
              Prodotto finito
            </span>

          </div>

          <h3
            style="margin:0 0 12px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
          >
            Confezionamento
          </h3>

          <p
            style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
          >
            I prodotti vengono confezionati secondo caratteristiche
            e requisiti specifici, attraverso sistemi e materiali
            adeguati alla tipologia di alimento e alle condizioni
            previste per la distribuzione e la conservazione.
          </p>

        </article>


        <!-- =====================================================
             10. STOCCAGGIO E DISTRIBUZIONE
             ===================================================== -->

        <article
          style="display:flex;flex:1 1 340px;min-width:280px;flex-direction:column;padding:28px;border:1px solid #e2e7e3;border-radius:16px;background:#ffffff;"
        >

          <div
            style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;"
          >

            <span
              style="display:flex;width:40px;height:40px;align-items:center;justify-content:center;border-radius:10px;background:#eaf2ed;color:#1f5c45;font-size:16px;font-weight:700;"
              aria-hidden="true"
            >
              10
            </span>

            <span
              style="color:#9aa39d;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;"
            >
              Prodotto finito
            </span>

          </div>

          <h3
            style="margin:0 0 12px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:700;"
          >
            Stoccaggio e distribuzione
          </h3>

          <p
            style="margin:0;color:#68736c;font-size:15px;line-height:1.65;"
          >
            Dopo il confezionamento, i prodotti vengono conservati
            e movimentati in condizioni controllate fino alla
            distribuzione, in funzione delle caratteristiche
            del prodotto e dei requisiti di conservazione.
          </p>

        </article>

      </div>


      <!-- =======================================================
           PROCESSI TRASVERSALI
           Separati dai processi produttivi per mantenere MECE
           ======================================================= -->

      <div
        style="margin-top:56px;padding:36px;border:1px solid #dce5df;border-radius:20px;background:#eef4f0;"
      >

        <div
          style="max-width:760px;margin-bottom:32px;"
        >

          <p
            style="margin:0 0 10px;color:#1f5c45;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;"
          >
            Attività trasversali
          </p>

          <h3
            style="margin:0 0 14px;font-size:28px;line-height:1.2;letter-spacing:-.025em;font-weight:700;"
          >
            Processi di supporto alla produzione
          </h3>

          <p
            style="margin:0;color:#536159;font-size:16px;line-height:1.7;"
          >
            Accanto ai processi di trasformazione del latte esistono
            attività trasversali che supportano il funzionamento
            dello stabilimento e la gestione igienica degli impianti,
            delle superfici, dell'acqua e degli ambienti produttivi.
          </p>

        </div>


        <div
          style="display:flex;flex-wrap:wrap;gap:12px;"
        >

          <a
            href="#cip"
            style="display:inline-flex;align-items:center;gap:8px;padding:12px 16px;border:1px solid #d5dfd8;border-radius:8px;background:#ffffff;color:#17201b;font-size:14px;font-weight:650;text-decoration:none;"
          >
            Pulizia e sistemi CIP
            <span aria-hidden="true">→</span>
          </a>

          <a
            href="#sanificazione"
            style="display:inline-flex;align-items:center;gap:8px;padding:12px 16px;border:1px solid #d5dfd8;border-radius:8px;background:#ffffff;color:#17201b;font-size:14px;font-weight:650;text-decoration:none;"
          >
            Sanificazione
            <span aria-hidden="true">→</span>
          </a>

          <a
            href="#acqua"
            style="display:inline-flex;align-items:center;gap:8px;padding:12px 16px;border:1px solid #d5dfd8;border-radius:8px;background:#ffffff;color:#17201b;font-size:14px;font-weight:650;text-decoration:none;"
          >
            Gestione dell'acqua
            <span aria-hidden="true">→</span>
          </a>

          <a
            href="#ambienti"
            style="display:inline-flex;align-items:center;gap:8px;padding:12px 16px;border:1px solid #d5dfd8;border-radius:8px;background:#ffffff;color:#17201b;font-size:14px;font-weight:650;text-decoration:none;"
          >
            Gestione degli ambienti
            <span aria-hidden="true">→</span>
          </a>

          <a
            href="#reflui"
            style="display:inline-flex;align-items:center;gap:8px;padding:12px 16px;border:1px solid #d5dfd8;border-radius:8px;background:#ffffff;color:#17201b;font-size:14px;font-weight:650;text-decoration:none;"
          >
            Gestione delle acque reflue
            <span aria-hidden="true">→</span>
          </a>

        </div>

      </div>


      <!-- =======================================================
           INTERNAL NAVIGATION
           ======================================================= -->

      <nav
        aria-label="Navigazione nei processi dell'industria lattiero-casearia"
        style="display:flex;flex-wrap:wrap;gap:12px;margin-top:48px;padding-top:28px;border-top:1px solid #e2e7e3;"
      >

        <a
          href="#panoramica-settore"
          style="display:inline-flex;align-items:center;gap:8px;padding:11px 16px;border:1px solid #e2e7e3;border-radius:8px;background:#ffffff;color:#17201b;font-size:14px;font-weight:650;text-decoration:none;"
        >
          ← Panoramica del settore
        </a>

        <a
          href="#applicazioni"
          style="display:inline-flex;align-items:center;gap:8px;padding:11px 16px;border:1px solid #e2e7e3;border-radius:8px;background:#ffffff;color:#17201b;font-size:14px;font-weight:650;text-decoration:none;"
        >
          Applicazioni dell'ozono →
        </a>

        <a
          href="#soluzioni"
          style="display:inline-flex;align-items:center;gap:8px;padding:11px 16px;border:1px solid #e2e7e3;border-radius:8px;background:#ffffff;color:#17201b;font-size:14px;font-weight:650;text-decoration:none;"
        >
          Soluzioni OzonoGroup →
        </a>

      </nav>

    </section>

  </main>


  <!-- =========================================================
       PREVIEW BUTTON
       ========================================================= -->

  <button
    type="button"
    onclick="document.getElementById('processi').scrollIntoView({behavior:'smooth'});"
    style="position:fixed;right:24px;bottom:24px;z-index:1000;padding:14px 20px;border:0;border-radius:999px;background:#1f5c45;color:#ffffff;font-family:inherit;font-size:14px;font-weight:700;line-height:1;cursor:pointer;box-shadow:0 8px 24px rgba(0,0,0,.15);"
    aria-label="Visualizza i processi dell'industria lattiero-casearia"
  >
    Preview
  </button>

</body>
</html>
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
            {components.header_light_logo()}
            <main class="listing container-xl" style="margin-top: 5rem; margin-bottom: 5rem;">
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

    sectors_data = io.csv_to_dict('C:\ozonogroup\data\ssot\dataset\manual\settori_nuovo.csv', delimiter='\\')
    for item in sectors_data:
        sector_gen(item)

    