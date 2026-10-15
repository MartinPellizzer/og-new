
from reportlab.platypus import SimpleDocTemplate, Table
import re

from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle

from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer


from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.platypus import KeepTogether

import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

doc = None

input_filepath = 'C:/og-new/products/aurora_module_relay_x8/v0_1_0/docs/inputs/specifications.md'
output_filepath = 'C:/og-new/products/aurora_module_relay_x8/v0_1_0/docs/outputs/specifications.pdf'


style = ParagraphStyle(
    "table",
    fontName="Helvetica",
    fontSize=9,
    textColor="#475467",
    leading=11,
)

header_style = ParagraphStyle(
    "header",
    parent=style,
    fontName="Helvetica-Bold",
    textColor="#344054",
)

def md_to_tables(md):
    md_elements = []
    md_element = ''

    for line in md.split('\n'):
        line = line.strip()
        if line.startswith('|'):
            md_element += line
            md_element += '\n'
        else:
            md_elements.append(md_element)
            md_element = ''

    if md_element != '':
        md_elements.append(md_element)

    return md_elements



def markdown_table(md):
    rows = [
        [x.strip() for x in line.strip("|").split("|")]
        for line in md.splitlines()
        if line.strip() and not re.match(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$", line)
    ]

    rows = [
        [Paragraph(cell, header_style if i == 0 else style) for cell in row]
        for i, row in enumerate(rows)
    ]

    # table = Table(rows, colWidths=[doc.width / len(rows[0])] * len(rows[0]))
    table = Table(
        rows,
        colWidths=[doc.width * 0.5, doc.width * 0.5] 
    )

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F2F4F7")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#344054")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("TEXTCOLOR", (0, 1), (-1, -1), colors.HexColor("#475467")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
        [colors.white, colors.HexColor("#FAFAFA")]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))

    return table

def browse():
    path = filedialog.askopenfilename(
        filetypes=[("Markdown files", "*.md *.markdown")]
    )
    if path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, path)

################################################################################
# PARSE
################################################################################
def parse(lines, elements):
    ul_start = False
    ul_items = []
    ol_start = False
    ol_items = []
    table_start = False
    table_items = []
    state = ''
    for line in lines:
        line = line.strip()
        line = line.replace('–', '-')
        line = line.replace('*', '')
        if line == '': continue

        if line == '[body]':  state = '[body]'
        elif line == '[/body]': state = ''

        if line.startswith('[') and line.endswith(']'): continue

        elif state == '[body]':
        
            if line.startswith('-----'):
                break
            
            if line.startswith('---'):
                if ul_start == True:
                    ul_start = False
                    ul_gen(ul_items)
                    ul_items = []
                if ol_start == True:
                    ol_start = False
                    ol_gen(ol_items)
                    ol_items = []
                if table_start == True:
                    table_start = False
                    table_gen(table_items)
                    table_items = []
                elements.append(PageBreak())
                continue
            
            if line.startswith('<spacer>'):
                elements.append(Spacer(1, 20))
                continue
            
            if line[0] == '-':
                line = line[1:].strip()
                ul_items.append(line)
                ul_start = True
                continue
            if ul_start == True:
                ul_start = False
                ul_gen(ul_items)
                ul_items = []
                
            if line[0].isdigit() and line[1] == '.':
                line = line[2:].strip()
                ol_items.append(line)
                ol_start = True
                continue
            if ol_start == True:
                ol_start = False
                ol_gen(ol_items)
                ol_items = []
                
            if line[0] == ':':
                line = line[1:].strip()
                row = [col.strip() for col in line.split(',')]
                table_items.append(row)
                table_start = True
                continue
            if table_start == True:
                table_start = False
                table_gen(table_items)
                table_items = []

            if line.startswith('###'):
                line = line.replace('###', '').strip()
                elements.append(Paragraph(line, h3))
            elif line.startswith('##'):
                line = line.replace('##', '').strip()
                elements.append(Paragraph(line, h2))
            elif line.startswith('#'):
                line = line.replace('#', '').strip()
                elements.append(Paragraph(line, h1))

            elif line.startswith('!'):
                line = line.split('(')[1].split(')')[0].split(' ')[0]
                print(line)
                # with PIL.Image.open(line) as img:
                #     width, height = img.size
                mul = 1.0
                # image_w = width * mul
                # image_h = height * mul
                target_width = 451.27
                target_width *= mul
                with PIL.Image.open(line) as im:
                    width, height = im.size
                scale = target_width / width
                image_w = width * scale
                image_h = height * scale  # SAME scale → keeps ratio

                img = Image(line, image_w, image_h)
                elements.append(Spacer(1, 10))
                img.hAlign = "CENTER"
                elements.append(img)
                elements.append(Spacer(1, 20))

            elif line.startswith('**'):
                line = line.replace('**', '').strip()
                # elements.append(Paragraph(line, body_bold_style))
                elements.append(Paragraph(line, body_style))
            else:
                line = line.strip()
                elements.append(Paragraph(line, body_style))
    if ul_start == True:
        ul_start = False
        ul_gen(ul_items)
        ul_items = []
    if lines:
        elements.append(PageBreak())

def convert_to_pdf():
    elements = []

    # input_filepath = f'output.md'
    # output_filepath = f'output.pdf'
    with open(input_filepath, encoding='utf-8') as f: lines = f.read().split('\n')
    print(lines)

    ################################################################################
    # DOCUMENT SETUP
    ################################################################################
    doc = MyDocTemplate(
        output_filepath,
        pagesize=A4,
        rightMargin=70,
        leftMargin=70,
        topMargin=90,
        bottomMargin=60
    )

    cover_add(elements)
    rev_parse(lines)
    rev_add(elements)
    toc_add(elements)
    parse(lines, elements)
    
    # BUILD
    # doc.build(elements, onFirstPage=header_footer, onLaterPages=header_footer)
    doc.multiBuild(elements)



    # global doc
    # input_filepath = Path(file_entry.get())

    # if not input_filepath.is_file():
    #     messagebox.showerror("Error", "Select a valid Markdown file.")
    #     return

    # doc = SimpleDocTemplate(output_filepath)

    # with open(input_filepath) as f: md = f.read()
    # md_elements = md_to_tables(md)

    # elements_parse = []
    # for i, md_element in enumerate(md_elements):

    #     element_parse = markdown_table(md_element)

    #     table_elements = [element_parse]

    #     if i < len(md_elements) - 1:
    #         table_elements.append(Spacer(1, 40))

    #     elements_parse.append(KeepTogether(table_elements))

    # story = elements_parse

    # doc.build(story)

    # try:
    #     text = path.read_text(encoding="utf-8")
    #     html = markdown.markdown(
    #         text, extensions=["tables", "fenced_code"]
    #     )

    #     pdf = FPDF()
    #     pdf.set_auto_page_break(auto=True, margin=15)
    #     pdf.add_page()
    #     pdf.write_html(html)

    #     output = path.with_suffix(".pdf")
    #     pdf.output(str(output))

    #     messagebox.showinfo("Success", f"PDF saved to:\n{output}")

    # except Exception as e:
    #     messagebox.showerror("Conversion error", str(e))


# root = tk.Tk()
# root.title("Markdown to PDF")

# file_entry = tk.Entry(root, width=45)
# file_entry.pack(side="left", padx=5, pady=10)

# file_entry.delete(0, tk.END)
# file_entry.insert(0, 'C:/og-new/products/aurora_module_relay_x8/v0_1_0/docs/inputs/specifications.md')

# tk.Button(root, text="Browse", command=browse).pack(side="left")
# tk.Button(root, text="Convert to PDF",
#           command=convert_to_pdf).pack(side="left", padx=5)

# root.mainloop()

convert_to_pdf()