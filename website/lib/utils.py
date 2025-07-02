import os

def aschii(paragraph):
    paragraph = paragraph.replace('è', '&#232;')
    paragraph = paragraph.replace('é', '&#233;')
    paragraph = paragraph.replace('à', '&#224;')
    paragraph = paragraph.replace('°', '&#176;')
    paragraph = paragraph.replace('©', '&#169;')
    return paragraph

def css_create_if_not_exists(css_filepath):
    if not os.path.exists(css_filepath):
        with open(css_filepath, 'w') as f: 
            f.write('')