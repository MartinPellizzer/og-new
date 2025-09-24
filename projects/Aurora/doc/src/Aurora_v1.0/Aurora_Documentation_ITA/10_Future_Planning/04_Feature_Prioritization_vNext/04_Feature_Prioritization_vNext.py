output_folderpath = f'doc/src/Aurora_v1.0/10_Future_planning/04_Feature_Prioritization_vNext'

output_xml = ''

_id = 'proposal-update-oxygen-sensor'
output_xml += f'''
    <?cml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
    <topic id="{_id}">
        <title>Proposta Aggiornamento: Aggiunta Sensori Ossigeno per Sistema Aurora</title>
        <shortdesc>
            Questo documento propone l'introduzione di sensori di ossigeno per monitorare il corretto funzionamento dei concentratori di ossigeno all'interno del sistema Aurora, con l'obiettivo di monitorare l'efficienza produttiva.
        </shortdesc>

        <body>
            <section>
                <title>Contesto</title>
                <p>
                    Attualmente, il sistema Aurora non dispone di un meccanismo di 
        monitoraggio della concentrazione di ossigeno erogata 
        dai concentratori. Per questo motivo, il sistema non è in grado di rilevare e monitorare
        se i concentratori di ossigeno stiano funzionando correttamente o se siano ancora performati.
                </p>
            </section>

            <section>
                <title>Aggiornamento Proposto</title>
                <p>
                    L'aggiornamento prevede l'integrazione di sensori di ossigeno 
        da posizionare "in linea" ai concentratori per consentire un monitoraggio 
        continuo della percentuale di ossigeno erogata. Questo 
        miglioramento permette una diagnosi più precisa e tempestiva 
        di eventuali malfunzionamenti.
                </p>
                <ul>
                    <li>Monitoraggio in tempo reale della concentrazione di ossigeno</li>
                    <li>Maggiore affidabilità nel rilevamento di anomalie operative.</li>
                    <li>Possibilità di integrare avvisi e notifiche per il personale.</li>
                </ul>
            </section>

            <section>
                <title>Valutazione dell'Impatto</title>
                <p>
                    L'implementazione richiede una modifica minima 
        all'hardware e un aggiornamento del 
        software di controllo del sistema Aurora. Sarà necessario 
        anche aggiornare i manuali operativi per includere le nuove funzionalità.
                </p>
            </section>

            <section>
                <title>Prossimi Passi</title>
                <ol>
                    <li>Sviluppo hardware (PCB) e software (Modulo Plugin).</li>
                    <li>Installazione prototipo su unità pilota.</li>
                    <li>Test di validazione in ambiente controllato.</li>
                    <li>Integrazione su tutte le nuove unità che usano il sistema Aurora.</li>
                </ol>
            </section>
        </body>
    </topic>
'''.strip()

with open(f'{output_folderpath}/{_id}.dita', 'w') as f: f.write(output_xml)
