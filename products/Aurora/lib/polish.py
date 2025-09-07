def text_format(text):
    text_formatted = text
    text_formatted = text_formatted.replace('–', '-')
    text_formatted = text_formatted.replace('—', '-')
    text_formatted = text_formatted.replace('₃', '3')
    text_formatted = text_formatted.replace('’', "'")
    text_formatted = text_formatted.replace('≥', ">=")
    text_formatted = text_formatted.replace('≤', "<=")
    text_formatted = text_formatted.replace(' ', " ")
    text_formatted = text_formatted.replace('“', '"')
    text_formatted = text_formatted.replace('”', '"')
    text_formatted = text_formatted.replace('μ', 'u')
    return text_formatted

