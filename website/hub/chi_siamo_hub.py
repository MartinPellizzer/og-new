from lib import g
from lib import components

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
                    <a class="button-default-3" href="/ozono.html">
                        <span>Prenota Consulenza Gratuita</span>
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#ffffff"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                    </a>
                </div>
            </div>
        </section>
    '''
    return html

def gen():
    section_hero_py = '5rem'
    section_py = '8rem'
    
    ########################################
    # hero
    ########################################
    hero = f'''
        <section class="container-xl" style="padding-top: {section_hero_py}; padding-bottom: {section_hero_py};">
            <div style="display: flex; justify-content: space-between; center;">
                <div style="flex: 2;">
                    <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
                        Innoviamo la sanificazione industriale con la forza dell'ozono
                    </h2>
                    <p style="color: #1f1f1f;">                        
                        Un team di tecnici, ingegneri e ricercatori al servizio della qualità dell'aria e dell'igiene industriale.
                    </p>
                </div>
                <div style="flex: 1; display: flex; justify-content: end; margin-top: 0.25rem;">
                    <div style="display: inline-block;">
                        <a class="button-default-1" href="/servizi.html">
                            <span>Richiedi Preventivo</span>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z"/></svg>                
                        </a>
                    </div>
                </div>
            </div>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div>  
    '''
    
    ########################################
    # Mission & Valori
    ########################################
    html_missione_valori = f'''
        <section class="container-md" style="padding-top: {section_py}; padding-bottom: {section_py};">
            <h2 style="color: #222222; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
                La nostra missione: innovare la sanificazione industriale in modo sostenibile
            </h2>
            <p style="color: #1f1f1f; margin-bottom: 1rem;">                        
                Crediamo che la sicurezza degli ambienti industriali e la tutela dell'ambiente possano coesistere.
                Per questo sviluppiamo e forniamo tecnologie professionali a ozono, pensate per eliminare batteri, muffe e odori senza l'uso di sostanze chimiche, garantendo un impatto ambientale minimo e risultati misurabili.
                La nostra missione è rendere la sanificazione un processo efficiente, automatico e scientificamente controllato, integrabile nei sistemi produttivi di ogni azienda moderna.            
            </p>
            <p style="color: #1f1f1f; margin-bottom: 1rem;">                        
                Per noi sostenibilità significa ridurre sprechi e residui, eliminando detergenti aggressivi e riducendo l'uso d'acqua.
                Ogni impianto a ozono che installiamo contribuisce a migliorare la qualità dell'aria e a ridurre l'impronta ecologica delle imprese che serviamo.
                Non è solo una scelta tecnica, ma un impegno etico verso l'ambiente e le generazioni future.            
            </p>
            <p style="color: #1f1f1f; margin-bottom: 1rem;">                        
Collaboriamo con ingegneri, laboratori e centri di ricerca per perfezionare i nostri generatori di ozono industriali.
Ogni sistema è progettato per essere efficiente, sicuro e conforme agli standard europei, con un controllo costante dei parametri di emissione e concentrazione.
Crediamo nella tecnologia come strumento di prevenzione, non solo di intervento: i nostri sistemi automatizzati trasformano la sanificazione in un processo costante e misurabile.            
            </p>
            <p style="color: #1f1f1f; margin-bottom: 1rem;">                        
Ogni progetto nasce da un'analisi tecnica dettagliata e si conclude con un supporto post-vendita reale, garantito da tecnici specializzati.
Non offriamo solo prodotti, ma soluzioni complete, calibrate sulle necessità di ogni settore: alimentare, logistica, Ho.Re.Ca., agricoltura e uffici.
La fiducia dei nostri clienti è la nostra misura di successo.
            </p>
            <p style="color: #1f1f1f; margin-bottom: 1rem;">                        
Nasciamo nel mondo industriale, e parliamo il linguaggio di chi produce.
Comprendiamo le sfide dei processi, le esigenze di continuità operativa e i protocolli di sicurezza.
Per questo le nostre soluzioni ad ozono sono integrabili in linee produttive, impianti HVAC, magazzini e aree di stoccaggio, adattandosi ai flussi reali delle aziende.            </p>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div> 
    '''

    ########################################
    # Storia
    ########################################
    html_storia = f'''
        <section class="container-md" style="padding-top: {section_py}; padding-bottom: {section_py};">
            <h2 style="color: #1f1f1f; font-size: 3rem; line-height: 1; font-weight: normal; margin-bottom: 1rem;">
15 anni di esperienza, ricerca e innovazione continua nel mondo dell'ozono
            </h2>
            <p style="color: #1f1f1f; margin-bottom: 1rem;">                        
                Da oltre 15 anni lavoriamo per rendere la sanificazione industriale più sicura, efficiente e sostenibile.
Nati come impresa tecnica specializzata nella disinfezione ad ozono per ambienti produttivi, abbiamo costruito la nostra reputazione su precisione, affidabilità e risultati verificabili.

Nel tempo abbiamo ampliato il nostro know-how, evolvendoci da semplici installatori a partner tecnologici per l'industria, capaci di progettare sistemi personalizzati su misura per ogni esigenza.
            </p>
            <h3 style="color: #1f1f1f; font-size: 1rem; line-height: 1.5; font-weight: bold; margin-bottom: 1rem;">
            2009-2012: Le origini
            </h3>
            <p style="color: #1f1f1f; margin-bottom: 1rem;">                        
                Abbiamo iniziato nel settore della sanificazione ad ozono per piccole imprese e ambienti alimentari, sperimentando le prime applicazioni pratiche della tecnologia in Italia.
In questa fase nasce la nostra competenza sul campo e la filosofia che ancora oggi ci guida: unire igiene e sostenibilità.
            </p>
            <h3 style="color: #1f1f1f; font-size: 1rem; line-height: 1.5; font-weight: bold; margin-bottom: 1rem;">
                2013-2018: Crescita e consolidamento
            </h3>
            <p style="color: #1f1f1f; margin-bottom: 1rem;">                        
Con la crescita della domanda industriale, abbiamo sviluppato i primi generatori professionali di nostra progettazione, e ampliato la rete di installazioni in ambito alimentare, logistico e Ho.Re.Ca..
Durante questi anni abbiamo costruito la nostra reputazione tecnica e una solida base di clienti fidelizzati.
            </p>
            <h3 style="color: #1f1f1f; font-size: 1rem; line-height: 1.5; font-weight: bold; margin-bottom: 1rem;">
                2019: Il rebranding e la nuova identità tecnologica
            </h3>
            <p style="color: #1f1f1f; margin-bottom: 1rem;">                        
Nel 2019 abbiamo intrapreso un profondo rebranding:
un'evoluzione naturale verso un'identità più tecnologica, scientifica e orientata alla ricerca.
Da quel momento abbiamo concentrato le nostre risorse su R&D, progettazione su misura e integrazione dei sistemi ad ozono nei processi produttivi complessi.
            </p>
            <h3 style="color: #1f1f1f; font-size: 1rem; line-height: 1.5; font-weight: bold; margin-bottom: 1rem;">
                2020-oggi: L'evoluzione verso l'automazione e l'industria 4.0
            </h3>
            <p style="color: #1f1f1f; margin-bottom: 1rem;">                        
Oggi progettiamo impianti fissi automatizzati e sistemi intelligenti di sanificazione integrabili con sensori, software di controllo e protocolli HACCP.
Collaboriamo con laboratori e università per sviluppare soluzioni sempre più precise e sostenibili, al servizio di industrie di ogni dimensione.
            </p>
        </section>
        <div style="background-color: #ededed; height: 1px;"></div> 
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
            <main>
                {hero}
                {html_missione_valori}
                {html_storia}
                {cta()}
            </main>
                
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_filepath = f'{g.website_folderpath}/chi-siamo.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: f.write(html)
