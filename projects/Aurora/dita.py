import os
import xml.etree.ElementTree as ET

import publish_pdf

output_folderpath = f'doc/src/Aurora_v1.0/Aurora_Documentation_ITA/10_Future_Planning/04_Feature_Prioritization_vNext'

_id = 'proposal-update-oxygen-sensor'
output_xml = f'''
    <?cml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
    <topic id="{_id}">
        <title>Aggiunta Sensori di Ossigeno</title>
        <shortdesc>
            Questo documento propone l'introduzione di sensori di ossigeno per monitorare il corretto funzionamento dei concentratori di ossigeno all'interno del sistema Aurora, con l'obiettivo di monitorare l'efficienza produttiva.
        </shortdesc>

        <body>
            <section>
                <title>Contesto</title>
                <p>Attualmente, il sistema Aurora non dispone di un meccanismo di monitoraggio della concentrazione di ossigeno erogata dai concentratori. Per questo motivo, il sistema non è in grado di rilevare e monitorare se i concentratori di ossigeno stiano funzionando correttamente o se siano ancora performati.</p>
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
                <p>L'implementazione richiede una modifica minima all'hardware e un aggiornamento del software di controllo del sistema Aurora. Sarà necessario anche aggiornare i manuali operativi per includere le nuove funzionalità.
                </p>
            </section>

            <section>
                <title>Prossimi Passi</title>
                <ol>
                    <li>Sviluppo hardware (PCB) e software.</li>
                    <li>Installazione prototipo su unità pilota.</li>
                    <li>Test di validazione in ambiente controllato.</li>
                    <li>Integrazione su tutte le nuove unità che usano il sistema Aurora.</li>
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
        <shortdesc>
            Si propone la riprogettazione del sistema di controllo (hardware PCB e software) per il sistema "Aurora", con l'obiettivo di renderlo il più modulare possibile, attraverso un'architettura basata su un core centrale e plugin.
        </shortdesc>

        <body>
            <section>
                <title>Contesto</title>
                <p>L'attuale sistema di controllo di Aurora è stato sviluppato con un'architettura monolitica, che presenta limiti di scalabilità e complessità nella manutenzione. La crescente necessità di adattabilità e personalizzazione richiede una nuova progettazione più flessibile e modulare.
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
        <shortdesc>
            Si propone di integrare sensori di corrente e voltaggio per il monitoraggio delle linee di distribuzione elettrica, con l'obiettivo di migliorare l'affidabilità operativa e la diagnostica preventiva.
        </shortdesc>

        <body>
            <section>
                <title>Contesto</title>
                <p>Attualmente il sistema Aurora non dispone di un monitoraggio diretto dei parametri elettrici sulle linee di distribuzione. Ciò comporta una minore capacità di rilevare tempestivamente anomalie come sovraccarichi, cadute di tensione, squilibri di fase o componenti con malfunzionamenti, che possono ridurre l'efficienza e aumentare il rischio di guasti imprevisti.
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
        <shortdesc>
            Si propone un aggiornamento al sistema Aurora, con l'aggiunta di un secondo generatore di ozono da alternare al primo, al fine di garantire una produzione continua e di ozono.
        </shortdesc>

        <body>
            <section>
                <title>Contesto</title>
                <p>
                    Attualmente, il sistema Aurora utilizza un singolo generatore di ozono per i processi di trattamento. Tuttavia, l'uso di un solo generatore comporta periodi di fermo durante la produzione di ozono perché necessita di cicli di raffreddamento, riducendo la disponibilità complessiva della produzione.
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

