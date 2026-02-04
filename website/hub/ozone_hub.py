from lib import g
from lib import components

def gen():
    intro_html = f'''
<h1>Ozono: guida completa, proprietà, applicazioni e sicurezza</h1>
<p>
Questa pagina è una guida completa all’ozono come tecnologia: ne analizza le proprietà, i meccanismi di azione, le applicazioni, i limiti e le corrette modalità di utilizzo.
</p>
<h2>Introduzione</h2>
<p>
Questa guida è pensata per chi vuole comprendere quando e come utilizzare l’ozono in modo consapevole, evitando applicazioni improprie e interpretazioni semplificate. Le sezioni seguenti possono essere lette in ordine o consultate singolarmente in base all’esigenza.
</p>
<h2>Indice della guida</h2>
<p>Consulta le sezioni principali cliccando sui titoli qui sotto:</p>
<ul>
  <li><a href="#cos-e-ozono">Cos’è l’ozono</a></li>
  <li><a href="#meccanismi-azione-ozono">Come funziona</a></li>
  <li><a href="#sicurezza-rischi-normative-ozono">Sicurezza e rischi</a></li>
  <li><a href="#applicazioni-casi-reali">Applicazioni</a></li>
  <li><a href="#ozono-vs-altre-tecnologie">Ozono vs altre tecnologie</a></li>
  <li><a href="#quando-ozono">Quando usare l’ozono</a></li>
  <li><a href="#approfondimenti-ozono">Approfondimenti</a></li>
</ul>
'''

    what_html = f'''
<section aria-labelledby="cos-e-ozono">
  <h2 id="cos-e-ozono">
    Cos’è l’ozono e le sue caratteristiche principali
  </h2>
  <p>
    L’ozono (O<sub>3</sub>) è una forma allotropica dell’ossigeno composta da tre atomi legati in una struttura instabile e altamente reattiva. Questa instabilità conferisce al gas un elevato potere ossidante, utile per trattamenti mirati su aria, acqua e superfici.
  </p>
  <h3>Composizione chimica e struttura</h3>
  <p>
    La molecola di ozono è angolata e instabile, con legami diversi da quelli dell’ossigeno molecolare (O<sub>2</sub>). Questa caratteristica determina la capacità di reagire rapidamente con contaminanti chimici e microbiologici.
  </p>
  <h3>Differenza tra ossigeno (O<sub>2</sub>) e ozono (O<sub>3</sub>)</h3>
  <p>
    A differenza dell’ossigeno molecolare stabile, l’ozono è temporaneo e altamente reattivo. Deve essere prodotto in situ e gestito tramite sistemi controllati per garantire sicurezza ed efficacia.
  </p>
  <h3>Formazione naturale e ruolo ambientale</h3>
  <p>
    In natura, l’ozono si forma per effetto della radiazione ultravioletta o scariche elettriche atmosferiche. Nell’alta atmosfera protegge dai raggi UV, mentre al suolo può comportarsi come inquinante secondario.
  </p>
  <h3>Proprietà chimiche e fisiche essenziali</h3>
  <ul>
    <li><strong>Potere ossidante elevato:</strong> reagisce rapidamente con contaminanti chimici e biologici.</li>
    <li><strong>Instabilità molecolare:</strong> decompone rapidamente in ossigeno, rendendo impossibile lo stoccaggio.</li>
    <li><strong>Stato fisico:</strong> gas blu pallido, più pesante dell’aria, odore pungente rilevabile a basse concentrazioni.</li>
    <li><strong>Solubilità in acqua:</strong> limitata, influenzata da temperatura, pH e composizione dell’acqua.</li>
  </ul>
  <p>
    Per comprendere l’azione dettagliata dell’ozono sui contaminanti e i parametri operativi per la sicurezza e l’efficacia, consulta la sezione 
    <a href="#meccanismi-azione-ozono">Meccanismi di azione</a> e 
    <a href="#progettazione-sistemi-ozono">Progettazione dei sistemi a ozono</a>.
  </p>
</section>
    '''

    mechanisms_html = f'''
<section aria-labelledby="meccanismi-azione-ozono">
  <h2 id="meccanismi-azione-ozono">
    Meccanismi di azione dell’ozono
  </h2>
    <p>
      L’ozono agisce come agente chimico reattivo, in grado di trasformare contaminanti chimici e microbiologici. Comprendere i meccanismi di base è fondamentale per un utilizzo tecnico corretto in aria, acqua e superfici.
    </p>
  <h3>Ossidazione diretta</h3>
  <p>
    L’ozono cede un atomo di ossigeno altamente reattivo alle sostanze con cui entra in contatto, provocando:
  </p>
  <ul>
    <li>Degradazione di contaminanti chimici specifici.</li>
    <li>Inattivazione di batteri, virus e funghi.</li>
    <li>Modifica di odori e VOC (composti organici volatili).</li>
  </ul>
  <h3>Reazioni in aria</h3>
  <p>
    In fase gassosa, l’ozono interagisce con particelle sospese, superfici e materiali. L’efficacia dipende da parametri chimici e fisici dell’ambiente, come umidità relativa e presenza di particelle reattive.
  </p>
  <h3>Reazioni in acqua</h3>
  <p>
    In soluzione acquosa, l’ozono agisce direttamente sui contaminanti o genera specie ossidanti secondarie. Parametri importanti includono pH, temperatura e natura dei composti organici/inorganici presenti.
  </p>
  <h3>Caratteristiche fondamentali</h3>
  <ul>
    <li><strong>Meccanismo di ossidazione chimica:</strong> l’azione reattiva dell’ozono trasforma contaminanti chimici e biologici in composti meno complessi.</li>
    <li><strong>Assenza di residuo chimico:</strong> l’ozono si decompone rapidamente in ossigeno, evitando accumuli persistenti.</li>
    <li><strong>Applicabilità versatile:</strong> aria, acqua e superfici.</li>
  </ul>
  <p>
    <a href="#sicurezza-rischi-normative-ozono">Approfondisci sicurezza e normative</a> |
    <a href="#progettazione-sistemi-ozono">Prossimo: Progettazione di sistemi a ozono</a>
  </p>
</section>
    '''

    safety_html = f'''
<section aria-labelledby="sicurezza-rischi-normative-ozono">
  <h2 id="sicurezza-rischi-normative-ozono">
    Sicurezza, rischi e normative sull’ozono
  </h2>

  <p>
  L’ozono è una tecnologia ad alta reattività, la cui gestione richiede attenzione: concentrazione, tempo di esposizione e contesto applicativo determinano sicurezza ed efficacia. Conoscere rischi, limiti normativi e misure di controllo è fondamentale in ogni applicazione, dal civile all’industriale.
  </p>
  <h3>Effetti sulla salute</h3>
  <p>
    L’esposizione a concentrazioni elevate di ozono può provocare irritazioni respiratorie, oculari e cutanee. La gravità dipende da concentrazione, durata e sensibilità individuale. In ambito domestico o civile, l’ozono deve essere utilizzato solo in ambienti non occupati e con sistemi di sicurezza appropriati.
  </p>
  <p>
    <strong>FAQ:</strong> L’ozono è sicuro per uso domestico? <br>
    <em>Risposta:</em> Solo se utilizzato con generatori certificati, rispettando tempi, concentrazioni e assenza di persone durante il trattamento.
  </p>
  <h3>Impatto su materiali e ambiente</h3>
  <p>
    L’ozono può ossidare materiali sensibili come gomme, plastiche, vernici e alcuni metalli. L’esposizione prolungata o non controllata può degradare proprietà meccaniche o estetiche. L’impatto ambientale è generalmente ridotto grazie alla rapida decomposizione dell’ozono in ossigeno, evitando residui chimici persistenti.
  </p>
  <h3>Gestione del rischio e controllo operativo</h3>
  <p>
    La sicurezza si basa su procedure operative, sistemi di monitoraggio e dispositivi di controllo. Tra le principali misure:
  </p>
  <ul>
    <li>Sensori per concentrazione e allarmi</li>
    <li>Temporizzazioni e sequenze di attivazione controllate</li>
    <li>Ventilazione e evacuazione degli ambienti trattati</li>
    <li>Formazione del personale e protocolli operativi documentati</li>
  </ul>
  <h3>Limiti di esposizione professionale e ambientale</h3>
  <p>
    Gli enti normativi definiscono limiti massimi per esposizioni professionali e ambientali, basati su durata e concentrazione. Il rispetto di questi valori è obbligatorio e richiede monitoraggio continuo e registrazione dei dati.
  </p>
  <p>
    <strong>FAQ:</strong> Quali limiti normativi devo rispettare? <br>
    <em>Risposta:</em> I limiti variano secondo settore e paese, ma in Italia e in Europa si fa riferimento a linee guida professionali e regolamenti specifici per aria, acqua e processi industriali.
  </p>
  <h3>Normative di settore e responsabilità operative</h3>
  <p>
    Alcuni settori, come alimentare, sanitario o trattamento acque, sono soggetti a regolamenti specifici che definiscono modalità operative, requisiti documentali e standard di sicurezza. La responsabilità ricade su chi progetta, installa e gestisce il sistema a ozono, che deve garantire conformità e sicurezza.
  </p>
  <p>
    La conoscenza normativa integrata con una corretta progettazione e monitoraggio operativo riduce rischi, inefficienze e responsabilità legali.
  </p>
  <p>
    <a href="#meccanismi-azione-ozono">Torna ai meccanismi di azione</a> | 
    <a href="#problemi-risolvibili-ozono">Prossimo: Problemi risolvibili con l’ozono</a>
  </p>
</section>
    '''

    applicazioni_html = f'''
<section aria-labelledby="applicazioni-casi-reali">
  <h2 id="applicazioni-casi-reali">
    Applicazioni e casi reali dell’ozono
  </h2>
  <p>

L’ozono è una tecnologia versatile, le cui prestazioni dipendono dal contesto d’uso e dalla corretta progettazione dei sistemi. In questa sezione esploriamo sia i contesti teorici in cui l’ozono è applicabile, sia esempi reali che dimostrano risultati concreti e lezioni operative.
  </p>
  <!-- CONTEXTI TEORICI -->
  <h3>Contesti teorici di applicazione</h3>
  <p>
    L’ozono può essere impiegato in diversi contesti, a patto che i parametri di concentrazione, tempo di esposizione e sicurezza siano controllati.
  </p>
  <h4>Contesti civili e residenziali</h4>
  <ul>
    <li>Trattamento aria e superfici in ambienti domestici e uffici.</li>
    <li>Disinfezione di acqua per uso domestico (piccoli impianti o filtri combinati).</li>
    <li>Odori persistenti: riduzione efficace di VOC e composti organici volatili.</li>
  </ul>
  <h4>Contesti commerciali e industriali</h4>
  <ul>
    <li>Uffici, negozi, strutture ricettive: sanificazione ambientale programmata.</li>
    <li>Processi industriali: trattamento aria, acqua o flussi produttivi con parametri controllati.</li>
    <li>Settori regolamentati (alimentare, sanitario, trattamento acque): uso conforme alle normative specifiche.</li>
  </ul>
  <h4>Problemi risolvibili e limiti</h4>
  <ul>
    <li><strong>Tipicamente trattabili:</strong> contaminanti microbiologici (batteri, virus, funghi), odori persistenti, composti chimici o organici ossidabili.</li>
    <li><strong>Tipicamente critici:</strong> materiali sensibili (gomme, plastiche, vernici), sostanze chimiche stabili non ossidabili.</li>
  </ul>
  <p>
    <em>Nota:</em> La valutazione preliminare del contesto è fondamentale per massimizzare efficacia e sicurezza.  
    <a href="#sicurezza-rischi-normative-ozono">Consulta la sezione Sicurezza e normative</a> per linee guida operative e limiti regolamentari.
  </p>
  <!-- CASI REALI -->
  <h3>Casi reali e lezioni operative</h3>
  <p>
    Ecco alcuni esempi concreti che illustrano come l’ozono è stato applicato con successo e quali criticità sono state riscontrate.
  </p>
  <h4>Applicazioni efficaci</h4>
  <ul>
    <li>Sanificazione ambientale in ospedali e laboratori: parametri di concentrazione calibrati, monitoraggio continuo e rispetto dei limiti normativi hanno garantito efficacia senza rischi.</li>
    <li>Trattamento acqua in impianti industriali: ossidazione controllata di contaminanti chimici e microbiologici, integrazione con sistemi automatizzati.</li>
    <li>Riduzione odori in strutture ricettive: utilizzo di generatori certificati con tempi di esposizione ottimizzati, minimizzando l’impatto su materiali sensibili.</li>
  </ul>
  <h4>Criticità comuni</h4>
  <ul>
    <li>Sovradosaggio o distribuzione non uniforme dell’ozono.</li>
    <li>Mancanza di monitoraggio continuo dei parametri di sicurezza.</li>
    <li>Sottovalutazione dei vincoli normativi in contesti regolamentati.</li>
  </ul>
  <h4>Lezioni apprese</h4>
  <ul>
    <li>Definizione chiara degli obiettivi e dei contaminanti target.</li>
    <li>Dimensionamento accurato dei sistemi di generazione e distribuzione.</li>
    <li>Monitoraggio costante e formazione del personale.</li>
    <li>Attenzione ai materiali e rispetto delle normative locali e internazionali.</li>
  </ul>
  <h4>Multimedia e approfondimenti</h4>
  <p>
    Per aumentare la comprensione e l’autorevolezza della pagina, è consigliabile integrare:
  </p>
  <ul>
    <li>Grafici dei parametri operativi ottimali (ppm aria, mg/L acqua).</li>
    <li>Schemi di impianti reali e flussi di trattamento.</li>
    <li>Foto o video dei sistemi installati in contesti civili, commerciali e industriali.</li>
    <li>Documentazione tecnica e report di performance reali.</li>
  </ul>
  <p>
    <a href="#quando-ozono">Prossimo: Quando scegliere (e quando no) l’ozono</a> | 
    <a href="#progettazione-sistemi-ozono">Torna a Progettazione e sistemi a ozono</a>
  </p>
</section>
    '''

    comparation_html = f'''
<section aria-labelledby="ozono-vs-altre-tecnologie">
  <h2 id="ozono-vs-altre-tecnologie">
    Ozono vs altre tecnologie
  </h2>
  <p>
    L’ozono è una tecnologia ossidante potente, ma non sempre la soluzione più adatta. Confrontarlo con altre tecnologie permette di scegliere lo strumento più adeguato in funzione dei vincoli applicativi e degli obiettivi specifici. 
  </p>
  <h3>Filtrazione fisica</h3>
  <p>
    Sistemi come filtri HEPA o a carbone attivo rimuovono particelle solide e alcuni contaminanti chimici. A differenza dell’ozono, non modificano chimicamente i composti organici o biologici, quindi non ossidano VOC o microrganismi.
  </p>
  <h3>Radiazioni UV</h3>
  <p>
    I sistemi a UV inattivano microrganismi in aria o acqua tramite esposizione diretta. L’efficacia dipende da distanza, tempo e trasparenza del mezzo, mentre l’ozono può agire anche in punti non direttamente irradiati, richiedendo però gestione della sicurezza.
  </p>
  <h3>Prodotti chimici alternativi</h3>
  <p>
    Alcuni ossidanti chimici, come cloro o perossido di idrogeno, offrono effetti simili all’ozono. Tuttavia, possono lasciare residui chimici o richiedere tempi di contatto più lunghi, mentre l’ozono si decompone rapidamente tornando ossigeno.
  </p>
  <h3>Vantaggi e limiti comparativi</h3>
  <table>
    <thead>
      <tr>
        <th>Tecnologia</th>
        <th>Vantaggi</th>
        <th>Limiti</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Ozono</td>
        <td>Azione chimica trasformativa, nessun residuo chimico persistente, applicabile in aria e acqua, integrabile in sistemi automatizzati</td>
        <td>Non adatto a tutti i materiali, richiede controllo accurato dei parametri, vincoli normativi</td>
      </tr>
      <tr>
        <td>Filtrazione fisica</td>
        <td>Rimuove particelle solide, semplice da implementare, basso rischio chimico</td>
        <td>Non ossida VOC o microrganismi, efficacia limitata ai flussi filtrati</td>
      </tr>
      <tr>
        <td>Radiazioni UV</td>
        <td>Inattiva microrganismi senza prodotti chimici, efficace su acqua chiara</td>
        <td>Richiede esposizione diretta, efficacia limitata in punti ombreggiati o aria stagnante</td>
      </tr>
      <tr>
        <td>Prodotti chimici alternativi</td>
        <td>Effetto ossidante potente, facilmente dosabile</td>
        <td>Residui chimici persistenti, tempi di contatto più lunghi, potenziali rischi ambientali</td>
      </tr>
    </tbody>
  </table>
  <p>
    La scelta della tecnologia dovrebbe basarsi su un’analisi oggettiva di obiettivi, limiti e rischi. Per approfondire l’integrazione dell’ozono nei sistemi e nelle applicazioni specifiche, consulta le sezioni dedicate a <a href="/progettazione-sistemi-ozono.html">progettazione dei sistemi</a> e <a href="/applicazioni.html">applicazioni reali</a>.
  </p>
  <p>
    <a href="#applicazioni-contesti-ozono">Torna a Applicazioni e contesti d’uso</a> | 
    <a href="#progettazione-sistemi-ozono">Prossimo: Progettazione di sistemi a ozono</a>
  </p>
</section>
    '''

    design_html = f'''
<section aria-labelledby="progettazione-sistemi-ozono">
  <h2 id="progettazione-sistemi-ozono">
    Progettazione e gestione dei sistemi a ozono
  </h2>
  <p>
    L’efficacia dell’ozono dipende da una progettazione accurata dei sistemi di generazione e distribuzione. Questa sezione fornisce linee guida pratiche per implementazioni sicure, efficienti e conformi alle normative.
  </p>
  <h3>Analisi del problema e obiettivi</h3>
  <p>
    La progettazione parte dall’identificazione del problema reale: tipo di contaminante, contesto operativo e risultati desiderati. Gli obiettivi devono essere chiari, misurabili e compatibili con i limiti normativi.
  </p>
  <h3>Parametri operativi e monitoraggio</h3>
  <ul>
    <li>Selezione della concentrazione ottimale di ozono in funzione del contesto e del target da trattare.</li>
    <li>Determinazione di tempi di esposizione e volumi da trattare per massimizzare l’efficacia.</li>
    <li>Monitoraggio costante con sensori e sistemi automatici per prevenire sovraesposizione o inefficienze.</li>
    <li>Procedure operative e formazione del personale in linea con i requisiti di sistema.</li>
  </ul>
  <h3>Scelta dei generatori e tecnologie integrate</h3>
  <p>
    I generatori costituiscono il cuore del sistema. Possono usare ossigeno puro o aria, e devono garantire produzione stabile e controllata. Nei sistemi integrati, l’ozono può essere distribuito in aria o disciolto in acqua tramite condotte, diffusori e controlli automatizzati.
  </p>
  <h3>Integrazione con processi civili, commerciali e industriali</h3>
  <p>
    La progettazione avanzata consente di adattare l’ozono a diversi scenari: ambienti domestici, uffici, strutture ricettive o impianti industriali complessi. L’integrazione corretta massimizza l’efficacia riducendo rischi e impatti su materiali sensibili.
  </p>
  <p>
    Per casi reali e applicazioni pratiche, consulta la sezione 
    <a href="#applicazioni-casi-reali">Applicazioni e casi reali</a>.
  </p>
  <p>
    <a href="#meccanismi-azione-ozono">Torna a Meccanismi di azione</a> | 
    <a href="#ozono-vs-altre-tecnologie">Prossimo: Ozono vs altre tecnologie</a>
  </p>
</section>
    '''

    decision_html = f'''
<section aria-labelledby="quando-ozono">
  <h2 id="quando-ozono">
    Quando usare e quando evitare l’ozono
  </h2>
    <p>
        L’ozono è una tecnologia ad alta reattività, ma non universalmente applicabile. Questa sezione aiuta a valutare se l’ozono è coerente con il contesto operativo e gli obiettivi del trattamento.
    </p>
  <!-- CONDIZIONI IDEALI -->
  <h3>Quando l’ozono è una scelta appropriata</h3>
  <ul>
    <li>È necessario un processo di ossidazione rapido e senza residui chimici persistenti.</li>
    <li>I parametri di utilizzo possono essere monitorati e controllati con sistemi dedicati.</li>
    <li>L’ambiente di applicazione consente trattamenti programmati e non continuativi.</li>
    <li>L’ozono è parte di un sistema progettato su misura per un obiettivo specifico.</li>
  </ul>
  <p>
    Gli aspetti di sicurezza, limiti normativi e gestione del rischio sono approfonditi nella sezione 
    <a href="#sicurezza-rischi-normative-ozono">Sicurezza, rischi e normative</a>.
  </p>
  <!-- CONDIZIONI NON IDONEE -->
  <h3>Quando è preferibile evitare l’ozono</h3>
  <ul>
    <li>Non è possibile garantire un controllo affidabile delle condizioni operative.</li>
    <li>Sono presenti materiali o componenti sensibili all’ossidazione che non possono essere protetti o rimossi.</li>
    <li>I contaminanti da trattare non reagiscono con processi ossidativi.</li>
    <li>Il contesto è soggetto a vincoli normativi incompatibili con l’uso dell’ozono.</li>
    <li>Il problema richiede una soluzione continuativa o meccanica anziché chimica.</li>
  </ul>
  <!-- RIMANDO TECNOLOGIE ALTERNATIVE -->
  <h3>Valutare soluzioni alternative</h3>
    <p>
      Nei casi in cui l’ozono non soddisfi i criteri decisionali del contesto, possono risultare più appropriate soluzioni tecnologiche alternative.
    </p>
  <p>
    Per una comparazione dettagliata tra ozono e altre soluzioni disponibili, consulta la sezione 
    <a href="#ozono-vs-altre-tecnologie">Ozono vs altre tecnologie</a>.
  </p>
  <p>
    <a href="#applicazioni-casi-reali">Torna a Applicazioni e casi reali</a> | 
    <a href="#approfondimenti-ozono">Prossimo: Approfondimenti tematici sull’ozono</a>
  </p>
</section>
    '''

    more_html = f'''
<section aria-labelledby="approfondimenti-ozono">
  <h2 id="approfondimenti-ozono">
    Approfondimenti e topic cluster correlati
  </h2>
  <p>
    Per comprendere appieno le potenzialità dell’ozono e integrarlo efficacemente, è utile esplorare le risorse correlate. Questi approfondimenti completano la pagina principale, creando un hub di riferimento autorevole.
  </p>
  <h3>Applicazioni</h3>
  <p>
    Scopri casi concreti e scenari d’uso dell’ozono in contesti civili, commerciali e industriali.  
    <a href="/applicazioni.html">Vai alle applicazioni</a>
  </p>
  <h3>Tecnologie e sistemi</h3>
  <p>
    Approfondisci generatori, sistemi integrati per aria e acqua e soluzioni tecnologiche innovative per il trattamento con ozono.  
    <a href="/prodotti.html">Esplora le tecnologie</a>
  </p>
  <h3>Servizi e progettazione</h3>
  <p>
    Linee guida per progettare impianti sicuri ed efficaci, analisi dei parametri critici e gestione dei rischi.  
    <a href="/servizi.html">Scopri i servizi di progettazione</a>
  </p>
  <h3>Casi tecnici</h3>
  <p>
    Analisi di applicazioni reali, criticità riscontrate e lezioni apprese dai progetti sul campo.  
    <a href="/progetti.html">Visualizza i casi tecnici</a>
  </p>
  <h3>Normative e certificazioni</h3>
  <p>
    Normative di riferimento, limiti di esposizione e certificazioni per l’uso sicuro e conforme dell’ozono.  
    <a href="/certificazioni.html">Consulta normative e certificazioni</a>
  </p>
  <p>
    <a href="#quando-ozono">Torna a Quando usare e quando no l’ozono</a>
  </p>
</section>
    '''


    html = f'''
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="/styles.css">
            <title>Ozono – Tecnologia, applicazioni e utilizzo corretto | Ozonogroup</title>
            <meta name="description" content="Guida completa all’ozono: cos’è, come funziona, sicurezza, applicazioni, progettazione dei sistemi, normative e casi reali.">
        </head>
        <body>
            {components.header_default()}
            <main class="hub container-md" id="contenuto-principale">
                {intro_html}
                {what_html}
                {mechanisms_html}
                {safety_html}
                {applicazioni_html}
                {comparation_html}
                {design_html}
                {decision_html}
                {more_html}
            </main>
            <!-- =======================================
                 FOOTER
                 Include company info, legal, sitemap, social links
            ======================================== -->
            {components.footer_dark()}
        </body>
        </html>
    '''
    
    html_filepath = f'{g.WEBSITE_FOLDERPATH}/ozono.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)
    print(html)

