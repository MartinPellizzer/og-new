from fpdf import FPDF
import xml.etree.ElementTree as ET

a4_w_mm = 210
a4_h_mm = 297
a4_x_pd = 20
container_w = a4_w_mm - int(a4_x_pd * 2)

h1_index = 0
h2_index = 0
h3_index = 0

def h2(pdf, text, border=0):
    gap = a4_w_mm - container_w
    font_size = 18
    line_height = font_size // 3
    pdf.set_font("Arial", size=font_size, style="B")
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=f'''{text.strip()}''', ln=True, border=border, align='L')
    pdf.ln()
    
def h3(pdf, text, border=0):
    gap = a4_w_mm - container_w
    font_size = 14
    line_height = font_size // 3
    pdf.set_font("Arial", size=font_size, style="B")
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=f'''{text.strip()}''', ln=True, border=border, align='L')
    pdf.ln()

def paragraph(pdf, text, border=0):
    gap = a4_w_mm - container_w
    font_size = 11
    line_height = 5
    pdf.set_font("Arial", size=font_size)
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=text.strip(), ln=True, border=border, align='L')
    pdf.ln()

def ol(pdf, number, text, border=0):
    global last_tag
    gap = a4_w_mm - container_w
    font_size = 11
    line_height = 5
    pdf.set_font("Arial", size=font_size)
    pdf.x = gap // 2
    pdf.x += 4
    line = '. '.join(text.split('. ')[1:])
    if len(number) == 1: number_w = 6
    else: number_w = 8 
    pdf.cell(number_w, line_height, txt=f'{number.strip()}. ', border=border, align='L')
    pdf.multi_cell(container_w - 10, line_height, txt=text, ln=True, border=border, align='L')
    pdf.ln(2)
    last_tag = 'ol'
    
def li(pdf, text, border=0):
    global last_tag
    gap = a4_w_mm - container_w
    font_size = 11
    line_height = 5
    pdf.set_font("Arial", size=font_size)
    pdf.x = gap // 2
    pdf.x += 4
    pdf.multi_cell(container_w - 10, line_height, txt=f'- {text}', ln=True, border=border, align='L')
    pdf.ln(2)
    last_tag = 'li'
    
def ol_li(pdf, text, step_num, border=0):
    global last_tag
    gap = a4_w_mm - container_w
    font_size = 11
    line_height = 5
    pdf.set_font("Arial", size=font_size)
    pdf.x = gap // 2
    pdf.x += 4
    pdf.multi_cell(container_w - 10, line_height, txt=f'{step_num}. {text}', ln=True, border=border, align='L')
    pdf.ln(2)
    last_tag = 'li'

image_num_cur = 0
y_cur = 0
gap_image = 2
def pdf_image_left(pdf, href):
    global y_cur
    y_cur = pdf.y
    gap = a4_w_mm - container_w
    pdf.x = gap // 2
    pdf.image(href, w=container_w//2 - gap_image//2)
    last_tag = 'img'
    print(image_num_cur)

def pdf_image_right(pdf, href):
    global y_cur
    pdf.y = y_cur
    gap = a4_w_mm - container_w
    pdf.x = (gap // 2) + container_w//2 + gap_image//2
    pdf.image(href, w=container_w//2 - gap_image//2)
    last_tag = 'img'
    pdf.ln(gap_image)

def pdf_image_grid_2(pdf, href):
    global y_cur
    if image_num_cur % 2 == 0:
        y_cur = pdf.y
        gap = a4_w_mm - container_w
        pdf.x = gap // 2
        pdf.image(href, w=container_w//2 - gap_image//2)
        last_tag = 'img'
    elif image_num_cur % 2 == 1:
        pdf.y = y_cur
        gap = a4_w_mm - container_w
        pdf.x = (gap // 2) + container_w//2 + gap_image//2
        pdf.image(href, w=container_w//2 - gap_image//2)
        last_tag = 'img'
        pdf.ln(gap_image)

def pdf_image_grid_3(pdf, href):
    global y_cur
    if image_num_cur % 3 == 0:
        y_cur = pdf.y
        gap = a4_w_mm - container_w
        pdf.x = gap // 2
        pdf.image(href, w=container_w//3 - gap_image//2)
        last_tag = 'img'
    elif image_num_cur % 3 == 1:
        pdf.y = y_cur
        gap = a4_w_mm - container_w
        pdf.x = (gap // 2) + container_w//3 + gap_image//2
        pdf.image(href, w=container_w//3 - gap_image//2)
        last_tag = 'img'
    elif image_num_cur % 3 == 2:
        pdf.y = y_cur
        gap = a4_w_mm - container_w
        pdf.x = (gap // 2) + container_w//3 * 2 + gap_image//2 * 2
        pdf.image(href, w=container_w//3 - gap_image//2)
        last_tag = 'img'
        pdf.ln(gap_image)

def pdf_image(pdf, href):
    y_cur = pdf.y
    gap = a4_w_mm - container_w
    pdf.x = gap // 2
    pdf.image(href, w=container_w)
    pdf.ln()
    last_tag = 'img'

def topic_proposal_generate(pdf, element):
    pdf.add_page()
    for child in element:
        if child.tag == 'title':
            title_text = child.text
            h2(pdf, title_text)
            print(child.text)
        if child.tag == 'shortdesc':
            paragraph(pdf, child.text)
        if child.tag == 'image':
            href = child.attrib['href']
            pdf_image(pdf, href)
        if child.tag == 'body':
            body = child
            for section in body:
                print(section)
                for section_child in section:
                    if section_child.tag == 'title':
                        h3(pdf, section_child.text)
                    elif section_child.tag == 'p':
                        paragraph(pdf, section_child.text)
                    elif section_child.tag == 'ul':
                        ul = section_child
                        for ul_child in ul:
                            if ul_child.tag == 'li':
                                li(pdf, ul_child.text)
                        pdf.ln()
                    elif section_child.tag == 'ol':
                        ol = section_child
                        for ol_i, ol_child in enumerate(ol):
                            if ol_child.tag == 'li':
                                ol_li(pdf, ol_child.text, ol_i+1)
                        pdf.ln()

def gen(ditamap_filepath):
    global image_num_cur
    pdf = FPDF()
    # pdf.add_page()
    tree = ET.parse(ditamap_filepath)
    root = tree.getroot()
    if root.tag == 'map':
        for element in root:
            if element.tag == 'task':
                pdf.add_page()
                for child in element:
                    if child.tag == 'title':
                        title_text = child.text
                        h2(pdf, title_text)
                        print(child.text)
                    elif child.tag == 'taskbody':
                        child_context = child[0]
                        for child_image in child_context:
                            href = child_image.attrib['href']
                            pdf_image_grid_3(pdf, href)
                            image_num_cur += 1
                        if image_num_cur % 3 == 2:
                            pdf.ln()
                        pdf.ln(gap_image)
                        image_num_cur = 0
                        for step_i, step in enumerate(child[1]):
                            cmd_text = step[0].text
                            ol(pdf, str(step_i+1), cmd_text)
                        result_text = child[2][0].text
                        print(result_text)
                        if result_text != None and result_text == "":
                            paragraph(pdf, result_text)
                pdf.ln(10)
            if element.tag == 'topic':
                topic_proposal_generate(pdf, element)
    pdf.output('test-map.pdf')
