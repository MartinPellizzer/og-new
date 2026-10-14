| Impostazione              | Valore |
| ------------------ | -------------------------- |
| Protocollo         | Modbus RTU      |
| Ruolo sensore      | Slave        |
| ID sensore   | 23 decimale (0x17 esadecimale)        |
| Baud rate       | 9600 bps    |
| Formato dati         | 8 bits, nessuna parità, 1 stop bit (8N1)      |
| Codice funzione registri di ingresso         | Codice funzione 04 (0x04 / FC04)      |
| Indirizzo iniziale registri di ingresso         | 0x0000 zero-based (30001 concettuale)      |
| Numero di registri da leggere         | 1      |
| Tipo di dato del registro          | Intero senza segno a 16 bit (uint16)     |
| Interfaccia fisica          | RS-485 a 2 fili (A e B)     |
| Valore ricevuto dal sensore          | Da 0 a 10000 ppb     |
| Risoluzione sensore          | 10 ppb     |
| Accuratezza sensore          | Non fornita dal costruttore     |
| Ripetibilità della misura          | Non fornita dal costruttore     |
| Tempo di risposta (T90)          | ≤ 90 s     |
| Tempo di stabilizzazione dopo l'accensione          | ≤ 3 min     |
| Comportamento in caso di guasto della cella          | Il sensore comunica un valore pari a 10001 ppb     |
| Registri Modbus aggiuntivi per diagnostica          | Non presenti     |
| Vita utile della cella del sensore          | 2 anni     |
| Modalità di calibrazione periodica          | Non disponibile     |
| Tensione di alimentazione          | 12 V     |
| Assorbimento del sensore          | 0.5 A     |
