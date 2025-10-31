###############################
# ;tier 1
###############################
### ;color_brown
color_brand_brown_50 = '#efebe9'
color_brand_brown_100 = '#d7ccc8'
color_brand_brown_700 = '#5d4037'
color_brand_brown_900 = '#3e2723'
### ;color_blue
color_brand_blue_50 = '#e3f2fd'
color_brand_blue_100 = '#bbdefb'
color_brand_blue_200 = '#90caf9'
color_brand_blue_300 = '#64b5f6'
color_brand_blue_400 = '#42a5f5'
color_brand_blue_500 = '#2196f3'
color_brand_blue_600 = '#1e88e5'
color_brand_blue_700 = '#1976d2'
color_brand_blue_800 = '#1565c0'
color_brand_blue_900 = '#0d47a1'
### ;color_gray
color_brand_white = '#ffffff'
color_brand_grey_50 = '#fafafa'
color_brand_grey_100 = '#f5f5f5'
color_brand_grey_200 = '#eeeeee'
color_brand_grey_300 = '#e0e0e0'
color_brand_grey_400 = '#bdbdbd'
color_brand_grey_500 = '#9e9e9e'
color_brand_grey_600 = '#757575'
color_brand_grey_700 = '#616161'
color_brand_grey_800 = '#424242'
color_brand_grey_900 = '#212121'
color_brand_black = '#000000'

###############################
# ;tier 2
###############################
### ;content
color_content_default = color_brand_grey_900
color_content_default_hover = color_brand_grey_600
color_content_subtle = color_brand_grey_600
color_content_knockout = color_brand_white
color_content_brand = color_brand_blue_800
color_content_brand_hover = color_brand_blue_700
color_content_disabled = color_brand_grey_500
### ;background
color_background_brand = color_brand_brown_50
### ;border
color_border_brand = color_brand_brown_900

###############################
# ;tier 3
###############################
### ;content
button_color_content_default = color_content_brand
### ;background
button_color_background_default = color_background_brand
### ;border
button_color_border_default = color_border_brand

css = []
glob_prefix = 'ds'
tier_prefix = 'theme'
css.append(':root {')
css.append(f'    --{glob_prefix}-{tier_prefix}-color-content-default: {color_content_default};')
css.append(f'    --{glob_prefix}-{tier_prefix}-color-content-default-hover: {color_content_default_hover};')
css.append(f'    --{glob_prefix}-{tier_prefix}-color-content-subtle: {color_content_subtle};')
css.append(f'    --{glob_prefix}-{tier_prefix}-color-content-knockout: {color_content_knockout};')
css.append(f'    --{glob_prefix}-{tier_prefix}-color-content-brand-hover: {color_content_brand_hover};')
css.append(f'    --{glob_prefix}-{tier_prefix}-color-content-brand: {color_content_brand};')
css.append(f'    --{glob_prefix}-{tier_prefix}-color-content-disabled: {color_content_disabled};')
css.append(f'    --{glob_prefix}-{tier_prefix}-button-color-content-default: {button_color_content_default};')
css.append(f'    --{glob_prefix}-{tier_prefix}-button-color-background-default: {button_color_background_default};')
css.append(f'    --{glob_prefix}-{tier_prefix}-button-color-border-default: {button_color_border_default};')
css.append('}\n')

css.append(f'''.ds-c-heading {{
    color: var(--{glob_prefix}-{tier_prefix}-color-content-brand);
}}\n''')
css.append(f'''.ds-c-paragraph {{
    color: var(--{glob_prefix}-{tier_prefix}-color-content-default);
}}\n''')
css.append(f'''.ds-c-button {{
    color: var(--{glob_prefix}-{tier_prefix}-button-color-content);
    background-color: var(--{glob_prefix}-{tier_prefix}-button-color-background);
    border: 1px solid var(--{glob_prefix}-{tier_prefix}-button-color-border);
    padding: 8px 16px;
    text-decoration-line: none;
}}\n''')

css_output = '\n'.join(css)
with open('public/style.css', 'w') as f: f.write(css_output)