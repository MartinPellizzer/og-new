[head]

[/head]

[rev]

Versione, Data, Autore, Descrizione

1.0.0, 2026-07-02, Martin Pellizzer, Versione iniziale

[/rev]

[body]

# Registro di sviluppo

## Obiettivo

L'obiettivo di questo progetto è quello di creare un sensore a ozono ottico, ovvero utilizzando un LED UVC e un photodiode.

---

## Stato attuale

Al momemnto si sta progettando la "camera di misurazione" del sensore, nonchè si stanno testando i LED UVC e i photodiodes.

Per "camera di misurazione", si intende l'involucro dentro il quale vnegono posizionati il LED e il photodiode. Il LED viene posizionato ad una estremità della camera, mentre il photodiode viene posizionato nell'altra estremità. Il LED viene orientato in direzione del photodiode, facendo in modo che la luce del LED colpisca il photodiode nel modo più diretto e lineare possiblile.

Questo camera di misurazione ha un foro di ingesso e uno di uscita. Lo scopo e quello di iniettare ozono nel foro di ingresso, far passare questo ozono all'interno della camera tra il LED e il photodiode, e farlo fuoriuscire attraverso il foro di uscita. In questo modo il la luce del LED viene bloccata dall'ozono e il photodiode rileva se c'è presenza di ozono.

---

## Attività completate

Le attività completate sono le seguenti:

- creazione della prima camera di misurazione
- creazione del primo software test per verificare il funzionamento dei componenti

---

## Problemi riscontrati

La camera di misurazione è troppo "corta" (lunghezza 1cm). Purtroppo il LED emette poca luce e questa luce non viene rilevata dal photodiode se la lunghezza è superiore a 1cm. Sebbene a questa lungezza si riesce a rilevare un calo di luce UVC tramite passaggio di ozono (e quindi dimostrare il funzionamento del principio di rilevamento ottico), si ritiene che tale calo non sia sufficente ad una lettura precisa dei PPM di ozono.

---

## Decisioni progettuali

A seguito dei problemi riscontrati nel punto precedente, si ritiene necessario testare led UVC più potenti, per fare in modo di aumentare la lunghezza della camera di misurazione (target 5cm).

Inoltre si vuole provare ad alimentare il led UVC in corrente-costante, invece che voltaggio-costante, per provare a tenere un livello fisso di illumiazione e una riduzione termica.

Infine, se si riesce ad aumentare la lunghezza della camera di misurazione, si vuole posizionare i fori di entrata e uscita dell'ozono sullo stesso lato. 

Per quanto riguarda il photodiode, al momento si tiene quello che è già presente, anche se non optimale.

---

## Prossimi passi

Creare delle schede campione da aquistare su JLCPCB, per testare diversi LED UVC presenti sul catalogo di LCSC, nella speranza di trovarne uno ottimale da posizionare a 5cm di disatanza dal photodiode.

---

## Idee future

In futuro sarà necessario trovare anche un photodiode ottimizzato per leggere UVC (se reperibile a basso costo), visto che quello attuale legge principalmente UVA-UVB. 

Inoltre, si valuterà di materiale riflettivo per UVC da utilizzare all'interno della camera di misurazione per aiutare il sengale luminoso ad arrivare al photodiode. Questo va fatto solo se necessario, in quanto aumenta la complessita progettuale di molto.