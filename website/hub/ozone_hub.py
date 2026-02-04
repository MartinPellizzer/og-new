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

              <!-- 4. PROBLEMI RISOLVIBILI -->
              <section aria-labelledby="problems-title">
                <h2 id="problems-title">
                  Problemi che l’ozono può risolvere
                </h2>

                <h3>Problemi legati all’aria</h3>
                <h3>Problemi legati all’acqua</h3>
                <h3>Problemi su superfici e processi</h3>
              </section>

              <!-- 5. CONTESTI DI APPLICAZIONE -->
              <section aria-labelledby="contexts-title">
                <h2 id="contexts-title">
                  Contesti di applicazione dell’ozono
                </h2>

                <h3>Ambito civile e residenziale</h3>
                <h3>Ambito commerciale</h3>
                <h3>Ambito industriale</h3>
                <h3>Ambiti regolamentati</h3>
              </section>

              <!-- 6. PROGETTAZIONE -->
              <section aria-labelledby="design-title">
                <h2 id="design-title">
                  Progettazione di sistemi a ozono
                </h2>

                <h3>Analisi del problema</h3>
                <h3>Definizione degli obiettivi</h3>
                <h3>Parametri critici</h3>
                <h3>Sicurezza e controllo</h3>
                <h3>Monitoraggio operativo</h3>
              </section>

              <!-- 7. TECNOLOGIE -->
              <section aria-labelledby="technologies-title">
                <h2 id="technologies-title">
                  Tecnologie e sistemi a ozono
                </h2>

                <h3>Generatori di ozono</h3>
                <h3>Sistemi per trattamento aria</h3>
                <h3>Sistemi per trattamento acqua</h3>
                <h3>Sistemi integrati</h3>
              </section>

              <!-- 8. NORMATIVE -->
              <section aria-labelledby="regulations-title">
                <h2 id="regulations-title">
                  Normative, standard e responsabilità
                </h2>

                <h3>Normative internazionali</h3>
                <h3>Normative di settore</h3>
                <h3>Responsabilità operative</h3>
              </section>

              <!-- 9. ESPERIENZA REALE -->
              <section aria-labelledby="cases-title">
                <h2 id="cases-title">
                  Applicazioni reali e casi tecnici
                </h2>

                <h3>Applicazioni corrette</h3>
                <h3>Criticità riscontrate</h3>
                <h3>Lezioni apprese</h3>
              </section>

              <!-- 10. SUPPORTO DECISIONALE -->
              <section aria-labelledby="decision-title">
                <h2 id="decision-title">
                  Quando scegliere (e quando no) l’ozono
                </h2>

                <h3>Quando l’ozono è indicato</h3>
                <h3>Quando l’ozono non è indicato</h3>
                <h3>Tecnologie alternative</h3>
              </section>

              <!-- 11. NAVIGAZIONE HUB -->
              <section aria-labelledby="hub-title">
                <h2 id="hub-title">
                  Approfondimenti sull’ozono
                </h2>

                <nav aria-label="Approfondimenti tematici">
                  <ul>
                    <li><a href="/applicazioni.html">Applicazioni dell’ozono</a></li>
                    <li><a href="/prodotti.html">Tecnologie e sistemi</a></li>
                    <li><a href="/servizi.html">Progettazione e servizi</a></li>
                    <li><a href="/progetti.html">Casi applicativi</a></li>
                    <li><a href="/certificazioni.html">Normative e conformità</a></li>
                  </ul>
                </nav>
              </section>

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
