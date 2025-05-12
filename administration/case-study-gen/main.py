import subprocess
from fpdf import FPDF

title = '20,000 Leagues Under the Sea'

with open('abstract.txt', 'rb') as f:
    abstract = f.read().decode('latin-1')

class PDF(FPDF):
    def header(self):
        self.image('logo.jpg', 10, 8, 40)

        '''
        self.set_font('helvetica', 'B', 15)
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)

        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.set_line_width(1)
        self.cell(title_w, 10, title, border=1, ln=1, align='C', fill=1)
        '''

        self.ln(30)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

pdf = PDF('P', 'mm', 'A4')

pdf.alias_nb_pages()

pdf.set_auto_page_break(auto=True, margin=15)

pdf.add_page()

title = 'Efficacy of Ozonated Water, Chlorine, Chlorine Dioxide, Quaternary Ammonium Compounds and Peroxyacetic Acid Against Listeria monocytogenes Biofilm on Polystyrene Surfaces'
pdf.set_font('helvetica', 'B', 16)
pdf.multi_cell(0, 5, title)
pdf.ln()

TABLE_DATA = (
    ("Genus", "Species", "Surface/Material", "Treatment", "Effect"),
    ("Listeria", "L. monocytogenes", "Polystyrene", "Ozonated water (1.0, 2.0, and 4.0 ppm for 1 min)", "0.9, 3.4, and 4.1 Log reduction"),
)

pdf.set_font('times', '', 9)
with pdf.table() as table:
    for data_row in TABLE_DATA:
        row = table.row()
        for datum in data_row:
            row.cell(datum)
pdf.ln()

'''
col_w = 38
pdf.set_font('times', '', 9)
pdf.cell(col_w, 5, 'Genus', border=1)
pdf.cell(col_w, 5, 'Species', border=1)
pdf.cell(col_w, 5, 'Surface/Material', border=1)
pdf.cell(col_w, 5, 'Treatment', border=1)
pdf.cell(col_w, 5, 'Effect', border=1)
pdf.ln()

pdf.cell(col_w, 5, 'Listeria', border=1)
pdf.cell(col_w, 5, 'L. monocytogenes', border=1)
pdf.cell(col_w, 5, 'Polystyrene', border=1)
pdf.cell(col_w, 5, 'Ozonated water (1.0, 2.0, and 4.0 ppm for 1 min)', border=1)
pdf.cell(col_w, 5, '0.9, 3.4, and 4.1 Log reduction', border=1)
pdf.ln()

'''
pdf.set_font('times', '', 12)
pdf.multi_cell(0, 5, abstract)
pdf.ln()

pdf.output('test.pdf')


subprocess.Popen('test.pdf', shell=True)