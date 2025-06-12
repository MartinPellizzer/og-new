from datetime import datetime, timedelta
from fpdf import FPDF
import locale

font = f'arial'
text_size = 12
locale.setlocale( locale.LC_ALL, '' )

class PDF(FPDF):
    def header(self):
        invoice_number = 0
        self.image('logo.jpg', 10, 8, 50)
        self.set_font(font, 'B', text_size)

        self.cell(130, 10)
        self.cell(0, 10, f'Offerta #{invoice_number}', ln=1)

        self.set_font(font, '', text_size)
        self.cell(130, 10)
        day = datetime.now().day
        if day < 10: day = '0' + str(day)
        month = datetime.now().month
        if month < 10: month = '0' + str(month)
        year = datetime.now().year
        self.cell(0, 6, f'Data: {day}/{month}/{year}', border=0, ln=1)
        self.cell(130, 10)
        end_date = datetime.now().date() + timedelta(days=30)
        
        day = end_date.day
        if day < 10: day = '0' + str(day)
        month = end_date.month
        if month < 10: month = '0' + str(month)
        year = end_date.year

        self.cell(0, 6, f'Valido fino a: {day}/{month}/{year}', border=0, ln=1)
        self.ln(15)
    
    def footer(self):
        self.set_y(-15)
        self.set_font(font, 'I', 10)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

def generate_pdf():
    business_name = 'Sugherificio Ganau (S.P.A.)'
    business_address_1 = 'Zona Industriale, 07029'
    business_address_2 = 'Tempio Pausania SS'
    business_iva = '??????????????'

    pdf = PDF('P', 'mm', 'Letter')
    pdf.add_font("Arial", "", "./fonts/arial.ttf", uni=True)
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()

    cell_height = 6
    cell_width = 90
    cell_width_divider = 10

    pdf.set_font(font, '', text_size)
    pdf.set_fill_color(255, 255, 255)

    pdf.cell(cell_width, cell_height, 'Fornitore:', border='B', fill=True)
    pdf.cell(cell_width_divider, cell_height, '', fill=True)
    pdf.cell(cell_width, cell_height, 'Cliente:', border='B', fill=True, ln=1)
    pdf.ln(2)

    pdf.cell(cell_width, cell_height, 'Ozonogroup s.r.l.', fill=True)
    pdf.cell(cell_width_divider, cell_height, '', fill=True)
    pdf.cell(cell_width, cell_height, business_name, fill=True, ln=1)

    # address = business_address.split(',')
    # address_1 = address[:2]
    # address_2 = address[2:]

    pdf.cell(cell_width, cell_height, 'Via dell\'Artigianato, 23', fill=True)
    pdf.cell(cell_width_divider, cell_height, '', fill=True)
    pdf.cell(cell_width, cell_height, business_address_1, fill=True, ln=1)

    pdf.cell(cell_width, cell_height, '31011 Asolo TV', fill=True)
    pdf.cell(cell_width_divider, cell_height, '', fill=True)
    pdf.cell(cell_width, cell_height, business_address_2, fill=True, ln=1)
    
    pdf.cell(cell_width, cell_height, 'P.IVA/C.F.: 86334519757', fill=True)
    pdf.cell(cell_width_divider, cell_height, '', fill=True)
    pdf.cell(cell_width, cell_height, f'P.IVA/C.F.: {business_iva}', fill=True, ln=1)
    pdf.ln(10)

    cell_height = 8
    pdf.set_font(font, 'B', text_size)
    pdf.set_fill_color(229, 229, 229)

    cell_width_numdoc = 25
    cell_width_data = 25

    cell_height = 8
    pdf.set_font(font, 'B', text_size)
    pdf.set_fill_color(229, 229, 229)

    cell_width_codice = 35
    cell_width_description = 60
    cell_width_um = 15
    cell_width_qta = 15
    cell_width_valuta = 20
    cell_width_valunit = 15
    cell_width_prezzo = 30
    cell_width_sconti = 20
    cell_width_totale = 35

    pdf.cell(cell_width_qta, cell_height, 'Q.tà', border=1, fill=True)
    pdf.cell(cell_width_codice, cell_height, 'Codice', border=1, fill=True)
    pdf.cell(cell_width_description, cell_height, 'Descrizione', border=1, fill=True)
    pdf.cell(cell_width_prezzo, cell_height, 'Prezzo', border=1, fill=True)
    pdf.cell(cell_width_sconti, cell_height, 'Sconto', border=1, fill=True)
    pdf.cell(cell_width_totale, cell_height, 'Subtotale', border=1, fill=True)
    pdf.ln()

    pdf.set_font(font, '', text_size)
    pdf.set_fill_color(255, 255, 255)

    price_total_num = 0
    discount_total_num = 0

    rows = [
        ['0', 'Aurora', 11000, 10,],
        ['1', 'Sensore', 310, 100,],
        ['2', 'Trasporto', 120, 100,],
        ['3', 'Installazione', 480, 100,],
    ]
    for row in rows:
        row_code_str = row[0]
        row_desc_str = row[1]
        price_num = row[2]
        discount_num = row[3]
        subtotal_num = price_num - price_num * (discount_num/100)

        price_total_num += price_num
        discount_total_num += price_num * (discount_num/100)

        # price_str = '€ ' + str(price_num)
        discount_str = str(discount_num) + "%"
        if discount_num == 100:
            subtotal_str = 'gratis'
        else:
            print(subtotal_num)
            subtotal_str = locale.currency(subtotal_num, grouping=True)

        price_str = locale.currency(price_num, grouping=True)

        pdf.cell(cell_width_qta, cell_height, '1', border=1, fill=True)
        pdf.cell(cell_width_codice, cell_height, row_code_str, border=1, fill=True)
        pdf.cell(cell_width_description, cell_height, row_desc_str, border=1, fill=True)
        pdf.cell(cell_width_prezzo, cell_height, price_str, border=1, fill=True)
        pdf.cell(cell_width_sconti, cell_height, discount_str, border=1, fill=True)
        pdf.cell(cell_width_totale, cell_height, subtotal_str, border=1, fill=True)
        pdf.ln(cell_height)

    pdf.ln(3)
    
    subtotal_str = locale.currency(price_total_num, grouping=True)

    margin_left = 135

    pdf.cell(margin_left, cell_height, '')
    pdf.set_font(font, 'B', text_size)
    pdf.cell(25, cell_height, 'Totale Prezzo: ', align='R')
    pdf.set_font(font, '', text_size)
    pdf.cell(25, cell_height, subtotal_str)
    pdf.ln(cell_height)

    discount_total_str = locale.currency(discount_total_num, grouping=True)

    pdf.cell(margin_left, cell_height, '')
    pdf.set_font(font, 'B', text_size)
    pdf.cell(25, cell_height, 'Totale Sconto: ', align='R')
    pdf.set_font(font, '', text_size)
    pdf.cell(25, cell_height, discount_total_str)
    pdf.ln(cell_height)

    iva_perc = 22
    iva_num = (price_total_num - discount_total_num) * (22/100)
    iva_str = locale.currency(iva_num, grouping=True) + f' ({iva_perc}%)'

    pdf.cell(margin_left, cell_height, '')
    pdf.set_font(font, 'B', text_size)
    pdf.cell(25, cell_height, 'IVA: ', align='R')
    pdf.set_font(font, '', text_size)
    pdf.cell(25, cell_height, iva_str)
    pdf.ln(cell_height)

    totale_str = locale.currency(iva_num + price_total_num - discount_total_num, grouping=True)

    pdf.cell(margin_left, cell_height, '')
    pdf.set_font(font, 'B', text_size)
    pdf.cell(25, cell_height, 'Totale: ', align='R')
    pdf.set_font(font, '', text_size)
    pdf.cell(25, cell_height, totale_str)
    pdf.ln(cell_height)
    pdf.ln(10)

    cell_height = 6

    pdf.set_font(font, 'B', text_size)
    pdf.cell(130, cell_height, 'Condizioni di fornitura')
    pdf.cell(100, cell_height, 'Timbro e firma per accettazione', ln=1)
    pdf.set_font(font, '', text_size)
    pdf.cell(100, cell_height, 'Merce: da pronta a 40gg lavorativi', ln=1)
    pdf.cell(100, cell_height, 'Garanzia: 12 mesi', ln=1)
    pdf.cell(100, cell_height, "Pagamento: 50% all'ordine, 50% alla consegna", ln=1)

    pdf.ln(20)

    pdf.set_font(font, '', 10)
    cell_height = 5
    privacy = 'Privacy L. 675 del 31.12.96 : Si informa che i dati a voi relativi e riportati nel presente documento vengono trattati in base alle esigenze contrattuali ed i conseguenti adempimenti degli obblighi fiscali e contabili. Con tale avviso ci riteniamo esonerati da eventuali responsabilità.'

    pdf.multi_cell(0, cell_height, privacy)

    pdf.output('report.pdf')

generate_pdf()

