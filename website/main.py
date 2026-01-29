import os
import shutil

from lib import g

shutil.copy2(f'style.css', f'{g.WEBSITE_FOLDERPATH}/style.css')
shutil.copy2(f'styles-applications.css', f'{g.WEBSITE_FOLDERPATH}/styles-applications.css')

if 1:
    from hub import applications_hub
    applications_hub.gen()

quit()

if 1:
    from hub import prodotti_hub
    prodotti_hub.gen()

from hub import home_hub
home_hub.gen()

if 0:
    from hub import servizi_hub
    servizi_hub.gen()

    from hub import prodotti_hub
    prodotti_hub.gen()


    from hub import chi_siamo_hub
    chi_siamo_hub.gen()

    from hub import contatti_hub
    contatti_hub.gen()

    from hub import ozono_hub
    ozono_hub.gen()
