Buongiorno,
abbiamo verificato le specifiche di comunicazione proposte e confermiamo che sono compatibili con il nostro PLC Schneider Modicon TM241.
Possiamo pertanto confermare:
Protocollo Modbus RTU, sensore Slave
Slave ID 23
Velocità 9600 baud, formato 8N1
Funzione FC04 (Read Input Registers)
Lettura di un registro a 16 bit unsigned
Valore restituito in ppb, campo 0–10000
Interfaccia RS485 a 2 fili

Per quanto riguarda l'indirizzamento, chiediamo conferma che il registro 30001 corrisponda all'indirizzo Modbus zero-based 0x0000 nella richiesta FC04.
La resistenza di terminazione interna da 120 Ω non rappresenta un problema, prevedendo il collegamento del sensore all'estremità della linea RS485.

Prima di procedere, avremmo inoltre bisogno di conoscere:
- Risoluzione effettiva, accuratezza e ripetibilità della misura.
- Tempo di risposta (T90) e tempo di stabilizzazione dopo l'accensione.
- Comportamento in caso di guasto della cella, misura non valida o concentrazione superiore a 10000 ppb.
- Eventuali registri Modbus aggiuntivi per diagnostica e stato del sensore.
- Vita utile prevista della cella e modalità di calibrazione periodica.
- Tensione di alimentazione e assorbimento del dispositivo.
- Restiamo in attesa delle informazioni per completare la verifica tecnica.

Per quanto riguarda l'indirizzamento, chiediamo conferma che il registro 30001 corrisponda all'indirizzo Modbus zero-based 0x0000 nella richiesta FC04.
- Confermo che il registro 30001 corrisponda all'indirizzo Modbus zero-based 0x0000.

Risoluzione effettiva, accuratezza e ripetibilità della misura.
- Risoluzione di 10 ppb. Può restituire valori come 110, 120, 130 ppb. NOTA: In realtà, la cella del sensore rileva/comunica i dati con risoluzione di 1 ppb (es. 101 ppb), ma il costruttore esplicitamente scrive nel manuale tecnico che la risoluzione effettiva è di 10 ppb, quindi consigliamo di seguire le specifiche ufficial è considerare come risoluzione effettiva 10 ppb. 
- L'accuratezza non viene specificata dal fornitore della cella. Per nostra esperienza, questa cellula ha una buona accuratezza, almeno alla pari degli altri sensori di tipo elettrochimico che si trovano sul mercato.
- Neanche la ripetibilità viene fornita dal produttore purtroppo. Al contrario della accuratezza, non siamo in grado di confermarvi se la ripetibilità è soddisfacente per voi. Di solito in ambienti grandi riusciamo a confermare una buona ripetibilità. In ambienti piccoli è più complicato, perchè c'è più variazioni del flusso d'aria è le letture del sensore sono molto più soggette a variazioni.

Tempo di risposta (T90) e tempo di stabilizzazione dopo l'accensione:
- Il tempo di risposta è ≤90s (dato ufficiale del fornitore).
- Il tempo di stabilizzazione dopo l'accensione è ≤3min (dato ufficiale del fornitore).

Comportamento in caso di guasto della cella, misura non valida o concentrazione superiore a 10000 ppb.
- In caso di guasto, il sensore vi comunica una concentrazione di 10001 ppb. Per guasto, noi intendiamo che la cella del sensore non riesce a comunicare il valore di ozono al nostro microcontrollore per un tempo maggiore di 5 secondi.

Eventuali registri Modbus aggiuntivi per diagnostica e stato del sensore.
- Al momento non ci sono altri registri aggiuntivi per lo stato del sensore. Il sensore è da considerarsi in stato "ok" se il valore letto è tra 0 e 10000 ppb e "errore" se il valore letto è maggiore di 10000 ppb (10001).

Vita utile prevista della cella e modalità di calibrazione periodica.
- La vita utile della cella del sensore è 2 anni (dato ufficiale del fornitore).
- Il sensore non dispone di una modalità di calibrazione periodica. Va sostituita la cella al termine della sua vita utile.

Tensione di alimentazione e assorbimento del dispositivo.
- La tensione di alimentazione è 12V.
- L'assorbimento è circa 0.5A (prevalentemente durante la trasmissione dati RS485). 