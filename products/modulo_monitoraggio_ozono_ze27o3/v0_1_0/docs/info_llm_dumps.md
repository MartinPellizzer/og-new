# Cosa deve fornire il modulo a CORE, esattamente?

Quando dico che il modulo deve fornire a CORE “l’ultima misura di ozono validata, insieme a stato di validità, informazioni sulla freschezza e diagnostica essenziale”, intendo che CORE non deve ricevere soltanto un numero, per esempio `0,08 ppm`.

Deve ricevere anche le informazioni necessarie per capire se quel numero è attendibile, quanto è recente e se ci sono problemi con il sensore o con il modulo.

Vediamo ogni elemento separatamente, usando il tuo sistema con il sensore ZE27-O3, il modulo di espansione e CORE.

## 1. Ultima misura di ozono validata

![ZE27-O3 Electrochemical Ozone O3 Sensor Module with Pin for Disinfection Cabinets Ozone Monitoring 010ppm – Alexnld.com](https://images.openai.com/static-rsc-4/uPFWpVvKSp87e48I0vduumSifKNbZziOOfgVSY_jnvaG_ZGDywfhv6SF6DdY4ZFKAJ0zsZOzuEkdAOqxGmigwiR1yDrm2M19bVajwBVnUIpjQPYrnC6knhjFaJHNa7LhLUROZ9KlohLwefMaA-oZkIDc1ANUhhLIqNvKsxSsMCM?purpose=inline)

## Il valore misurato

È la concentrazione di ozono ricavata dall'ultima risposta del sensore che il modulo ha verificato e accettato come valida.

### Esempio

Il sensore invia una misura di `0,08 ppm`.

Il modulo verifica che:

* Il frame ricevuto sia completo e correttamente strutturato.

* Il CRC sia corretto.

* Il valore sia decodificato correttamente.

* Il valore rispetti i controlli di validità definiti.

Se tutti i controlli sono superati, il modulo memorizza `0,08 ppm` come ultima misura valida.

Perché è importante? Se arriva successivamente un frame corrotto, il modulo non deve sovrascrivere `0,08 ppm` con un dato non valido.

|
Evento

|

Valore memorizzato

|
| --- | --- |
|

Arriva una misura valida

|

`0,08 ppm`

|
|

Arriva un'altra misura valida

|

`0,10 ppm`

|
|

Arriva un frame con CRC errato

|

`0,10 ppm`

|
|

Il sensore non risponde

|

`0,10 ppm`

|

Il valore memorizzato rimane l'ultima misura valida. Questo, però, non significa che sia ancora recente o utilizzabile: per quello servono le informazioni successive.

## 2. Stato di validità (Validity Status)

Lo stato di validità dice a CORE se il valore numerico può essere considerato una misura valida secondo le regole del sistema.

Non è il valore dell'ozono: è un'informazione separata che accompagna il valore.


### Esempio di stato di validità

|
Stato

|

Significato

|

Esempio

|
| --- | --- | --- |
|

`VALID`

|

È disponibile una misura che ha superato i controlli.

|

`0,08 ppm`

|
|

`NO_VALID_MEASUREMENT`

|

Il modulo non ha ancora acquisito una misura valida.

|

Dopo l'accensione

|
|

`INVALID`

|

La misura corrente non può essere accettata come valida.

|

Il sensore segnala un errore

|

La distinzione tra `NO_VALID_MEASUREMENT` e `INVALID` può essere implementata in modi diversi: ciò che conta è definire chiaramente la semantica.

Esempio pratico: il modulo si accende, ma il sensore non ha ancora risposto correttamente. CORE legge il valore numerico `0` e lo stato `NO_VALID_MEASUREMENT`.

CORE non deve interpretare quel valore come una concentrazione di ozono pari a zero.

### Perché non basta il valore numerico?

Perché un valore pari a zero potrebbe significare:

* Una misura reale di zero, se il sensore può misurarla.

* Un valore iniziale del firmware.

* Un dato non ancora acquisito.

* Un valore usato per rappresentare un errore.

Lo stato di validità elimina questa ambiguità.

## 3. Informazioni sulla freschezza (Freshness Information)

La freschezza indica a CORE quanto tempo è trascorso dall'acquisizione dell'ultima misura valida.

Una misura può essere stata valida quando è stata acquisita, ma diventare troppo vecchia per essere utilizzata.

Per questo progetto, abbiamo ipotizzato una soglia di 5 secondi. È un valore di esempio da confermare con i responsabili del sistema.

### Esempio

Il modulo acquisisce una misura valida di `0,08 ppm` alle 10:00:00.

|
Ora

|

Età della misura

|

Stato di freschezza

|
| --- | --- | --- |
|

10:00:01

|

1 s

|

`FRESH`

|
|

10:00:03

|

3 s

|

`FRESH`

|
|

10:00:05

|

5 s

|

Al limite

|
|

10:00:06

|

6 s

|

`STALE`

|

Se la soglia è 5 secondi, una misura con più di 5 secondi di età viene dichiarata obsoleta.

### Quali informazioni può fornire il modulo?

Due possibilità sono:

* Età della misura (`DATA_AGE`): per esempio, `3 s`.

* Stato di freschezza (`FRESHNESS_STATUS`): per esempio, `FRESH` oppure `STALE`.

Il modulo potrebbe fornire entrambi, oppure soltanto l'età, lasciando a CORE il compito di confrontarla con la soglia.

L'età dovrebbe essere calcolata a partire dall'acquisizione della misura valida, non dal momento in cui CORE la legge.

Nota importante: la freschezza e la validità sono due concetti distinti. Una misura può essere stata validata correttamente, ma essere ormai obsoleta.

## 4. Diagnostica essenziale (Essential Diagnostics)

La diagnostica consente a CORE di capire se il modulo e il sensore stanno funzionando correttamente e, in caso contrario, quale problema si è verificato.

Non significa necessariamente trasferire tutti i dettagli interni del firmware. Significa esporre le informazioni utili per identificare e gestire i guasti.

### Esempi di informazioni diagnostiche

|
Informazione

|

Esempio

|

A cosa serve

|
| --- | --- | --- |
|

Stato comunicazione sensore

|

`SENSOR_COMM_OK`

|

Indica se il sensore risponde correttamente.

|
|

Stato generale del modulo

|

`MODULE_OK`

|

Indica se il modulo è operativo.

|
|

Errore di comunicazione

|

`SENSOR_TIMEOUT`

|

Indica che il sensore non ha risposto entro il timeout.

|
|

Errori CRC

|

`CRC_ERROR_COUNT = 3`

|

Indica quanti frame sono stati scartati per CRC errato.

|
|

Frame non validi

|

`INVALID_FRAME_COUNT = 2`

|

Aiuta a identificare problemi nei dati ricevuti.

|
|

Identificazione firmware

|

`FW_VERSION = 1.2.0`

|

Consente di identificare la versione software installata.

|

Queste sono informazioni proposte, non un registro Modbus già definito.

### Esempio di problema

Il sensore smette di rispondere.

Il modulo potrebbe fornire a CORE:

* Ultima misura valida: `0,08 ppm`

* Stato di validità: `VALID`

* Età della misura: `7 s`

* Stato di freschezza: `STALE`

* Stato comunicazione sensore: `SENSOR_TIMEOUT`

CORE può così distinguere una misura precedentemente valida ma ormai obsoleta da un guasto della comunicazione con il modulo stesso.

# 5. Come si combinano le quattro informazioni?

Immagina che CORE esegua una lettura Modbus e riceva questo insieme di dati:

## Dati del modulo

Dato obsoleto

Misura di ozono

## 0,08 ppm

Validità

VALID

Età della misura

7 secondi

Freschezza

STALE

Comunicazione sensore

TIMEOUT

Interpretazione di CORE

Il valore `0,08 ppm` è stato validato quando è stato acquisito, ma ha superato la soglia di freschezza di 5 secondi. CORE non deve trattarlo come una misura corrente utilizzabile.

Questo esempio mostra perché non è sufficiente trasferire a CORE soltanto il valore numerico.

## 6. Quali dati dovrebbe leggere CORE tramite Modbus?

Una possibile interfaccia logica è questa:

|
Campo

|

Esempio

|

Significato

|
| --- | --- | --- |
|

`OZONE_VALUE`

|

`0,08 ppm`

|

Ultima misura valida memorizzata

|
|

`OZONE_VALIDITY`

|

`VALID`

|

Esito dei controlli di validità

|
|

`OZONE_AGE`

|

`7 s`

|

Età della misura

|
|

`OZONE_FRESHNESS`

|

`STALE`

|

Indica se la misura è ancora recente

|
|

`SENSOR_STATUS`

|

`TIMEOUT`

|

Stato della comunicazione con il sensore

|
|

`MODULE_STATUS`

|

`OK`

|

Stato generale del modulo

|

I nomi sono illustrativi: la mappa registri effettiva deve essere definita durante la progettazione dell'interfaccia.

## 7. La distinzione fondamentale da inserire nei requisiti

Io separerei questi quattro requisiti:

1. Misura: il modulo deve rendere disponibile a CORE l'ultima misura di ozono validata.

2. Validità: il modulo deve indicare esplicitamente se è disponibile una misura valida.

3. Freschezza: il modulo deve fornire l'età della misura, oppure un'indicazione equivalente che permetta a CORE di determinare se è obsoleta.

4. Diagnostica: il modulo deve rendere disponibili informazioni sufficienti a distinguere almeno un errore del sensore da un errore di comunicazione con il modulo.

In sintesi: il valore dice quanto ozono è stato misurato; la validità dice se la misura ha superato i controlli; la freschezza dice quanto è recente; la diagnostica dice se qualcosa non sta funzionando correttamente.
