import os

from lib import g
from lib import components

def main():
    hero_html = f'''
        <section style="padding-top: 4rem; padding-bottom: 8rem;">
            <div class="container-xl m-flex" style="gap: 3rem; align-items: center;">
                <div class="flex-1">
                    <h1 style="margin-bottom: 1rem;
                        font-size: 2.5rem; line-height: 1.2;
                    ">
                        Tecnologia a ozono per applicazioni industriali
                    </h1>
                    <p style="margin-bottom: 2rem;">
                        La generazione e l'integrazione dell'ozono in ambito industriale richiedono controllo preciso di concentrazione, portata, sicurezza e automazione. 
                    </p>
                    <a href="#" class="button-blue">
                        Scopri le applicazioni industriali → 
                    </a>
                </div>
                <div class="flex-1">
                    <img src="/immagini/tecnologia-featured.jpg">
                </div>
            </div>
        </section>
    '''

    html_breadcrumbs = components.breadcrumbs_new('')
    hero_html = f'''
        <section style="background-color: #000; padding-top: 5rem; padding-bottom: 5rem; margin-bottom: 5rem;">
            <div class="container-xl">
                <div class="m-flex" style="align-items: center;">
                    <div style="flex: 2;">
                        {html_breadcrumbs}
                        <h1 style="color: #fff; margin-bottom: 1rem;
                            font-size: 4rem; font-weight: 400; line-height: 1.3;
                        ">
                            Tecnologia dell'ozono nei sistemi industriali
                        </h1>
                        <p style="color: #fff;">
                            Aprile 14, 2026 <span>•</span> Staff Tecnico Ozonogroup
                        </p>
                    </div>
                    <div style="flex: 1;">
                        <img 
                            style="height: 14rem; object-fit: cover;"
                            src="/immagini/tecnologia/ozono.jpg"
                        >
                    </div>
                </div>
            </div>
        </section>
    '''

    html_article = f'''
        <div class="container-xl">
            <div class="m-flex" style="align-items: center;">
                <div style="flex: 3;">
                    <section style="padding-bottom: 3rem;">
                        <p style="font-size: 1.75rem; line-height: 1.3; color: #202124; margin-bottom: 2rem;">
La tecnologia dell'ozono è alla base dei moderni sistemi industriali a ozono, utilizzati per processi di ossidazione, disinfezione e trattamento di acqua, aria e superfici. 
                        </p>
                        <p style="color: #5f6368;">
L'ozono (O₃) è un gas altamente reattivo con uno dei più elevati potenziali ossidativi tra gli agenti utilizzati nei processi industriali, capace di degradare contaminanti organici, inattivare microrganismi e neutralizzare composti indesiderati senza lasciare residui chimici persistenti. Nei contesti industriali, l'ozono viene generato in loco tramite generatori di ozono, integrato nei processi produttivi e trasferito nei fluidi attraverso sistemi progettati per massimizzare efficienza di dissoluzione e tempo di contatto. Comprendere i principi tecnologici dell'ozono è quindi fondamentale per progettare, dimensionare e gestire impianti industriali a ozono efficienti e sicuri.
                        </p>
                    </section>
                    <section style="padding-bottom: 3rem;">
                        <h2 style="font-size: 3rem; font-weight: 400; line-height: 1.1; color: #202124; margin-bottom: 1rem;">
Cos'è l'ozono e perché è rilevante nei processi industriali
                        </h2>
                        <p style="color: #5f6368;">
L’ozono (O₃) è una molecola composta da tre atomi di ossigeno caratterizzata da un elevato potenziale di ossidazione, superiore a molti disinfettanti chimici tradizionali. Grazie a questa proprietà, l’ozono reagisce rapidamente con composti organici, microrganismi e contaminanti attraverso meccanismi di ossidazione diretta e tramite la formazione di specie reattive dell’ossigeno (Reactive Oxygen Species). Queste reazioni chimiche permettono di inattivare batteri, virus e altri patogeni, rendendo l’ozono particolarmente efficace nei processi di disinfezione e trattamento industriale. Nei sistemi più avanzati, l’ozono può inoltre partecipare a processi di ossidazione avanzata (Advanced Oxidation Process), nei quali la generazione di radicali altamente reattivi consente la degradazione di contaminanti complessi e difficili da rimuovere con metodi convenzionali.
                        </p>
                    </section>
                    <section style="padding-bottom: 3rem;">
                        <h2 style="font-size: 3rem; font-weight: 400; line-height: 1.1; color: #202124; margin-bottom: 1rem;">
Come si produce l’ozono nei sistemi industriali
                        </h2>
                        <p style="color: #5f6368;">
Nei sistemi industriali, l’ozono viene prodotto mediante generatori di ozono che utilizzano energia elettrica per convertire l’ossigeno (O₂) in ozono (O₃). La tecnologia più diffusa è la scarica corona (corona discharge), in cui un trasformatore ad alta tensione genera un campo elettrico che dissocia le molecole di ossigeno, permettendo la formazione dell’ozono; una variante tecnologica è la dielectric barrier discharge, che utilizza materiali dielettrici per stabilizzare il processo e migliorare l’efficienza operativa. Il gas di alimentazione del generatore può essere aria secca (air feed gas) oppure ossigeno puro (oxygen feed gas), spesso fornito tramite un oxygen concentrator, che aumenta la concentrazione di ossigeno disponibile e consente di ottenere livelli di ozono più elevati e stabili. Questa combinazione di generazione elettrica, controllo del gas di alimentazione e gestione delle condizioni operative permette ai sistemi industriali di produrre ozono in modo continuo e controllato per applicazioni di trattamento, sanificazione e ossidazione.
                        </p>
                    </section>
                    <section style="padding-bottom: 3rem;">
                        <h2 style="font-size: 3rem; font-weight: 400; line-height: 1.1; color: #202124; margin-bottom: 1rem;">
Fattori che influenzano la produzione di ozono
                        </h2>
                        <p style="color: #5f6368;">
La produzione di ozono nei sistemi industriali è influenzata da diverse variabili operative che determinano sia la quantità di ozono generato sia l’efficienza complessiva del processo. La purezza del gas di alimentazione e la concentrazione di ossigeno sono fattori fondamentali: l’utilizzo di ossigeno ad alta purezza consente di ottenere concentrazioni di ozono più elevate e una maggiore efficienza di generazione rispetto all’aria. Anche le condizioni ambientali, come temperatura e umidità, incidono significativamente: l’umidità in particolare può ridurre l’efficienza della scarica elettrica e accelerare la decomposizione dell’ozono. Infine, il livello e la stabilità dell’energia elettrica applicata nel generatore influenzano direttamente la formazione delle molecole di ozono, rendendo essenziale un controllo preciso dei parametri elettrici per mantenere prestazioni costanti del sistema.
                        </p>
                    </section>
                    <section style="padding-bottom: 3rem;">
                        <h2 style="font-size: 3rem; font-weight: 400; line-height: 1.1; color: #202124; margin-bottom: 1rem;">
Proprietà chimico-fisiche dell’ozono
                        </h2>
                        <p style="color: #5f6368;">
L’ozono (O₃) possiede proprietà chimico-fisiche che ne determinano l’efficacia nei processi industriali di ossidazione e disinfezione. Il suo potenziale di ossidazione elevato lo rende uno degli agenti ossidanti più potenti utilizzati nel trattamento di acqua e aria, permettendo la degradazione di contaminanti organici, microrganismi e composti responsabili di odori. Allo stesso tempo, l’ozono è un gas termodinamicamente instabile: presenta una emivita limitata e una velocità di decomposizione che dipende da fattori come temperatura, pH e presenza di catalizzatori, influenzando quindi la cinetica delle reazioni di ossidazione. La sua solubilità in acqua consente un trasferimento efficace nei sistemi gas-liquido, ma richiede una progettazione adeguata dei processi per ottimizzare stabilità del gas, tempo di contatto e rendimento delle reazioni chimiche.
                        </p>
                    </section>
                    <section style="padding-bottom: 3rem;">
                        <h2 style="font-size: 3rem; font-weight: 400; line-height: 1.1; color: #202124; margin-bottom: 1rem;">
Trasferimento dell’ozono nei sistemi acqua-gas
                        </h2>
                        <p style="color: #5f6368;">
Nei sistemi industriali a ozono, l’efficacia del trattamento dipende in modo determinante dal trasferimento di massa gas-liquido, ovvero dalla capacità di dissolvere l’ozono gassoso nell’acqua in modo rapido e uniforme. Per aumentare l’efficienza di dissoluzione dell’ozono, vengono utilizzate tecnologie di iniezione e miscelazione come venturi injector, static mixer e diffuser, che favoriscono la dispersione delle microbolle di gas nel flusso liquido. Il processo di trasferimento è spesso completato all’interno di un contact tank, dove l’ozono rimane in soluzione per un determinato contact time, consentendo alle reazioni di ossidazione e disinfezione di avvenire in modo efficace. Ottimizzare il contatto tra ozono e acqua attraverso adeguati sistemi di miscelazione e tempi di reazione è quindi essenziale per massimizzare le prestazioni dei sistemi industriali a ozono.
                        </p>
                    </section>
                    <section style="padding-bottom: 3rem;">
                        <h2 style="font-size: 3rem; font-weight: 400; line-height: 1.1; color: #202124; margin-bottom: 1rem;">
Parametri tecnici dei sistemi a ozono
                        </h2>
                        <p style="color: #5f6368; margin-bottom: 1rem;">
Il funzionamento dei sistemi industriali a ozono è regolato da una serie di parametri ingegneristici che determinano l’efficacia del processo di ossidazione e disinfezione. Tra questi, il dosaggio di ozono (ozone dosage) indica la quantità di ozono introdotta nel sistema in relazione al volume del fluido trattato, mentre la concentrazione di ozono (ozone concentration) definisce la quantità di ozono presente nel flusso gassoso generato. Parallelamente, la portata del gas (gas flow rate) e la portata dell’acqua (water flow rate) influenzano direttamente la dinamica di trasferimento tra fase gassosa e liquida, determinando la capacità del sistema di distribuire uniformemente l’ozono nel processo.
                        </p>
                        <p style="color: #5f6368;">
Un ulteriore parametro fondamentale è l’efficienza di trasferimento di massa (mass transfer efficiency), che misura quanto efficacemente l’ozono passa dalla fase gassosa alla fase liquida attraverso dispositivi di iniezione e miscelazione. Questo parametro è strettamente legato al tempo di contatto (contact time), ovvero il periodo durante il quale l’ozono rimane in contatto con il fluido da trattare per completare le reazioni di ossidazione. L’ottimizzazione combinata di questi fattori consente di progettare sistemi a ozono più efficienti, capaci di massimizzare l’abbattimento di contaminanti e garantire prestazioni stabili nei processi industriali di trattamento.
                        </p>
                    </section>
                    <section style="padding-bottom: 3rem;">
                        <h2 style="font-size: 3rem; font-weight: 400; line-height: 1.1; color: #202124; margin-bottom: 1rem;">
Applicazioni tecnologiche dell’ozono nei processi industriali
                        </h2>
                        <p style="color: #5f6368;">
La tecnologia dell’ozono trova applicazione in diversi processi industriali grazie alla sua elevata capacità di ossidazione e disinfezione. Nei sistemi di water treatment e wastewater treatment, l’ozono viene utilizzato per eliminare microrganismi patogeni, ossidare composti organici e migliorare la qualità dell’acqua senza generare sottoprodotti chimici persistenti. Nel settore della food sanitation, l’ozono contribuisce alla riduzione della carica microbica su superfici, acqua di lavaggio e ambienti di produzione, mentre nei sistemi di cooling tower treatment aiuta a controllare biofilm, batteri e accumuli organici che compromettono l’efficienza degli impianti. Applicazioni aggiuntive includono la industrial deodorization, dove l’ozono ossida composti responsabili degli odori industriali, e l’aquaculture, in cui viene impiegato per migliorare la qualità dell’acqua e mantenere condizioni sanitarie ottimali per gli organismi acquatici.
                        </p>
                    </section>
                    <section style="padding-bottom: 3rem;">
                        <h2 style="font-size: 3rem; font-weight: 400; line-height: 1.1; color: #202124; margin-bottom: 1rem;">
Vantaggi tecnologici dell’ozono rispetto ad altri metodi
                        </h2>
                        <p style="color: #5f6368;">
L’ozono offre vantaggi tecnologici significativi rispetto a metodi come clorazione, disinfezione UV e ossidazione chimica con perossido di idrogeno, principalmente grazie al suo elevato potenziale ossidativo e alla capacità di reagire rapidamente con microorganismi e contaminanti organici. A differenza della chlorination, che può generare sottoprodotti indesiderati come composti clorurati e altri residual byproducts, l’ozono si decompone naturalmente in ossigeno, riducendo l’impatto ambientale del processo. Rispetto alla UV disinfection, che agisce solo durante l’esposizione alla radiazione, l’ozono può continuare a reagire chimicamente con sostanze disciolte nell’acqua o nell’aria, migliorando l’efficacia complessiva del trattamento. Inoltre, nei processi di chemical oxidation, l’ozono consente spesso di ottenere prestazioni elevate con minori residui chimici, contribuendo a un minore environmental impact nei sistemi industriali di trattamento.
                        </p>
                    </section>
                    <section style="padding-bottom: 5rem;">
                        <h2 style="font-size: 3rem; font-weight: 400; line-height: 1.1; color: #202124; margin-bottom: 1rem;">
Limiti tecnologici e considerazioni operative
                        </h2>
                        <p style="color: #5f6368;">
L’uso dell’ozono nei sistemi industriali presenta alcune limitazioni tecnologiche legate alle sue proprietà fisiche e alle condizioni operative necessarie per gestirlo in sicurezza. L’ozono è una molecola instabile che tende a decomporsi rapidamente in ossigeno, rendendo necessaria la generazione in loco tramite generatori di ozono, poiché il gas non può essere immagazzinato o trasportato come altri reagenti chimici. Inoltre, la produzione di ozono richiede energia elettrica ad alta tensione, e l’efficienza del sistema dipende da fattori come purezza del gas di alimentazione, temperatura e umidità. Dal punto di vista operativo, è fondamentale utilizzare materiali compatibili con l’ozono (come acciaio inox o specifici polimeri resistenti all’ossidazione) e integrare sistemi di sicurezza e monitoraggio per controllare eventuali perdite di gas e rispettare i limiti di esposizione negli ambienti di lavoro.
                        </p>
                    </section>
                </div>
                <div style="flex: 1;">
                </div>
            </div>
        </div>
    '''
    html_article = html_article.replace('’', "'")

    html = f'''
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="/styles.css">
            <title>Tecnologia dell'ozono nei sistemi industriali </title>
            <meta name="description" content="">
        </head>
        <body>
            {components.header_default()}
            <main>
                {hero_html}
                {html_article}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    html_folderpath = f'{g.WEBSITE_FOLDERPATH}/tecnologia'
    os.makedirs(html_folderpath, exist_ok=True)
    html_filepath = f'{html_folderpath}/index.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)
