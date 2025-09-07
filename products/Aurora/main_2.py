from fpdf import FPDF
from fpdf.outline import TableOfContents

from lib import g
from lib import layout
from lib import t
from lib import polish

a4_w_mm = 210
a4_h_mm = 297
a4_x_pd = 20
container_w = a4_w_mm - int(a4_x_pd * 2)

h1_index = 0
h2_index = 0
h3_index = 0

last_tag = ''

gap = a4_w_mm - container_w
to_toc = None

def toc(pdf):
    global last_tag
    global to_toc
    pdf.add_page()
    to_toc = pdf.add_link()
    # pdf.set_link()
    toc = TableOfContents()
    pdf.insert_toc_placeholder(toc.render_toc, allow_extra_pages=True)
    last_tag = 'toc'

def h1(pdf, text, border=0):
    global last_tag
    text = polish.text_format(text)
    pdf.add_page()
    font_size = 18
    line_height = font_size // 3
    pdf.set_font("Arial", size=font_size)
    if last_tag == 'ul' or last_tag == 'ol': pdf.ln(3)
    pdf.start_section(name=f"{text.strip().upper()}", level=0)
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=f'''{text.strip().upper()}''', ln=True, border=border, align='L')
    pdf.ln()
    last_tag = 'h1'

def h2(pdf, text, border=0):
    global last_tag
    text = polish.text_format(text)
    if last_tag != 'toc': pdf.add_page()
    pdf.start_section(name=f"{text.strip().upper()}", level=1)
    font_size = 16
    line_height = font_size // 3
    pdf.set_font("Arial", size=font_size)
    if last_tag == 'ul' or last_tag == 'ol': pdf.ln(3)
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=f'''{text.strip().upper()}''', ln=True, border=border, align='L', link=to_toc)
    pdf.ln()
    last_tag = 'h2'

def h3(pdf, text, border=0):
    global last_tag
    text = polish.text_format(text)
    font_size = 14
    line_height = font_size // 3
    pdf.set_font("Arial", size=font_size)
    pdf.ln(3)
    pdf.start_section(name=f"{text.strip()}", level=2)
    # if last_tag == 'ul' or last_tag == 'ol': pdf.ln(3)
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=f'''{text.strip().upper()}''', ln=True, border=border, align='L')
    pdf.ln()
    last_tag = 'h3'

def h4(pdf, text, border=0):
    global last_tag
    text = polish.text_format(text)
    font_size = 11
    line_height = font_size // 3
    pdf.set_font("Arial", size=font_size, style="B")
    # pdf.set_font("Arial", size=font_size)
    # pdf.start_section(name=f"{text.strip()}", level=3)
    pdf.ln(2)
    # if last_tag == 'ul' or last_tag == 'ol': pdf.ln(3)
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=f'''{text.strip()}''', ln=True, border=border, align='L')
    pdf.ln()
    last_tag = 'h4'

def paragraph(pdf, text, border=0):
    global last_tag
    text = polish.text_format(text)
    gap = a4_w_mm - container_w
    font_size = 11
    line_height = 5
    pdf.set_font("Arial", size=font_size)
    if last_tag == 'ul' or last_tag == 'ol': pdf.ln(3)
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=text.strip(), ln=True, border=border, align='L')
    pdf.ln()
    last_tag = 'p'

def ul(pdf, text, border=0, px=4):
    global last_tag
    text = polish.text_format(text)
    gap = a4_w_mm - container_w
    font_size = 11
    line_height = 5
    pdf.set_font("Arial", size=font_size)
    pdf.x = gap // 2
    pdf.x += px
    pdf.cell(4, line_height, txt='-', border=border, align='L')
    pdf.multi_cell(container_w - 10, line_height, txt=text.strip(), ln=True, border=border, align='L')
    pdf.ln(2)
    last_tag = 'ul'

def ol(pdf, text, border=0):
    global last_tag
    text = polish.text_format(text)
    gap = a4_w_mm - container_w
    font_size = 11
    line_height = 5
    pdf.set_font("Arial", size=font_size)
    pdf.x = gap // 2
    pdf.x += 4
    number = text.split('. ')[0]
    line = '. '.join(text.split('. ')[1:])
    if len(number) == 1: number_w = 6
    else: number_w = 8 
    pdf.cell(number_w, line_height, txt=f'{number.strip()}. ', border=border, align='L')
    pdf.multi_cell(container_w - 10, line_height, txt=line.strip(), ln=True, border=border, align='L')
    pdf.ln(2)
    last_tag = 'ol'

table_data = []

def empty_line(pdf):
    global last_tag
    if last_tag == 'table':
        pdf.set_font("Arial", size=11)
        with pdf.table(width=container_w, line_height=5, padding=2, text_align='LEFT') as table:
            for data_row in table_data:
                row = table.row()
                for datum in data_row:
                    row.cell(datum)
        pdf.ln()
    if last_tag == 'ul':
        pdf.set_font("Arial", size=11)
        pdf.ln(2)
    if last_tag == 'ol':
        pdf.set_font("Arial", size=11)
        pdf.ln(2)
    if last_tag != 'toc':
        last_tag = 'empty_line'

def table(pdf, line):
    global last_tag
    global table_data
    if last_tag != 'table':
        table_data = []
    cols = [col.strip() for col in line.split('|') if col.strip() != '']
    valid = False
    for col in cols: 
        for char in col: 
            if char != '-':
                valid = True
                break
        if valid:
            break
    if valid:
        table_data.append(cols)
    last_tag = 'table'

def pdf_aurora_hardware_design():
    filepaths_relative = [
        'Aurora_Documentation_ENG/Aurora_v1.0/01_Product_Overview/01_Product_Concept',
        'Aurora_Documentation_ENG/Aurora_v1.0/10_Future_Planning/04_Feature_Prioritization_vNext',
    ]
    ###
    for filepath_relative in filepaths_relative:
        pdf = FPDF()
        input_filepath = f'doc/src/{filepath_relative}.md'
        output_filepath = f'doc/dst/{filepath_relative}.pdf'
        with open(input_filepath, encoding='utf-8', errors='ignore') as f: content = f.read()
        for line in content.split('\n'):
            # print(line)
            # line = line.strip()
            line = polish.text_format(line)
            if line.strip() == '':
                empty_line(pdf)
                continue
            line = line.replace('*', '')
            if line.startswith('---'):
                continue
            elif line.startswith('[page]'):
                pdf.add_page()
                continue
            elif line.startswith('# '):
                line = line.replace('# ', '')
                h1(pdf, line)
            elif line.startswith('[toc]'):
                line = line.replace('[toc]', '')
                toc(pdf)
            elif line.startswith('## '):
                line = line.replace('## ', '')
                h2(pdf, line)
            elif line.startswith('### '):
                line = line.replace('### ', '')
                h3(pdf, line)
            elif line.startswith('#### '):
                line = line.replace('#### ', '')
                h4(pdf, line)
            elif line.startswith('- '):
                line = line.replace('- ', '')
                ul(pdf, line, border=0)
            elif line.startswith('* '):
                line = line.replace('* ', '')
                ul(pdf, line, border=0)
            elif line[0].isdigit():
                ol(pdf, line, border=0)
            elif line.startswith('    '):
                line = line.replace('    ', '')
                if line.startswith('- '):
                    line = line.replace('- ', '')
                    ul(pdf, line, border=0, px=8)
                elif line[0].isdigit():
                    ol(pdf, line, border=0)
            elif line.startswith('|'):
                table(pdf, line)
            else:
                paragraph(pdf, line)
        pdf.ln()
        pdf.output(output_filepath)

def doc_master():
    pdf_aurora_hardware_design()

doc_master()

