import json

from lib import llm

source_context = f'Progettazione, realizzazione e integrazione di sistemi industriali a ozono su misura per la risoluzione di problematiche tecniche nei processi produttivi, con consulenza preliminare, studio di fattibilità, installazione, collaudo e supporto post-vendita.'
central_entity = f'Sistemi industriali a ozono su misura'
central_search_intent = f'Risoluzione di problematiche tecniche industriali e ottimizzazione dei processi produttivi tramite soluzioni impiantistiche personalizzate'

'''
Source Context → ingegneria industriale su misura
Central Entity → sistemi industriali a ozono su misura
Central Search Intent → risolvere problemi tecnici industriali
Il partner tecnico che risolve problemi industriali tramite sistemi a ozono personalizzati.

Mostrare chi sei → ingegneria industriale
Mostrare cosa fai → sistemi a ozono su misura
Mostrare perché servi → risolvere problemi tecnici industriali
'''

def central_entity__clusters__gen():
    import textwrap
    prompt = textwrap.dedent(f'''
        Ho un sito con la seguente "central entity" e il seguente "source context".
        Central entity: {central_entity}
        Source context: {source_context}
        Dammi una lista di "clusters" per questa "central entity", dove per cluster intendo gli argomenti da trattare nel sito per essere un autority.
        /no_think
    ''').strip()
    reply = llm.reply(prompt)
    if '</think>' in reply:
        reply = reply.split('</think>')[1].strip()
    return reply

if 1:
    central_entity__clusters__gen()
