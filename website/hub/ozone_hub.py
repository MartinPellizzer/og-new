from lib import g
from lib import components

def gen():
    intro_html = f'''
<section aria-labelledby="ozono-hub-title">
  <h1 id="ozono-hub-title">
    Ozono: cos’è, come funziona, quando usarlo e quando no
  </h1>
  <p>
    L’ozono è una tecnologia basata su un gas altamente reattivo, utilizzata in ambiti
    civili, commerciali e industriali per il trattamento dell’aria, dell’acqua
    e di specifici processi produttivi.
    La sua efficacia deriva da un forte potere ossidante, che consente di reagire
    con contaminanti chimici e biologici in modo rapido e senza lasciare residui persistenti.
  </p>
  <p>
    Allo stesso tempo, l’ozono non è una soluzione universale né un prodotto da applicare
    in modo indistinto.
    La sua reattività, la sua instabilità e i potenziali rischi per la salute e i materiali
    rendono necessarie competenze tecniche, progettazione corretta
    e rispetto rigoroso dei limiti di sicurezza e delle normative vigenti.
  </p>
  <p>
    Questa guida rappresenta un hub informativo completo sull’ozono come tecnologia.
    Il contenuto è strutturato per fornire una visione chiara e progressiva dell’argomento:
    dalla definizione scientifica ai meccanismi di funzionamento,
    dai limiti di sicurezza ai contesti di applicazione,
    fino ai criteri decisionali che permettono di stabilire
    quando l’ozono è una scelta appropriata e quando non lo è.
  </p>
  <p>
    L’obiettivo non è promuovere l’ozono come soluzione generica,
    ma fornire un riferimento tecnico autorevole
    per comprenderne le reali potenzialità, i limiti operativi
    e le responsabilità connesse al suo utilizzo.
  </p>
</section>
    '''

    intro_html = f'''
<h1>Ozono: guida completa, proprietà, applicazioni e sicurezza</h1>
<p>L’ozono è un gas altamente reattivo utilizzato in diversi settori per trattamenti di aria, acqua e superfici. 
Questa guida fornisce una panoramica completa sulle sue proprietà, modalità di utilizzo, sicurezza e applicazioni pratiche.</p>
<h2>Introduzione</h2>
<p>In questa sezione scoprirai perché l’ozono è importante, quali sono i suoi ambiti di applicazione e come questa guida ti aiuterà a comprenderne l’uso corretto.</p>
<h2>Indice della guida</h2>
<p>Consulta le sezioni principali cliccando sui titoli qui sotto:</p>
<ul>
  <li><a href="#cos-e-ozono">Cos’è l’ozono</a></li>
  <li><a href="#meccanismi-azione-ozono">Come funziona</a></li>
  <li><a href="#sicurezza-rischi-ozono">Sicurezza e rischi</a></li>
  <li><a href="#applicazioni-ozono">Applicazioni</a></li>
  <li><a href="#progettazione-sistemi-ozono">Progettazione sistemi</a></li>
  <li><a href="#casi-reali-ozono">Applicazioni reali</a></li>
  <li><a href="#quando-ozono">Quando usare l’ozono</a></li>
  <li><a href="#approfondimenti-ozono">Approfondimenti</a></li>
</ul>
'''

    definition_html = f'''
<section aria-labelledby="ozono-tecnologia">
  <h2 id="ozono-tecnologia">
    Ozono come tecnologia: definizione e ambito di utilizzo
  </h2>
  <p>
    Nel contesto di questa guida, l’ozono viene considerato come una tecnologia
    chimico-fisica e non come una sostanza da utilizzare in modo generico.
    Il termine “ozono” fa riferimento a un gas altamente reattivo,
    prodotto e impiegato in condizioni controllate
    per ottenere specifici effetti di ossidazione
    su contaminanti chimici e biologici.
  </p>
  <p>
    Parlare di ozono come tecnologia significa spostare l’attenzione
    dal semplice concetto di “presenza di ozono”
    al sistema complessivo che ne governa la produzione,
    la distribuzione, il controllo e la sicurezza.
    L’ozono, infatti, non può essere immagazzinato
    e deve essere generato direttamente nel punto di utilizzo,
    all’interno di un processo progettato in funzione
    di obiettivi e vincoli ben definiti.
  </p>
  <h3>
    Ozono naturale e ozono tecnologico
  </h3>
  <p>
    In natura, l’ozono si forma attraverso fenomeni energetici
    come l’azione dei raggi ultravioletti nell’atmosfera
    o le scariche elettriche durante i temporali.
    In questo contesto, l’ozono svolge un ruolo ambientale
    legato alla protezione dai raggi solari
    o alla chimica dell’atmosfera.
  </p>
  <p>
    L’ozono utilizzato in ambito tecnico e industriale
    è invece prodotto artificialmente
    mediante sistemi progettati per generarlo
    in quantità e concentrazioni controllate.
    Sebbene la molecola sia la stessa,
    il contesto di utilizzo, le finalità
    e le responsabilità operative
    sono completamente differenti.
  </p>
  <h3>
    Ozono come agente ossidante controllato
  </h3>
  <p>
    La funzione principale dell’ozono, quando utilizzato come tecnologia,
    è quella di agire come agente ossidante.
    Attraverso reazioni di ossidazione,
    l’ozono può modificare la struttura chimica
    di determinate sostanze,
    inattivare microrganismi
    o trasformare contaminanti in forme diverse.
  </p>
  <p>
    Questa capacità non è illimitata né universale.
    L’efficacia dell’azione ossidante dipende
    dalla natura del contaminante,
    dalle condizioni ambientali
    e dai parametri operativi del sistema.
    Per questo motivo, l’ozono deve essere inserito
    all’interno di un processo controllato
    e non applicato in modo indistinto.
  </p>
  <h3>
    Cosa l’ozono non è
  </h3>
  <p>
    L’ozono non è una soluzione automatica
    né una tecnologia priva di rischi.
    Non sostituisce l’analisi del problema,
    non elimina la necessità di progettazione
    e non può essere considerato sicuro
    in assenza di controlli adeguati.
  </p>
  <p>
    Utilizzare l’ozono senza una valutazione tecnica,
    senza il rispetto dei limiti normativi
    o senza sistemi di sicurezza appropriati
    può portare a inefficienze,
    danni ai materiali
    o rischi per la salute.
    Per questo motivo,
    l’ozono deve essere considerato
    una tecnologia da gestire,
    non un prodotto da applicare indiscriminatamente.
  </p>
</section>
    '''

    what_html = f'''
<section aria-labelledby="cos-e-ozono">
  <h2 id="cos-e-ozono">
    Cos’è l’ozono e le sue caratteristiche principali
  </h2>
  <p>
    L’ozono (O<sub>3</sub>) è una forma allotropica dell’ossigeno, composta da tre atomi legati in una struttura instabile e altamente reattiva. La sua reattività lo rende uno strumento potente per trattamenti mirati su aria, acqua e superfici, ma richiede gestione tecnica e sicurezza rigorosa.
  </p>
  <h3>Composizione chimica e struttura</h3>
  <p>
    La molecola di ozono è angolata e instabile: il legame tra i tre atomi di ossigeno non è equivalente a quello dell’ossigeno molecolare (O<sub>2</sub>). Questa instabilità conferisce all’ozono un elevato potere ossidante, che ne determina l’efficacia nei processi di trattamento.
  </p>
  <h3>Differenza tra ossigeno (O<sub>2</sub>) e ozono (O<sub>3</sub>)</h3>
  <p>
    A differenza dell’ossigeno molecolare, stabile e presente naturalmente nell’aria, l’ozono è temporaneo e reattivo. Questa differenza è cruciale per comprendere perché l’ozono deve essere prodotto in situ e utilizzato in sistemi controllati.
  </p>
  <h3>Formazione naturale e ruolo ambientale</h3>
  <p>
    In natura, l’ozono si forma per effetto della radiazione ultravioletta o delle scariche elettriche atmosferiche. Nell’alta atmosfera, protegge dai raggi UV, mentre al suolo può comparire come inquinante secondario. La sua molecola, identica a quella prodotta artificialmente, assume funzioni diverse a seconda del contesto.
  </p>
  <h3>Proprietà chimiche e fisiche essenziali</h3>
  <ul>
    <li><strong>Potere ossidante:</strong> l’ozono reagisce rapidamente con contaminanti chimici e biologici.</li>
    <li><strong>Instabilità molecolare:</strong> decompone rapidamente in ossigeno, rendendo impossibile lo stoccaggio.</li>
    <li><strong>Stato fisico:</strong> gas blu pallido, più pesante dell’aria, odore pungente rilevabile anche a basse concentrazioni.</li>
    <li><strong>Solubilità in acqua:</strong> limitata, influenzata da temperatura, pH e composizione dell’acqua.</li>
  </ul>
  <p>
    Comprendere queste caratteristiche permette di pianificare correttamente l’uso dell’ozono, dimensionare i sistemi di generazione, controllare i parametri operativi e garantire sicurezza ed efficacia.
  </p>
  <p>
    <a href="#meccanismi-azione-ozono">Scopri come l’ozono agisce sui contaminanti</a>
  </p>
</section>
    '''

    properties_html = f'''
<section aria-labelledby="proprieta-ozono">
  <h2 id="proprieta-ozono">
    Proprietà chimiche e fisiche dell’ozono
  </h2>
  <p>
    Conoscere le proprietà chimiche e fisiche dell’ozono è essenziale
    per comprendere il suo comportamento, l’efficacia nei trattamenti
    e i limiti operativi della tecnologia.
    Queste caratteristiche determinano come, dove e con quali parametri
    l’ozono può essere applicato in sicurezza ed efficacia.
  </p>
  <h3>
    Struttura molecolare e reattività
  </h3>
  <p>
    L’ozono (O<sub>3</sub>) è una molecola instabile con tre atomi di ossigeno legati
    in una configurazione angolata. Questa instabilità genera un forte potere ossidante,
    rendendo l’ozono altamente reattivo nei confronti di numerose sostanze organiche e inorganiche.
  </p>
  <p>
    La capacità ossidante dell’ozono è superiore a quella dell’ossigeno molecolare
    e permette di degradare contaminanti, inattivare microrganismi
    e modificare la struttura chimica di alcune sostanze.
  </p>
  <h3>
    Instabilità e tempo di decadimento
  </h3>
  <p>
    La molecola di ozono è instabile e tende a decomporsi spontaneamente
    in ossigeno molecolare. Il tempo di decadimento dipende da:
  </p>
  <ul>
    <li>Temperatura ambientale</li>
    <li>Umidità relativa</li>
    <li>Pressione e ventilazione</li>
    <li>Presenza di altre sostanze reattive</li>
  </ul>
  <p>
    Questa instabilità rende impossibile il trasporto o lo stoccaggio dell’ozono,
    imponendo la produzione in loco e il monitoraggio costante della concentrazione
    per garantire efficacia e sicurezza.
  </p>
  <h3>
    Proprietà fisiche rilevanti
  </h3>
  <p>
    L’ozono a temperatura ambiente si presenta come un gas blu pallido
    con odore pungente, percepibile anche a basse concentrazioni.
    È più pesante dell’aria e tende ad accumularsi nelle zone basse degli ambienti chiusi.
  </p>
  <p>
    La solubilità in acqua dell’ozono è limitata e dipende da temperatura, pH
    e composizione dell’acqua stessa. In soluzione acquosa,
    l’ozono reagisce rapidamente con contaminanti, determinando l’efficacia del trattamento
    e il tempo di persistenza in fase liquida.
  </p>
  <h3>
    Implicazioni pratiche delle proprietà chimico-fisiche
  </h3>
  <p>
    Comprendere struttura, reattività e instabilità dell’ozono
    permette di progettare sistemi più sicuri ed efficaci.
    Le proprietà chimiche e fisiche guidano:
  </p>
  <ul>
    <li>Il dimensionamento dei generatori e dei sistemi di distribuzione</li>
    <li>Il controllo dei parametri di esposizione</li>
    <li>La gestione dei rischi per salute e materiali</li>
    <li>L’ottimizzazione dell’efficienza in aria e acqua</li>
  </ul>
  <p>
    Senza una conoscenza approfondita di queste caratteristiche,
    l’ozono può risultare inefficace o pericoloso, anche se applicato con tecnologie avanzate.
  </p>
</section>
    '''

    mechanisms_html = f'''
<section aria-labelledby="meccanismi-azione-ozono">
  <h2 id="meccanismi-azione-ozono">
    Meccanismi di azione e funzionamento dell’ozono
  </h2>
  <p>
    L’ozono agisce principalmente tramite ossidazione controllata, trasformando sostanze chimiche e microrganismi in composti meno nocivi. Comprendere questi meccanismi è fondamentale per applicazioni sicure ed efficaci in aria, acqua e superfici.
  </p>
  <h3>Ossidazione diretta</h3>
  <p>
    L’ossidazione diretta avviene quando l’ozono cede un atomo di ossigeno altamente reattivo alle sostanze con cui entra in contatto. Questo processo consente di:
  </p>
  <ul>
    <li>Degradare contaminanti chimici specifici</li>
    <li>Inattivare batteri, virus e funghi</li>
    <li>Modificare odori e composti organici volatili (VOC)</li>
  </ul>
  <h3>Reazioni in aria</h3>
  <p>
    In fase gassosa, l’ozono reagisce con superfici, materiali e particelle sospese. L’efficacia dipende da parametri come concentrazione, temperatura e umidità. Applicazioni tipiche includono sanificazione ambientale controllata e trattamento odori.
  </p>
  <h3>Reazioni in acqua</h3>
  <p>
    In soluzione acquosa, l’ozono può agire direttamente sui contaminanti o generare specie ossidanti secondarie. Parametri critici da monitorare sono pH, temperatura e presenza di sostanze organiche o inorganiche reattive.
  </p>
  <h3>Assenza di residuo chimico</h3>
  <p>
    Dopo la reazione, l’ozono si decompone rapidamente in ossigeno, evitando accumuli chimici persistenti. Questa caratteristica richiede monitoraggio costante per mantenere efficacia e sicurezza, ma riduce rischi ambientali e residui nocivi.
  </p>
  <h3>Implicazioni operative</h3>
  <p>
    La conoscenza dei meccanismi di azione guida:
  </p>
  <ul>
    <li>Dimensionamento corretto dei sistemi di generazione e distribuzione</li>
    <li>Determinazione di tempi di esposizione e concentrazioni ottimali</li>
    <li>Gestione dei rischi per operatori e materiali</li>
    <li>Integrazione dell’ozono in processi industriali o civili complessi</li>
  </ul>
  <p>
    <a href="#sicurezza-rischi-ozono">Approfondisci sicurezza e gestione dei rischi</a>
  </p>
</section>
    '''

    safety_html = f'''
<section aria-labelledby="sicurezza-rischi-normative-ozono">
  <h2 id="sicurezza-rischi-normative-ozono">
    Sicurezza, rischi e normative sull’ozono
  </h2>
  <p>
    L’ozono è una tecnologia potente, ma la sua gestione richiede attenzione: concentrazione, tempo di esposizione e contesto applicativo determinano sicurezza ed efficacia. Conoscere rischi, limiti normativi e misure di controllo è fondamentale in ogni applicazione, dal civile all’industriale.
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

    limits_html = f'''
<section aria-labelledby="normative-limiti-ozono">
  <h2 id="normative-limiti-ozono">
    Normative e limiti di esposizione all’ozono
  </h2>
  <p>
    L’impiego dell’ozono in ambiti civili, commerciali e industriali è regolato da normative nazionali e internazionali, volte a garantire sicurezza, protezione della salute e conformità operativa.
  </p>
  <h3>Limiti di esposizione professionale</h3>
  <p>
    Gli enti normativi stabiliscono concentrazioni massime ammissibili e durate di esposizione in contesti lavorativi. Il rispetto di questi limiti richiede:
  </p>
  <ul>
    <li>Monitoraggio costante della concentrazione di ozono</li>
    <li>Procedure operative conformi agli standard</li>
    <li>Formazione specifica del personale addetto</li>
  </ul>
  <h3>Normative settoriali e ambientali</h3>
  <p>
    Settori regolamentati come industria alimentare, trattamento acque o ambienti sanitari adottano standard specifici per l’uso dell’ozono, che definiscono modalità operative, requisiti documentali e controlli obbligatori.
  </p>
  <ul>
    <li>Ventilazione e sicurezza ambientale</li>
    <li>Segnaletica e dispositivi di allarme</li>
    <li>Registrazione e tracciamento dei trattamenti</li>
  </ul>
  <h3>Conformità e responsabilità operativa</h3>
  <p>
    Operare entro i limiti normativi è essenziale per ridurre rischi legali, sanitari e tecnici. La valutazione normativa deve essere integrata fin dalla progettazione del sistema a ozono.
  </p>
  <ul>
    <li>Analisi del quadro normativo applicabile</li>
    <li>Verifica dei limiti di esposizione e sicurezza</li>
    <li>Implementazione di sistemi di controllo e monitoraggio</li>
  </ul>
  <p>
    L’aderenza alle normative non solo tutela la salute e l’ambiente, ma rafforza la credibilità tecnica dell’applicazione dell’ozono.
  </p>
  <p>
    <a href="#progettazione-sistemi-ozono">Passa alla progettazione dei sistemi a ozono</a>
  </p>
</section>
    '''

    problems_html = f'''
<section aria-labelledby="problemi-risolvibili-ozono">
  <h2 id="problemi-risolvibili-ozono">
    Problemi risolvibili con l’ozono
  </h2>
  <p>
    L’ozono è efficace nel trattamento di problemi specifici legati a contaminanti chimici,
    biologici o organici. Non agisce su sintomi generici, ma su cause precise
    tramite meccanismi di ossidazione controllata.
  </p>
  <p>
    Comprendere i problemi affrontabili con l’ozono è essenziale
    per evitare applicazioni improprie e per confrontare l’efficacia
    rispetto ad altre tecnologie disponibili.
  </p>
  <h3>
    Contaminazione microbiologica
  </h3>
  <p>
    L’ozono può ridurre la presenza di batteri, virus, muffe e lieviti
    quando questi rappresentano un rischio per aria, acqua o superfici.
    La sua efficacia dipende dalla concentrazione, durata e distribuzione uniforme.
  </p>
  <h3>
    Odori persistenti e composti organici volatili (VOC)
  </h3>
  <p>
    Alcuni odori e VOC derivano da processi di degradazione, attività produttive
    o contaminazioni ambientali. L’ozono reagisce chimicamente con questi composti,
    riducendone percezione e concentrazione.
  </p>
  <h3>
    Contaminanti chimici ossidabili
  </h3>
  <p>
    In ambienti industriali o civili, l’ozono può trattare sostanze chimiche ossidabili
    presenti in aria o acqua, come residui organici o composti reattivi,
    contribuendo a migliorare sicurezza e qualità dei processi.
  </p>
  <h3>
    Limiti di applicabilità
  </h3>
  <p>
    Non tutti i problemi possono essere risolti con l’ozono. 
    In presenza di contaminanti non ossidabili, materiali sensibili
    o vincoli normativi stringenti, l’ozono può risultare inefficace o inadatto.
  </p>
  <p>
    L’analisi preliminare del problema rappresenta il primo passo
    per determinare se l’ozono sia una soluzione appropriata,
    evitando sprechi di risorse o rischi non necessari.
  </p>
</section>
    '''

    problems_not_html = f'''
<section aria-labelledby="problemi-non-risolvibili-ozono">
  <h2 id="problemi-non-risolvibili-ozono">
    Problemi NON risolvibili con l’ozono
  </h2>
  <p>
    Pur essendo potente e versatile, l’ozono non è una soluzione universale.
    Alcune problematiche non possono essere trattate efficacemente
    con l’ozono, e tentare di farlo può risultare inefficace o rischioso.
  </p>
  <h3>
    Contaminanti non ossidabili
  </h3>
  <p>
    L’ozono agisce tramite ossidazione. Sostanze chimiche stabili o non ossidabili
    non vengono alterate, rendendo il trattamento inefficace.
  </p>
  <h3>
    Materiali sensibili
  </h3>
  <p>
    Superfici e componenti particolarmente sensibili all’ossidazione
    (come alcuni metalli, tessuti, plastiche o vernici) possono subire danni
    se esposti all’ozono, limitandone l’utilizzo in certi contesti.
  </p>
  <h3>
    Contesti con vincoli normativi stringenti
  </h3>
  <p>
    In settori regolamentati, come alimentare o farmaceutico,
    l’ozono può essere soggetto a restrizioni operative. 
    Applicazioni non conformi rischiano sanzioni legali o compromissione della sicurezza.
  </p>
  <h3>
    Effetti indiretti non controllabili
  </h3>
  <p>
    L’ozono non risolve problemi che richiedono azioni meccaniche,
    filtrazione fisica o processi biologici specifici.
    In questi casi, tecnologie complementari o alternative
    sono necessarie per ottenere risultati efficaci.
  </p>
  <p>
    Conoscere i limiti dell’ozono è essenziale per decisioni consapevoli,
    progettazione corretta e per evitare inefficienze o rischi operativi.
  </p>
</section>
    '''

    applicazioni_html = f'''
<section aria-labelledby="applicazioni-casi-reali">
  <h2 id="applicazioni-casi-reali">
    Applicazioni e casi reali dell’ozono
  </h2>
  <p>
    L’ozono è una tecnologia versatile, ma la sua efficacia dipende da parametri operativi, contesto d’uso e progettazione dei sistemi. In questa sezione esploriamo sia i contesti teorici in cui l’ozono è applicabile, sia esempi reali che dimostrano risultati concreti e lezioni operative.
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
    <li><strong>Risolvibili:</strong> contaminanti microbiologici (batteri, virus, funghi), odori persistenti, composti ossidabili chimici o organici.</li>
    <li><strong>Non risolvibili:</strong> materiali sensibili (gomme, plastiche, vernici), sostanze chimiche stabili non ossidabili, vincoli normativi stringenti.</li>
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
    L’ozono è una tecnologia ossidante potente, ma non sempre la soluzione più adatta. Confrontarlo con altre tecnologie permette di scegliere lo strumento più efficace in funzione del contesto, dei limiti e degli obiettivi specifici.
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
        <td>Ossidazione rapida, nessun residuo chimico persistente, applicabile in aria e acqua, integrabile in sistemi automatizzati</td>
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
    Progettazione e sistemi a ozono
  </h2>
  <p>
    L’efficacia e la sicurezza dell’ozono dipendono da una progettazione accurata del sistema. Ogni impianto deve essere dimensionato in funzione del problema da risolvere, del contesto operativo e dei vincoli normativi, evitando approcci generici.
  </p>
  <h3>Analisi del problema e definizione degli obiettivi</h3>
  <p>
    La progettazione parte dall’analisi dettagliata del problema reale: tipo di contaminante, condizioni ambientali e risultati desiderati. Gli obiettivi devono essere misurabili, realistici e coerenti con i limiti di sicurezza e normativi.
  </p>
  <h3>Parametri critici, sicurezza e monitoraggio</h3>
  <p>
    Parametri come concentrazione di ozono, tempo di contatto, volume da trattare e condizioni ambientali determinano l’efficacia del trattamento. La sicurezza richiede dispositivi di controllo automatico, sensori di concentrazione e procedure operative standardizzate. Il monitoraggio continuo permette di garantire performance costanti e prevenire esposizioni accidentali.
  </p>
  <h3>Tecnologie e generatori</h3>
  <p>
    I generatori di ozono costituiscono il cuore del sistema. Possono utilizzare ossigeno puro o aria come materia prima e devono garantire produzione stabile e controllata. La scelta del generatore influenza efficienza, affidabilità e integrazione con il sistema complessivo.
  </p>
  <h3>Sistemi integrati per aria e acqua</h3>
  <p>
    Nei sistemi integrati, l’ozono viene distribuito in aria o disciolto in acqua tramite condotte, diffusori e controlli automatizzati. Questi sistemi combinano generazione, distribuzione e monitoraggio, adattandosi a contesti civili, commerciali e industriali. La progettazione avanzata assicura sicurezza, efficienza e rispetto delle normative.
  </p>
  <p>
    Per approfondire le soluzioni disponibili e i servizi di progettazione, consulta le pagine dedicate a <a href="/servizi.html">Servizi e progettazione</a> e <a href="/tecnologie-sistemi-ozono.html">Tecnologie e sistemi a ozono</a>.
  </p>
  <p>
    <a href="#ozono-vs-altre-tecnologie">Torna a Ozono vs altre tecnologie</a> | 
    <a href="#applicazioni-realizzate-ozono">Prossimo: Applicazioni reali e casi tecnici</a>
  </p>
</section>
    '''

    technologies_html = f'''
<section aria-labelledby="tecnologie-sistemi-ozono">
  <h2 id="tecnologie-sistemi-ozono">
    Tecnologie e sistemi a ozono
  </h2>
  <p>
    Le tecnologie a ozono comprendono diversi sistemi progettati
    per generare, distribuire e controllare l’ozono in funzione del contesto applicativo.
    La scelta della tecnologia influisce su efficacia, sicurezza e affidabilità.
  </p>
  <p>
    I sistemi a ozono non sono dispositivi isolati, ma soluzioni integrate
    che combinano generazione, controllo, distribuzione e monitoraggio.
  </p>
  <h3>
    Generatori di ozono
  </h3>
  <p>
    I generatori di ozono sono il cuore del sistema. 
    Producono ozono a partire dall’ossigeno mediante processi fisici controllati.
    Caratteristiche del generatore come capacità produttiva e stabilità
    influenzano l’efficienza complessiva del trattamento.
  </p>
  <h3>
    Sistemi per trattamento aria
  </h3>
  <p>
    Nei sistemi per il trattamento dell’aria, l’ozono viene distribuito
    in ambienti chiusi o in condotte, secondo volume, ventilazione
    e presenza di persone. Il controllo delle concentrazioni è essenziale.
  </p>
  <h3>
    Sistemi per trattamento acqua
  </h3>
  <p>
    Nel trattamento dell’acqua, l’ozono viene disciolto per reagire
    con contaminanti biologici o chimici. Parametri come temperatura, pH
    e qualità dell’acqua influenzano velocità e distribuzione del trattamento.
  </p>
  <h3>
    Sistemi integrati
  </h3>
  <p>
    I sistemi integrati combinano più tecnologie e funzioni,
    adattandosi a processi complessi. Richiedono progettazione avanzata
    e coordinamento preciso tra le diverse componenti.
  </p>
</section>
    '''

    regulations_html = f'''
<section aria-labelledby="normative-standard-ozono">
  <h2 id="normative-standard-ozono">
    Normative, standard e responsabilità
  </h2>
  <p>
    L’utilizzo dell’ozono è soggetto a normative, standard tecnici
    e responsabilità operative che variano in base al contesto applicativo
    e al settore di riferimento. Conoscere e rispettare queste regole
    è essenziale per garantire sicurezza, conformità e corretto funzionamento dei sistemi.
  </p>
  <p>
    La conoscenza del quadro normativo non è accessoria,
    ma parte integrante della progettazione e gestione
    di qualsiasi sistema a ozono.
  </p>
  <h3>
    Normative internazionali
  </h3>
  <p>
    Diversi enti internazionali definiscono linee guida relative all’esposizione all’ozono,
    alla sicurezza sul lavoro e alla tutela ambientale.
    Queste normative forniscono riferimenti generali
    per l’impiego controllato dell’ozono in ambito professionale.
  </p>
  <h3>
    Normative di settore
  </h3>
  <p>
    Alcuni settori, come il trattamento delle acque, l’industria alimentare
    o ambienti industriali regolamentati, sono soggetti a normative specifiche.
    Queste disciplinano l’uso dell’ozono come tecnologia di processo,
    definendo condizioni operative e requisiti documentali.
  </p>
  <h3>
    Responsabilità operative
  </h3>
  <p>
    La responsabilità dell’utilizzo dell’ozono ricade su chi progetta,
    installa e gestisce il sistema. Ciò include la valutazione dei rischi,
    il rispetto dei limiti normativi e la formazione degli operatori.
  </p>
  <p>
    Un approccio responsabile richiede competenze tecniche,
    consapevolezza normativa e procedure operative chiare,
    evitando applicazioni improvvisate o non conformi.
  </p>
</section>
    '''

    cases_html = f'''
<section aria-labelledby="applicazioni-realizzate-ozono">
  <h2 id="applicazioni-realizzate-ozono">
    Applicazioni reali e casi tecnici
  </h2>
  <p>
    L’ozono è stato applicato con successo in numerosi contesti civili, commerciali e industriali. Analizzare esempi concreti consente di comprendere l’efficacia reale della tecnologia, i parametri critici da controllare e le criticità più comuni.
  </p>
  <h3>Applicazioni corrette</h3>
  <p>
    Le applicazioni efficaci condividono caratteristiche comuni: obiettivi chiari, parametri operativi controllati e integrazione del sistema a ozono nel processo complessivo. Questi interventi mostrano come la progettazione, il monitoraggio e il rispetto dei limiti di sicurezza massimizzino i risultati senza rischi.
  </p>
  <h3>Criticità riscontrate</h3>
  <p>
    Le principali criticità includono sovradosaggio, distribuzione non uniforme dell’ozono, mancanza di monitoraggio continuo o sottovalutazione dei vincoli normativi. La comprensione di questi errori permette di evitare inefficienze e rischi operativi nei futuri impianti.
  </p>
  <h3>Lezioni apprese</h3>
  <p>
    Dall’analisi dei casi reali emergono principi chiave: la corretta definizione degli obiettivi, il dimensionamento accurato dei sistemi, il monitoraggio costante e l’attenzione ai materiali e alle normative. Queste lezioni guidano scelte progettuali più consapevoli e strategie operative ottimali.
  </p>
  <h3>Multimedia e documentazione tecnica</h3>
  <p>
    L’integrazione di grafici, schemi di impianti, foto dei sistemi installati e dati operativi concreti aiuta a rendere immediata la comprensione dei processi e a supportare l’autorità tecnica della pagina.
  </p>
  <p>
    <a href="#quando-ozono">Prossimo: Quando scegliere (e quando no) l’ozono</a> | 
    <a href="#progettazione-sistemi-ozono">Torna a Progettazione e sistemi a ozono</a>
  </p>
</section>
    '''

    decision_html = f'''
<section aria-labelledby="quando-ozono">
  <h2 id="quando-ozono">
    Quando usare e quando no l’ozono
  </h2>
  <p>
    L’ozono è una tecnologia potente, ma la sua efficacia dipende da condizioni operative controllate e dalla compatibilità del contesto. Questa sezione aiuta a prendere decisioni informate, evitando applicazioni improprie o rischiose.
  </p>
  <h3>Condizioni per uso corretto</h3>
  <p>
    L’ozono è indicato quando:
  </p>
  <ul>
    <li>È necessario un effetto ossidante rapido e mirato senza residui chimici.</li>
    <li>I parametri di concentrazione, tempo e distribuzione possono essere controllati con precisione.</li>
    <li>Il contesto operativo consente un monitoraggio costante e il rispetto delle normative vigenti.</li>
    <li>La progettazione integra l’ozono come parte di un sistema complesso, non come soluzione generica.</li>
  </ul>
  <h3>Contesti non idonei</h3>
  <p>
    L’ozono non è adatto quando:
  </p>
  <ul>
    <li>Non è possibile garantire controllo sicuro di concentrazione e tempi di esposizione.</li>
    <li>Sono presenti materiali sensibili o contaminanti non ossidabili.</li>
    <li>Il contesto operativo è regolamentato con limiti restrittivi che impediscono l’uso dell’ozono.</li>
    <li>Sono richieste azioni meccaniche, filtrazione fisica o processi biologici specifici che l’ozono non può sostituire.</li>
  </ul>
  <h3>Tecnologie alternative quando l’ozono non è adatto</h3>
  <p>
    In contesti non compatibili con l’ozono, altre soluzioni possono garantire risultati efficaci, ad esempio:
  </p>
  <ul>
    <li>Filtrazione fisica (HEPA, carbone attivo) per rimuovere particelle solide e VOC senza ossidazione chimica.</li>
    <li>Radiazioni UV per inattivazione mirata di microrganismi in aria e acqua.</li>
    <li>Prodotti chimici alternativi come cloro o perossido di idrogeno, quando è necessario un effetto ossidante con tempi di contatto più lunghi.</li>
  </ul>
  <p>
    <a href="#applicazioni-realizzate-ozono">Torna a Applicazioni reali e casi tecnici</a> | 
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

