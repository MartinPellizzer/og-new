import os
import json
from fpdf import FPDF

with open("data.json", "r", encoding="utf-8") as f: data = json.load(f)

def header_insert():
    # header
    pdf.image(f'logo.jpg', x=10, y=8, w=1182//20)
    pdf.ln(10)
    pdf.cell(0, 5, 'Ozonogroup s.r.l.', ln=True, align="R")
    pdf.cell(0, 5, '''Via dell'Artigianato, 23, 31011 Asolo TV''', ln=True, align="R")
    pdf.cell(0, 5, '''+39 0423 952833''', ln=True, align="R")
    pdf.ln(10)
    pdf.set_draw_color(0, 0, 0)
    pdf.cell(0, 0, "", ln=True, border="T")
    pdf.ln(10)




dati = []
# dati.append([
#     'Versione', 
#     data['versioni'][0]['versione'], 
#     data['versioni'][1]['versione'], 
#     data['versioni'][2]['versione'], 
#     data['versioni'][3]['versione'], 
#     data['versioni'][4]['versione'], 
#     data['versioni'][5]['versione'],
# ])
# dati.append([
#     'Categoria', 
#     data['versioni'][0]['categoria'], 
#     data['versioni'][1]['categoria'], 
#     data['versioni'][2]['categoria'], 
#     data['versioni'][3]['categoria'], 
#     data['versioni'][4]['categoria'], 
#     data['versioni'][5]['categoria'],
# ])
# dati.append([
#     'Dimensioni (mm)', 
#     data['versioni'][0]['dimensioni'], 
#     data['versioni'][1]['dimensioni'], 
#     data['versioni'][2]['dimensioni'], 
#     data['versioni'][3]['dimensioni'], 
#     data['versioni'][4]['dimensioni'], 
#     data['versioni'][5]['dimensioni'],
# ])
# dati.append([
#     'Peso (Kg)', 
#     data['versioni'][0]['peso'], 
#     data['versioni'][1]['peso'], 
#     data['versioni'][2]['peso'], 
#     data['versioni'][3]['peso'], 
#     data['versioni'][4]['peso'], 
#     data['versioni'][5]['peso'],
# ])
# dati.append([
#     'Potenza (W)', 
#     data['versioni'][0]['potenza'], 
#     data['versioni'][1]['potenza'], 
#     data['versioni'][2]['potenza'], 
#     data['versioni'][3]['potenza'], 
#     data['versioni'][4]['potenza'], 
#     data['versioni'][5]['potenza'],
# ])
# dati.append([
#     'Tensione (V)', 
#     data['versioni'][0]['tensione'], 
#     data['versioni'][1]['tensione'], 
#     data['versioni'][2]['tensione'], 
#     data['versioni'][3]['tensione'], 
#     data['versioni'][4]['tensione'], 
#     data['versioni'][5]['tensione'],
# ])
# dati.append([
#     'Frequenza (Hz)', 
#     data['versioni'][0]['frequenza'], 
#     data['versioni'][1]['frequenza'], 
#     data['versioni'][2]['frequenza'], 
#     data['versioni'][3]['frequenza'], 
#     data['versioni'][4]['frequenza'], 
#     data['versioni'][5]['frequenza'],
# ])
# dati.append([
#     'Fusibile (A)',
#     data['versioni'][0]['fusibile'], 
#     data['versioni'][1]['fusibile'], 
#     data['versioni'][2]['fusibile'], 
#     data['versioni'][3]['fusibile'], 
#     data['versioni'][4]['fusibile'], 
#     data['versioni'][5]['fusibile'],
# ])
# dati.append([
#     'Flusso ozono (LPM)',
#     data['versioni'][0]['flusso_uscita_ozono'], 
#     data['versioni'][1]['flusso_uscita_ozono'], 
#     data['versioni'][2]['flusso_uscita_ozono'], 
#     data['versioni'][3]['flusso_uscita_ozono'], 
#     data['versioni'][4]['flusso_uscita_ozono'], 
#     data['versioni'][5]['flusso_uscita_ozono'],
# ])
# dati.append([
#     'Livello ozono (Mg/L)',
#     data['versioni'][0]['concentrazione_ozono'], 
#     data['versioni'][1]['concentrazione_ozono'], 
#     data['versioni'][2]['concentrazione_ozono'], 
#     data['versioni'][3]['concentrazione_ozono'], 
#     data['versioni'][4]['concentrazione_ozono'], 
#     data['versioni'][5]['concentrazione_ozono'],
# ])
# dati.append([
#     'Ozono nominale (g/h)',
#     data['versioni'][0]['produzione_nominale'], 
#     data['versioni'][1]['produzione_nominale'], 
#     data['versioni'][2]['produzione_nominale'], 
#     data['versioni'][3]['produzione_nominale'], 
#     data['versioni'][4]['produzione_nominale'], 
#     data['versioni'][5]['produzione_nominale'],
# ])
# dati.append([
#     'Ozono reale (g/h)',
#     data['versioni'][0]['produzione_reale'], 
#     data['versioni'][1]['produzione_reale'], 
#     data['versioni'][2]['produzione_reale'], 
#     data['versioni'][3]['produzione_reale'], 
#     data['versioni'][4]['produzione_reale'], 
#     data['versioni'][5]['produzione_reale'],
# ])
# dati.append([
#     'Diametro diffusore',
#     data['versioni'][0]['diffusore_ozono'], 
#     data['versioni'][1]['diffusore_ozono'], 
#     data['versioni'][2]['diffusore_ozono'], 
#     data['versioni'][3]['diffusore_ozono'], 
#     data['versioni'][4]['diffusore_ozono'], 
#     data['versioni'][5]['diffusore_ozono'],
# ])
# dati.append([
#     'Timer manuale (minuti)',
#     data['versioni'][0]['timer_manuale'], 
#     data['versioni'][1]['timer_manuale'], 
#     data['versioni'][2]['timer_manuale'], 
#     data['versioni'][3]['timer_manuale'], 
#     data['versioni'][4]['timer_manuale'], 
#     data['versioni'][5]['timer_manuale'],
# ])

for prodotto in data['prodotti']:
    prodotto_image_src = prodotto['image_src']
    prodotto_name = prodotto['name']
    pdf = FPDF()
    pdf.set_font("Arial", size=10)

    pdf.add_page()
    header_insert()

    # Titolo
    font_size = 30
    pdf.set_font("Arial", "B", size=font_size)
    pdf.cell(0, font_size//2, prodotto_name, ln=True, align="C")
    pdf.set_font("Arial", size=10)
    pdf.ln(10)  # Spazio dopo il titolo

    # Dati della tabella
    intestazioni = ["Descrizione", "Valore", "Valore", "Valore", "Valore", "Valore", "Valore"]

    pdf.image(prodotto_image_src, w=100, x=210//2 - 100//2)

    for item in prodotto['versioni']:
        print(prodotto)
        intestazioni = ['Parametro', 'Valore',]
        dati = [
            ['Codice', item['codice'],],
            ['Modello', item['versione'],],
            ['Produzione nominale', item['produzione_nominale'],],
            ['Peso', item['peso'],],
            ['Dimensioni', item['dimensioni'],],
            ['Alimentazione', item['alimentazione'],],
            ['Potenza', item['potenza'],],
        ]

        pdf.add_page()
        header_insert()
        font_size = 30
        pdf.set_font("Arial", "B", size=font_size)
        pdf.cell(0, font_size//2, f"Modello: {item['versione']}", ln=True, align="C")
        pdf.ln(10)  # Spazio dopo il titolo
        
        # Larghezza delle colonne (puoi regolarle)
        cell_valore_width = 95
        # larghezze = [40, cell_valore_width, cell_valore_width, cell_valore_width, cell_valore_width, cell_valore_width, cell_valore_width]
        larghezze = [cell_valore_width, cell_valore_width]

        # --- DISEGNA LA TABELLA ---

        # Intestazioni
        font_size = 12
        pdf.set_font("Arial", "B", size=font_size)
        for i, header in enumerate(intestazioni):
            pdf.cell(larghezze[i], font_size, f'  {header}  ', border=1, align="L")
        pdf.set_font("Arial", size=12)
        pdf.ln()

        # Righe dati
        for riga in dati:
            for i, cella in enumerate(riga):
                pdf.cell(larghezze[i], font_size, f'  {cella}  ', border=1, align="L")
            pdf.ln()

    # Salvataggio
    prodotto_name = prodotto['name']
    prodotto_slug = prodotto_name.lower().strip().replace(' ', '-')
    output_filepath = f'{prodotto_slug}-scheda-tecnica.pdf'
    pdf.output(output_filepath)
    print(f"PDF creato: {output_filepath}")

os.startfile(output_filepath)
