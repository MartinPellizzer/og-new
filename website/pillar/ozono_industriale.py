
import os

from lib import g
from lib import components

def sidebar_core_entity(): 
    html = f'''
        <div>
        <nav class="nav-global">
            <h2 style="margin-top: 0rem;">Sezioni principali</h2>
            <ul>
                <li><a href="/ozono-industriale/">Sistemi ad Ozono Industriali</a>
                    <ul>
                        <li><a href="/ozono-industriale/struttura/">Struttura</a></li>
                        <li><a href="/ozono-industriale/tecnologia/">Tecnologia</a></li>
                        <li><a href="/ozono-industriale/funzionamento/">Funzionamento</a></li>
                        <li><a href="/ozono-industriale/applicazioni/">Applicazioni</a></li>
                        <li><a href="/ozono-industriale/benefici/">Benefici</a></li>
                        <li><a href="/ozono-industriale/sicurezza/">Sicurezza</a></li>
                        <li><a href="/ozono-industriale/normativa/">Normativa</a></li>
                        <li><a href="/ozono-industriale/progettazione/">Progettazione</a></li>
                        <li><a href="/ozono-industriale/gestione/">Gestione</a></li>
                        <li><a href="/ozono-industriale/prestazioni/">Prestazioni</a></li>
                        <li><a href="/ozono-industriale/confronti/">Confronti</a></li>
                        <li><a href="/ozono-industriale/limiti/">Limiti</a></li>
                    </ul>
                </li>
            </ul>
        </nav>
        </div>
    '''
    return html

def sidebar_page(items): 
    if not items: return ''
    ###
    items_html = f''
    for item in items:
        href = item['href']
        anchor = item['anchor']
        item_html = f'<li><a href="#{href}">{anchor}</a></li>\n'
        items_html += item_html
    html = f'''
        <aside>
            <nav class="nav-page">
                <h2 style="margin-top: 0rem;">Tabella dei Contenuti</h2>
                <ul>
                    {items_html}
                </ul>
            <nav>
        </aside>
    '''
    return html

def main():
    url_slug = 'ozono-industriale'

    article_html = f'''
<h1>Guida completa ai sistemi di ozonizzazione industriale</h1>
<!-- Search Intent: Overview / Topical Authority -->
<!-- Entities: Sistemi a ozono industriale, Depurazione industriale, Sostenibilità aziendale -->

<section id="cos-e-ozono-industriale">
  <h2>Cos’è l’ozono industriale e come funziona</h2>
  <!-- Search Intent: Mechanism -->
  <!-- Entities: O3, Ossidazione -->
  <p>L’ozono industriale (<strong>O3</strong>) è un potente ossidante utilizzato per <em>depurazione acqua e aria</em> nelle aziende. Scopri come funziona e quali contaminanti può eliminare.</p>

  <h3>Proprietà fisico-chimiche dell’ozono</h3>
  <p>Stabilità, solubilità e potere ossidante spiegati per applicazioni industriali.</p>

  <h3>Come l’ozono elimina batteri, virus e contaminanti</h3>
  <p>Meccanismo microbicida e sanificante.</p>
  <p>Approfondisci il confronto con altre tecnologie: 
    <a href="sistemi_ozono_vs_cloro.html">Sistemi a ozono vs sistemi a cloro</a>
  </p>
</section>

<section id="applicazioni-ozono-industriale">
  <h2>Applicazioni principali dei sistemi a ozono industriale</h2>
  <!-- Search Intent: Use Case / Outcome -->
  <!-- Entities: Industria alimentare, Lavanderie industriali, Settori non alimentari -->

  <h3>Trattamento dell’acqua</h3>
  <p>Riduzione consumo idrico e miglioramento della qualità dell’acqua.</p>
  <p>Vedi i dettagli sui benefici: 
    <a href="benefici_depuration.html">Benefici dei sistemi a ozono industriale per la depurazione delle acque aziendali</a>
  </p>

  <h3>Trattamento dell’aria</h3>
  <p>Applicazioni nelle industrie alimentari e farmaceutiche.</p>

  <h3>Altre applicazioni industriali</h3>
  <p>Tessile, cartario e chimico: riduzione di prodotti chimici tradizionali.</p>
  <p>Leggi esempi pratici: 
    <a href="casi_pratici.html">Casi pratici di implementazione dell’ozono in industrie non alimentari</a>
  </p>
</section>

<section id="vantaggi-sistemi-ozono">
  <h2>Vantaggi dei sistemi a ozono industriale</h2>
  <!-- Search Intent: Outcome -->
  <!-- Entities: Efficienza energetica, Manutenzione predittiva -->
  <p>Scopri i principali benefici in termini operativi, economici e ambientali.</p>
  <ul>
    <li><a href="riduzione_costi.html">Ridurre i costi di manutenzione grazie ai sistemi a ozono industriale</a></li>
    <li><a href="sostenibilita_ozono.html">Come l’ozono contribuisce alla sostenibilità aziendale e al risparmio energetico</a></li>
  </ul>
</section>

<section id="rischi-e-sicurezza">
  <h2>Rischi e sicurezza nell’uso dei sistemi a ozono</h2>
  <!-- Search Intent: Risk / Trust Flow -->
  <!-- Entities: Sicurezza industriale, Impatto ambientale -->
  <p>Indicazioni sui rischi per i lavoratori e l’ambiente, e come mitigarli.</p>
  <ul>
    <li><a href="rischi_ambientali.html">Rischi ambientali dei sistemi a ozono industriale e come mitigarli</a></li>
  </ul>

  <h3>Sicurezza dei lavoratori</h3>
  <p>Procedure operative, DPI e monitoraggio ambientale.</p>

  <h3>Impatti ambientali</h3>
  <p>Emissioni, normative e compliance industriale.</p>
</section>

<section id="scelta-sistema-ozono">
  <h2>Come scegliere il sistema a ozono più adatto</h2>
  <!-- Search Intent: Decision -->
  <!-- Entities: Criteri di selezione impianti industriali, ROI -->
  <p>Linee guida per valutare criteri tecnici, economici e normativi.</p>
  <ul>
    <li><a href="criteri_scelta.html">Criteri per scegliere il sistema a ozono giusto per la tua azienda</a></li>
    <li><a href="sistemi_ozono_vs_cloro.html">Sistemi a ozono vs sistemi a cloro</a></li>
  </ul>
</section>

<section id="confronto-tecnologie">
  <h2>Confronto tra tecnologie alternative</h2>
  <!-- Search Intent: Comparison / Query Disambiguation -->
  <!-- Entities: Cloro, Ossigeno attivo -->
  <p>Come l’ozono si distingue da altre tecnologie per la sanificazione industriale.</p>
  <a href="sistemi_ozono_vs_cloro.html">Sistemi a ozono vs sistemi a cloro</a>
</section>

<section id="faq-approfondimenti">
  <h2>Domande frequenti e approfondimenti</h2>
  <!-- Search Intent: Navigation / Utility / Topical Reinforcement -->
  <ul>
    <li><a href="benefici_depuration.html">Benefici acqua</a></li>
    <li><a href="riduzione_costi.html">Riduzione costi</a></li>
    <li><a href="casi_pratici.html">Casi pratici</a></li>
    <li><a href="rischi_ambientali.html">Rischi ambientali</a></li>
  </ul>
</section>
    '''
    article_html = article_html.replace("’", "'")

    sidebar_core_entity_html = sidebar_core_entity()
    sidebar_core_entity_html = '<div></div>'
    sidebar_page_html = sidebar_page([]) 

    html = f'''
    <!DOCTYPE tml>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guida completa ai sistemi di ozonizzazione industriale</title>
    <link rel="stylesheet" href="/styles.css">
    </head>
    <body>
        {components.header_default()}
        <div class="hub">
            {sidebar_core_entity_html}
            <main>
                <article>
                    {article_html}
                </article>
            </main>
            {sidebar_page_html}
        </div>
        {components.footer_dark()}
    </body>
    </html>
    '''

    html_folderpath = f'{g.WEBSITE_FOLDERPATH}/{url_slug}'
    os.makedirs(html_folderpath, exist_ok=True)
    html_filepath = f'{html_folderpath}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)

