import os
import xml.etree.ElementTree as ET

import publish_pdf

output_folderpath = f'doc/src/Aurora_v1.0/Aurora_Documentation_ITA/10_Future_Planning/04_Feature_Prioritization_vNext'
resources_folderpath = f'doc/src/Aurora_v1.0/Aurora_Documentation_ITA/resources'
images_folderpath = f'{resources_folderpath}/images'


_id = 'proposal-update-oxygen-sensor'
output_xml = f'''
    <?cml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
    <topic id="{_id}">
        <title>Aggiunta Sensori di Ossigeno</title>
        <image href="{images_folderpath}/proposal-update-oxygen-sensor.jpg" alt="" placement=""/>
        <shortdesc>
            Si propone l'introduzione di sensori di ossigeno per monitorare il corretto funzionamento dei concentratori di ossigeno all'interno del sistema Aurora, con l'obiettivo di monitorare l'efficienza produttiva.
        </shortdesc>

        <body>
            <section>
                <title>Contesto</title>
                <p>Attualmente, il sistema non dispone di un meccanismo di monitoraggio della concentrazione di ossigeno erogata dai concentratori. Per questo motivo, il sistema non è in grado di rilevare e monitorare se i concentratori di ossigeno stiano funzionando correttamente o se siano ancora performati.</p>
            </section>

            <section>
                <title>Aggiornamento Proposto</title>
                <p>L'aggiornamento prevede l'integrazione di sensori di ossigeno da posizionare "in linea" ai concentratori per consentire un monitoraggio continuo della percentuale di ossigeno erogata. Questo miglioramento permette una diagnosi più precisa e tempestiva di eventuali malfunzionamenti.
                </p>
                <ul>
                    <li>Monitoraggio in tempo reale della concentrazione di ossigeno</li>
                    <li>Maggiore affidabilità nel rilevamento di anomalie operative.</li>
                    <li>Possibilità di integrare avvisi e notifiche per il personale.</li>
                </ul>
            </section>

            <section>
                <title>Valutazione dell'Impatto</title>
                <p>L'implementazione richiede una modifica minima all'hardware e un aggiornamento del software di controllo del sistema. Sarà necessario anche aggiornare i manuali operativi per includere le nuove funzionalità.
                </p>
            </section>

            <section>
                <title>Prossimi Passi</title>
                <ol>
                    <li>Sviluppo hardware (PCB) e software.</li>
                    <li>Installazione prototipo su unità pilota.</li>
                    <li>Test di validazione in ambiente controllato.</li>
                    <li>Integrazione su tutte le nuove unità che usano il sistema.</li>
                </ol>
            </section>
        </body>
    </topic>
'''.strip()
with open(f'{output_folderpath}/{_id}.dita', 'w', encoding='utf-8') as f: f.write(output_xml)

_id = 'proposal-update-modular-architecture'
output_xml = f'''
    <?cml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
    <topic id="{_id}">
        <title>Progettazione Sistema di Controllo Modulare</title>
        <image href="{images_folderpath}/proposal-update-modular-architecture.jpg" alt="" placement=""/>
        <shortdesc>
            Si propone la riprogettazione del sistema di controllo (hardware PCB e software) per il sistema Aurora, con l'obiettivo di renderlo il più modulare possibile, attraverso un'architettura basata su un core centrale e plugin.
        </shortdesc>

        <body>
            <section>
                <title>Contesto</title>
                <p>L'attuale sistema di controllo del sistema è stato sviluppato con un'architettura monolitica, che presenta limiti di scalabilità e complessità nella manutenzione. La crescente necessità di adattabilità e personalizzazione richiede una nuova progettazione più flessibile e modulare.
                </p>
            </section>

            <section>
                <title>Aggiornamento Proposto</title>
                <p>La proposta prevede la creazione di un'architettura modulare composta da un core centrale e da moduli plugin, sia hardware che software. Questa soluzione garantisce maggiore flessibilità, tempi di sviluppo più rapidi e possibilità di aggiornamento incrementale.
                </p>
                <ul>
                    <li>Separazione chiara tra core e plugin.</li>
                    <li>Riduzione della complessità hardware tramite PCB modulare.</li>
                    <li>Maggiore riutilizzabilità del software tra progetti diversi.</li>
                    <li>Facilità di manutenzione e aggiornamento.</li>
                </ul>
            </section>

            <section>
                <title>Valutazione dell'Impatto</title>
                <p>L'implementazione richiede la riprogettazione della PCB principale, la definizione di interfacce standard per i plugin e l'aggiornamento del software di controllo. Saranno necessari anche test di compatibilità e la revisione della documentazione tecnica.
                </p>
            </section>

            <section>
                <title>Prossimi Passi</title>
                <ol>
                    <li>Definizione delle specifiche architetturali.</li>
                    <li>Sviluppo e test di un prototipo con architettura modulare.</li>
                    <li>Validazione delle prestazioni e della compatibilità dei plugin.</li>
                    <li>Piano di implementazione per la produzione.</li>
                </ol>
            </section>
        </body>
    </topic>
'''.strip()
with open(f'{output_folderpath}/{_id}.dita', 'w', encoding='utf-8') as f: f.write(output_xml)

_id = 'proposal-update-current-monitoring'
output_xml = f'''
    <?cml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
    <topic id="{_id}">
        <title>Aggiunta Sensori Corrente/Voltaggio per Monitoraggio</title>
        <image href="{images_folderpath}/proposal-update-current-monitoring.jpg" alt="" placement=""/>
        <shortdesc>
            Si propone di integrare sensori di corrente e voltaggio per il monitoraggio delle linee di distribuzione elettrica, con l'obiettivo di migliorare l'affidabilità operativa e la diagnostica preventiva.
        </shortdesc>

        <body>
            <section>
                <title>Contesto</title>
                <p>Attualmente il sistema non dispone di un monitoraggio diretto dei parametri elettrici sulle linee di distribuzione. Ciò comporta una minore capacità di rilevare tempestivamente anomalie come sovraccarichi, cadute di tensione, squilibri di fase o componenti con malfunzionamenti, che possono ridurre l'efficienza e aumentare il rischio di guasti imprevisti.
                </p>
            </section>

            <section>
                <title>Aggiornamento Proposto</title>
                <p>L'aggiornamento proposto prevede l'installazione di sensori di corrente e voltaggio dedicati, integrati con il sistema di supervisione. Questi dispositivi permetteranno un monitoraggio in tempo reale delle linee di distribuzione, fornendo dati utili per la manutenzione predittiva e la prevenzione di interruzioni.
                </p>
                <ul>
                    <li>Rilevamento componenti difettosi.</li>
                    <li>Rilevamento in tempo reale di sovraccarichi e anomalie.</li>
                    <li>Miglioramento della diagnostica preventiva.</li>
                    <li>Integrazione dei dati elettrici nei report di sistema.</li>
                    <li>Supporto a strategie di manutenzione predittiva.</li>
                </ul>
            </section>

            <section>
                <title>Valutazione dell'Impatto</title>
                <p>
                    L'implementazione richiede modifiche al cablaggio delle linee di distribuzione, allo sviluppo della scheda con i sensori di rilevamento e l'aggiornamento del software di supervisione per l'acquisizione e l'elaborazione dei nuovi parametri. Saranno necessari anche test di compatibilità e la revisione della documentazione tecnica.
                </p>
            </section>

            <section>
                <title>Prossimi Passi</title>
                <ol>
                    <li>Installazione pilota su un nodo di distribuzione.</li>
                    <li>Test di validazione delle misurazioni e integrazione software.</li>
                    <li>Piano di implementazione per la produzione.</li>
                </ol>
            </section>
        </body>
    </topic>
'''.strip()
with open(f'{output_folderpath}/{_id}.dita', 'w', encoding='utf-8') as f: f.write(output_xml)

_id = 'proposal-update-ozone-continuous-production'
output_xml = f'''
    <?cml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
    <topic id="{_id}">
        <title>Produzione Continua di Ozono</title>
        <image href="{images_folderpath}/proposal-update-ozone-continuous-production.jpg" alt="" placement=""/>
        <shortdesc>
            Si propone un aggiornamento al sistema Aurora, con l'aggiunta di un secondo generatore di ozono da alternare al primo, al fine di garantire una produzione continua e di ozono.
        </shortdesc>

        <body>
            <section>
                <title>Contesto</title>
                <p>
                    Attualmente, il sistema utilizza un singolo generatore di ozono per i processi di trattamento. Tuttavia, l'uso di un solo generatore comporta periodi di fermo durante la produzione di ozono perché necessita di cicli di raffreddamento, riducendo la disponibilità complessiva della produzione.
                </p>
            </section>

            <section>
                <title>Aggiornamento Proposto</title>
                <p>
                    L'aggiornamento prevede l'aggiunta di un secondo generatore di ozono, configurato per funzionare in alternanza con il primo. Questo garantisce continuità operativa, riduce i tempi di inattività e migliora l'efficienza complessiva del sistema.
                </p>
                <ul>
                    <li>Assicura una produzione continua di ozono senza interruzioni.</li>
                </ul>
            </section>

            <section>
                <title>Valutazione dell'Impatto</title>
                <p>
                    L'implementazione richiede l'integrazione del secondo generatore nell'infrastruttura esistente, l'aggiornamento del software di controllo per la gestione automatica dell'alternanza e la revisione della documentazione tecnica e dei manuali di manutenzione. Inoltre, è necessario includere anche il corrispettivo ossigenatore.
                </p>
            </section>

            <section>
                <title>Prossimi Passi</title>
                <ol>
                    <li>Installazione di un prototipo con doppio generatore.</li>
                    <li>Test di validazione per continuità e prestazioni operative.</li>
                    <li>Piano di implementazione per la produzione.</li>
                </ol>
            </section>
        </body>
    </topic>
'''.strip()
with open(f'{output_folderpath}/{_id}.dita', 'w', encoding='utf-8') as f: f.write(output_xml)

_id = 'proposal-update-din-rail-enclosure'
output_xml = f'''
    <?cml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
    <topic id="{_id}">
        <title>PCB su misura per contenitori guida DIN</title>
        <image href="{images_folderpath}/{_id}.jpg" alt="" placement=""/>
        <shortdesc>
            Si propone di progettare le PCB su misura per renderle compatibili con i contenitori per guide DIN, in modo da consentire un'installazione semplice e diretta all'interno dei quadri elettrici.
        </shortdesc>

        <body>
            <section>
                <title>Contesto</title>
                <p>
                    Attualmente il sistema Aurora utilizza soluzioni elettroniche integrate che non sono ottimizzate per un'installazione rapida nei quadri elettrici. Questo può comportare tempi di montaggio più lunghi e maggiore complessità nelle operazioni di cablaggio e manutenzione.
                </p>
            </section>

            <section>
                <title>Aggiornamento Proposto</title>
                <p>
                    L'aggiornamento consiste nella progettazione e realizzazione di PCB personalizzate inserite in case predisposti per guide DIN. Questa soluzione permette un'installazione modulare, ordinata e più sicura all'interno dei quadri elettrici.
                </p>
                <ul>
                    <li>Facilita il montaggio grazie al supporto standardizzato DIN.</li>
                    <li>Riduce il tempo di cablaggio e manutenzione.</li>
                    <li>Garantisce maggiore robustezza meccanica e protezione dei componenti.</li>
                    <li>Favorisce la scalabilità del sistema.</li>
                </ul>
            </section>

            <section>
                <title>Valutazione dell'Impatto</title>
                <p>
                    L'implementazione richiederà una revisione dei progetti PCB attuali, l'adattamento dei layout ai nuovi case DIN e un aggiornamento della documentazione tecnica. 
                </p>
            </section>

            <section>
                <title>Prossimi Passi</title>
                <ol>
                    <li>Ricerca contenitori per guide DIN.</li>
                    <li>Progettazione e realizzazione dei primi prototipi.</li>
                    <li>Test di installazione e validazione in ambiente reale.</li>
                    <li>Piano di implementazione per la produzione.</li>
                </ol>
            </section>
        </body>
    </topic>
'''.strip()
with open(f'{output_folderpath}/{_id}.dita', 'w', encoding='utf-8') as f: f.write(output_xml)

_id = 'proposal-update-ozone-sensor-optical'
output_xml = f'''
    <?cml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
    <topic id="{_id}">
        <title>Sensore Ottico per Monitoraggio Ozono</title>
        <image href="{images_folderpath}/{_id}.jpg" alt="" placement=""/>
        <shortdesc>
            Si propone di progettare un sensore ottico di ozono per monitorare con precisione la produzione dei generatori e valutare il loro livello di usura.
        </shortdesc>

        <body>
            <section>
                <title>Contesto</title>
                <p>
                    Attualmente, il sistema Aurora non dispone di un metodo integrato per misurare in tempo reale la produzione di ozono dei generatori. Questa mancanza rende complesso valutare sia la quantità effettiva prodotta (in grammi/ora e ppb), sia lo stato di efficienza del generatore nel tempo. 
                </p>
            </section>

            <section>
                <title>Aggiornamento Proposto</title>
                <p>
                    L'aggiornamento proposto prevede l'integrazione di un sensore di ozono con tecnologia ottica, capace di monitorare con alta precisione la produzione dei generatori. Il sistema fornirà dati sia quantitativi (grammi/ora, ppb) sia qualitativi sullo stato di usura dei generatori.
                </p>
                <ul>
                    <li>Misurazione precisa della produzione di ozono in tempo reale.</li>
                    <li>Valutazione del livello di usura dei generatori.</li>
                    <li>Supporto alla pianificazione predittiva delle manutenzioni.</li>
                    <li>Miglioramento della tracciabilità e dell'affidabilità del sistema.</li>
                </ul>
            </section>

            <section>
                <title>Valutazione dell'Impatto</title>
                <p>
                    L'implementazione richiede l'integrazione hardware del sensore in linea con i generatori esistenti e un aggiornamento software del sistema per elaborare e visualizzare i dati raccolti. Sarà inoltre necessario aggiornare i manuali operativi.
                </p>
            </section>

            <section>
                <title>Prossimi Passi</title>
                <ol>
                    <li>Installazione del sensore ottico su un generatore pilota.</li>
                    <li>Test di validazione delle misure e analisi dei dati raccolti.</li>
                    <li>Piano di implementazione per la produzione.</li>
                </ol>
            </section>
        </body>
    </topic>
'''.strip()
with open(f'{output_folderpath}/{_id}.dita', 'w', encoding='utf-8') as f: f.write(output_xml)

_id = 'proposal-update-ozone-generator-adjustable'
output_xml = f'''
    <?cml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
    <topic id="{_id}">
        <title>Generatore di Ozono Regolabile Elettronicamente</title>
        <image href="{images_folderpath}/{_id}.jpg" alt="" placement=""/>
        <shortdesc>
            Si propone propone di utilizzare un generatore di ozono regolabile in modo elettronico dal sistema di controllo, al fine di produrre con precisione la quantità di ozono richiesta per l'applicazione specifica.
        </shortdesc>

        <body>
            <section>
                <title>Contesto</title>
                <p>
                    Attualmente, la produzione di ozono nei sistemi industriali è regolata tramite impostazioni manuali, parametri fissi o combinazione di generatori. Questa modalità può comportare una produzione non ottimale, con possibili livelli di ozono non adeguati alle esigenze operative.
                </p>
            </section>

            <section>
                <title>Aggiornamento Proposto</title>
                <p>
                    L'aggiornamento prevede l'integrazione di un generatore di ozono completamente regolabile dal sistema di controllo elettronico. Questo consente di modulare in tempo reale la produzione di ozono, garantendo precisione e flessibilità operativa.
                </p>
                <ul>
                    <li>Regolazione automatizzata della produzione di ozono in base al fabbisogno.</li>
                    <li>Riduzione degli sprechi energetici e maggiore efficienza.</li>
                    <li>Integrazione diretta con la logica di controllo esistente.</li>
                    <li>Miglioramento della qualità complessiva del processo.</li>
                </ul>
            </section>

            <section>
                <title>Valutazione dell'Impatto</title>
                <p>
                    L'implementazione richiede un aggiornamento del firmware del sistema e una revisione della configurazione del software di controllo. Sarà inoltre necessario illustrare le nuove modalità di regolazione e monitoraggio.
                </p>
            </section>

            <section>
                <title>Prossimi Passi</title>
                <ol>
                    <li>Installazione di un prototipo su un'unità pilota.</li>
                    <li>Test di validazione delle prestazioni e della precisione di regolazione.</li>
                    <li>Piano di implementazione per la produzione.</li>
                </ol>
            </section>
        </body>
    </topic>
'''.strip()
with open(f'{output_folderpath}/{_id}.dita', 'w', encoding='utf-8') as f: f.write(output_xml)


ditamap_filename = output_folderpath.split('/')[-1]
ditamap_filepath = f'{output_folderpath}/{ditamap_filename}.ditamap'

def ditamap_expand(map_filepath):
    map_xml_output = ''
    with open(map_filepath) as f: map_xml = f.read()
    lines = map_xml.split('\n')
    for line in lines:
        if line.strip().startswith('<topicref '):
            tmp = line
            tmp = tmp.strip().split('href="')[1]
            tmp = tmp.strip().split('" ')[0]
            with open(tmp) as f: topic_xml = f.read()
            for topic_line in topic_xml.split('\n'):
                if topic_line.strip().startswith('<?cml '): continue
                if topic_line.strip().startswith('<!DOCTYPE '): continue
                map_xml_output += '    ' + topic_line + '\n'
        else:
            map_xml_output += line + '\n'
    return map_xml_output

ditamap_xml = ditamap_expand(ditamap_filepath)
print(ditamap_xml)
with open('tmp/tmp.ditamap', 'w') as f: f.write(ditamap_xml)
publish_pdf.gen('tmp/tmp.ditamap')

