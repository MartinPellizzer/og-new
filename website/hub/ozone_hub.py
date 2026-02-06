from lib import g
from lib import components

def gen():
    '''
H1 – Ozono (O₃): guida completa su proprietà, chimica, ambiente, salute e applicazioni

H2 – Introduzione all’ozono
H3 – Cos’è l’ozono: definizione chimica e identità molecolare
H3 – Differenze tra O₃, O₂ e altre forme di ossigeno
H3 – Struttura molecolare, caratteristiche uniche e stabilità
H3 – Fonti naturali e artificiali di ozono

H2 – Storia e scoperta dell’ozono
H3 – Scopritore e contesto storico
H3 – Evoluzione della comprensione scientifica
H3 – Prime applicazioni storiche e casi studio

H2 – Chimica e proprietà dell’ozono
H3 – Proprietà fisiche e chimiche principali
H3 – Meccanismi chimici: ozonolisi, radicali e ossidazione
H3 – Interazioni chimiche con acqua, aria, materiali e inquinanti (NOx, VOC, PM2.5)
H3 – Isotopi di ossigeno e fotocatalisi
H3 – Reattività e stabilità in diverse condizioni ambientali

H2 – Generazione artificiale dell’ozono
H3 – Principi e metodi: UV, corona discharge, elettrolisi
H3 – Tipologie di generatori: industriali, domestici, portatili
H3 – Differenze tra ozono naturale e generato
H3 – Sicurezza, monitoraggio e scenari di rischio

H2 – Ozono nell’ambiente e impatto sull’uomo
H3 – Strati atmosferici: troposfera, stratosfera e ozonosfera
H3 – Formazione naturale dell’ozono: fotolisi, fulmini e reazioni atmosferiche
H3 – Cicli naturali e formazione dell’ozono
H3 – Qualità dell’aria urbana e indoor: fonti, concentrazioni e rischi
H3 – Ruolo dell’ozono nel cambiamento climatico e interazioni con gas serra
H3 – Buco dell’ozono e protezione globale

H2 – Applicazioni dell’ozono
H3 – Ambientale: aria, depurazione e gestione rifiuti
H3 – Acqua: potabile, reflui e trattamento industriale
H3 – Industria alimentare e chimica
H3 – Industria tessile, cosmetica e materiali
H3 – Medica e veterinaria: ozonoterapia, disinfezione clinica
H3 – Sostenibilità, costi, ROI e confronto con altre tecnologie ossidanti

H2 – Salute, esposizione e normative
H3 – Dose, tempo, concentrazione e sicurezza
H3 – Effetti sull’uomo: esposizione ambientale vs ozonoterapia
H3 – Tossicologia, rischi e precauzioni
H3 – Normative globali e italiane: UE, WHO, EPA, ISO, UNI, Protocollo di Montreal

H2 – Innovazione e futuro dell’ozono
H3 – Tecnologie emergenti: fotocatalisi, nuove terapie, microbiomi
H3 – Trend scientifici, pubblicazioni recenti e ricerche in corso
H3 – Sfide e limiti: ricerca, regolamentazione e sostenibilità

H2 – FAQ e miti comuni
H3 – Chimica e proprietà: domande frequenti e interpretazioni errate
H3 – Salute e sicurezza: esposizione, ozonoterapia e misurazioni
H3 – Ambiente e clima: indoor, outdoor, buco dell’ozono
H3 – Industria e applicazioni: purificazione, alimentare, chimica
H3 – Falsi miti commerciali e scientifici

H2 – Risorse e approfondimenti
H3 – Sintesi concettuale e diagrammi per chimica, ambiente e applicazioni
H3 – Timeline storica dell’ozono
H3 – Glossario ed entità correlate
H3 – Link interni a hub correlati: applicazioni, servizi
H3 – Link a studi scientifici, report autorevoli e dataset

H2 – Call-to-action
H3 – Approfondimenti, download risorse, contatti e preventivi
    '''

    intro_html = f'''
<h1>Ozono (O₃): guida completa su proprietà, chimica, ambiente, salute e applicazioni</h1>

<p>
L’<strong>ozono</strong>, conosciuto chimicamente come <strong>O₃</strong>, è una <strong>molecola di ossigeno</strong> triatomica con straordinarie proprietà chimiche. 
Questa guida fornisce un approfondimento completo sulle caratteristiche fisiche e chimiche dell’ozono, il suo ruolo nell’<strong>atmosfera</strong>, le interazioni con l’<strong>ambiente</strong> e la <strong>salute umana</strong>, nonché le <strong>applicazioni industriali</strong> e tecnologiche, inclusi processi di <strong>ossidazione</strong> e <strong>ozonoterapia</strong>.
</p>

<p>
La pagina funge da <strong>topic hub</strong> sull’ozono, organizzando in modo chiaro e progressivo tutte le informazioni essenziali, dai concetti di base fino alle applicazioni avanzate, con riferimento a studi scientifici e normative di settore. 
È pensata sia per chi desidera comprendere la scienza dell’ozono sia per professionisti e aziende interessati a implementazioni pratiche e sostenibili.
</p>

<p>
Attraverso questa struttura, il lettore ottiene una mappa concettuale completa della molecola, esplorandone la formazione naturale e artificiale, la chimica, la stabilità, i rischi e i benefici, senza duplicazioni tra le varie sezioni successive della guida.
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
<h2>Introduzione all’ozono</h2>

<h3>Cos’è l’ozono: definizione chimica e identità molecolare</h3>
<p>
L’<strong>ozono</strong> è una molecola composta da tre atomi di ossigeno ed è indicata dalla formula chimica <strong>O₃</strong>.
Si tratta di una forma allotropica dell’ossigeno, cioè una configurazione molecolare diversa
rispetto alla forma più comune presente nell’aria, senza che cambi l’elemento chimico di base.
</p>

<p>
Dal punto di vista dell’identità chimica, l’ozono è una sostanza distinta,
con comportamento, stabilità e reattività proprie.
Non è un composto dell’ossigeno con altri elementi,
ma una riorganizzazione degli stessi atomi di ossigeno in una struttura molecolare differente.
</p>

<h3>Differenze tra O₃, O₂ e altre forme di ossigeno</h3>
<p>
L’ossigeno molecolare <strong>O₂</strong> è costituito da due atomi di ossigeno
ed è la forma più stabile e abbondante nell’atmosfera terrestre.
L’ozono <strong>O₃</strong>, invece, contiene un atomo in più,
caratteristica che ne modifica profondamente il comportamento chimico e fisico.
</p>

<p>
Oltre a O₂ e O₃, l’ossigeno può esistere anche in forme meno comuni,
come l’ossigeno atomico (O) o specie transitorie altamente reattive.
Rispetto a queste, l’ozono occupa una posizione intermedia:
è meno stabile dell’ossigeno molecolare,
ma più persistente di specie atomiche o radicaliche.
</p>

<h3>Struttura molecolare, caratteristiche uniche e stabilità</h3>
<p>
La molecola di ozono presenta una <strong>struttura angolare</strong>,
in cui i tre atomi di ossigeno non sono disposti in linea retta.
Questa configurazione geometrica determina una distribuzione asimmetrica della carica elettronica,
conferendo all’ozono proprietà distintive rispetto ad altre molecole di ossigeno.
</p>

<p>
Dal punto di vista della stabilità, l’ozono è intrinsecamente instabile
e tende a riconvertirsi spontaneamente in ossigeno molecolare.
La velocità di questo processo dipende dalle condizioni ambientali
e rappresenta una delle caratteristiche fondamentali che ne definiscono il comportamento generale.
</p>

<h3>Fonti naturali e artificiali di ozono</h3>
<p>
L’ozono si forma naturalmente attraverso processi fisici ed energetici
che coinvolgono l’ossigeno e l’energia.
Fenomeni come le scariche elettriche atmosferiche
o l’interazione tra radiazioni e molecole di ossigeno
possono portare alla formazione temporanea di ozono.
</p>

<p>
Oltre alle fonti naturali, l’ozono può essere prodotto artificialmente
attraverso dispositivi progettati per generarlo in modo controllato.
Questi sistemi imitano o amplificano i meccanismi naturali di formazione,
rendendo possibile la presenza di ozono in contesti non naturali.
La distinzione tra origine naturale e artificiale è rilevante
per comprenderne i diversi ambiti di utilizzo e di studio.
</p>

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
<h2>Generazione artificiale dell’ozono</h2>

<h3>Principi e metodi: UV, corona discharge, elettrolisi</h3>
<p>
L’ozono artificiale viene prodotto sfruttando processi fisici che separano e riorganizzano molecole di ossigeno.
Tra i metodi principali troviamo:
</p>
<ul>
  <li><strong>Radiazione ultravioletta (UV):</strong> l’esposizione dell’ossigeno a lampade UV ad alta intensità favorisce la dissociazione di O₂ in atomi singoli, che si ricombinano in O₃.</li>
  <li><strong>Corona discharge:</strong> attraverso scariche elettriche controllate, l’ossigeno viene convertito in ozono, processo largamente utilizzato in ambito industriale per la produzione di grandi volumi.</li>
  <li><strong>Elettrolisi:</strong> in soluzioni acquose contenenti ossigeno disciolto, correnti elettriche possono generare ozono in situ, metodo impiegato per applicazioni locali o portatili.</li>
</ul>

<h3>Tipologie di generatori: industriali, domestici, portatili</h3>
<p>
I generatori di ozono si distinguono principalmente per scala e applicazione:
</p>
<ul>
  <li><strong>Industriali:</strong> progettati per grandi volumi, impiegati in depurazione di acqua, aria o processi industriali, con sistemi di controllo avanzati.</li>
  <li><strong>Domestici:</strong> dispositivi compatibili con uso domestico, per purificazione dell’aria o trattamento dell’acqua in piccole quantità.</li>
  <li><strong>Portatili:</strong> unità leggere e mobili, spesso utilizzate per test, applicazioni locali o interventi temporanei, con produzione limitata di ozono.</li>
</ul>

<h3>Differenze tra ozono naturale e generato</h3>
<p>
L’ozono artificiale e quello naturale condividono la stessa composizione chimica (O₃),
ma differiscono per origine, concentrazione e contesto di formazione.
L’ozono naturale si forma tramite processi energetici nell’atmosfera,
mentre quello generato è prodotto in ambienti controllati con finalità tecniche.
</p>

<p>
Questa distinzione è fondamentale per comprendere l’affidabilità, la concentrazione ottenibile e le modalità di utilizzo:
l’ozono artificiale può raggiungere concentrazioni più elevate e costanti rispetto a quello naturale,
rendendolo adatto a scopi specifici, mentre l’ozono naturale è limitato dai processi ambientali.
</p>

<h3>Sicurezza, monitoraggio e scenari di rischio</h3>
<p>
La produzione artificiale di ozono richiede attenzione ai rischi connessi alla sua instabilità e al suo potere ossidante.
Il monitoraggio delle concentrazioni è essenziale per prevenire esposizioni pericolose,
sia in impianti industriali sia in contesti domestici.
</p>

<p>
I principali scenari di rischio includono la formazione di ozono in ambienti chiusi senza ventilazione,
contatto con materiali sensibili o reattivi e generazione non controllata di specie ossidanti secondarie.
I generatori moderni integrano sistemi di sicurezza,
sensori e protocolli di interruzione automatica per ridurre al minimo questi rischi.
</p>

    '''

    propriety_html = f'''
      <h2>Chimica e proprietà dell’ozono</h2>

<h3>Proprietà fisiche e chimiche principali</h3>
<p>
L’ozono è un gas di colore azzurro pallido, caratterizzato da un odore penetrante e facilmente riconoscibile.
Dal punto di vista fisico, è più denso dell’ossigeno molecolare e presenta una solubilità in acqua superiore rispetto a O₂,
pur rimanendo una sostanza scarsamente persistente in fase acquosa.
</p>

<p>
Chimicamente, l’ozono è una molecola ad alto potenziale ossidante.
Questa proprietà deriva dalla sua configurazione elettronica instabile,
che favorisce il trasferimento di atomi di ossigeno o di elettroni
nelle reazioni con altre sostanze.
Il suo potere ossidante è superiore a quello di molti agenti ossidanti comuni,
caratteristica che ne definisce il ruolo nei processi chimici.
</p>

<h3>Meccanismi chimici: ozonolisi, radicali e ossidazione</h3>
<p>
Uno dei meccanismi chimici più noti associati all’ozono è l’<strong>ozonolisi</strong>,
una reazione in cui la molecola di ozono interagisce con legami insaturi,
in particolare doppi legami carbonio–carbonio.
Questo processo porta alla frammentazione della molecola bersaglio
e alla formazione di specie ossidate.
</p>

<p>
Oltre all’ozonolisi, l’ozono può partecipare a reazioni indirette
attraverso la formazione di specie radicaliche.
In determinate condizioni, la decomposizione dell’ozono
genera radicali altamente reattivi,
che contribuiscono a catene di reazioni di ossidazione.
Questi meccanismi rendono l’ozono un attore chiave nei sistemi chimici complessi.
</p>

<h3>Interazioni chimiche con acqua, aria, materiali e inquinanti (NOx, VOC, PM2.5)</h3>
<p>
In fase acquosa, l’ozono può reagire sia direttamente con i soluti
sia indirettamente attraverso prodotti della sua decomposizione.
La velocità e il tipo di reazione dipendono da parametri come pH,
temperatura e composizione chimica del mezzo.
</p>

<p>
In aria, l’ozono interagisce con numerose sostanze presenti in tracce,
inclusi ossidi di azoto (NOx) e composti organici volatili (VOC).
Queste interazioni danno origine a trasformazioni chimiche secondarie
e alla formazione di specie ossidate.
Anche il contatto con superfici solide e materiali
può innescare reazioni di decomposizione o di ossidazione superficiale.
</p>

<h3>Isotopi di ossigeno e fotocatalisi</h3>
<p>
L’ozono può incorporare diversi isotopi dell’ossigeno,
come <sup>16</sup>O, <sup>17</sup>O e <sup>18</sup>O,
rendendo possibile lo studio dei suoi percorsi di formazione
attraverso analisi isotopiche.
Questi studi forniscono informazioni dettagliate
sui meccanismi chimici che portano alla sua generazione e trasformazione.
</p>

<p>
In presenza di luce e materiali fotocatalitici,
l’ozono può partecipare a processi fotochimici complessi.
La fotocatalisi può influenzarne la formazione, la decomposizione
o la produzione di specie reattive derivate,
collegando l’ozono a sistemi chimici attivati dall’energia luminosa.
</p>

<h3>Reattività e stabilità in diverse condizioni ambientali</h3>
<p>
La reattività dell’ozono è strettamente legata alle condizioni del sistema in cui si trova.
Fattori come temperatura, pressione, umidità e presenza di catalizzatori
influenzano la velocità delle reazioni e la durata della molecola.
</p>

<p>
In generale, l’ozono tende a decomporsi spontaneamente,
con un processo che porta alla rigenerazione di ossigeno molecolare.
Questa instabilità intrinseca rappresenta una caratteristica chimica fondamentale,
che ne condiziona il comportamento in tutti i contesti chimici,
indipendentemente dall’origine o dall’ambiente di formazione.
</p>

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
    <h2>Storia e scoperta dell’ozono</h2>

<h3>Scopritore e contesto storico</h3>
<p>
L’ozono fu identificato per la prima volta nel 1840 dal chimico tedesco <strong>Christian Friedrich Schönbein</strong>,
durante esperimenti di elettrolisi dell’acqua e scariche elettriche in presenza di ossigeno.
Schönbein osservò un odore pungente e caratteristico, già noto in precedenza in contesti naturali
come i temporali, ma mai formalmente attribuito a una sostanza chimica distinta.
</p>

<p>
Il termine <em>ozono</em> deriva dal greco <em>ozein</em>, che significa “emanare odore”,
a sottolineare come la prima identificazione fosse basata su una percezione sensoriale
prima ancora che su una piena comprensione molecolare.
La scoperta avvenne in un periodo di forte espansione della chimica sperimentale,
in cui elettricità e gas erano al centro della ricerca scientifica europea.
</p>

<h3>Evoluzione della comprensione scientifica</h3>
<p>
Dopo la scoperta iniziale, la comprensione dell’ozono si sviluppò gradualmente nel corso del XIX secolo.
Nei decenni successivi, diversi scienziati contribuirono a chiarire la natura chimica della sostanza,
fino al riconoscimento dell’ozono come forma allotropica dell’ossigeno distinta dalla molecola biatomica.
</p>

<p>
Alla fine dell’Ottocento, l’ozono venne studiato in relazione ai fenomeni atmosferici,
in particolare alla composizione dell’aria e ai processi elettrici naturali.
Nel corso del XX secolo, l’attenzione scientifica si ampliò ulteriormente,
portando alla distinzione tra ozono presente negli strati alti dell’atmosfera
e ozono rilevato a livello del suolo, aprendo nuovi filoni di ricerca interdisciplinari.
</p>

<h3>Prime applicazioni storiche e casi studio</h3>
<p>
Le prime applicazioni pratiche dell’ozono risalgono alla fine del XIX secolo,
quando venne utilizzato sperimentalmente per il trattamento dell’acqua potabile.
Uno dei primi impianti documentati fu realizzato in Europa all’inizio del Novecento,
segnando l’ingresso dell’ozono nelle infrastrutture civili.
</p>

<p>
Parallelamente, l’ozono attirò l’interesse in ambito medico e igienico,
in un’epoca in cui la lotta contro i microrganismi patogeni stava assumendo un ruolo centrale.
Sebbene molte applicazioni iniziali fossero ancora empiriche,
questi primi casi studio storici contribuirono a consolidare la reputazione dell’ozono
come agente attivo nei processi di sanificazione e trattamento.
</p>
    '''

    research_html = f'''
    <h2>Innovazione e futuro dell’ozono</h2>

<h3>Tecnologie emergenti: fotocatalisi, nuove terapie, microbiomi</h3>
<p>
Le applicazioni future dell’ozono sono strettamente legate allo sviluppo di tecnologie emergenti.
La <strong>fotocatalisi</strong> permette di generare ozono e specie ossidanti in modo più efficiente e mirato, aprendo nuovi scenari per purificazione dell’aria e dell’acqua.
In campo medico, nuove modalità di <strong>ozonoterapia</strong> stanno esplorando interazioni con microbiomi umani e animali,
potenziando gli effetti terapeutici minimizzando i rischi.
Altri studi sperimentali stanno valutando l’uso dell’ozono in combinazione con materiali innovativi e processi green per ottimizzare la sostenibilità.
</p>

<h3>Trend scientifici, pubblicazioni recenti e ricerche in corso</h3>
<p>
La letteratura scientifica recente evidenzia un crescente interesse verso l’ozono in ambito ambientale, industriale e biomedico.
Pubblicazioni e report analizzano nuovi metodi di monitoraggio, tecniche di dosaggio controllato e strategie per migliorare l’efficacia ossidante
in applicazioni specifiche.
I laboratori internazionali conducono sperimentazioni su molecole derivate dall’ozono,
nuovi dispositivi di generazione e protocolli terapeutici ottimizzati.
Questi trend delineano una roadmap scientifica verso impieghi più sicuri, mirati e sostenibili.
</p>

<h3>Sfide e limiti: ricerca, regolamentazione e sostenibilità</h3>
<p>
Nonostante le potenzialità, l’adozione dell’ozono presenta sfide significative.
La <strong>ricerca scientifica</strong> deve ancora chiarire molti meccanismi d’azione a livello molecolare e biologico.
La <strong>regolamentazione</strong> varia tra paesi e settori, richiedendo protocolli chiari e linee guida aggiornate.
Dal punto di vista della <strong>sostenibilità</strong>, la produzione e l’uso controllato devono bilanciare efficienza, sicurezza e impatto ambientale.
Superare questi limiti è essenziale per garantire un futuro innovativo e responsabile dell’ozono in tutti i contesti applicativi.
</p>

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
<h2>Salute, esposizione e normative</h2>

<h3>Dose, tempo, concentrazione e sicurezza</h3>
<p>
L’esposizione all’ozono è determinata da tre parametri principali: <strong>concentrazione</strong>, <strong>tempo di esposizione</strong> e <strong>frequenza</strong>.
La combinazione di questi fattori definisce il livello di rischio per la salute umana.
Bassi livelli di ozono nell’aria possono essere tollerati per brevi periodi, mentre concentrazioni elevate o esposizioni prolungate possono causare irritazioni respiratorie, tosse e affaticamento polmonare.
</p>

<h3>Effetti sull’uomo: esposizione ambientale vs ozonoterapia</h3>
<p>
L’esposizione ambientale a ozono troposferico, ad esempio in aree urbane o industriali, può irritare le vie respiratorie e aggravare condizioni preesistenti come asma e broncopatie croniche.
Al contrario, l’<strong>ozonoterapia</strong>, effettuata in contesti clinici controllati, utilizza dosaggi e tempi calibrati per ottenere effetti terapeutici, come supporto alla rigenerazione tissutale o azione antimicrobica, minimizzando i rischi per il paziente.
</p>

<h3>Tossicologia, rischi e precauzioni</h3>
<p>
L’ozono è classificato come agente ossidante potenzialmente tossico se inalato in concentrazioni elevate.
Gli studi tossicologici hanno evidenziato effetti su polmoni, mucose e tessuti oculari.
Le precauzioni includono l’uso di sistemi di ventilazione adeguati, monitoraggio continuo dei livelli di ozono,
limitazione dell’esposizione e dispositivi di protezione individuale (DPI) quando necessario.
Queste misure garantiscono che l’ozono possa essere impiegato in sicurezza in ambito industriale, ambientale e clinico.
</p>

<h3>Normative globali e italiane: UE, WHO, EPA, ISO, UNI, Protocollo di Montreal</h3>
<p>
La gestione dell’ozono è regolata da normative internazionali e nazionali che definiscono limiti di esposizione, metodologie di monitoraggio e requisiti di sicurezza.
Organizzazioni come la <strong>World Health Organization (WHO)</strong>, la <strong>Environmental Protection Agency (EPA)</strong> e le direttive <strong>UE</strong> stabiliscono soglie per l’ozono ambientale.
In Italia, norme <strong>UNI</strong> e standard <strong>ISO</strong> forniscono linee guida per uso industriale e clinico.
Il <strong>Protocollo di Montreal</strong> interviene sulla protezione stratosferica limitando sostanze chimiche che contribuiscono al degrado dell’ozono.
</p>

    '''

    applicazioni_html = f'''
<h2>Applicazioni dell’ozono</h2>

<h3>Ambientale: aria, depurazione e gestione rifiuti</h3>
<p>
L’ozono viene utilizzato per il trattamento dell’aria in contesti industriali e civili,
grazie al suo elevato potere ossidante che consente la decomposizione di contaminanti e odori.
È impiegato anche nella gestione dei rifiuti, contribuendo alla sanificazione di rifiuti organici
e alla riduzione di cariche microbiche in impianti di trattamento.
Queste applicazioni sfruttano l’ozono come agente disinfettante e ossidante senza aggiunta di prodotti chimici complessi.
</p>

<h3>Acqua: potabile, reflui e trattamento industriale</h3>
<p>
L’ozono è largamente utilizzato per il trattamento delle acque potabili e reflue.
In ambito civile, garantisce la disinfezione rapida e la rimozione di odori o sapori sgradevoli.
In ambito industriale, viene impiegato nei processi di purificazione e depurazione di acque di scarico,
riducendo il carico microbico e migliorando la qualità del flusso trattato.
Queste applicazioni valorizzano la capacità dell’ozono di ossidare composti organici e inorganici presenti nell’acqua.
</p>

<h3>Industria alimentare e chimica</h3>
<p>
Nel settore alimentare, l’ozono trova impiego nella conservazione e sanificazione di prodotti freschi,
superfici e attrezzature, riducendo la proliferazione microbica senza residui chimici.
In ambito chimico, l’ozono è utilizzato come agente ossidante in sintesi selettiva e processi di purificazione,
sfruttando la sua reattività controllata per ottenere risultati specifici senza eccessiva produzione di scarti.
</p>

<h3>Industria tessile, cosmetica e materiali</h3>
<p>
L’ozono viene impiegato nella decolorazione, sanificazione e trattamento di tessuti e materiali.
Nel settore cosmetico, è utilizzato per la sterilizzazione di strumenti e superfici,
mentre in ambito industriale contribuisce alla modifica di materiali polimerici e superfici,
ottenendo miglioramenti funzionali come aumento della resistenza o eliminazione di contaminanti.
</p>

<h3>Medica e veterinaria: ozonoterapia, disinfezione clinica</h3>
<p>
In ambito clinico e veterinario, l’ozono viene utilizzato come agente disinfettante per superfici,
strumenti e ambienti controllati.
L’ozonoterapia, applicata sotto protocolli rigorosi, sfrutta le proprietà ossidanti dell’ozono
per supportare trattamenti locali o sistemici, in contesti dove la gestione della sterilità è cruciale.
Queste applicazioni sono strettamente regolamentate e differiscono dalla semplice generazione industriale.
</p>

<h3>Sostenibilità, costi, ROI e confronto con altre tecnologie ossidanti</h3>
<p>
L’uso dell’ozono come agente ossidante presenta vantaggi ambientali rispetto a prodotti chimici tradizionali:
non lascia residui tossici, può ridurre l’uso di cloro e altri composti, e richiede minore logistica per stoccaggio.
Dal punto di vista economico, l’analisi del ritorno sull’investimento (ROI) dipende dalla scala dell’impianto,
dalla concentrazione necessaria e dal confronto con alternative come cloro, perossido di idrogeno o altri ossidanti industriali.
L’ozono si distingue per efficienza, rapidità di azione e sostenibilità operativa.
</p>

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
   <h2>FAQ e miti comuni</h2>

<h3>Chimica e proprietà: domande frequenti e interpretazioni errate</h3>
<p>
Molti si chiedono se l’ozono sia semplicemente “ossigeno con odore” o se abbia proprietà chimiche particolari.
In realtà, la molecola O₃ possiede caratteristiche uniche come alto potere ossidante e instabilità relativa,
che la distinguono nettamente dall’O₂.
Alcune FAQ riguardano anche la durata dell’ozono nell’aria e in acqua, spesso sovrastimate a causa di confusione tra concentrazione e stabilità.
</p>

<h3>Salute e sicurezza: esposizione, ozonoterapia e misurazioni</h3>
<p>
Domande frequenti riguardano l’inalazione di ozono, i limiti di sicurezza e la differenza tra esposizione ambientale e ozonoterapia.
È importante ricordare che l’esposizione a concentrazioni elevate può essere nociva,
mentre trattamenti clinici controllati utilizzano dosi calibrate.
Le misurazioni accurate tramite sensori certificati sono essenziali per garantire sicurezza sia in ambienti indoor sia in ambito clinico.
</p>

<h3>Ambiente e clima: indoor, outdoor, buco dell’ozono</h3>
<p>
Molti miti nascono dalla confusione tra ozono benefico in stratosfera e ozono nocivo al suolo.
FAQ comuni riguardano l’accumulo indoor, l’efficacia della purificazione dell’aria e il legame tra ozono e cambiamento climatico.
È fondamentale distinguere tra ozono naturale e antropico, e tra concentrazioni troposferiche e stratosferiche,
per interpretare correttamente il suo ruolo nell’ambiente.
</p>

<h3>Industria e applicazioni: purificazione, alimentare, chimica</h3>
<p>
Alcune domande riguardano l’efficacia dell’ozono in applicazioni industriali e alimentari.
Miti comuni includono credenze errate sulla sostituzione completa di prodotti chimici tradizionali
o l’idea che l’ozono possa essere utilizzato senza protocolli di sicurezza.
La realtà è che l’ozono è altamente efficace solo se dosato correttamente
e applicato secondo procedure standardizzate.
</p>

<h3>Falsi miti commerciali e scientifici</h3>
<p>
Alcuni miti commerciali presentano l’ozono come panacea universale per salute, ambiente e industria.
È importante sfatare queste interpretazioni, distinguendo tra evidenze scientifiche documentate
e promesse ingannevoli.
Questo approccio aiuta il lettore a comprendere i limiti reali della molecola e a fare scelte informate
nel rispetto di sicurezza e normativa.
</p>

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

    environment_html = f'''
<h2>Ozono nell’ambiente e impatto sull’uomo</h2>

<h3>Strati atmosferici: troposfera, stratosfera e ozonosfera</h3>
<p>
L’ozono è presente in concentrazioni variabili nei diversi strati dell’atmosfera terrestre.
Nella <strong>stratosfera</strong> (10–50 km di altitudine) forma lo strato di ozono, o <em>ozonosfera</em>,
che assorbe gran parte della radiazione ultravioletta dannosa proveniente dal sole.
Nella <strong>troposfera</strong> (0–10 km), l’ozono è presente in concentrazioni molto più basse,
ma può influenzare la qualità dell’aria e avere effetti diretti sulla salute umana e sugli ecosistemi.
</p>

<h3>Formazione naturale dell’ozono: fotolisi, fulmini e reazioni atmosferiche</h3>
<p>
L’ozono si forma naturalmente tramite processi energetici che coinvolgono l’ossigeno molecolare.
La <strong>fotolisi</strong> dei raggi UV provoca la scissione di O₂ in atomi singoli,
che si combinano rapidamente per formare O₃.
Altri fenomeni naturali, come <strong>scariche elettriche atmosferiche</strong> durante i temporali,
possono generare ozono localmente.
Reazioni tra ossigeno e altre specie chimiche presenti nell’aria completano i cicli di produzione naturale.
</p>

<h3>Cicli naturali e formazione dell’ozono</h3>
<p>
L’ozono è parte di cicli naturali complessi che regolano la sua concentrazione nell’atmosfera.
Questi cicli includono la continua formazione tramite radiazione solare,
la decomposizione spontanea e le interazioni con altre molecole atmosferiche.
La dinamica tra produzione e degradazione determina l’equilibrio locale e globale dell’ozono,
influenziando sia la protezione UV che l’esposizione al suolo.
</p>

<h3>Qualità dell’aria urbana e indoor: fonti, concentrazioni e rischi</h3>
<p>
L’ozono può accumularsi anche a livello del suolo, dove diventa un componente chiave della <strong>qualità dell’aria</strong>.
In contesti urbani, la formazione avviene principalmente tramite reazioni fotochimiche tra inquinanti come NOx e VOC sotto l’azione della luce solare.
Al chiuso, l’ozono può derivare dall’ingresso dall’esterno o dalla generazione tramite dispositivi elettronici.
Elevate concentrazioni al suolo possono avere effetti negativi sulla salute respiratoria e sugli ecosistemi urbani.
</p>

<h3>Ruolo dell’ozono nel cambiamento climatico e interazioni con gas serra</h3>
<p>
L’ozono contribuisce indirettamente al bilancio radiativo terrestre.
N stratosfera, agisce come filtro UV senza effetto diretto sul clima,
mentre nel troposfera funge da gas serra secondario, trattenendo calore e influenzando la temperatura locale.
Interazioni con altri gas serra, come CO₂, CH₄ e N₂O,
possono modulare la concentrazione e la distribuzione dell’ozono atmosferico.
</p>

<h3>Buco dell’ozono e protezione globale</h3>
<p>
Il cosiddetto <strong>buco dell’ozono</strong> è la riduzione significativa dello strato di ozono nella stratosfera,
causata principalmente da sostanze chimiche di origine antropica, come clorofluorocarburi (CFC).
Questa riduzione aumenta la quantità di radiazione UV che raggiunge la superficie terrestre.
Grazie a misure internazionali, come il Protocollo di Montreal, sono stati implementati interventi per limitare i composti distruttivi,
favorendo la lenta ripresa dello strato protettivo.
</p>

    '''

    cta_html = f'''
    <h2>Call-to-action</h2>
<h3>Approfondimenti, download risorse, contatti e preventivi</h3>
<p>
Per approfondire la conoscenza sull’ozono e le sue applicazioni, è possibile accedere a materiali aggiuntivi,
scaricare guide, schemi e report completi in formato digitale.
Gli utenti interessati a soluzioni personalizzate possono contattare direttamente Ozonogroup
per consulenze, preventivi o supporto tecnico specifico.
Questa sezione facilita l’interazione con il sito, collegando la conoscenza teorica a opportunità concrete di applicazione e supporto.
</p>
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
                {history_html}
                {propriety_html}
                {ozone_production_html}
                {environment_html}
                {applicazioni_html}
                {safety_html}
                {research_html}
                {faq_html}
                {cta_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''
    
    html_filepath = f'{g.WEBSITE_FOLDERPATH}/ozono.html'
    with open(html_filepath, 'w', encoding='utf-8', errors='ignore') as f: 
        f.write(html)
    print(html_filepath)
    print(html)

