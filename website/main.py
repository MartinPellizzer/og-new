import os
import shutil

from lib import g

shutil.copy2(f'style.css', f'{g.website_folderpath}/style.css')

from hub import home_hub
home_hub.gen()

from hub import servizi_hub
servizi_hub.gen()

from hub import prodotti_hub
prodotti_hub.gen()

from hub import ozono_hub
ozono_hub.gen()