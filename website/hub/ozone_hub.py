from lib import g
from lib import components

def gen():
    intro_html = f'''
        <section aria-labelledby="ozono-title">
          <h1 id="ozono-title">
            Ozono: tecnologia, applicazioni e utilizzo corretto
          </h1>
          <p>
            L’ozono è una tecnologia basata su un gas altamente reattivo, utilizzata in diversi ambiti
            per il trattamento dell’aria, dell’acqua e dei processi industriali.
            La sua efficacia deriva da un forte potere ossidante, ma il suo utilizzo richiede
            conoscenze specifiche, progettazione corretta e attenzione ai limiti di sicurezza.
          </p>
          <p>
            In questa pagina viene fornita una visione strutturata e completa dell’argomento ozono,
            partendo dai fondamenti scientifici fino alle applicazioni pratiche, alle normative
            e alle considerazioni decisionali.
            L’obiettivo è offrire un punto di riferimento tecnico per comprendere
            quando e come l’ozono può essere utilizzato in modo appropriato.
          </p>
          <p>
            L’ozono non è una soluzione universale.
            In alcuni contesti rappresenta una tecnologia estremamente efficace,
            in altri può risultare inadatta o controproducente se applicata senza
            un’analisi corretta del problema e delle condizioni operative.
            Per questo motivo è fondamentale considerare l’ozono come parte di un sistema,
            e non come un prodotto isolato.
          </p>
          <p>
            Le sezioni successive approfondiscono in modo progressivo
            le proprietà dell’ozono, i suoi meccanismi di azione,
            i limiti di sicurezza, i contesti di applicazione,
            le tecnologie disponibili e le responsabilità normative,
            fornendo una mappa concettuale completa dell’argomento.
          </p>
        </section>
    '''

    what_html = f'''
        <section aria-labelledby="cos-e-ozono">
          <h2 id="cos-e-ozono">
            Cos’è l’ozono
          </h2>
          <p>
            L’ozono è una forma allotropica dell’ossigeno composta da tre atomi (O₃).
            A differenza dell’ossigeno molecolare presente nell’aria (O₂),
            l’ozono è una molecola instabile, caratterizzata da un’elevata reattività chimica.
          </p>
          <p>
            In natura, l’ozono si forma attraverso reazioni energetiche
            che coinvolgono l’ossigeno, come l’azione dei raggi ultravioletti
            nell’atmosfera o le scariche elettriche durante i temporali.
            Questi stessi principi fisici sono alla base della produzione
            dell’ozono in ambito tecnologico.
          </p>
          <p>
            Dal punto di vista chimico, l’ozono è un forte agente ossidante.
            Questa proprietà gli consente di reagire rapidamente con numerose
            sostanze organiche e inorganiche, modificandone la struttura molecolare.
            È proprio questo meccanismo che rende l’ozono efficace in specifici
            processi di trattamento e sanificazione.
          </p>
          <p>
            Tuttavia, la stessa reattività che rende l’ozono utile in ambito tecnico
            ne limita la stabilità e l’utilizzo indiscriminato.
            L’ozono tende a decomporsi rapidamente tornando a ossigeno,
            e la sua presenza in concentrazioni non controllate può risultare
            dannosa per persone, materiali e ambienti.
          </p>
          <p>
            Comprendere cosa sia l’ozono significa quindi considerarlo
            non come una sostanza “benefica” o “nociva” in senso assoluto,
            ma come una tecnologia chimico-fisica con caratteristiche precise,
            vantaggi specifici e limiti ben definiti.
          </p>
        </section>
    '''

    properties_html = f'''
        <section aria-labelledby="proprieta-ozono">
          <h2 id="proprieta-ozono">
            Proprietà chimiche e fisiche dell’ozono
          </h2>
          <p>
            Le proprietà chimiche e fisiche dell’ozono determinano
            il suo comportamento, la sua efficacia e i suoi limiti
            nei diversi contesti di utilizzo.
            Comprendere queste caratteristiche è essenziale
            per valutare correttamente quando l’ozono può essere
            una soluzione adeguata e quando no.
          </p>
          <h3>
            Struttura molecolare e reattività
          </h3>
          <p>
            L’ozono è composto da tre atomi di ossigeno legati
            in una configurazione instabile.
            Questa instabilità rende la molecola altamente reattiva,
            con una forte tendenza a cedere uno degli atomi di ossigeno
            per ossidare altre sostanze.
          </p>
          <p>
            La capacità ossidante dell’ozono è superiore
            a quella dell’ossigeno molecolare
            e inferiore solo ad alcuni agenti chimici specifici.
            Questa caratteristica spiega la rapidità delle reazioni
            che l’ozono innesca a contatto con composti organici,
            microrganismi e contaminanti.
          </p>
          <h3>
            Instabilità e tempo di decadimento
          </h3>
          <p>
            L’ozono è una molecola instabile e tende a decomporsi
            spontaneamente tornando a ossigeno.
            Il tempo di decadimento dipende da diversi fattori,
            tra cui temperatura, umidità, pressione
            e presenza di altre sostanze reattive.
          </p>
          <p>
            Questa instabilità rende impossibile lo stoccaggio
            dell’ozono e richiede una produzione in situ,
            direttamente nel punto di utilizzo.
            Allo stesso tempo, limita la persistenza dell’ozono
            nell’ambiente, riducendo l’effetto residuo nel tempo.
          </p>
          <h3>
            Proprietà fisiche rilevanti
          </h3>
          <p>
            A temperatura ambiente, l’ozono si presenta come un gas
            di colore blu pallido, con un odore caratteristico
            percepibile anche a basse concentrazioni.
            È più pesante dell’aria e tende ad accumularsi
            nelle zone più basse degli ambienti chiusi.
          </p>
          <p>
            La solubilità dell’ozono in acqua è limitata
            e dipende dalla temperatura e dalle condizioni operative.
            In fase acquosa, l’ozono reagisce rapidamente,
            influenzando l’efficacia e la durata del trattamento.
          </p>
        </section>
    '''

    mechanisms_html = f'''
        <section aria-labelledby="meccanismi-azione-ozono">
          <h2 id="meccanismi-azione-ozono">
            Come funziona l’ozono: meccanismi di azione
          </h2>
          <p>
            Il funzionamento dell’ozono si basa su reazioni chimiche
            di ossidazione che avvengono quando la molecola di ozono
            entra in contatto con altre sostanze.
            Questi meccanismi di azione spiegano sia l’efficacia
            dell’ozono in determinati contesti, sia i suoi limiti
            e le precauzioni necessarie.
          </p>
          <h3>
            Ossidazione diretta
          </h3>
          <p>
            L’ozono agisce principalmente attraverso un processo
            di ossidazione diretta.
            Durante la reazione, la molecola di ozono cede un atomo
            di ossigeno altamente reattivo, modificando la struttura
            chimica della sostanza con cui entra in contatto.
          </p>
          <p>
            Questo meccanismo consente all’ozono di degradare
            composti organici, inattivare microrganismi
            e trasformare alcune sostanze in forme chimicamente
            diverse o meno reattive.
            L’efficacia dell’ossidazione dipende dalla natura
            del contaminante e dalle condizioni operative.
          </p>
          <h3>
            Reazioni in fase gassosa e in fase acquosa
          </h3>
          <p>
            Il comportamento dell’ozono varia in base al mezzo
            in cui viene applicato.
            In fase gassosa, l’ozono reagisce direttamente
            con le superfici e con i composti presenti nell’aria.
            In fase acquosa, l’ozono può reagire sia direttamente
            sia attraverso la formazione di specie ossidanti secondarie.
          </p>
          <p>
            In acqua, il pH, la temperatura e la presenza
            di altre sostanze influenzano la velocità delle reazioni
            e la distribuzione dell’ozono disciolto.
            Questi fattori determinano la durata dell’effetto
            e l’efficienza complessiva del trattamento.
          </p>
          <h3>
            Assenza di effetto residuo
          </h3>
          <p>
            A differenza di altri agenti chimici,
            l’ozono non lascia un effetto residuo persistente.
            Dopo aver reagito, si decompone rapidamente
            tornando a ossigeno.
          </p>
          <p>
            Questa caratteristica può rappresentare
            un vantaggio o un limite a seconda del contesto:
            riduce l’accumulo di sostanze chimiche,
            ma richiede un controllo continuo del processo
            per mantenere l’efficacia nel tempo.
          </p>
        </section>
    '''

    safety_html = f'''
        <section aria-labelledby="sicurezza-rischi-ozono">
          <h2 id="sicurezza-rischi-ozono">
            Sicurezza e rischi dell’ozono
          </h2>
          <p>
            L’ozono è una sostanza chimicamente reattiva e,
            come tale, il suo utilizzo comporta rischi
            se non viene gestito correttamente.
            La sicurezza rappresenta un aspetto centrale
            in qualsiasi applicazione tecnologica dell’ozono
            e deve essere considerata fin dalle fasi di progettazione.
          </p>
          <p>
            Un approccio consapevole all’ozono non si limita
            a valutarne l’efficacia, ma richiede una comprensione
            chiara dei potenziali effetti sull’uomo,
            sui materiali e sugli ambienti trattati.
          </p>
          <h3>
            Effetti dell’ozono sulla salute
          </h3>
          <p>
            L’esposizione a concentrazioni elevate di ozono
            può causare irritazioni alle vie respiratorie,
            agli occhi e alle mucose.
            Gli effetti dipendono dalla concentrazione,
            dalla durata dell’esposizione
            e dalla sensibilità individuale.
          </p>
          <p>
            Per questo motivo, l’ozono non deve essere utilizzato
            in presenza di persone o animali,
            salvo in condizioni strettamente controllate
            e conformi alle normative vigenti.
          </p>
          <h3>
            Impatto su materiali e ambienti
          </h3>
          <p>
            Oltre agli effetti sulla salute,
            l’ozono può reagire con alcuni materiali,
            in particolare gomme, elastomeri,
            componenti plastici e superfici sensibili.
            Un’esposizione prolungata o non controllata
            può accelerare fenomeni di degrado.
          </p>
          <p>
            La valutazione dei materiali presenti
            nell’ambiente di applicazione
            è quindi una fase essenziale
            nella progettazione di un sistema a ozono.
          </p>
          <h3>
            Gestione del rischio e controllo
          </h3>
          <p>
            La sicurezza nell’utilizzo dell’ozono
            si basa su sistemi di controllo,
            monitoraggio e ventilazione adeguati.
            Sensori, temporizzazioni e procedure operative
            consentono di mantenere le concentrazioni
            entro limiti accettabili.
          </p>
          <p>
            L’ozono deve essere considerato
            una tecnologia da gestire,
            non una soluzione automatica.
            La corretta progettazione
            e la formazione degli operatori
            sono elementi indispensabili
            per ridurre i rischi e garantire
            un utilizzo responsabile.
          </p>
        </section>
    '''

    limits_html = f'''
      <section aria-labelledby="normative-limiti-ozono">
      <h2 id="normative-limiti-ozono">
        Normative e limiti di esposizione
      </h2>
      <p>
        L’utilizzo dell’ozono in ambito tecnico e industriale
        è regolato da normative e linee guida
        che definiscono i limiti di esposizione
        e le condizioni di sicurezza.
        Queste disposizioni hanno l’obiettivo
        di proteggere la salute delle persone
        e garantire un impiego controllato della tecnologia.
      </p>
      <p>
        Le normative non stabiliscono se l’ozono sia
        “consentito” o “vietato” in senso assoluto,
        ma ne regolano l’uso in funzione
        delle concentrazioni, dei tempi di esposizione
        e dei contesti applicativi.
      </p>
      <h3>
        Limiti di esposizione professionale
      </h3>
      <p>
        In ambito lavorativo, sono previsti
        limiti di esposizione definiti
        da enti normativi nazionali e internazionali.
        Questi valori indicano le concentrazioni massime
        ammissibili per un’esposizione ripetuta
        durante l’attività professionale.
      </p>
      <p>
        Il rispetto di tali limiti richiede
        l’adozione di sistemi di monitoraggio,
        procedure operative adeguate
        e una progettazione conforme
        alle normative di riferimento.
      </p>
      <h3>
        Normative ambientali e di sicurezza
      </h3>
      <p>
        Oltre ai limiti per l’esposizione umana,
        esistono normative che regolano
        l’installazione e il funzionamento
        dei sistemi a ozono in ambienti chiusi,
        industriali o civili.
      </p>
      <p>
        Queste disposizioni riguardano
        aspetti quali ventilazione,
        segnalazione del rischio,
        dispositivi di sicurezza
        e responsabilità dell’operatore.
        Il quadro normativo può variare
        in base al Paese e al settore applicativo.
      </p>
      <h3>
        Importanza della conformità normativa
      </h3>
      <p>
        La conformità alle normative
        non è un elemento opzionale,
        ma una condizione essenziale
        per l’utilizzo professionale dell’ozono.
        Operare al di fuori dei limiti normativi
        espone a rischi sanitari,
        tecnici e legali.
      </p>
      <p>
        Per questo motivo,
        la valutazione normativa
        deve essere parte integrante
        di qualsiasi progetto che preveda
        l’impiego di sistemi a ozono,
        fin dalle fasi iniziali.
      </p>
    </section>
    '''

    problems_html = f'''
      <section aria-labelledby="problemi-risolvibili-ozono">
        <h2 id="problemi-risolvibili-ozono">
          Problemi risolvibili con l’ozono
        </h2>
        <p>
          L’ozono viene utilizzato per affrontare specifiche categorie di problemi
          legati alla presenza di contaminanti chimici, biologici o organici.
          Non agisce su sintomi generici, ma su cause precise,
          attraverso meccanismi di ossidazione controllata.
        </p>
        <p>
          Comprendere quali problemi possono essere affrontati con l’ozono
          è essenziale per evitare applicazioni improprie
          e per valutare correttamente l’idoneità della tecnologia
          rispetto ad alternative disponibili.
        </p>
        <h3>
          Contaminazione microbiologica
        </h3>
        <p>
          L’ozono può essere utilizzato per ridurre
          la presenza di microrganismi come batteri,
          virus, muffe e lieviti,
          quando questi rappresentano un problema
          per la qualità dell’aria, dell’acqua
          o delle superfici.
        </p>
        <h3>
          Odori persistenti e composti organici volatili
        </h3>
        <p>
          Alcuni odori e composti organici volatili
          derivano da processi di degradazione,
          attività produttive o contaminazioni ambientali.
          L’ozono può reagire con queste sostanze,
          modificandone la struttura chimica
          e riducendone la percezione.
        </p>
        <h3>
          Contaminanti chimici e residui ossidabili
        </h3>
        <p>
          In determinati contesti,
          l’ozono viene impiegato per trattare
          contaminanti chimici ossidabili
          presenti in aria o in acqua.
          L’efficacia dipende dalla natura del contaminante
          e dalle condizioni operative del sistema.
        </p>
        <h3>
          Limiti di applicabilità
        </h3>
        <p>
          Non tutti i problemi possono essere risolti con l’ozono.
          In presenza di contaminanti non ossidabili,
          materiali sensibili o vincoli normativi stringenti,
          l’ozono può risultare inefficace o non appropriato.
        </p>
        <p>
          Per questo motivo,
          l’analisi del problema rappresenta
          il primo passo fondamentale
          prima di considerare l’ozono
          come possibile soluzione tecnologica.
        </p>
      </section>
    '''

    applicazioni_html = f'''
      <section aria-labelledby="contexts-title">
        <h2 id="contexts-title">
          Contesti di applicazione dell’ozono
        </h2>
        <p>
          L’ozono viene utilizzato in contesti molto diversi tra loro,
          ma la sua applicazione non è mai indipendente
          dalle condizioni operative, dal livello di controllo
          e dai vincoli normativi del settore di riferimento.
          Ogni ambito presenta esigenze, rischi e obiettivi differenti.
        </p>
        <p>
          Comprendere i contesti di applicazione dell’ozono
          consente di valutare correttamente
          quando questa tecnologia può essere appropriata
          e quando richiede soluzioni progettuali complesse
          o alternative tecnologiche.
        </p>
        <h3>
          Ambito civile e residenziale
        </h3>
        <p>
          In ambito civile e residenziale,
          l’ozono viene talvolta considerato
          per il trattamento di aria, acqua o superfici.
          Tuttavia, questi contesti richiedono
          particolare attenzione ai livelli di esposizione,
          alla presenza di persone
          e alla semplicità dei sistemi di controllo.
        </p>
        <h3>
          Ambito commerciale
        </h3>
        <p>
          Gli ambienti commerciali presentano
          esigenze legate alla continuità operativa,
          alla sicurezza degli occupanti
          e alla gestione di spazi condivisi.
          L’utilizzo dell’ozono in questi contesti
          è subordinato a procedure controllate
          e a una chiara definizione dei tempi di trattamento.
        </p>
        <h3>
          Ambito industriale
        </h3>
        <p>
          In ambito industriale,
          l’ozono viene utilizzato come tecnologia di processo
          per il trattamento di aria, acqua
          o flussi produttivi complessi.
          Qui l’ozono può essere integrato
          in sistemi strutturati,
          con monitoraggio continuo
          e personale formato.
        </p>
        <h3>
          Ambiti regolamentati
        </h3>
        <p>
          Alcuni settori sono soggetti
          a normative particolarmente stringenti,
          come l’industria alimentare,
          il trattamento delle acque
          o ambienti ad alta criticità sanitaria.
          In questi casi,
          l’applicazione dell’ozono
          deve rispettare requisiti tecnici,
          documentali e normativi specifici.
        </p>
      </section>
    '''

    design_html = f'''
    <section aria-labelledby="design-title">
      <h2 id="design-title">
        Progettazione di sistemi a ozono
      </h2>
      <p>
        L’efficacia e la sicurezza di un sistema a ozono
        dipendono in larga misura dalla fase di progettazione.
        L’ozono non può essere applicato in modo standardizzato:
        ogni sistema deve essere dimensionato
        in base al problema da risolvere,
        al contesto operativo
        e ai vincoli normativi.
      </p>
      <p>
        Una progettazione corretta considera l’ozono
        come parte di un sistema integrato,
        in cui parametri chimici, fisici e operativi
        devono essere controllati in modo coerente.
      </p>
      <h3>
        Analisi del problema
      </h3>
      <p>
        La progettazione inizia con l’analisi del problema reale:
        tipologia di contaminante,
        condizioni ambientali,
        obiettivi del trattamento
        e limiti operativi.
        Senza una definizione chiara del problema,
        l’ozono rischia di essere applicato
        in modo inefficace o non appropriato.
      </p>
      <h3>
        Definizione degli obiettivi
      </h3>
      <p>
        Gli obiettivi di un sistema a ozono
        devono essere misurabili e realistici.
        Riduzione, inattivazione o trasformazione
        sono risultati diversi
        che richiedono approcci progettuali differenti.
      </p>
      <h3>
        Parametri critici
      </h3>
      <p>
        La concentrazione di ozono,
        il tempo di contatto,
        il volume da trattare
        e le condizioni ambientali
        rappresentano parametri critici
        per il funzionamento del sistema.
        Questi elementi devono essere bilanciati
        per ottenere l’effetto desiderato
        senza superare i limiti di sicurezza.
      </p>
      <h3>
        Sicurezza e controllo
      </h3>
      <p>
        Un sistema a ozono deve integrare
        dispositivi di sicurezza,
        sistemi di controllo automatico
        e procedure operative chiare.
        La prevenzione dell’esposizione accidentale
        è un requisito fondamentale
        della fase progettuale.
      </p>
      <h3>
        Monitoraggio operativo
      </h3>
      <p>
        Il monitoraggio consente di verificare
        che il sistema funzioni
        secondo i parametri progettati.
        Sensori, registrazione dei dati
        e controlli periodici
        permettono di mantenere
        l’efficacia e la sicurezza nel tempo.
      </p>
    </section>
    '''

    technologies_html = f'''
    <section aria-labelledby="technologies-title">
      <h2 id="technologies-title">
        Tecnologie e sistemi a ozono
      </h2>
      <p>
        Le tecnologie a ozono comprendono
        diversi tipi di sistemi progettati
        per generare, distribuire e controllare
        l’ozono in funzione del contesto applicativo.
        La scelta della tecnologia influenza
        l’efficacia del trattamento,
        la sicurezza operativa
        e l’affidabilità del sistema.
      </p>
      <p>
        I sistemi a ozono non sono dispositivi isolati,
        ma soluzioni integrate
        che combinano generazione,
        controllo, distribuzione
        e monitoraggio.
      </p>
      <h3>
        Generatori di ozono
      </h3>
      <p>
        I generatori di ozono sono il cuore del sistema.
        Producono ozono a partire dall’ossigeno
        mediante processi fisici controllati.
        Le caratteristiche del generatore
        determinano la capacità produttiva,
        la stabilità dell’emissione
        e l’efficienza complessiva.
      </p>
      <h3>
        Sistemi per trattamento aria
      </h3>
      <p>
        Nei sistemi per il trattamento dell’aria,
        l’ozono viene distribuito
        in ambienti chiusi o in condotte,
        secondo modalità che dipendono
        dal volume, dalla ventilazione
        e dalla presenza di persone.
        Il controllo delle concentrazioni
        è un aspetto essenziale.
      </p>
      <h3>
        Sistemi per trattamento acqua
      </h3>
      <p>
        Nel trattamento dell’acqua,
        l’ozono viene disciolto
        per reagire con contaminanti
        biologici o chimici.
        Il contatto tra ozono e acqua
        è influenzato da parametri
        come temperatura, pH
        e qualità dell’acqua stessa.
      </p>
      <h3>
        Sistemi integrati
      </h3>
      <p>
        I sistemi integrati combinano
        più tecnologie e funzioni,
        adattandosi a processi complessi.
        Queste soluzioni richiedono
        una progettazione avanzata
        e un coordinamento preciso
        tra le diverse componenti.
      </p>
    </section>
    '''

    regulations_html = f'''
    <section aria-labelledby="regulations-title">
      <h2 id="regulations-title">
        Normative, standard e responsabilità
      </h2>
      <p>
        L’utilizzo dell’ozono come tecnologia
        è soggetto a normative, standard tecnici
        e responsabilità operative
        che variano in base al contesto applicativo
        e al settore di riferimento.
        Questi elementi definiscono
        i limiti entro cui l’ozono può essere impiegato
        in modo sicuro e conforme.
      </p>
      <p>
        La conoscenza del quadro normativo
        non è un aspetto accessorio,
        ma una parte integrante
        della progettazione e gestione
        di qualsiasi sistema a ozono.
      </p>
      <h3>
        Normative internazionali
      </h3>
      <p>
        A livello internazionale,
        diversi enti definiscono linee guida
        relative all’esposizione all’ozono,
        alla sicurezza sul lavoro
        e alla tutela ambientale.
        Queste normative forniscono
        riferimenti generali
        per l’impiego controllato dell’ozono
        in ambito professionale.
      </p>
      <h3>
        Normative di settore
      </h3>
      <p>
        Alcuni settori applicativi,
        come il trattamento delle acque,
        l’industria alimentare
        o gli ambienti industriali regolamentati,
        sono soggetti a normative specifiche
        che disciplinano l’uso dell’ozono
        come tecnologia di processo.
      </p>
      <p>
        In questi contesti,
        l’ozono può essere ammesso,
        limitato o vincolato
        a determinate condizioni operative
        e documentali.
      </p>
      <h3>
        Responsabilità operative
      </h3>
      <p>
        La responsabilità dell’utilizzo dell’ozono
        ricade su chi progetta,
        installa e gestisce il sistema.
        Ciò include la valutazione dei rischi,
        il rispetto dei limiti normativi
        e la formazione degli operatori.
      </p>
      <p>
        Un approccio responsabile all’ozono
        richiede competenze tecniche,
        consapevolezza normativa
        e procedure operative chiare,
        evitando applicazioni improvvisate
        o non conformi.
      </p>
    </section>
    '''

    cases_html = f'''
    <section aria-labelledby="cases-title">
      <h2 id="cases-title">
        Applicazioni reali e casi tecnici
      </h2>
      <p>
        L’ozono viene utilizzato in numerosi contesti reali,
        spesso con risultati molto differenti
        a seconda delle condizioni operative,
        della progettazione del sistema
        e del livello di controllo applicato.
        L’esperienza sul campo è fondamentale
        per comprendere cosa funziona,
        cosa non funziona
        e perché.
      </p>
      <p>
        Analizzare applicazioni reali
        consente di superare
        una visione teorica dell’ozono
        e di valutarne l’efficacia concreta
        all’interno di processi complessi.
      </p>
      <h3>
        Applicazioni corrette
      </h3>
      <p>
        Le applicazioni corrette dell’ozono
        sono caratterizzate da
        obiettivi chiari,
        parametri controllati
        e un’integrazione coerente
        con il contesto operativo.
        In questi casi,
        l’ozono viene utilizzato
        come strumento mirato,
        non come soluzione generica.
      </p>
      <h3>
        Criticità riscontrate
      </h3>
      <p>
        In molte applicazioni reali,
        emergono criticità legate
        a sovradosaggio,
        mancanza di controllo,
        errata valutazione del contesto
        o aspettative non realistiche.
        Questi aspetti possono ridurre
        l’efficacia del trattamento
        o introdurre rischi evitabili.
      </p>
      <h3>
        Lezioni apprese
      </h3>
      <p>
        L’analisi dei casi tecnici
        evidenzia l’importanza
        di una progettazione consapevole,
        di un monitoraggio continuo
        e di una comprensione reale
        dei limiti dell’ozono.
        Le lezioni apprese
        guidano scelte più informate
        nelle applicazioni future.
      </p>
    </section>
    '''

    decision_html = f'''
    <section aria-labelledby="decision-title">
      <h2 id="decision-title">
        Quando scegliere (e quando no) l’ozono
      </h2>
      <p>
        L’ozono non è una tecnologia universale.
        In alcuni contesti rappresenta
        una soluzione efficace e sostenibile,
        mentre in altri può risultare
        non indicato o sproporzionato
        rispetto agli obiettivi da raggiungere.
      </p>
      <p>
        Un supporto decisionale corretto
        richiede la valutazione congiunta
        del problema da risolvere,
        delle condizioni operative
        e delle alternative disponibili.
      </p>
      <h3>
        Quando l’ozono è indicato
      </h3>
      <p>
        L’ozono è indicato
        quando è necessario
        un’azione ossidante rapida,
        senza residui chimici,
        e quando il processo consente
        un controllo accurato
        dei parametri di utilizzo.
      </p>
      <p>
        In questi casi,
        l’ozono viene scelto
        come strumento specifico,
        integrato in un sistema progettato
        attorno al problema reale.
      </p>
      <h3>
        Quando l’ozono non è indicato
      </h3>
      <p>
        L’ozono non è indicato
        in assenza di controllo,
        in ambienti non compatibili
        o quando le condizioni operative
        non permettono di gestirne
        la reattività e la sicurezza.
      </p>
      <p>
        Utilizzare l’ozono
        come soluzione generica
        o senza una progettazione adeguata
        può portare a inefficienze
        o a rischi evitabili.
      </p>
      <h3>
        Tecnologie alternative
      </h3>
      <p>
        In alcuni contesti,
        tecnologie alternative
        possono risultare più adatte
        in termini di semplicità,
        costi o compatibilità operativa.
        La scelta tecnologica
        dovrebbe sempre basarsi
        su un confronto oggettivo
        tra opzioni disponibili.
      </p>
    </section>
    '''

    more_html = f'''
      <section aria-labelledby="hub-title">
        <h2 id="hub-title">
          Approfondimenti sull’ozono
        </h2>
        <p>
          Questa sezione raccoglie
          i principali approfondimenti tematici
          legati all’ozono.
          Ogni area esplora un aspetto specifico,
          permettendo di approfondire
          applicazioni, tecnologie
          e responsabilità operative.
        </p>
        <nav aria-label="Approfondimenti tematici sull’ozono">
          <ul>
            <li>
              <a href="/applicazioni.html">
                Applicazioni dell’ozono
              </a>
            </li>
            <li>
              <a href="/prodotti.html">
                Tecnologie e sistemi
              </a>
            </li>
            <li>
              <a href="/servizi.html">
                Progettazione e servizi
              </a>
            </li>
            <li>
              <a href="/progetti.html">
                Applicazioni reali e casi tecnici
              </a>
            </li>
            <li>
              <a href="/certificazioni.html">
                Normative e conformità
              </a>
            </li>
          </ul>
        </nav>
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
                {properties_html}
                {mechanisms_html}
                {safety_html}
                {limits_html}
                {problems_html}
                {applicazioni_html}
                {design_html}
                {technologies_html}
                {regulations_html}
                {cases_html}
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
