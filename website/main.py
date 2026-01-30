import os
import shutil

from lib import g

shutil.copy2(f'style.css', f'{g.WEBSITE_FOLDERPATH}/style.css')
shutil.copy2(f'styles-applications.css', f'{g.WEBSITE_FOLDERPATH}/styles-applications.css')
shutil.copy2(f'styles-home.css', f'{g.WEBSITE_FOLDERPATH}/styles-home.css')
shutil.copy2(f'styles-components.css', f'{g.WEBSITE_FOLDERPATH}/styles-components.css')

if 1:
    from hub import applications_hub
    applications_hub.gen()

if 0:
    from hub import prodotti_hub
    prodotti_hub.gen()

from hub import home_hub
home_hub.gen()