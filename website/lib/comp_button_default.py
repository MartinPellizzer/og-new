from lib import ds

def gen(text, href):
    html = f'''
<div>
    <a class="button-default" href="/contatti.html">
        Prenota consulenza
    </a>
</div>
    '''.strip()

    css = f'''
.button-default {{
    color: {ds.ds_theme_button_color_content_inverted_primary};
    background-color: {ds.ds_theme_button_color_background_inverted_primary};
    
    border-radius: 9999px;
    padding: 8px 16px;
    text-decoration-line: none;
}}
    '''.strip()
    with open(f'components/button-default.html', 'w') as f:
        f.write(html)
    with open(f'components/button-default.css', 'w') as f:
        f.write(css)
    # border: 1px solid var(--ds-theme-button-color-border-inverted-primary);
