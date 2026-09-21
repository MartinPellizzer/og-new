# chapter (users' top-level goals)
## section (goal)
### sub-section

---

# stakeholders
utenti
installatori
manutentori
costruttori
ingegnieri

# goal
creare un MODULO che trasmetta al CORE le letture di 1 sensore ozono ZE27-O3.

## Ricevere i dati dal sensore

### Impostare l'rs485 1 in modalità lettura
### Leggere i bytes ricevuti dal rs485 1
### Attendere che tutti i bytes del messaggio siano arrivati
### Salvare i bytes in un buffer

## Verificare i dati ricevuti

### Leggere i dati salvati nel buffer
### Calcolare il CRC
### Verificare che il CRC corrisponda con quello ricevuto

## Trasmettere i dati al core

### Impostare l'rs485 2 in modalità lettura
### Attendere che il core (master) chieda il valore del sensore al modulo (slave), con protocollo modbus
### Impostare l'rs485 2 in modalità scrittura
### Inviare i dati del buffer al core tramite l'rs485 2
### Impostare l'rs485 2 in modalità lettura

ricevere i dati dal sensore
verificare i dati ricevuti
trasmettere i dati al core

# exceptions
dati ricevuti incorrettamente
modulo non funzionante

# requirement (who wants what)













Sì. Per un **documento tecnico dei requisiti** ti suggerisco di separare nettamente:

1. **Requisiti funzionali** → cosa deve fare il modulo.
2. **Sequenza nominale** → il caso in cui tutto funziona correttamente.
3. **Gestione delle eccezioni** → cosa deve succedere quando qualcosa va storto.
4. **Timeout e condizioni di errore** → quando una situazione viene considerata anomala.
5. **Stati del modulo** → utile soprattutto perché hai due RS485 e una comunicazione master/slave.
6. **Interfaccia verso il CORE** → registri Modbus, formato dati, stato/diagnostica.
7. **Requisiti di inizializzazione e recovery** → power-on, reset, perdita di comunicazione, recovery.

C'è anche un punto importante nella tua procedura: **il modulo non dovrebbe necessariamente "aspettare" continuamente il sensore e poi aspettare il CORE in modo sequenziale**. Se il sensore ZE27-O3 produce dati autonomamente, conviene pensare al modulo come a un piccolo nodo che **acquisisce e valida continuamente il dato del sensore**, mentre contemporaneamente rende disponibile l'ultimo dato valido al CORE tramite Modbus. Questo evita di legare temporalmente le due comunicazioni.

Ti propongo quindi una struttura più adatta a un requisito tecnico.

---

# 1. Scopo del modulo

**FR-001 — Acquisizione e comunicazione del dato ozono**

Il modulo deve acquisire le misure provenienti da un sensore ozono ZE27-O3 tramite interfaccia RS485 e rendere disponibile al controller principale (CORE) l'ultima misura validata tramite una seconda interfaccia RS485 utilizzando protocollo Modbus.

**FR-002 — Separazione delle interfacce**

Il modulo deve utilizzare:

* **RS485-1** per la comunicazione con il sensore ZE27-O3;
* **RS485-2** per la comunicazione con il CORE;
* RS485-2 deve operare come **slave Modbus**;
* il CORE deve operare come **master Modbus**.

---

# 2. Architettura logica

Suggerirei di esplicitare nel documento una struttura simile:

```text
                ┌─────────────────────┐
                │     ZE27-O3         │
                └──────────┬──────────┘
                           │
                         RS485-1
                           │
                           ▼
                ┌─────────────────────┐
                │                     │
                │   MODULE            │
                │                     │
                │  RX buffer          │
                │  Frame validation   │
                │  CRC validation     │
                │  Data storage       │
                │  Diagnostics        │
                │                     │
                └──────────┬──────────┘
                           │
                         RS485-2
                           │
                           ▼
                ┌─────────────────────┐
                │       CORE          │
                │   Modbus Master     │
                └─────────────────────┘
```

Questo ti permette poi di definire chiaramente i requisiti di ciascuna interfaccia.

---

# 3. Procedura nominale

Io riscriverei la tua procedura così.

## 3.1 Inizializzazione

### FR-010 — Inizializzazione del modulo

All'accensione o al reset, il modulo deve inizializzare:

* microcontrollore;
* RS485-1;
* RS485-2;
* buffer di ricezione;
* variabili contenenti il dato del sensore;
* stato della comunicazione con il sensore;
* stato della comunicazione con il CORE;
* diagnostica ed eventuali contatori di errore.

### FR-011 — Configurazione RS485-1

Il modulo deve configurare RS485-1 secondo i parametri richiesti dal sensore ZE27-O3:

* baud rate;
* numero di data bit;
* parity;
* stop bit;
* modalità half/full duplex, se applicabile;
* eventuale indirizzo del sensore;
* eventuali parametri specifici del protocollo del sensore.

**Nota:** qui nel documento metterei i valori effettivi derivanti dal datasheet del modello ZE27-O3 utilizzato, anziché lasciarli impliciti.

### FR-012 — Configurazione RS485-2

Il modulo deve configurare RS485-2 secondo i parametri definiti per la comunicazione Modbus con il CORE.

Il modulo deve operare come **Modbus slave**.

---

# 4. Acquisizione del sensore

Qui cambierei leggermente la tua sequenza.

## 4.1 Ricezione

### FR-020 — Ricezione dei dati dal sensore

Il modulo deve monitorare continuamente RS485-1 per rilevare dati provenienti dal sensore.

### FR-021 — Rilevamento dell'inizio del frame

Il modulo deve identificare l'inizio di un messaggio ricevuto secondo il protocollo utilizzato dal sensore.

### FR-022 — Ricezione dei byte

Il modulo deve acquisire sequenzialmente tutti i byte appartenenti al messaggio ricevuto.

### FR-023 — Memorizzazione del frame

Durante la ricezione, il modulo deve memorizzare i byte ricevuti in un buffer dedicato.

### FR-024 — Dimensione massima del buffer

Il buffer di ricezione deve essere dimensionato per contenere almeno il massimo frame previsto dal protocollo del sensore.

Il requisito dovrebbe specificare:

> `RX_BUFFER_SIZE >= MAX_FRAME_SIZE`

dove `MAX_FRAME_SIZE` deve essere definito sulla base della specifica del sensore.

### FR-025 — Rilevamento della fine del frame

Il modulo deve determinare quando tutti i byte del frame sono stati ricevuti utilizzando i criteri definiti dal protocollo del sensore.

Questo è importante: eviterei di scrivere semplicemente "attendere che tutti i bytes siano arrivati", perché devi definire **come** il modulo lo determina.

Può essere, ad esempio:

* lunghezza contenuta nel frame;
* numero di byte atteso;
* timeout tra due byte;
* carattere/firma di terminazione;
* combinazione di questi metodi.

---

# 5. Validazione del frame

## 5.1 Verifica integrità

### FR-030 — Validazione della lunghezza

Il modulo deve verificare che la lunghezza del frame ricevuto sia compatibile con un messaggio valido.

### FR-031 — Validazione della struttura

Il modulo deve verificare che i campi del frame siano conformi al formato previsto dal protocollo del sensore.

### FR-032 — Calcolo CRC

Il modulo deve calcolare il CRC del frame ricevuto utilizzando l'algoritmo specificato dal protocollo del sensore.

### FR-033 — Verifica CRC

Il modulo deve confrontare il CRC calcolato con il CRC ricevuto.

### FR-034 — Accettazione del frame

Il modulo deve considerare il frame **valido** solamente se tutte le verifiche previste hanno esito positivo.

### FR-035 — Aggiornamento del dato

Quando viene ricevuto un frame valido, il modulo deve estrarre il valore di concentrazione di ozono e aggiornare il dato memorizzato.

---

# 6. Gestione del dato

Questa parte manca nella tua procedura originale, ma secondo me è fondamentale.

### FR-040 — Memorizzazione dell'ultima misura valida

Il modulo deve conservare l'ultima misura di ozono ricevuta e validata correttamente.

### FR-041 — Timestamp / age del dato

Il modulo dovrebbe mantenere un'informazione relativa all'età dell'ultima misura valida.

Ad esempio:

```text
last_valid_measurement_timestamp
```

oppure:

```text
measurement_age
```

Questo è molto utile per distinguere:

> "il valore è 10 ppm"

da:

> "il valore 10 ppm è stato ricevuto 30 secondi fa e da allora il sensore non comunica più".

### FR-042 — Validità della misura

Il modulo deve mantenere uno stato di validità della misura, ad esempio:

```text
VALID
INVALID
NOT_AVAILABLE
STALE
```

I nomi effettivi possono essere definiti successivamente.

---

# 7. Comunicazione con il CORE

Questa parte la strutturerei in maniera leggermente diversa dalla tua.

### FR-050 — Attesa delle richieste Modbus

Il modulo deve mantenere RS485-2 in modalità ricezione quando non sta trasmettendo una risposta.

### FR-051 — Ricezione della richiesta Modbus

Il modulo deve ricevere dal CORE le richieste Modbus indirizzate al proprio slave address.

### FR-052 — Validazione della richiesta Modbus

Il modulo deve verificare che la richiesta ricevuta:

* sia indirizzata al modulo;
* abbia un function code supportato;
* abbia parametri validi;
* abbia CRC corretto;
* abbia una lunghezza valida.

### FR-053 — Identificazione della richiesta di misura

Quando il CORE richiede il valore del sensore, il modulo deve recuperare l'ultima misura valida disponibile.

### FR-054 — Preparazione della risposta

Il modulo deve preparare una risposta Modbus contenente:

* valore della concentrazione di ozono;
* eventuale stato di validità;
* eventuali informazioni diagnostiche previste dall'interfaccia.

### FR-055 — Calcolo CRC della risposta

Il modulo deve calcolare il CRC della risposta Modbus secondo le specifiche del protocollo Modbus utilizzato.

### FR-056 — Trasmissione della risposta

Il modulo deve commutare RS485-2 in trasmissione e inviare la risposta al CORE.

### FR-057 — Fine trasmissione

Al termine della trasmissione, il modulo deve completare la gestione della periferica RS485 e riportare l'interfaccia nello stato di ricezione.

### FR-058 — Disponibilità del modulo

Il modulo deve essere nuovamente pronto a ricevere una richiesta Modbus successiva.

---

# 8. Una cosa importante: il dato che mandi al CORE

Qui ti consiglio fortemente di **non limitarti a trasferire "i dati del buffer"**.

Il buffer del sensore è un dettaglio interno del modulo.

Verso il CORE dovresti definire una vera **interfaccia dati**.

Per esempio:

| Registro | Descrizione                  |
| -------- | ---------------------------- |
| 0x0000   | Ozono                        |
| 0x0001   | Stato misura                 |
| 0x0002   | Age misura                   |
| 0x0003   | Error status                 |
| 0x0004   | Sensor communication counter |
| 0x0005   | CRC error counter            |

Naturalmente gli indirizzi sono solo esempi.

Questo rende il sistema molto più robusto e indipendente dal protocollo interno del sensore.

---

# 9. Eccezioni

Questa è probabilmente la parte più importante per il tuo documento.

Io costruirei una **tabella delle eccezioni**, invece di inserirle tutte dentro la procedura nominale.

## 9.1 Eccezioni di inizializzazione

### EX-001 — Errore inizializzazione RS485-1

Se RS485-1 non può essere inizializzata correttamente, il modulo deve:

1. impostare lo stato della comunicazione sensore come `ERROR`;
2. registrare l'errore;
3. tentare, se previsto, una reinizializzazione;
4. continuare a mantenere disponibile la comunicazione con il CORE, se tecnicamente possibile.

### EX-002 — Errore inizializzazione RS485-2

Se RS485-2 non può essere inizializzata, il modulo deve:

1. impostare lo stato della comunicazione CORE come `ERROR`;
2. registrare l'errore;
3. tentare la reinizializzazione secondo la strategia definita.

---

# 10. Eccezioni durante la ricezione del sensore

### EX-010 — Frame troppo corto

Se il frame ricevuto contiene meno byte del minimo previsto, il modulo deve scartare il frame.

### EX-011 — Frame troppo lungo

Se il numero di byte ricevuti supera la dimensione massima prevista:

* il modulo deve interrompere la ricezione del frame;
* scartare il frame;
* registrare un errore di overflow/frame length.

### EX-012 — Timeout ricezione

Se durante la ricezione trascorre un intervallo superiore al timeout configurato senza ricevere il byte successivo atteso, il modulo deve considerare il frame incompleto e scartarlo.

### EX-013 — Overflow del buffer

Se il buffer raggiunge la propria capacità massima prima della conclusione del frame, il modulo deve:

* interrompere la memorizzazione;
* scartare il frame;
* registrare l'errore;
* ripristinare il buffer per la ricezione del frame successivo.

### EX-014 — Frame non riconosciuto

Se il frame non rispetta la struttura prevista dal protocollo del sensore, il modulo deve scartarlo.

### EX-015 — CRC errato

Se il CRC calcolato non corrisponde al CRC ricevuto, il modulo deve:

* considerare il frame non valido;
* non aggiornare l'ultima misura valida;
* incrementare il contatore degli errori CRC;
* attendere il frame successivo.

Questo requisito è particolarmente importante:

> **Un dato con CRC errato non deve mai sostituire l'ultima misura valida.**

---

# 11. Perdita di comunicazione con il sensore

Questa è un'altra eccezione che metterei esplicitamente.

### EX-020 — Nessun dato dal sensore

Se non viene ricevuto alcun frame valido dal sensore entro il timeout configurato, il modulo deve impostare lo stato della comunicazione sensore a `NOT_AVAILABLE` o equivalente.

### EX-021 — Sensore non responsivo

Se il protocollo prevede richieste dal modulo al sensore e il sensore non risponde per N tentativi consecutivi, il modulo deve considerare il sensore non disponibile.

### EX-022 — Misura obsoleta

Se l'ultima misura valida supera il tempo massimo di validità configurato:

```text
measurement_age > MAX_MEASUREMENT_AGE
```

il modulo non deve presentare la misura come valida.

Questa distinzione è molto importante per un sistema industriale.

---

# 12. Eccezioni della comunicazione Modbus

### EX-030 — Richiesta Modbus con CRC errato

Il modulo deve ignorare la richiesta e non trasmettere una risposta.

### EX-031 — Indirizzo Modbus errato

Se la richiesta non è indirizzata al modulo, il modulo non deve rispondere.

### EX-032 — Function code non supportato

Il modulo deve rispondere secondo il meccanismo di exception response previsto da Modbus.

### EX-033 — Registro non valido

Se il CORE richiede un registro non implementato, il modulo deve generare la relativa eccezione Modbus prevista.

### EX-034 — Richiesta Modbus incompleta

Se il frame non viene completato entro il timeout previsto, il modulo deve scartare il frame.

### EX-035 — Richiesta Modbus troppo lunga

Il modulo deve scartare la richiesta e registrare l'errore.

---

# 13. Problemi durante la trasmissione al CORE

### EX-040 — Errore durante la trasmissione

Se viene rilevato un errore hardware durante la trasmissione RS485, il modulo deve:

* interrompere la trasmissione, se necessario;
* riportare l'interfaccia nello stato definito;
* registrare l'errore;
* rendersi nuovamente disponibile alla ricezione quando possibile.

### EX-041 — Timeout fine trasmissione

Il modulo deve rilevare il mancato completamento della trasmissione entro il timeout previsto.

### EX-042 — Impossibilità di ritornare in ricezione

Se il driver RS485 non può essere riportato correttamente in modalità ricezione, il modulo deve segnalare un errore di comunicazione e tentare il recovery previsto.

---

# 14. Richieste Modbus consecutive

Questa situazione va specificata.

### EX-050 — Ricezione di una nuova richiesta durante la trasmissione

Se il CORE invia una nuova richiesta mentre il modulo sta ancora trasmettendo una risposta precedente, il comportamento deve essere definito.

Per esempio:

> Il modulo deve ignorare i dati ricevuti durante la trasmissione e processare la richiesta successiva una volta completata la trasmissione corrente.

Oppure puoi definire una gestione più sofisticata.

L'importante è **non lasciare questo comportamento implicito**.

---

# 15. Errori simultanei

Anche questo è spesso dimenticato.

Per esempio:

```text
sensore → frame CRC errato
CORE → richiesta Modbus
```

Il modulo deve comunque poter rispondere al CORE con:

```text
ozono = ultima misura valida
status = SENSOR_DATA_INVALID / STALE
```

anziché mandare semplicemente un valore casuale o zero.

Quindi aggiungerei:

### FR-060 — Indipendenza delle comunicazioni

La gestione della comunicazione con il sensore e la gestione delle richieste provenienti dal CORE devono essere logicamente indipendenti.

Un errore sulla comunicazione con il sensore non deve impedire, salvo condizioni hardware che lo rendano inevitabile, la comunicazione del modulo con il CORE.

---

# 16. Stati del modulo

Per rendere tutto questo molto più chiaro, ti consiglio di aggiungere una **state machine**.

Ad esempio:

```text
                    ┌───────────────┐
                    │ INITIALIZING  │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
              ┌────►│    RUNNING    │◄────┐
              │     └───────┬───────┘     │
              │             │             │
              │             ▼             │
              │     ┌───────────────┐     │
              │     │ SENSOR ERROR  │─────┘
              │     └───────────────┘
              │
              │
              │     ┌───────────────┐
              └─────│ COMM ERROR    │
                    └───────────────┘
```

Ma separerei ulteriormente lo stato del **modulo** dagli stati delle **comunicazioni**.

Per esempio:

```text
Module state:
    INITIALIZATION
    OPERATIONAL
    ERROR

Sensor communication:
    NOT_INITIALIZED
    WAITING_FRAME
    RECEIVING
    VALID_DATA
    INVALID_DATA
    TIMEOUT
    ERROR

Core communication:
    NOT_INITIALIZED
    IDLE
    RECEIVING_REQUEST
    PROCESSING_REQUEST
    TRANSMITTING_RESPONSE
    ERROR
```

Questo è molto più utile quando poi devi fare software, test e diagnostica.

---

# 17. Requisiti temporali

Qui aggiungerei una sezione specifica, perché in un sistema industriale è fondamentale.

Devi definire almeno:

* tempo massimo tra due byte;
* timeout di ricezione frame;
* tempo massimo di elaborazione frame;
* tempo massimo di risposta Modbus;
* tempo massimo di trasmissione;
* tempo massimo per il recovery;
* frequenza minima/massima di aggiornamento del sensore.

Per esempio:

### TR-001 — Timeout ricezione sensore

Il modulo deve considerare incompleto un frame se l'intervallo tra due byte consecutivi supera `T_SENSOR_BYTE_TIMEOUT`.

### TR-002 — Tempo massimo risposta Modbus

Il modulo deve iniziare la trasmissione della risposta Modbus entro `T_MODBUS_RESPONSE_MAX` dalla ricezione completa di una richiesta valida.

I valori numerici li definirei poi sulla base dei datasheet e dei requisiti del CORE.

---

# 18. Requisiti di robustezza

Aggiungerei anche:

### ROB-001 — Recupero dopo frame invalido

La ricezione di un frame invalido non deve richiedere il riavvio del modulo.

### ROB-002 — Recupero dopo timeout

Un timeout di comunicazione non deve richiedere il riavvio del modulo.

### ROB-003 — Persistenza dell'ultima misura

La ricezione di un frame invalido non deve sovrascrivere l'ultima misura valida.

### ROB-004 — Contatori diagnostici

Il modulo deve mantenere contatori per almeno:

* frame ricevuti;
* frame validi;
* frame con CRC errato;
* frame incompleti;
* timeout;
* overflow;
* richieste Modbus valide;
* richieste Modbus invalide.

---

# 19. Un requisito particolarmente importante: cosa deve vedere il CORE

Alla fine, suggerirei che il CORE **non debba interpretare il protocollo ZE27-O3**.

Il modulo deve fare da vera astrazione:

```text
ZE27-O3
   │
   │ protocollo sensore
   ▼
MODULE
   │
   │ valore + stato + diagnostica
   ▼
CORE
   │
   │ Modbus
```

Quindi il CORE dovrebbe poter leggere qualcosa del tipo:

```text
OZONE_VALUE
OZONE_STATUS
SENSOR_STATUS
DATA_AGE
COMMUNICATION_ERROR
```

e non:

```text
raw_byte_0
raw_byte_1
raw_byte_2
raw_byte_3
...
```

a meno che non ci sia una precisa esigenza diagnostica.

---

## Struttura finale che userei nel documento

Per il tuo documento completo, imposterei quindi il capitolo così:

```text
1. Scope
2. System architecture
3. Module interfaces
   3.1 RS485-1 – ZE27-O3
   3.2 RS485-2 – CORE
4. Functional requirements
   4.1 Initialization
   4.2 Sensor communication
   4.3 Frame reception
   4.4 Frame validation
   4.5 Data management
   4.6 Modbus communication
   4.7 Diagnostics
5. Nominal operation sequence
6. Exception handling
   6.1 Initialization errors
   6.2 Sensor communication errors
   6.3 Frame errors
   6.4 CRC errors
   6.5 Timeout errors
   6.6 Buffer errors
   6.7 Modbus errors
   6.8 RS485 transmission errors
   6.9 Recovery
7. Timing requirements
8. Data interface with CORE
9. Diagnostic interface
10. Reset and recovery requirements
11. Electrical/mechanical requirements
12. Environmental requirements
13. Verification and test requirements
```

**Una modifica concettuale che farei subito alla tua procedura originale:** invece di descriverla come una singola sequenza lineare

> ricevi sensore → valida → aspetta CORE → trasmetti → ricomincia

la descriverei come **due flussi concorrenti**:

```text
                 ┌─────────────────────────┐
                 │        MODULE           │
                 │                         │
ZE27-O3 ─RS485-1─►  Acquire → Validate     │
                 │              │          │
                 │              ▼          │
                 │       Last Valid Data   │
                 │              │          │
CORE ◄──RS485-2──┤  Modbus Request/Response │
                 │                         │
                 └─────────────────────────┘
```

Questo ti permette di definire in modo molto più pulito anche tutte le eccezioni.

Se vuoi, nel prossimo passaggio posso trasformare tutto questo in una **vera tabella di requisiti software/firmware**, con colonne tipo **ID | Requirement | Description | Priority | Input | Output | Exception | Verification method**, e costruire una lista abbastanza completa (FR-001… FR-0xx + EX-001… EX-0xx) che puoi praticamente incollare nel documento tecnico.
