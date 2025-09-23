def text_format(text):
    text_formatted = text
    text_formatted = text_formatted.replace('—', '')
    text_formatted = text_formatted.replace('₃', '3')
    text_formatted = text_formatted.replace('’', "'")
    return text_formatted

def list_unordered(lst):
    text_formatted = ''
    for item in lst:
        item = item.strip()
        item = text_format(item)
        text_formatted += f'* {item}\n'
    return text_formatted
