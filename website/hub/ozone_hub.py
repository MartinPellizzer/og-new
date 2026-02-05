from lib import g
from lib import components

def gen():
H1 – Ozono (O₃): guida completa su proprietà, chimica, ambiente, salute e applicazioni

H2 – Introduzione all’ozono
H3 – Cos’è l’ozono: definizione chimica e identità molecolare
H3 – Differenze tra O₃, O₂ e altre forme di ossigeno
H3 – Struttura molecolare, caratteristiche uniche e stabilità

H2 – Storia e scoperta dell’ozono
H3 – Scopritore e contesto storico
H3 – Evoluzione della comprensione scientifica
H3 – Prime applicazioni storiche e casi studio

H2 – Proprietà e reattività chimica
H3 – Proprietà fisiche e chimiche principali
H3 – Meccanismi chimici: ozonolisi, radicali liberi, radicali singoletto
H3 – Interazioni con acqua, aria e altri composti
H3 – Isotopi di ossigeno e fotocatalisi

H2 – Ozono nell’ambiente naturale
H3 – Strati atmosferici: troposfera vs stratosfera e ozonosfera
H3 – Cicli naturali e formazione dell’ozono
H3 – Interazioni con gas serra, inquinanti e particolato (NOx, VOC, PM2.5, SOx)
H3 – Buco dell’ozono e protezione globale
H3 – Effetti biologici su ecosistemi: piante, animali e microbiomi ambientali
H3 – Qualità dell’aria urbana e indoor

H2 – Generazione artificiale dell’ozono
H3 – Principi e metodi: UV, corona discharge, elettrolisi
H3 – Differenze tra ozono naturale e generato: vantaggi e limiti
H3 – Controlli di sicurezza e monitoraggio
H3 – Limitazioni e scenari di rischio

H2 – Applicazioni industriali e pratiche
H3 – Aria e depurazione ambientale
H3 – Trattamento acqua potabile e reflui
H3 – Industria alimentare: ossidazione controllata e sicurezza
H3 – Chimica industriale e processi specifici
H3 – Impatto sui materiali e corrosione
H3 – Confronto con altre tecnologie ossidanti: cloro, ossigeno attivo
H3 – Sostenibilità e costi delle tecnologie a ozono

H2 – Misurazione e monitoraggio
H3 – Unità di misura e concentrazione
H3 – Strumenti e metodologie avanzate: ambientale, industriale, urbano/indoor, sensori IoT, fotometri, spettroscopia

H2 – Effetti sulla salute e normative
H3 – Esposizione: dose, tempo, concentrazione
H3 – Effetti sull’uomo: ozonoterapia, esposizione ambientale
H3 – Rischi, tossicologia e sicurezza
H3 – Linee guida operative e casi studio
H3 – Normative globali e italiane: UE, WHO, EPA, ISO, UNI, Protocollo di Montreal

H2 – Innovazione e futuro
H3 – Tecnologie emergenti: fotocatalisi, nuove terapie, microbiomi
H3 – Trend scientifici, pubblicazioni recenti e ricerche in corso
H3 – Impatti futuri su salute, ambiente e industria
H3 – Sfide e limiti dell’ozono: ricerca, regolamentazione e sostenibilità

H2 – FAQ e miti comuni
H3 – Chimica e proprietà
H3 – Salute e sicurezza
H3 – Ambiente e clima
H3 – Industria e applicazioni
H3 – Falsi miti e interpretazioni commerciali

H2 – Risorse e approfondimenti
H3 – Sintesi concettuale: concetti chiave da ricordare
H3 – Mini-mappa concettuale visuale
H3 – Glossario ed entità correlate: O₃, ozonosfera, ozonolisi, tipologie e applicazioni, VOC, PM2.5, UV, protocolli e standard
H3 – Link interni a hub correlati: applicazioni, servizi

H2 – Call-to-action
H3 – Approfondimenti, download risorse

    intro_html = f'''
<h1>Ozono: guida completa alla tecnologia, alle proprietà chimiche e alle applicazioni operative</h1>
<p class="last-updated">
  Ultimo aggiornamento: <time datetime="2026-02">febbraio 2026</time>
</p>
<p>
Questa pagina è una guida completa all’ozono come tecnologia ossidante, analizzata dal punto di vista chimico, tecnico e applicativo. Il contenuto affronta proprietà, meccanismi di reazione, ambiti di utilizzo, limiti operativi e criteri di sicurezza, fornendo un riferimento strutturato per un uso consapevole dell’ozono in aria, acqua e superfici.
</p>
<h2>Introduzione</h2>
<p>
Questa guida è pensata per chi vuole comprendere quando e come utilizzare l’ozono in modo consapevole, evitando applicazioni improprie e interpretazioni semplificate. Le sezioni seguenti possono essere lette in ordine o consultate singolarmente in base all’esigenza.
</p>
'''

    toc_html = f'''
    <h2>Indice della guida</h2>
<p>Consulta le sezioni principali cliccando sui titoli qui sotto:</p>
<ul>
  <li><a href="#cos-e-ozono">Cos’è l’ozono</a></li>
  <li><a href="#storia-ozono">Storia</a></li>
  <li><a href="#ricerca-scientifica-ozono">Ricerca Scientifica</a></li>
  <li><a href="#glossario-ozono">Glossario</a></li>
  <li><a href="#meccanismi-azione-ozono">Come funziona</a></li>
  <li><a href="#sicurezza-rischi-normative-ozono">Sicurezza e rischi</a></li>
  <li><a href="#applicazioni-casi-reali">Applicazioni</a></li>
  <li><a href="#ozono-vs-altre-tecnologie">Ozono vs altre tecnologie</a></li>
  <li><a href="#quando-ozono">Quando usare l’ozono</a></li>
  <li><a href="#faq-ozono">FAQ</a></li>
  <li><a href="#approfondimenti-ozono">Approfondimenti</a></li>
</ul>
    '''
    
    responsability_html = f'''
    <section aria-labelledby="responsabilita-uso-ozono">
  <h2 id="responsabilita-uso-ozono">
    Uso responsabile e limiti informativi
  </h2>
  <p>
    Le informazioni fornite hanno finalità esclusivamente informative e non sostituiscono analisi tecniche specifiche, valutazioni di rischio o progetti esecutivi. L’utilizzo dell’ozono richiede sempre una valutazione preliminare del contesto applicativo e il rispetto delle normative vigenti.
  </p>
  <p>
    Ogni applicazione reale deve essere progettata e gestita da personale qualificato, con sistemi di controllo adeguati e procedure operative documentate.
  </p>
</section>
    '''

    standards_html = f'''
    <section aria-labelledby="standard-pratiche-ozono">
  <h2 id="standard-pratiche-ozono">
    Allineamento a pratiche tecniche e standard di settore
  </h2>
  <p>
    La progettazione e l’utilizzo dei sistemi a ozono fanno riferimento a pratiche tecniche consolidate, documentazione di settore e linee guida operative adottate nei contesti industriali, ambientali e sanitari.
  </p>
  <p>
    L’efficacia e la sicurezza dell’ozono dipendono dall’aderenza a tali pratiche, dall’aggiornamento continuo delle competenze e dall’integrazione con sistemi di monitoraggio e controllo affidabili.
  </p>
</section>
    '''

    what_html = f'''
<section aria-labelledby="cos-e-ozono">
  <h2 id="cos-e-ozono">
    Cos’è l’ozono e le sue caratteristiche principali
  </h2>
  <p>
L’ozono (O<sub>3</sub>) è una forma allotropica dell’ossigeno, caratterizzata da una struttura molecolare instabile e da un elevato potere ossidante, che lo rende efficace nei processi di ossidazione chimica e inattivazione microbiologica.
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

    ozone_types_html = f'''
    <section aria-labelledby="tipologie-ozono">
  <h2 id="tipologie-ozono">Tipologie di ozono e forme di utilizzo</h2>
  <p>
    L’ozono può essere classificato in base alla sua origine, modalità di generazione e applicazione. Comprendere queste tipologie è fondamentale per scegliere l’approccio corretto in ogni contesto operativo.
  </p>
  <h3>Ozono naturale e ozono tecnico</h3>
  <p>
    L’ozono naturale si forma nell’atmosfera attraverso scariche elettriche o radiazioni UV e contribuisce alla protezione dai raggi ultravioletti. L’ozono tecnico, invece, è prodotto artificialmente mediante generatori e utilizzato in ambiti civili, industriali e ambientali.
  </p>
  <h3>Ozono in aria e ozono in acqua</h3>
  <p>
    L’ozono può essere applicato come gas (ozono in aria) per sanificazione di ambienti e superfici, oppure disciolto in acqua (ozono in acqua) per trattamenti igienico-sanitari e ossidazione di contaminanti chimici.
  </p>
  <h3>Trattamento continuo e shock</h3>
  <p>
    L’ozono può essere impiegato in modalità continua, con basse concentrazioni monitorate per periodi prolungati, o in modalità shock, con elevate concentrazioni per brevi periodi, per rimuovere contaminanti o odori persistenti.
  </p>
</section>
    '''

    ozone_production_html = f'''
<section aria-labelledby="produzione-ozono">
  <h2 id="produzione-ozono">Come viene prodotto l’ozono</h2>
  <p>
    L’ozono tecnico non può essere conservato a lungo e deve essere prodotto in loco mediante generatori specializzati. La scelta della tecnologia di generazione influisce su efficacia, stabilità e sicurezza.
  </p>
  <h3>Scarica a corona</h3>
  <p>
    Questo metodo sfrutta una differenza di potenziale elettrico tra due elettrodi per trasformare l’ossigeno in ozono. È il metodo più diffuso per la produzione di ozono in aria e acqua, grazie alla sua efficienza e affidabilità.
  </p>
  <h3>Radiazione UV</h3>
  <p>
    L’ozono può essere generato esponendo l’ossigeno a radiazioni ultraviolette specifiche. Questo metodo produce basse concentrazioni ed è tipicamente usato per applicazioni di laboratorio o purificazione dell’aria in piccoli spazi.
  </p>
  <h3>Elettrolisi</h3>
  <p>
    L’elettrolisi dell’acqua produce ozono insieme ad ossigeno. Questo metodo è più recente e permette integrazione in sistemi di trattamento idrico e dispositivi sanitari, riducendo la necessità di ossigeno puro.
  </p>
  <h3>Ossigeno puro vs aria ambiente</h3>
  <p>
    I generatori possono utilizzare ossigeno puro o aria ambiente come fonte. L’uso di ossigeno puro aumenta la concentrazione massima di ozono generabile, mentre l’aria ambiente è più economica ma limita la concentrazione e richiede gestione dei sottoprodotti.
  </p>
</section>
    '''

    propriety_html = f'''
        <section aria-labelledby="proprieta-ambientali-chimiche">
          <h2 id="proprieta-ambientali-chimiche">Proprietà ambientali e chimiche avanzate</h2>
          <p>
            L’ozono è un gas altamente reattivo con caratteristiche chimiche e fisiche che influenzano la sua applicazione tecnica e il comportamento ambientale.
          </p>
          <h3>Instabilità e decomposizione</h3>
          <p>
            L’ozono si decompone rapidamente in ossigeno, con una velocità influenzata da temperatura, umidità e presenza di catalizzatori chimici. Questa instabilità impone produzione on-demand e sistemi di distribuzione controllati.
          </p>
          <h3>Interazioni chimiche</h3>
          <p>
            L’ozono reagisce con composti organici e inorganici, ossidando contaminanti chimici e microrganismi. L’efficacia dipende dalla concentrazione, dal tempo di contatto e dalla natura dei substrati.
          </p>
          <h3>Effetti ambientali</h3>
          <p>
            Nell’alta atmosfera, l’ozono è benefico, proteggendo dai raggi UV. Al livello del suolo, può agire come inquinante secondario. In applicazioni controllate, il rapido decadimento previene residui chimici persistenti.
          </p>
          <h3>Compatibilità con materiali</h3>
          <p>
            L’ozono può ossidare materiali sensibili come gomme, plastiche e metalli. La conoscenza della reattività chimica permette di pianificare protezioni o limitare l’esposizione, minimizzando danni a strutture o componenti.
          </p>
        </section>
    '''

    context_html = f'''
    <section aria-labelledby="contesto-competenza-ozono">
  <h2 id="contesto-competenza-ozono">
    Contesto tecnico e competenza professionale
  </h2>
  <p>
    I contenuti di questa guida si basano sull’esperienza diretta nella progettazione, gestione e analisi di sistemi a ozono applicati in contesti civili, commerciali e industriali. L’approccio adottato privilegia criteri tecnici, valutazioni operative e rispetto dei vincoli di sicurezza e conformità.
  </p>
  <p>
    L’obiettivo non è promuovere l’ozono come soluzione universale, ma fornire una base informativa solida per comprenderne potenzialità, limiti e condizioni di utilizzo corretto.
  </p>
</section>
    '''

    history_html = f'''
    <section aria-labelledby="storia-ozono">
  <h2 id="storia-ozono">
    Storia, scoperta e sviluppo dell’ozono
  </h2>
  <p>
    L’ozono è stato identificato scientificamente nel XIX secolo e il suo utilizzo tecnologico si è evoluto parallelamente allo sviluppo dell’ingegneria chimica e dei sistemi di trattamento ambientale.
  </p>
  <h3>Scoperta scientifica</h3>
  <p>
    L’ozono venne identificato per la prima volta nel 1840 da Christian Friedrich Schönbein, che ne osservò l’odore caratteristico durante esperimenti con scariche elettriche. Da qui il termine greco <em>ózein</em>, “odorare”.
  </p>
  <h3>Evoluzione dell’utilizzo tecnologico</h3>
  <p>
    Le prime applicazioni pratiche dell’ozono risalgono alla fine del XIX secolo nel trattamento delle acque potabili. Nel corso del XX secolo, l’ozono è stato progressivamente adottato in ambiti industriali, sanitari e ambientali grazie alla sua elevata capacità ossidante e all’assenza di residui chimici persistenti.
  </p>
  <h3>Diffusione moderna</h3>
  <p>
    Oggi l’ozono è utilizzato in sistemi automatizzati e controllati, integrati in processi civili, commerciali e industriali, con applicazioni che spaziano dalla sanificazione ambientale al trattamento avanzato delle acque.
  </p>
</section>
    '''

    research_html = f'''
    <section aria-labelledby="ricerca-scientifica-ozono">
  <h2 id="ricerca-scientifica-ozono">
    Ricerca scientifica e validazione dell’ozono
  </h2>
  <p>
    L’utilizzo dell’ozono come tecnologia di trattamento è supportato da numerosi studi scientifici che ne analizzano efficacia, limiti e condizioni operative ottimali in diversi contesti applicativi.
  </p>
  <h3>Ambiti di ricerca principali</h3>
  <ul>
    <li>Ossidazione di contaminanti chimici e microinquinanti.</li>
    <li>Inattivazione microbiologica in aria e acqua.</li>
    <li>Interazioni tra ozono, materiali e sottoprodotti di reazione.</li>
    <li>Ottimizzazione dei parametri operativi (concentrazione, tempo, temperatura).</li>
  </ul>
  <h3>Validazione tecnica</h3>
  <p>
    La letteratura tecnica evidenzia come l’efficacia dell’ozono dipenda fortemente dalla progettazione del sistema, dal controllo dei parametri e dal contesto applicativo. Studi comparativi dimostrano che l’ozono è particolarmente efficace quando integrato in processi progettati su misura, piuttosto che come soluzione universale.
  </p>
  <p>
    Le evidenze scientifiche costituiscono la base per normative, linee guida operative e standard di settore, che regolano l’uso sicuro e conforme dell’ozono.
  </p>
</section>
<section aria-labelledby="ricerca-scientifica-ozono">
  <h2 id="ricerca-scientifica-ozono">
    Ricerca scientifica e validazione dell’ozono
  </h2>
  <p>
    L’utilizzo dell’ozono come tecnologia di trattamento è supportato da numerosi studi scientifici che ne analizzano efficacia, limiti e condizioni operative ottimali in diversi contesti applicativi.
  </p>
  <h3>Ambiti di ricerca principali</h3>
  <ul>
    <li>Ossidazione di contaminanti chimici e microinquinanti.</li>
    <li>Inattivazione microbiologica in aria e acqua.</li>
    <li>Interazioni tra ozono, materiali e sottoprodotti di reazione.</li>
    <li>Ottimizzazione dei parametri operativi (concentrazione, tempo, temperatura).</li>
  </ul>
  <h3>Validazione tecnica</h3>
  <p>
    La letteratura tecnica evidenzia come l’efficacia dell’ozono dipenda fortemente dalla progettazione del sistema, dal controllo dei parametri e dal contesto applicativo. Studi comparativi dimostrano che l’ozono è particolarmente efficace quando integrato in processi progettati su misura, piuttosto che come soluzione universale.
  </p>
  <p>
    Le evidenze scientifiche costituiscono la base per normative, linee guida operative e standard di settore, che regolano l’uso sicuro e conforme dell’ozono.
  </p>
</section>
    '''

    glossary_html = f'''
    <section aria-labelledby="glossario-ozono">
  <h2 id="glossario-ozono">
    Glossario tecnico dell’ozono
  </h2>
  <p>
    Questo glossario definisce i principali termini tecnici utilizzati nei sistemi e nelle applicazioni a ozono, facilitando una comprensione precisa e coerente della tecnologia.
  </p>
  <dl>
    <dt>Ozono (O<sub>3</sub>)</dt>
    <dd>Forma allotropica dell’ossigeno composta da tre atomi, caratterizzata da elevata reattività chimica.</dd>
    <dt>Potere ossidante</dt>
    <dd>Capacità di una sostanza di ossidare altri composti chimici tramite trasferimento di elettroni.</dd>
    <dt>Ozonizzazione</dt>
    <dd>Processo di trattamento che utilizza ozono per ossidare contaminanti in aria, acqua o su superfici.</dd>
    <dt>Tempo di contatto</dt>
    <dd>Durata durante la quale l’ozono interagisce con il mezzo o il contaminante target.</dd>
    <dt>Concentrazione</dt>
    <dd>Quantità di ozono presente in un dato volume di aria o acqua, generalmente espressa in ppm o mg/L.</dd>
    <dt>Decomposizione dell’ozono</dt>
    <dd>Processo naturale mediante il quale l’ozono si trasforma in ossigeno molecolare.</dd>
  </dl>
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
  <p>
Per un’analisi dettagliata dei singoli settori applicativi, dei requisiti tecnici e dei vincoli normativi specifici, consulta la pagina dedicata alle 
<a href="/applicazioni.html">applicazioni dell’ozono</a>.
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
L’ozono è una tecnologia di trattamento basata su ossidazione avanzata, spesso confrontata con sistemi fisici, chimici o fotochimici. Il confronto con altre tecnologie consente di valutare efficacia, limiti operativi, residui e requisiti di sicurezza in funzione dell’obiettivo specifico.
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
  <p>
I criteri qui descritti rappresentano una base generale. La progettazione operativa viene approfondita nella sezione dedicata ai 
<a href="/servizi.html">servizi di progettazione dei sistemi a ozono</a>.
</p>
  <h3>Parametri tecnici indicativi dell’ozono</h3>
<p>
I valori riportati rappresentano intervalli tipici utilizzati come riferimento preliminare nella progettazione dei sistemi a ozono. I parametri reali devono essere sempre definiti tramite analisi specifica del contesto.
</p>
<table>
  <thead>
    <tr>
      <th>Ambito</th>
      <th>Parametro</th>
      <th>Intervallo indicativo</th>
      <th>Unità di misura</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Aria</td>
      <td>Concentrazione operativa</td>
      <td>0,1 – 5</td>
      <td>ppm</td>
    </tr>
    <tr>
      <td>Aria</td>
      <td>Tempo di contatto</td>
      <td>10 – 120</td>
      <td>minuti</td>
    </tr>
    <tr>
      <td>Acqua</td>
      <td>Concentrazione disciolta</td>
      <td>0,1 – 5</td>
      <td>mg/L</td>
    </tr>
    <tr>
      <td>Acqua</td>
      <td>Tempo di contatto</td>
      <td>1 – 20</td>
      <td>minuti</td>
    </tr>
    <tr>
      <td>Generazione</td>
      <td>Produzione di ozono</td>
      <td>g/h – kg/h</td>
      <td>variabile</td>
    </tr>
  </tbody>
</table>
<h3>Relazione tra problema, parametri e vincoli</h3>
<p>
La scelta dei parametri di utilizzo dell’ozono dipende dal tipo di problema da risolvere e dai vincoli tecnici, materiali e normativi presenti nel contesto applicativo.
</p>
<table>
  <thead>
    <tr>
      <th>Problema principale</th>
      <th>Parametro critico</th>
      <th>Vincolo dominante</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contaminazione microbiologica</td>
      <td>Tempo di contatto</td>
      <td>Limiti di esposizione</td>
    </tr>
    <tr>
      <td>Odori persistenti</td>
      <td>Concentrazione</td>
      <td>Sensibilità dei materiali</td>
    </tr>
    <tr>
      <td>Trattamento acqua</td>
      <td>Solubilità e pH</td>
      <td>Temperatura e composizione chimica</td>
    </tr>
    <tr>
      <td>Processi industriali</td>
      <td>Produzione di ozono</td>
      <td>Normative di settore</td>
    </tr>
  </tbody>
</table>
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

    faq_html = f'''
    <section aria-labelledby="faq-ozono">
  <h2 id="faq-ozono">
    Domande frequenti sull’ozono (FAQ)
  </h2>
  <p>
    Questa sezione risponde alle domande più comuni sull’ozono, chiarendo dubbi ricorrenti e aspetti spesso fraintesi, senza sostituire la progettazione tecnica o le valutazioni normative.
  </p>
  <h3>L’ozono elimina virus e batteri?</h3>
  <p>
    L’ozono può inattivare batteri, virus e funghi tramite ossidazione, ma l’efficacia dipende da concentrazione, tempo di contatto e contesto applicativo.
  </p>
  <h3>L’ozono può essere utilizzato in presenza di persone?</h3>
  <p>
    No. I trattamenti con ozono devono essere effettuati in ambienti non occupati, salvo applicazioni specifiche progettate per concentrazioni estremamente basse e controllate.
  </p>
  <h3>L’ozono lascia residui chimici?</h3>
  <p>
    No. L’ozono si decompone naturalmente in ossigeno molecolare e non lascia residui chimici persistenti.
  </p>
  <h3>L’ozono rimuove gli odori o li copre?</h3>
  <p>
    L’ozono non maschera gli odori: ossida i composti responsabili, trasformandoli in sostanze meno odorose o inodori.
  </p>
  <h3>L’ozono è adatto a tutti i materiali?</h3>
  <p>
    No. Materiali come gomme, alcune plastiche e vernici possono degradarsi se esposti a ozono in modo prolungato o non controllato.
  </p>
  <h3>Qual è la differenza tra sanificazione e disinfezione con ozono?</h3>
  <p>
    Il termine “sanificazione” indica un miglioramento delle condizioni igieniche, mentre “disinfezione” implica una riduzione controllata dei microrganismi secondo criteri specifici. L’uso corretto dipende dal contesto normativo.
  </p>
  <h3>L’ozono sostituisce altri sistemi di trattamento?</h3>
  <p>
    No. In molti casi l’ozono funziona meglio come parte di un sistema integrato, non come soluzione unica o universale.
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
  <h3>Applicazioni dell’ozono</h3>
<p>
La pagina dedicata alle <strong>applicazioni dell’ozono</strong> approfondisce in modo specifico i contesti civili, commerciali e industriali in cui questa tecnologia viene utilizzata, con esempi operativi e criteri decisionali.
<a href="/applicazioni.html">Approfondisci le applicazioni dell’ozono</a>
</p>

<h3>Tecnologie e generatori di ozono</h3>
<p>
I <strong>sistemi e generatori di ozono</strong> rappresentano il cuore tecnologico delle applicazioni. Questa sezione analizza le principali soluzioni disponibili e le loro caratteristiche operative.
<a href="/prodotti.html">Analisi delle tecnologie a ozono</a>
</p>

<h3>Servizi di progettazione e consulenza</h3>
<p>
La <strong>progettazione dei sistemi a ozono</strong> richiede analisi tecnica, valutazione dei rischi e conformità normativa. Questa pagina descrive i servizi dedicati alla corretta implementazione della tecnologia.
<a href="/servizi.html">Servizi di progettazione a ozono</a>
</p>
</section>
    '''

    conclusion_html = f'''
    <section aria-labelledby="conclusione-ozono">
  <h2 id="conclusione-ozono">
    Considerazioni finali
  </h2>
  <p>
    L’ozono è una tecnologia potente e versatile, il cui valore dipende dalla corretta comprensione dei principi di funzionamento, dei limiti applicativi e dei requisiti di sicurezza. Una valutazione tecnica consapevole è il presupposto per un utilizzo efficace e responsabile.
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
                {context_html}
                {responsability_html}
                {standards_html}
                {toc_html}
                {what_html}
                {ozone_types_html}
                {ozone_production_html}
                {propriety_html}
                {history_html}
                {research_html}
                {mechanisms_html}
                {safety_html}
                {applicazioni_html}
                {comparation_html}
                {design_html}
                {decision_html}
                {faq_html}
                {more_html}
                {conclusion_html}
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

