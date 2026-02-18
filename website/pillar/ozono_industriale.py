
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

def ozono_industriale__vs_cloro__gen():
    url_slug = 'ozono-industriale/vs-cloro'
    article_html = f'''
    '''
    article_html = article_html.replace("’", "'")
    sidebar_core_entity_html = sidebar_core_entity()
    sidebar_core_entity_html = '<div></div>'
    sidebar_page_html = sidebar_page([]) 
    html = f'''
    <!DOCTYPE html>
    <html lang="it">
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
    print(html)

def ozono_industriale__benefici__gen():
    url_slug = 'ozono-industriale/benefici'
    article_html = f'''
    '''
    article_html = article_html.replace("’", "'")
    sidebar_core_entity_html = sidebar_core_entity()
    sidebar_core_entity_html = '<div></div>'
    sidebar_page_html = sidebar_page([]) 
    html = f'''
    <!DOCTYPE html>
    <html lang="it">
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
    print(html)

def ozono_industriale__casi__gen():
    url_slug = 'ozono-industriale/casi'
    article_html = f'''
    '''
    article_html = article_html.replace("’", "'")
    sidebar_core_entity_html = sidebar_core_entity()
    sidebar_core_entity_html = '<div></div>'
    sidebar_page_html = sidebar_page([]) 
    html = f'''
    <!DOCTYPE html>
    <html lang="it">
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
    print(html)

def ozono_industriale__risparmio__gen():
    url_slug = 'ozono-industriale/risparmio'
    article_html = f'''
    '''
    article_html = article_html.replace("’", "'")
    sidebar_core_entity_html = sidebar_core_entity()
    sidebar_core_entity_html = '<div></div>'
    sidebar_page_html = sidebar_page([]) 
    html = f'''
    <!DOCTYPE html>
    <html lang="it">
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
    print(html)

def ozono_industriale__sostenibilita__gen():
    url_slug = 'ozono-industriale/sostenibilita'
    article_html = f'''
    '''
    article_html = article_html.replace("’", "'")
    sidebar_core_entity_html = sidebar_core_entity()
    sidebar_core_entity_html = '<div></div>'
    sidebar_page_html = sidebar_page([]) 
    html = f'''
    <!DOCTYPE html>
    <html lang="it">
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
    print(html)

def ozono_industriale__rischi__gen():
    url_slug = 'ozono-industriale/rischi'
    article_html = f'''
    '''
    article_html = article_html.replace("’", "'")
    sidebar_core_entity_html = sidebar_core_entity()
    sidebar_core_entity_html = '<div></div>'
    sidebar_page_html = sidebar_page([]) 
    html = f'''
    <!DOCTYPE html>
    <html lang="it">
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
    print(html)

def ozono_industriale__scelta__gen():
    url_slug = 'ozono-industriale/scelta'
    article_html = f'''
    '''
    article_html = article_html.replace("’", "'")
    sidebar_core_entity_html = sidebar_core_entity()
    sidebar_core_entity_html = '<div></div>'
    sidebar_page_html = sidebar_page([]) 
    html = f'''
    <!DOCTYPE html>
    <html lang="it">
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
    print(html)

def ozono_industriale__gen():
    url_slug = 'ozono-industriale'

    article_html = f'''

<h1>Guida completa ai sistemi di ozonizzazione industriale</h1>

<p>
I sistemi di ozonizzazione industriale ossidano batteri, virus e composti organici complessi, garantendo la sanificazione dell’acqua di processo, dell’aria dei reparti produttivi e delle superfici nell’industria alimentare, tessile e chimica.
</p>

<p>
L’ozono (O<sub>3</sub>) ossida rapidamente le membrane cellulari di batteri, virus e spore, degradando biofilm e composti organici complessi nei flussi d’acqua industriali, senza generare residui chimici persistenti. L’implementazione di un impianto di ozonizzazione richiede l’analisi delle portate, della concentrazione target, delle normative di sicurezza e della compatibilità con i processi produttivi esistenti.
</p>

<p>
Questa guida illustra il funzionamento dei generatori di ozono industriale, applicazioni pratiche, vantaggi operativi ed economici, rischi per sicurezza e ambiente, confronto con cloro e UV, e criteri tecnici per selezionare il sistema più adatto a ogni settore industriale.
</p>

<!-- ========================= -->
<!-- FUNZIONAMENTO -->
<!-- ========================= -->

<section id="cose-ozono-industriale">
  <h2>Cos’è l’ozono industriale e come funziona</h2>
  <p>L’ozono (O<sub>3</sub>) è una molecola triatomica composta da tre atomi di ossigeno. In ambito industriale viene prodotto tramite <strong>scarica a corona</strong> o sistemi ad alta tensione che trasformano l’ossigeno (O<sub>2</sub>) in ozono.</p>
  <p>L’elevato potenziale ossidativo dell’ozono, superiore al cloro, distrugge rapidamente le membrane cellulari dei microrganismi e ossida composti organici complessi nei sistemi idrici industriali.</p>
  <h3>Proprietà fisico-chimiche dell’ozono</h3>
  <ul>
    <li>Elevato potere ossidante</li>
    <li>Instabilità naturale (si riconverte in O<sub>2</sub>)</li>
    <li>Nessun residuo chimico persistente</li>
    <li>Produzione in loco (misurata in g/h)</li>
    <li>Concentrazione operativa espressa in ppm o mg/L</li>
  </ul>
  <p>La progettazione dell’impianto richiede il calcolo di:</p>
  <ol>
    <li>Portata del fluido trattato</li>
    <li>Tempo di contatto</li>
    <li>Concentrazione target</li>
    <li>Volume del reattore</li>
  </ol>
  <h3>Meccanismo di inattivazione microbiologica</h3>
  <p>L’ozono agisce ossidando le membrane cellulari dei microrganismi, distruggendo pareti cellulari e strutture proteiche. Questo processo porta all’eliminazione di:</p>
  <ul>
    <li>Batteri</li>
    <li>Virus</li>
    <li>Spore</li>
    <li>Biofilm</li>
  </ul>
  <p>Rispetto ad altre tecnologie come il cloro, l’ozono non genera sottoprodotti organoclorurati. Per un’analisi tecnica dettagliata delle differenze operative, consulta il <a href="/ozono-industriale/vs-cloro">confronto tra sistemi a ozono vs sistemi a cloro</a>.</p>
</section>


<!-- ========================= -->
<!-- APPLICAZIONI -->
<!-- ========================= -->

<section id="applicazioni-industriali-ozono">
  <h2>Applicazioni industriali dei sistemi a ozono</h2>
  <p>I sistemi di ozonizzazione industriale sono utilizzati in acqua e aria di reparti alimentari, tessili e cartari per mantenere standard igienici elevati e ridurre l’uso di prodotti chimici tradizionali.</p>
    <h3>Trattamento delle acque industriali</h3>
    <p>L’ozono è impiegato per:</p>
    <ul>
      <li>Riduzione di COD e BOD</li>
      <li>Eliminazione di odori</li>
      <li>Ossidazione di composti organici complessi</li>
      <li>Miglioramento della qualità dell’acqua di processo</li>
    </ul>
    <p>
    Nelle aziende con flussi idrici superiori a 500 m³/giorno, i sistemi di ozonizzazione riducono i costi di smaltimento dei reflui e aumentano il riutilizzo dell’acqua di processo fino al 30%.  
    Consulta anche <a href="/ozono-industriale/benefici">i benefici dei sistemi a ozono per la depurazione delle acque aziendali</a>.
    </p>
    <h3>Sanificazione dell’aria e ambienti produttivi</h3>
    <p>
      In ambienti a rischio microbiologico, come l’industria alimentare, 
      l’ozono consente di:
    </p>
    <p>
    Nei magazzini frigoriferi e nelle linee di produzione alimentare, l’ozonizzazione dell’aria abbassa la carica batterica fino al 99%, inibisce la crescita di muffe e neutralizza odori di fermentazione.
    </p>
    <h3>Applicazioni nei settori non alimentari</h3>
    <p>
      Nel tessile e nel cartario l’ozono viene utilizzato per:
    </p>
    <ul>
      <li>Trattamenti ossidativi</li>
      <li>Riduzione dell’uso di agenti chimici</li>
      <li>Miglioramento dei processi di sbiancamento</li>
    </ul>
    <p>
      Approfondisci alcuni 
      <a href="/ozono-industriale/casi">
        casi pratici di implementazione dell’ozono in industrie non alimentari
      </a>
      per comprendere scenari applicativi concreti.
    </p>
</section>

<!-- ========================= -->
<!-- VANTAGGI -->
<!-- ========================= -->

<section id="vantaggi-sistemi-ozono">
  <h2>Vantaggi operativi ed economici dei sistemi a ozono</h2>
  <p>L’adozione di un sistema di ozonizzazione comporta vantaggi misurabili sia sul piano tecnico che economico.</p>
  <h3>Riduzione dei costi operativi</h3>
    <p>
    L’installazione di un impianto di ozonizzazione industriale riduce l’uso di cloro del 70%, diminuisce i fermi macchina e taglia i costi operativi annui di trattamento acqua e aria.
    </p>
    <p>Scopri come è possibile <a href="/ozono-industriale/risparmio">ridurre i costi di manutenzione grazie ai sistemi a ozono industriale</a>.</p>
  <h3>Miglioramento della qualità produttiva</h3>
  <ul>
    <li>Stabilità microbiologica</li>
    <li>Riduzione contaminazioni crociate</li>
    <li>Minori fermi impianto</li>
  </ul>
  <h3>Sostenibilità e conformità ambientale</h3>
  <p>L’ozono si riconverte naturalmente in ossigeno, contribuendo a:</p>
  <ul>
    <li>Riduzione dell’impatto ambientale</li>
    <li>Migliore conformità normativa</li>
    <li>Miglioramento dell’immagine aziendale</li>
  </ul>
  <p>Per approfondire l’impatto ambientale positivo, leggi come <a href="/ozono-industriale/sostenibilita">l’ozono contribuisce alla sostenibilità aziendale</a>.</p>
</section>

<!-- ========================= -->
<!-- CONFRONTO -->
<!-- ========================= -->

<section id="confronto-tecnologie">
  <h2>Confronto tra ozono e tecnologie alternative</h2>
  <p>
    Per selezionare il sistema di sanificazione più efficace, confronta ozono, cloro e UV in termini di residui chimici, efficacia microbiologica, impatto ambientale e requisiti operativi.
  </p>
  <table border="1" cellspacing="0" cellpadding="6">
    <thead>
      <tr>
        <th>Tecnologia</th>
        <th>Residui</th>
        <th>Efficacia</th>
        <th>Impatto ambientale</th>
        <th>Gestione</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Ozono</td>
        <td>Nessuno</td>
        <td>Molto alta</td>
        <td>Basso</td>
        <td>Produzione in loco</td>
      </tr>
      <tr>
        <td>Cloro</td>
        <td>Sottoprodotti</td>
        <td>Alta</td>
        <td>Medio</td>
        <td>Stoccaggio chimico</td>
      </tr>
      <tr>
        <td>UV</td>
        <td>Nessuno</td>
        <td>Limitata al punto di esposizione</td>
        <td>Basso</td>
        <td>Nessun effetto residuo</td>
      </tr>
    </tbody>
  </table>
  <p>L’ozono si distingue per l’assenza di residui e per l’azione ossidativa estesa. Per un confronto tecnico dettagliato, consulta la guida su 
    <a href="/ozono-industriale/vs-cloro">sistemi a ozono vs sistemi a cloro</a>.
  </p>
</section>

<!-- ========================= -->
<!-- SICUREZZA -->
<!-- ========================= -->
<section id="rischi-e-sicurezza">
  <h2>Rischi, sicurezza e conformità normativa</h2>
  <p>
L’ozono industriale è un gas ossidante che, se non monitorato con sensori di concentrazione e sistemi di abbattimento, può superare i limiti di esposizione e compromettere sicurezza dei lavoratori e ambientale.
  </p>
  <h3>Sicurezza dei lavoratori</h3>
  <ul>
    <li>Monitoraggio delle concentrazioni ambientali (ppm)</li>
    <li>Sensori di rilevamento dell’ozono</li>
    <li>Sistemi di distruzione dell’ozono residuo</li>
    <li>Formazione e addestramento del personale</li>
  </ul>
  <h3>Impatto ambientale e controllo emissioni</h3>
  <ul>
    <li>Sistemi di abbattimento delle emissioni</li>
    <li>Controllo continuo dei livelli di ozono rilasciati</li>
    <li>Conformità ai limiti normativi vigenti</li>
  </ul>
  <p>Per approfondire, consulta l’analisi sui <a href="/ozono-industriale/rischi">rischi ambientali dei sistemi a ozono industriale e come mitigarli</a>.</p>
</section>

<!-- ========================= -->
<!-- DECISION FRAMEWORK -->
<!-- ========================= -->

<section id="scelta-sistema-ozono">
  <h2>Come scegliere il sistema di ozonizzazione più adatto</h2>
  <p>
    La scelta di un generatore di ozono industriale richiede la valutazione di portata idrica, concentrazione target, tempo di contatto, compatibilità di processo e costi energetici.
  </p>
  <h3>5 criteri tecnici per valutare un sistema</h3>
  <ol>
    <li><strong>Capacità di produzione di ozono (g/h)</strong> – Misura la quantità di ozono prodotto per ora in base alle esigenze del processo.</li>
    <li><strong>Portata e volume del fluido trattato</strong> – Verifica che il sistema gestisca correttamente il volume di acqua o aria da sanificare.</li>
    <li><strong>Tempo di contatto necessario</strong> – Determina quanto tempo l’ozono deve restare in contatto con il fluido per ottenere efficacia microbiologica.</li>
    <li><strong>Sistema di monitoraggio e controllo</strong> – Include sensori, regolazioni automatiche e sicurezza operativa.</li>
    <li><strong>ROI e costi operativi stimati</strong> – Valutazione economica complessiva considerando manutenzione, consumi energetici e risparmio chimico.</li>
  </ol>
  <p>Una corretta analisi preliminare evita sovradimensionamenti o inefficienze. Approfondisci i <a href="/ozono-industriale/scelta">criteri per scegliere il sistema a ozono giusto per la tua azienda</a> per un’analisi completa.</p>
</section>

<!-- ========================= -->
<!-- AFFIDABILITA -->
<!-- ========================= -->

<section id="affidabilita-conformita">
  <h2>Affidabilità tecnica e standard di conformità</h2>
  <p>
    Ogni impianto industriale deve assicurare continuità operativa, utilizzo di componenti certificati ISO e UNI, manutenzione programmata e piena conformità a norme HACCP e ambientali.
  </p>
  <p>La scelta di fornitori qualificati e sistemi certificati è determinante per assicurare affidabilità nel lungo periodo.</p>
</section>

<!-- ========================= -->
<!-- FAQ -->
<!-- ========================= -->

<section id="faq-ozonizzazione">
  <h2>Domande frequenti sui sistemi di ozonizzazione industriale</h2>

  <div class="faq-item">
    <h3>Quanto è sicuro un sistema di ozonizzazione industriale?</h3>
    <p>
    Un impianto di ozonizzazione progettato con sensori di monitoraggio in tempo reale mantiene le concentrazioni di O3 sotto i 0,1 ppm, rispettando i limiti di esposizione OSHA e UNI EN 60079.
    </p>
  </div>

  <div class="faq-item">
    <h3>Qual è il costo medio di implementazione?</h3>
    <p>
    Il costo di installazione di un sistema di ozonizzazione industriale varia dai 15.000 ai 120.000 €, in funzione della capacità produttiva (g/h), del settore industriale e dei requisiti di automazione.
    </p>
  </div>

  <div class="faq-item">
    <h3>L’ozono può sostituire completamente il cloro?</h3>
    <p>In molte applicazioni sì, ma la sostituzione totale dipende dal contesto normativo e dalle esigenze microbiologiche specifiche.</p>
  </div>

</section>

<!-- ========================= -->
<!-- CTA -->
<!-- ========================= -->

<section id="consulenza-tecnica">
  <h2>Richiedi una consulenza tecnica personalizzata</h2>
  <p>Ogni impianto industriale presenta esigenze specifiche. Una valutazione tecnica preliminare consente di:</p>
  <ul>
    <li>Analizzare il fabbisogno reale</li>
    <li>Calcolare il dimensionamento ottimale</li>
    <li>Stimare il ritorno dell’investimento (ROI)</li>
  </ul>
  <p>Richiedi una consulenza tecnica per valutare la soluzione più adatta alla tua azienda.</p>
  <a href="/contatti" class="cta-button" style="display:inline-block;padding:12px 24px;background-color:#0056b3;color:#fff;text-decoration:none;border-radius:4px;">Richiedi valutazione tecnica</a>
</section>

<!-- ========================= -->
<!-- AUTHOR -->
<!-- ========================= -->


<section id="autore">
  <h2>Autore</h2>
  <div itemscope itemtype="https://schema.org/Person">
    <p><strong itemprop="name">Nome Cognome</strong></p>
    <p itemprop="jobTitle">Ingegnere ambientale specializzato in sistemi di ozonizzazione industriale</p>
    <p itemprop="description">Oltre X anni di esperienza nella progettazione e implementazione di impianti per trattamento acqua e aria in ambito industriale.</p>
    <!-- <link itemprop="url" href="https://www.tuosito.it/autore/nome-cognome"> -->
  </div>
</section>

    '''
    article_html = article_html.replace("’", "'")

    sidebar_core_entity_html = sidebar_core_entity()
    sidebar_core_entity_html = '<div></div>'
    sidebar_page_html = sidebar_page([]) 

    html = f'''
    <!DOCTYPE html>
    <html lang="it">
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
    print(html)


def main():
    ozono_industriale__gen()
    ozono_industriale__vs_cloro__gen()
    ozono_industriale__benefici__gen()
    ozono_industriale__casi__gen()
    ozono_industriale__risparmio__gen()
    ozono_industriale__sostenibilita__gen()
    ozono_industriale__rischi__gen()
    ozono_industriale__scelta__gen()
    
