# 1. Introduzione

## 1.1 Scopo del documento

Il presente documento descrive la progettazione hardware e firmware del **Modulo Monitoraggio Ossigeno**, destinato al monitoraggio della concentrazione di ossigeno all'interno di sistemi industriali per la produzione di ozono.

L'obiettivo del documento è fornire una descrizione tecnica completa del dispositivo, comprendente l'architettura hardware, l'architettura firmware, le caratteristiche elettriche, le interfacce di comunicazione, il principio di funzionamento e le modalità operative del modulo.

Il documento costituisce il riferimento tecnico per le attività di progettazione, produzione, collaudo, integrazione, manutenzione ed eventuale evoluzione del prodotto.

Le informazioni contenute nel presente documento si riferiscono alla revisione hardware e firmware riportata nella sezione **Document Control**.

---

## 1.2 Campo di applicazione

Il **Modulo Monitoraggio Ossigeno** è un dispositivo elettronico basato su microcontrollore progettato per il monitoraggio continuo della concentrazione di ossigeno all'interno di sistemi di produzione di ozono.

Il modulo integra un sensore di ossigeno a ultrasuoni modello **US1010**, installato direttamente sul circuito stampato, e acquisisce in modo continuo il valore di concentrazione dell'ossigeno presente nel flusso di gas proveniente dal concentratore di ossigeno.

Le misure acquisite vengono elaborate dal microcontrollore, visualizzate localmente mediante display integrato e trasmesse al sistema di controllo tramite interfaccia seriale **RS485**. È inoltre disponibile un'uscita analogica **0–10 V**, destinata all'integrazione con PLC o altri sistemi di supervisione che non supportano la comunicazione seriale RS485.

Il modulo svolge esclusivamente funzioni di acquisizione, elaborazione e trasmissione delle misure. L'interpretazione dei dati, la gestione degli allarmi e le logiche di controllo del processo sono demandate al controllore principale della macchina.

Il presente documento descrive esclusivamente il **Modulo Monitoraggio Ossigeno** e non tratta il funzionamento del sistema completo di produzione di ozono né delle altre unità elettroniche che lo compongono.

---

# 2. Architettura del Sistema

## 2.1 Contesto del Sistema

Il **Modulo Monitoraggio Ossigeno** è un’unità funzionale integrata all’interno di un sistema industriale per la produzione di ozono gassoso.

All’interno dell’architettura complessiva, il modulo si colloca tra il sistema di generazione del gas e il sistema di conversione in ozono, con la funzione di monitorare in tempo reale la concentrazione di ossigeno presente nel flusso proveniente dal concentratore.

Il modulo non implementa logiche di controllo del processo produttivo, ma opera esclusivamente come unità di acquisizione e trasmissione dati verso il sistema di controllo principale. Quest’ultimo è responsabile della gestione del processo, dell’interpretazione delle misure e della generazione di eventuali condizioni di allarme.

Dal punto di vista fisico e funzionale, il modulo è integrato sia nel dominio elettronico sia nel dominio pneumatico del sistema.

---

## 2.2 Architettura Funzionale Elettronica

L’architettura elettronica del sistema è basata su un microcontrollore che gestisce l’acquisizione dei dati provenienti dal sensore di ossigeno, l’elaborazione delle misure e la distribuzione delle informazioni verso le diverse interfacce di uscita.

Il segnale proveniente dal sensore viene acquisito e convertito in forma digitale dal microcontrollore, che esegue le operazioni di elaborazione e validazione del dato.

Il sistema elettronico fornisce tre principali uscite funzionali:

- interfaccia di comunicazione seriale **RS485**, utilizzata per la trasmissione dei dati al sistema di controllo principale o a dispositivi compatibili (PLC o controller custom);
- uscita analogica **0–10 V**, utilizzata come segnale di compatibilità per sistemi di acquisizione analogici;
- interfaccia di visualizzazione locale tramite display integrato.

Il diagramma seguente rappresenta l’architettura funzionale del sistema elettronico:

                +------------------------+
                |  Concentratore O₂      |
                +------------------------+
                          │
                          ▼
                +------------------------+
                | Sensore US1010        |
                | (montato su PCB)      |
                +------------------------+
                          │
                          ▼
                +------------------------+
                | Microcontrollore       |
                |                        |
                | - Acquisizione dati    |
                | - Elaborazione         |
                | - Diagnostica          |
                +------------------------+
                 │           │           │
                 │           │           │
                 ▼           ▼           ▼
        +--------------+  +--------+  +----------------+
        | Display      |  | RS485  |  | Uscita 0–10 V  |
        +--------------+  +--------+  +----------------+
                                  │
                                  ▼
                    +---------------------------+
                    | Sistema di Controllo     |
                    | principale               |
                    +---------------------------+

---

## 2.3 Architettura Pneumatica (Flusso del Gas)

Il modulo è integrato direttamente nel percorso pneumatico del sistema di produzione dell’ozono.

Il gas proveniente dal concentratore di ossigeno non viene convogliato direttamente al generatore di ozono, ma attraversa il modulo di misura, consentendo il monitoraggio in linea della concentrazione di ossigeno.

Il sensore di ossigeno US1010 è montato direttamente sul circuito stampato tramite i fori di fissaggio meccanici previsti dal costruttore. Il PCB integra quindi sia la funzione elettronica sia la struttura di supporto per la camera di misura del sensore.

Il flusso del gas è descritto dal seguente schema:

Concentratore di Ossigeno
        │
        ▼
Tubo di ingresso gas
        │
        ▼
+---------------------------+
| Modulo Monitoraggio O₂    |
|                           |
| Camera di misura US1010   |
| integrata su PCB          |
+---------------------------+
        │
        ▼
Tubo di uscita gas
        │
        ▼
Generatore di Ozono

Questa configurazione consente un monitoraggio continuo del gas senza interrompere il flusso pneumatico principale del sistema.

---

## 2.4 Decomposizione Funzionale del Sistema

Il sistema può essere suddiviso in un insieme di funzioni logiche indipendenti implementate a livello hardware e firmware.

Le principali funzioni sono:

- acquisizione del segnale proveniente dal sensore di ossigeno;
- conversione del segnale in valore digitale;
- filtraggio e stabilizzazione della misura;
- conversione in unità ingegneristiche;
- gestione dello stato operativo del sistema;
- gestione delle condizioni di errore e diagnostica del sensore;
- gestione della comunicazione tramite interfaccia RS485;
- generazione del segnale analogico 0–10 V;
- aggiornamento del display locale.

Il sistema opera secondo una logica a stati che può essere riassunta nelle seguenti condizioni principali:

- inizializzazione del sistema;
- funzionamento normale;
- stato di fault o errore;
- recupero da condizioni anomale.

Questa separazione funzionale consente di mantenere indipendenti le responsabilità di acquisizione, elaborazione e comunicazione.

---

## 2.5 Interfacce di Sistema

Il modulo espone le seguenti interfacce verso il sistema esterno:

### Interfaccia RS485

L’interfaccia RS485 rappresenta il canale di comunicazione principale con il sistema di controllo. Attraverso questa interfaccia vengono trasmessi i dati relativi alla concentrazione di ossigeno e allo stato del sistema.

La comunicazione può essere utilizzata sia con un controllore dedicato sia con dispositivi industriali compatibili come PLC.

### Uscita analogica 0–10 V

È presente un’uscita analogica proporzionale alla concentrazione di ossigeno misurata.

Questa interfaccia è destinata all’integrazione con sistemi di acquisizione analogici o controllori che non supportano la comunicazione digitale.

### Interfaccia sensore US1010

Il sensore di ossigeno è un componente commerciale integrato direttamente sul PCB. L’interfaccia tra sensore e sistema è di tipo fisico e elettrico, mentre l’elaborazione del segnale avviene nel microcontrollore.

### Interfaccia utente locale

Il modulo integra un display locale utilizzato esclusivamente per la visualizzazione della concentrazione di ossigeno e delle condizioni operative.

---

## 2.6 Requisiti di Sistema

Il sistema è progettato per operare in contesti industriali e deve rispettare i seguenti requisiti generali:

- funzionamento continuo in regime di monitoraggio;
- acquisizione stabile e ripetibile della misura di ossigeno;
- separazione funzionale tra monitoraggio e controllo di processo;
- compatibilità con sistemi di controllo industriali via RS485;
- compatibilità con ingressi analogici standard 0–10 V;
- comportamento deterministico in condizioni di errore;
- segnalazione di fault senza intervento sulle logiche di processo.

Il modulo non è responsabile del controllo del processo di produzione dell’ozono, né della gestione delle condizioni di sicurezza del sistema complessivo.

---

# 3. Hardware Design

## 3.1 Architettura Hardware Generale

L’architettura hardware del **Modulo Monitoraggio Ossigeno** è basata su un microcontrollore ESP32 che gestisce l’acquisizione dei dati provenienti dal sensore di ossigeno, l’elaborazione delle misure e la generazione delle interfacce di comunicazione verso il sistema esterno.

Il sistema è alimentato da una tensione di ingresso unica a 12 V, dalla quale vengono generate tutte le tensioni interne necessarie al funzionamento dei vari sottosistemi elettronici, inclusa la rail a 5 V per il sensore e la regolazione a 3.3 V per il microcontrollore e la logica digitale.

L’architettura è organizzata secondo una struttura a blocchi funzionali composta da:

- sistema di alimentazione e regolazione tensioni;
- unità di controllo basata su ESP32;
- interfaccia sensore di ossigeno US1010;
- interfaccia di comunicazione RS485;
- uscita analogica 0–10 V isolata;
- interfaccia utente tramite display LCD.

---

## 3.2 Alimentazione

Il modulo è alimentato tramite una tensione continua nominale di **12 V**.

La gestione dell’alimentazione è realizzata mediante una singola catena di regolazione che genera le tensioni interne necessarie:

- **5 V** per alimentazione del sensore di ossigeno US1010;
- **3.3 V** per alimentazione del microcontrollore ESP32 e della logica digitale.

La conversione di tensione verso il rail a 3.3 V è implementata tramite regolatore lineare (LDO), garantendo semplicità circuitale e riduzione del rumore elettrico sul dominio digitale.

Il sistema integra protezione contro l’inversione di polarità sulla linea di ingresso e protezioni transitorie mediante dispositivi TVS, in particolare sull’interfaccia di comunicazione RS485.

---

## 3.3 Microcontrollore

Il sistema è basato su un microcontrollore **ESP32** alimentato a 3.3 V.

L’ESP32 gestisce le seguenti funzioni principali:

- acquisizione dati dal sensore di ossigeno US1010 tramite interfaccia UART;
- elaborazione del segnale e conversione in unità ingegneristiche;
- gestione della comunicazione RS485 verso il sistema di controllo principale;
- generazione del segnale PWM per l’uscita analogica;
- aggiornamento del display LCD;
- gestione della logica di sistema in modalità loop continuo (superloop).

L’architettura firmware non utilizza un sistema operativo real-time, ma si basa su un ciclo di esecuzione deterministico.

---

## 3.4 Interfaccia Sensore US1010

Il sensore di ossigeno utilizzato è un dispositivo commerciale **US1010**, alimentato a 5 V e montato direttamente sul circuito stampato.

La comunicazione tra sensore e microcontrollore avviene tramite interfaccia **UART**.

Il sensore fornisce al sistema il valore di concentrazione di ossigeno già digitalizzato, riducendo la necessità di condizionamento analogico del segnale.

Il sensore è fisicamente integrato nel PCB tramite fori di fissaggio meccanici, garantendo stabilità strutturale e corretto allineamento con il percorso del gas.

---

## 3.5 Interfaccia RS485

La comunicazione con il sistema di controllo principale è realizzata tramite interfaccia **RS485 half-duplex**, basata sul transceiver **SP3485**.

La linea RS485 rappresenta il canale di comunicazione principale del sistema e viene utilizzata per la trasmissione dei dati di misura e dello stato operativo del modulo.

L’interfaccia è protetta mediante dispositivi **TVS** per la soppressione di transitori e scariche elettrostatiche, migliorando la robustezza del sistema in ambiente industriale.

---

## 3.6 Uscita Analogica 0–10 V

Il modulo dispone di un’uscita analogica **0–10 V** proporzionale alla concentrazione di ossigeno misurata.

Il segnale viene generato a partire da un’uscita PWM del microcontrollore, successivamente filtrata mediante rete RC e convertita in tensione continua.

L’uscita è **isolata elettricamente** rispetto alla logica digitale del sistema, al fine di garantire compatibilità con dispositivi industriali esterni e ridurre il rischio di disturbi o loop di massa.

Questa interfaccia è destinata principalmente a sistemi PLC o controllori analogici non dotati di comunicazione digitale RS485.

---

## 3.7 Interfaccia Utente (Display)

Il modulo integra un display LCD utilizzato per la visualizzazione locale della concentrazione di ossigeno e dello stato operativo del sistema.

La comunicazione tra microcontrollore e display avviene tramite interfaccia **I2C**, riducendo il numero di linee necessarie e semplificando il routing del PCB.

Il display ha esclusivamente funzione informativa e non consente interazione con il sistema.

---

## 3.8 Protezioni e Robustezza del Sistema

Il progetto include diverse misure di protezione per garantire affidabilità in ambiente industriale:

- protezione contro inversione di polarità sulla linea di alimentazione a 12 V;
- protezione transitoria mediante dispositivi **TVS** sull’interfaccia RS485;
- layout progettato per riduzione delle interferenze su linee di comunicazione;
- separazione tra dominio analogico (uscita 0–10 V) e dominio digitale (ESP32 e logica interna).

Queste soluzioni contribuiscono a migliorare la robustezza complessiva del sistema in condizioni operative reali.

---

# 4. Firmware Design

## 4.1 Architettura Software

Il firmware del **Modulo Monitoraggio Ossigeno** è implementato su microcontrollore ESP32 e segue un’architettura di tipo **superloop non bloccante**, in cui tutte le funzionalità vengono eseguite all’interno di un ciclo principale.

L’esecuzione del firmware non utilizza un sistema operativo real-time (RTOS), ma si basa su una gestione temporale tramite timer software indipendenti, che attivano le diverse funzionalità a intervalli definiti.

L’architettura software è organizzata secondo le seguenti responsabilità principali:

- gestione dello stato del sistema;
- acquisizione dati dal sensore di ossigeno US1010;
- gestione comunicazione RS485;
- generazione segnali analogici 0–10 V;
- aggiornamento interfaccia utente (display);
- sincronizzazione temporale delle attività.

---

## 4.2 State Machine

Il firmware è basato su una macchina a stati semplice composta dai seguenti stati operativi:

- **INIT**: inizializzazione del sistema e delle periferiche;
- **RUN**: funzionamento normale del modulo.

Durante lo stato INIT vengono eseguite le operazioni di configurazione hardware, inizializzazione delle interfacce di comunicazione e verifica preliminare del corretto avvio del sistema.

Al termine della fase di inizializzazione, il sistema passa automaticamente allo stato RUN, nel quale tutte le funzioni operative vengono eseguite ciclicamente.

Non è attualmente implementata una gestione locale dei fault; eventuali condizioni di errore sono gestite dal sistema di controllo principale.

---

## 4.3 Acquisizione del Sensore

Il sensore di ossigeno **US1010** fornisce dati in modo continuo tramite interfaccia **UART** con frequenza di aggiornamento pari a **1 Hz**.

Il microcontrollore riceve i dati senza utilizzo di polling, ma tramite ricezione continua del flusso seriale.

I dati acquisiti includono:

- concentrazione di ossigeno (O₂);
- temperatura del flusso;
- velocità/portata del flusso.

I valori vengono aggiornati internamente ogni secondo e resi disponibili alle altre funzioni del sistema.

---

## 4.4 Elaborazione Dati

I dati ricevuti dal sensore vengono elaborati dal microcontrollore per ottenere valori utilizzabili dalle interfacce di sistema.

L’elaborazione include:

- validazione del frame ricevuto;
- estrazione dei parametri misurati;
- conversione in formato numerico interno;
- aggiornamento delle variabili globali di sistema.

Non sono attualmente implementati filtri avanzati o algoritmi di media temporale; il sistema utilizza direttamente i valori forniti dal sensore con aggiornamento a 1 Hz.

---

## 4.5 Comunicazione RS485

La comunicazione con il sistema di controllo principale avviene tramite interfaccia **RS485 half-duplex** utilizzando un protocollo **custom**, compatibile con quello utilizzato dal sensore US1010.

Il modulo opera come **slave** e risponde alle richieste del sistema master.

Attraverso l’interfaccia RS485 vengono trasmessi i seguenti dati:

- concentrazione di ossigeno (O₂);
- temperatura del flusso;
- portata del gas;
- stato generale del modulo (RUN/INIT).

La comunicazione avviene in modo non bloccante all’interno del ciclo principale del firmware.

---

## 4.6 Uscite Analogiche 0–10 V

Il sistema genera tre uscite analogiche indipendenti:

- uscita 0–10 V proporzionale alla concentrazione di ossigeno;
- uscita 0–10 V proporzionale alla portata del flusso;
- uscita 0–10 V proporzionale alla temperatura del flusso.

Le uscite sono generate tramite segnale **PWM**, successivamente filtrato e convertito in tensione analogica continua.

Le grandezze sono scalate in modo direttamente proporzionale rispetto ai valori misurati dal sensore, secondo un mapping lineare.

---

## 4.7 Gestione dei Fault

Il modulo non implementa una gestione autonoma dei fault a livello firmware.

Eventuali condizioni di errore, perdita del segnale del sensore o anomalie operative vengono rilevate e gestite dal **sistema di controllo principale**, che è responsabile della logica di sicurezza e della gestione degli allarmi.

Il modulo continua comunque a fornire i dati disponibili fino a perdita totale della comunicazione o del segnale del sensore.

---

## 4.8 Interfaccia Utente (Display)

Il modulo integra un display LCD con interfaccia **I2C**, utilizzato per la visualizzazione locale dei parametri misurati.

Il display mostra in tempo reale:

- concentrazione di ossigeno (O₂);
- temperatura del flusso;
- portata del gas.

L’aggiornamento del display avviene con periodicità di **1 secondo**, sincronizzato con la ricezione dei dati dal sensore.

Il display ha esclusivamente funzione informativa e non consente interazione con il sistema.

---

# 5. Communication Protocol

## 5.1 Panoramica del Protocollo

La comunicazione tra il **Modulo Monitoraggio Ossigeno** e il sistema di controllo principale avviene tramite interfaccia **RS485 half-duplex**.

Il protocollo implementato è di tipo **frame-based proprietario**, basato su pacchetti strutturati con delimitazione esplicita e controllo di integrità mediante checksum.

Il modulo opera in modalità **trasmissione spontanea (broadcast periodico)**, inviando i dati al sistema di controllo principale con periodicità di 1 secondo.

Non è prevista una modalità di interrogazione (polling) da parte del master.

---

## 5.2 Struttura del Frame

Ogni messaggio trasmesso dal modulo segue la seguente struttura:

+-----------+-----------+-----------+----------------+------------+
| Head | Length | Command | Data | Checksum |
+-----------+-----------+-----------+----------------+------------+
1 byte 1 byte 1 byte n byte 1 byte


### Descrizione dei campi

- **Head (1 byte)**  
  Byte di sincronizzazione che identifica l’inizio del frame.

- **Length (1 byte)**  
  Indica la lunghezza del campo Data.

- **Command (1 byte)**  
  Identifica il tipo di messaggio trasmesso.

- **Data (n byte)**  
  Dati relativi alle misure del sistema.

- **Checksum (1 byte)**  
  Byte di controllo per la verifica dell’integrità del frame.

---

## 5.3 Tipologia dei Messaggi

Il sistema prevede un unico tipo di messaggio trasmesso dal modulo al controllore principale.

### Messaggio di trasmissione dati sensore

Il modulo invia periodicamente un frame contenente i valori misurati dal sensore.

Il contenuto del campo **Data** include:

- concentrazione di ossigeno (O₂);
- temperatura del flusso;
- portata del gas.

Il campo **Command** identifica il messaggio come trasmissione dati sensore.

Non sono previste richieste di lettura o comandi di configurazione da parte del sistema master.

---

## 5.4 Formato dei Dati

I dati contenuti nel campo Data sono codificati in formato binario secondo una struttura fissa.

I parametri trasmessi sono:

- **O₂ (ossigeno)**  
- **Temperatura del flusso**
- **Flusso gas**

Tutti i valori sono rappresentati come variabili numeriche scalate (interi), secondo una rappresentazione interna del sistema.

La scalatura esatta dei valori è definita a livello di implementazione firmware e garantisce la compatibilità tra modulo sensore e sistema di controllo.

---

## 5.5 Temporizzazione della Comunicazione

Il modulo trasmette i dati in modo **autonomo e periodico**.

- Frequenza di trasmissione: **1 Hz (ogni 1 secondo)**
- Modalità: trasmissione spontanea (no polling)
- Sincronizzazione: basata su timer interno del firmware

Ogni aggiornamento del frame corrisponde all’ultimo set di dati disponibili acquisiti dal sensore.

---

## 5.6 Controllo di Integrità (Checksum)

Il protocollo implementa un meccanismo di verifica dell’integrità del frame mediante un **checksum a 1 byte**.

Il checksum è calcolato sull’intero pacchetto dati secondo una logica di controllo di base (somma o XOR dei byte del frame, escluso il byte Head), garantendo la rilevazione di errori di trasmissione su linea RS485.

In caso di errore di checksum, il frame viene considerato non valido dal sistema ricevente e scartato.

---

## 5.7 Considerazioni sul Protocollo

Il protocollo è progettato per garantire:

- semplicità di implementazione su microcontrollore ESP32;
- ridotto overhead di comunicazione;
- compatibilità con sistemi industriali basati su RS485;
- trasmissione deterministica dei dati a 1 Hz;
- robustezza base contro errori di trasmissione.

L’assenza di una modalità di polling riduce la complessità del sistema, rendendo il modulo completamente autonomo nella trasmissione dei dati.

---

# 6. Specifiche Elettriche

## 6.1 Alimentazione

Il **Modulo Monitoraggio Ossigeno** è alimentato tramite una tensione continua nominale di **12 VDC**, con un range operativo compreso tra:

- **Tensione minima:** 6.1 VDC  
- **Tensione nominale:** 12 VDC  
- **Tensione massima:** 15 VDC  

L’alimentazione viene distribuita internamente verso i vari sottosistemi attraverso una rete di regolazione a singolo stadio.

---

## 6.2 Consumi

Il consumo totale del sistema dipende dallo stato operativo dei diversi blocchi funzionali.

Le principali stime di assorbimento sono:

- **ESP32 (3.3 V):** ~120–250 mA (picchi inclusi comunicazione WiFi interna non utilizzata ma idle core attivi)
- **Sensore US1010 + LCD (5 V):** ~80–150 mA
- **Circuiteria analogica e RS485:** ~20–50 mA

### Consumo totale stimato:
- **Tipico:** ~250–400 mA @ 12 V  
- **Picco massimo stimato:** fino a ~500 mA @ 12 V  

---

## 6.3 Interfacce Elettriche

### RS485

- Standard: RS485 half-duplex
- Baud rate: **9600 bps**
- Terminazione: **120 Ω presente**
- Lunghezza cavo tipica: **1 m**
- Protezione: TVS su linea differenziale
- Topologia: punto-punto verso sistema di controllo principale

---

### Sensore US1010

- Alimentazione: **5 VDC**
- Interfaccia dati: **UART**
- Connessione diretta al microcontrollore ESP32
- Nessuna protezione aggiuntiva lato alimentazione

---

## 6.4 Uscite Analogiche

Il modulo dispone di tre uscite analogiche indipendenti:

- Uscita O₂ (0–10 V)
- Uscita temperatura flusso (0–10 V)
- Uscita portata flusso (0–10 V)

### Caratteristiche elettriche:

- Range tensione: **0–10 V**
- Tipo di uscita: analogica attiva
- Carico minimo consigliato: **≥ 10 kΩ** (tipico ingresso PLC)
- Driver: buffer analogico con generazione tramite PWM + filtro RC
- Isolamento: **non presente**
- Protezione: **non presente**

Le tre uscite sono indipendenti e scalate linearmente rispetto ai valori misurati.

---

## 6.5 Interfaccia RS485

La comunicazione RS485 è utilizzata come canale principale verso il sistema di controllo.

Caratteristiche elettriche:

- Standard: RS485 half-duplex
- Protocollo: proprietario
- Velocità: **9600 bps**
- Terminazione linea: **120 Ω presente**
- Lunghezza cavo: **~1 m (installazione tipica)**
- Protezioni: TVS su linea differenziale

La comunicazione è progettata per ambienti industriali a breve distanza all’interno dello stesso quadro elettrico.

---

## 6.6 Range Operativi

Il sistema è progettato per operare nei seguenti intervalli di misura:

- **Concentrazione ossigeno (O₂):** 0 – 100 %
- **Temperatura del flusso:** 0 – 100 °C
- **Portata del gas:** 0 – 100 L/min

I valori sono rappresentati internamente in forma scalata e convertiti nei rispettivi segnali digitali e analogici.

---

## 6.7 Protezioni e Limitazioni

Il sistema include un numero limitato di protezioni hardware:

- protezione contro inversione di polarità sull’ingresso 12 V
- protezione TVS sull’interfaccia RS485

Non sono presenti le seguenti protezioni:

- fusibile di ingresso
- protezione dedicata sulle uscite analogiche 0–10 V
- protezione dedicata sul rail 5 V del sensore

Il funzionamento affidabile del sistema si basa principalmente sulla corretta integrazione all’interno del quadro elettrico e sulle protezioni presenti nel sistema di alimentazione principale.

---

## 6.8 Considerazioni Generali

Le specifiche elettriche del modulo sono ottimizzate per integrazione in sistemi industriali compatti, con particolare attenzione alla semplicità circuitale e alla riduzione del numero di componenti attivi.

Il sistema privilegia la funzionalità e l’integrazione rispetto all’isolamento elettrico completo, che è demandato all’architettura del sistema principale.

---

# 7. Progettazione Meccanica

## 7.1 Dimensioni del PCB

Il **Modulo Monitoraggio Ossigeno** è realizzato su circuito stampato con dimensioni complessive pari a:

- **100 mm x 100 mm**
- **Spessore PCB:** 1.6 mm (standard)

La geometria della scheda è di tipo quadrato, ottimizzata per facilitare l’integrazione meccanica all’interno del quadro elettrico e garantire una distribuzione uniforme dei componenti elettronici e delle interfacce di connessione.

---

## 7.2 Sistema di Fissaggio

Il fissaggio del PCB è realizzato mediante quattro punti di ancoraggio posizionati agli angoli della scheda.

### Caratteristiche meccaniche:

- Numero fori di fissaggio: **4**
- Standard: angoli PCB
- Diametro fori: **M3**
- Distanza tra i fori: **94 mm** (sia asse orizzontale che verticale)

Il fissaggio avviene mediante viti e distanziatori, garantendo il corretto isolamento della scheda dalla superficie di montaggio e assicurando stabilità meccanica durante il funzionamento.

L’altezza dei distanziatori è pari a circa **20 mm**, al fine di garantire spazio sufficiente per il cablaggio inferiore e per la dissipazione termica naturale dei componenti.

---

## 7.3 Integrazione del Sensore US1010

Il sensore di ossigeno **US1010** è montato direttamente sulla scheda PCB.

Il montaggio avviene tramite fissaggio meccanico su fori dedicati, utilizzando la stessa struttura prevista dal costruttore del sensore.

Il sensore è integrato con il circuito stampato sia dal punto di vista elettrico sia meccanico, garantendo:

- stabilità strutturale durante il funzionamento;
- corretto allineamento con il percorso del gas;
- riduzione di vibrazioni e disallineamenti.

La distanza del sensore rispetto al piano PCB è determinata dalla struttura meccanica del componente e dai distanziatori utilizzati.

---

## 7.4 Connessioni Pneumatiche

Il modulo integra due connessioni pneumatiche:

- ingresso gas (dal concentratore di ossigeno)
- uscita gas (verso generatore di ozono)

Le connessioni sono realizzate tramite raccordi **push-fit** con diametro nominale di **4 mm**.

Il tubo utilizzato è di tipo flessibile industriale (specifica non vincolata in questa revisione).

Il flusso del gas attraversa direttamente la camera di misura del sensore US1010, consentendo il monitoraggio in linea della concentrazione di ossigeno senza interrompere il circuito pneumatico principale.

---

## 7.5 Installazione nel Sistema

Il modulo è progettato per essere installato all’interno del quadro elettrico del sistema di produzione ozono.

Il montaggio avviene mediante fissaggio a pannello tramite viti, senza utilizzo di guida DIN.

L’orientamento del modulo è **verticale**, in modo da:

- garantire una corretta leggibilità del display LCD;
- facilitare l’accesso ai connettori pneumatici;
- ottimizzare la disposizione interna del quadro.

Il posizionamento deve garantire spazio sufficiente per il cablaggio elettrico e per la connessione dei tubi gas in ingresso e uscita.

---

## 7.6 Condizioni Ambientali

Il modulo è destinato all’utilizzo esclusivamente in ambiente interno, installato all’interno di un quadro elettrico industriale.

Le condizioni operative previste sono:

- ambiente industriale chiuso
- assenza di esposizione diretta agli agenti atmosferici
- assenza di vibrazioni significative (tipiche di quadri elettrici statici)

Non sono definite specifiche estese per ambienti estremi, in quanto il modulo dipende dall’integrazione all’interno del sistema principale che ne garantisce le condizioni operative.


---

# Appendice A – Schemi Elettrici (Descrizione Strutturata)

## A.1 Scopo dell’Appendice

Questa appendice fornisce una descrizione funzionale strutturata degli schemi elettrici del **Modulo Monitoraggio Ossigeno**, al fine di chiarire l’organizzazione circuitale del sistema senza fare riferimento diretto ai disegni CAD originali.

L’obiettivo è descrivere le principali sezioni elettroniche, le interconnessioni e la suddivisione funzionale del circuito stampato.

---

## A.2 Architettura Elettrica Generale

L’architettura elettrica del modulo è suddivisa nelle seguenti sezioni principali:

- sezione di alimentazione e regolazione tensioni;
- sezione microcontrollore (ESP32);
- interfaccia sensore di ossigeno US1010;
- interfaccia di comunicazione RS485;
- sezione uscita analogica 0–10 V;
- interfaccia utente (display LCD);
- circuiti di protezione e filtraggio.

Ogni sezione è progettata per operare in modo funzionalmente indipendente pur condividendo la stessa alimentazione principale a 12 V.

---

## A.3 Sezione di Alimentazione

La sezione di alimentazione riceve una tensione in ingresso di 12 VDC e la distribuisce alle varie sottosezioni del sistema.

### Blocchi funzionali:

- ingresso alimentazione 12 VDC
- protezione contro inversione di polarità
- regolazione verso 5 VDC per sensore e display
- regolazione verso 3.3 VDC per microcontrollore

La regolazione a 3.3 V è realizzata mediante regolatore lineare (LDO), mentre la linea a 5 V alimenta direttamente il sensore US1010 e il display LCD.

---

## A.4 Sezione Microcontrollore (ESP32)

La sezione centrale del sistema è basata su un microcontrollore ESP32 alimentato a 3.3 V.

### Funzioni principali:

- acquisizione dati da sensore tramite UART
- gestione logica firmware
- generazione segnali PWM per uscite analogiche
- gestione comunicazione RS485
- aggiornamento display LCD via I2C

Il microcontrollore è il nodo centrale di elaborazione del sistema e coordina tutte le periferiche.

---

## A.5 Interfaccia Sensore US1010

Il sensore di ossigeno US1010 è alimentato a 5 V e comunica con il microcontrollore tramite interfaccia UART.

### Caratteristiche circuitali:

- alimentazione dedicata 5 V
- linea seriale UART diretta verso ESP32
- connessione integrata su PCB
- nessuna isolazione galvanica

Il sensore è montato direttamente sul PCB e costituisce parte integrante sia del dominio elettrico sia del percorso pneumatico del sistema.

---

## A.6 Interfaccia RS485

La comunicazione RS485 è implementata tramite transceiver **SP3485** in configurazione half-duplex.

### Sezione funzionale:

- convertitore livello TTL ↔ RS485
- linea differenziale A/B
- terminazione 120 Ω (integrata sulla scheda)
- protezione transitoria tramite TVS

La sezione RS485 è collegata direttamente al microcontrollore ESP32 e rappresenta il canale di comunicazione principale verso il sistema di controllo esterno.

---

## A.7 Uscite Analogiche 0–10 V

Il modulo dispone di tre canali analogici indipendenti:

- O₂ concentration
- flusso gas
- temperatura flusso

### Implementazione circuitale:

- generazione segnale PWM da ESP32
- filtraggio passa-basso RC
- buffer analogico di uscita

Le uscite non sono isolate elettricamente e condividono la massa del sistema.

Ogni canale è linearmente proporzionale alla grandezza fisica misurata.

---

## A.8 Interfaccia Display LCD

Il display LCD è collegato al microcontrollore tramite bus I2C.

### Funzioni:

- visualizzazione concentrazione O₂
- visualizzazione temperatura flusso
- visualizzazione portata gas

Il display opera esclusivamente in modalità di output informativo e non prevede interazioni utente.

---

## A.9 Sezione di Protezione e Filtraggio

Il sistema include protezioni hardware essenziali per garantire il funzionamento in ambiente industriale.

### Protezioni implementate:

- protezione contro inversione di polarità sull’ingresso 12 V
- TVS su linea RS485

### Assenze progettuali:

- assenza fusibile di ingresso
- assenza protezione dedicata sulle linee 0–10 V
- assenza protezione specifica sul rail 5 V del sensore

Il sistema si basa sull’integrazione in un ambiente controllato (quadro elettrico industriale).

---

## A.10 Considerazioni Finali

Gli schemi elettrici del modulo sono organizzati secondo una struttura modulare che separa chiaramente:

- dominio di alimentazione
- dominio digitale (ESP32)
- dominio sensore
- dominio comunicazione industriale
- dominio analogico

Questa suddivisione facilita la manutenzione, l’analisi del sistema e l’eventuale evoluzione futura del progetto.