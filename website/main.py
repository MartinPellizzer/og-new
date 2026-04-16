import os
import shutil

from lib import g

shutil.copy2(f'style.css', f'{g.WEBSITE_FOLDERPATH}/style.css')
shutil.copy2(f'styles-applications.css', f'{g.WEBSITE_FOLDERPATH}/styles-applications.css')
shutil.copy2(f'styles-home.css', f'{g.WEBSITE_FOLDERPATH}/styles-home.css')
shutil.copy2(f'styles-components.css', f'{g.WEBSITE_FOLDERPATH}/styles-components.css')
shutil.copy2(f'styles.css', f'{g.WEBSITE_FOLDERPATH}/styles.css')
shutil.copy2(f'styles-topic-hub.css', f'{g.WEBSITE_FOLDERPATH}/styles-topic-hub.css')

if 1:
    from hub import layer1_hub
    layer1_hub.main()

if 1:
    from templates import templates_gen
    templates_gen.main()

if 1:
    from hub import azienda_hub
    azienda_hub.main()

if 1:
    from hub import confronti_hub
    confronti_hub.main()
    
if 1:
    from hub import tecnologia_hub
    tecnologia_hub.main()
    
if 1:
    from hub import metodo_hub
    metodo_hub.main()

if 1:
    from hub import settori_hub
    settori_hub.main()

if 1:
    from hub import soluzioni_hub
    soluzioni_hub.main()

if 0:
    from pillar import ozono_industriale
    ozono_industriale.main()

if 0:
    from pillar import ozono
    ozono.main()

if 0:
    from hub import core_hub
    core_hub.gen()

if 0:
    from hub import ozone_hub
    ozone_hub.gen()

if 0:
    from hub import applications_hub
    applications_hub.gen()

if 0:
    from hub import prodotti_hub
    prodotti_hub.gen()

from hub import home_hub
home_hub.gen()
