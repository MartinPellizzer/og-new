[head]

[/head]

[rev]

Versione, Data, Autore, Descrizione

1.0.0, 2026-07-02, Martin Pellizzer, Versione iniziale

[/rev]

[body]

## Obiettivo

L'obiettivo di questo progetto è quello di creare un sensore a ozono ottico, ovvero utilizzando un LED UVC e un photodiode.

---

## Stato attuale

Al momemnto si sta progettando la "camera di misurazione" del sensore, nonchè si stanno testando i LED UVC e i photodiodes.

Per "camera di misurazione", si intende l'involucro dentro il quale vengono posizionati il LED e il photodiode. Il LED viene posizionato ad una estremità della camera, mentre il photodiode viene posizionato nell'altra estremità. Il LED viene orientato in direzione del photodiode, facendo in modo che la luce del LED colpisca il photodiode nel modo più diretto e lineare possiblile.

Questo camera di misurazione ha un foro di ingesso e uno di uscita. Lo scopo e quello di iniettare ozono nel foro di ingresso, far passare questo ozono all'interno della camera tra il LED e il photodiode, e farlo fuoriuscire attraverso il foro di uscita. In questo modo la luce del LED viene bloccata dall'ozono e il photodiode rileva se c'è presenza di ozono.

Immagine camera di misurazione:

!(C:/og-new/products/modulo_ozono_ottico/modulo_ozono_ottico__v1_0_0/modulo_ozono_ottico__cella_misurazione__v1_0_0/docs/input_assets/img_0000.jpg)

---

Immagine foro entrata (e uscita) della celle di misurazione (montato supra e sotto la cella):

!(C:/og-new/products/modulo_ozono_ottico/modulo_ozono_ottico__v1_0_0/modulo_ozono_ottico__cella_misurazione__v1_0_0/docs/input_assets/img_0001.jpg)

---

## Attività completate

Le attività completate sono le seguenti:

- creata la camera di misurazione (1cm L)
- testai il LED UVC e il photodiode elettricamente
- creato il software test per la lettura del segnale

---

## Problemi riscontrati

La camera di misurazione è troppo "corta" (lunghezza 1cm). Purtroppo il LED emette poca luce e questa luce non viene rilevata dal photodiode se la lunghezza è superiore a 1cm. Sebbene a questa lungezza si riesce a rilevare un calo di luce UVC tramite passaggio di ozono (e quindi dimostrare il funzionamento del principio di rilevamento ottico), tale calo non è sufficente per una lettura precisa dei PPM di ozono.

Inoltre, viene usato un alimentatore da 12V DC per alimentare il LED, perchè il forward voltage del LED è superiore a 5V, quindi un alimentazione a 5V non basta. Però, alimentare a 12V genera troppo calore sulla resistenza utilizzanda per limitare la corrente.

Infine, la lettura del photodiode non è completamente stabile, ma aumenta lentamente nel corso del tempo. Si ipotizza che questo sia dovuto all'aumento di temperatura del LED.

---

## Decisioni progettuali

A seguito dei problemi riscontrati nel punto precedente, si ritiene necessario testare led UVC più potenti, per fare in modo di aumentare la lunghezza della camera di misurazione (target 5cm).

Inoltre si vuole provare ad alimentare il led UVC in corrente-costante, invece che voltaggio-costante, per provare a tenere un livello di illumiazione fisso. In aggiunta, si vuole provare a avere una riduzione termica con l'aggiunta di un dissipatore.

Infine, se si riesce ad aumentare la lunghezza della camera di misurazione, si vuole posizionare i fori di entrata e uscita dell'ozono sullo stesso lato. 

Per quanto riguarda il photodiode, al momento si tiene quello che è già presente, anche se non optimale.

---

## Prossimi passi

Si decide di proseguire come segue:

- Progettare un alimentatore di corrente-costante, da usare per alimentare il LED e verificare che produca una quantità di luce fissa.
- Comprare diversi campioni di LED UVC su alibaba, ognuno con una potenza diversa, dai 20 mA (come quello usato attuale) ai 100 mA e oltre.
- In alternaiva, resta l'opzione di usare i LED di LCSC (integrati in schede da progettare), ma da una prima ricerca sembra che abbiano LED UVC solo dai 260 nm in su (non ottimale per l'ozono, ma potrebbero comumnque bastare se si trovano ad alta potenza).

---

## Idee future

In futuro sarà necessario trovare anche un photodiode ottimizzato per leggere UVC a 254 nm (se reperibile a basso costo), visto che quello attuale legge principalmente UVA-UVB. 

Inoltre, si valuterà un materiale riflettivo per UVC da utilizzare all'interno della camera di misurazione per aiutare il sengale luminoso ad arrivare al photodiode. Questo va fatto solo se necessario, in quanto aumenta la complessita progettuale di molto.