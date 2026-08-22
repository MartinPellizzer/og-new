### generate list of facilities
### normalize / resolve (canonicalize)

### for each facility generate list of processes

### for each facility generate list of problems


import os
import json
import shutil

from lorem_text import lorem

from lib import g
from lib import io
from lib import llm
from lib import polish
from lib import components

model_filepath = '/home/ubuntu/vault-tmp/llm/gemma-4-12b-it-Q4_K_S.gguf'
model_filepath = '/home/ubuntu/vault-tmp/llm/gemma-4-12B-it-qat-UD-Q4_K_XL.gguf'


import sectors_data
# import facilities_data


def sectors_gen():
    prompt = f'''
        Write a list of sectors where ozone is being used.
        Use as few words as possible.
        Write only one sector per line.
        By sectors, i mean like food and beverage, hospitality, etc.
    '''.strip()
    print(prompt)
    reply = llm.reply(prompt, model_filepath)
    if '</think>' in reply: reply = reply.split('</think>')[1].strip()
    reply = polish.vanilla(reply)
    print()
    print('########################################################################')
    print(reply)
    print('########################################################################')
    print()

def facility_gen():
    prompt = f'''
        Write a list of facility types in the food industry where ozone is being used.
        Use as few words as possible.
        Write only one facility per line.
        Give me the normalized, canonical name for each facility type.
        Use the minimum amount of words as term for each facility type.
    '''.strip()
    print(prompt)
    reply = llm.reply(prompt, model_filepath)
    if '</think>' in reply: reply = reply.split('</think>')[1].strip()
    reply = polish.vanilla(reply)
    print()
    print('########################################################################')
    print(reply)
    print('########################################################################')
    print()

def render_sectors_html():
    input_data = sectors_data.data
    for sector_item in input_data:
        sector_name = sector_item['sector_name']
        sector_name_simple = sector_item['sector_name_simple']
        sector_slug = sector_item['sector_slug']
        ###
        children = []
        for candidate_child_item in input_data:
            if sector_item['sector_name_normalize'] == candidate_child_item['sector_parent_name_normalize']:
                print(sector_item['sector_name'])
                children.append(candidate_child_item)
        ###
        html_children = ''
        if children != []:
            html_children += '<ul>'
            for child in children:
                html_children += f'''<li><a href="/settori/{child['sector_slug']}">{child['sector_name']}</a></li>'''
            html_children += '</ul>'
        
    sectors_lvl_1 = [item for item in input_data if item['sector_parent_name_normalize'] == None]

    ###
    html_h1 = f'''<h1>Settori</h1>'''
    html_sectors = ''
    if sectors_lvl_1 != []:
        html_sectors += '<ul>'
        for sector in sectors_lvl_1:
            html_sectors += f'''<li><a href="/settori/{sector['sector_slug']}">{sector['sector_name']}</a></li>'''
        html_sectors += '</ul>'
    article_html = f'''
        {html_h1}
        {html_sectors}
    '''

    ###
    url_slug = f'''settori'''
    meta_title = f'''Settori'''
            # <link rel="stylesheet" href="/styles.css">
    html = f''' 
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>{meta_title}</title>

            <!-- USWDS initializer -->
            <script src="/assets/uswds/dist/js/uswds-init.min.js"></script>

            <!-- USWDS -->
            <link rel="stylesheet" href="/assets/uswds/dist/css/uswds.min.css">

        </head>
        <body>
            {components.header_light_logo()}
            <main class="listing container-md">
                {article_html}
            </main>
            {components.footer_dark()}
        </body>
        </html>
    '''.strip()
    ###
    html_folderpath = f'{g.website_folderpath}/{url_slug}'
    io.folders_recursive_gen(html_folderpath)
    html_filepath = f'{g.website_folderpath}/{url_slug}/index.html'
    with open(html_filepath, 'w') as f: f.write(html)
    print(html_filepath)

def render_sector_html():
    input_data = sectors_data.data
    for sector_item in input_data:
        sector_name = sector_item['sector_name']
        sector_name_simple = sector_item['sector_name_simple']
        sector_slug = sector_item['sector_slug']
        ###
        children = []
        for candidate_child_item in input_data:
            if sector_item['sector_name_normalize'] == candidate_child_item['sector_parent_name_normalize']:
                print(sector_item['sector_name'])
                children.append(candidate_child_item)
        ###
        html_h1 = f'''<h1>{sector_name_simple}</h1>'''
        html_children = ''
        if children != []:
            html_children += '<ul>'
            for child in children:
                html_children += f'''<li><a href="/settori/{child['sector_slug']}">{child['sector_name']}</a></li>'''
            html_children += '</ul>'
        
        ###
        article_html = f'''
            {html_h1}
            {html_children}
        '''

        ###
        url_slug = f'''settori/{sector_slug}'''
        meta_title = f'''{sector_name_simple}'''

        html_h1 = f'''<h1>{sector_name_simple}</h1>'''
        html_intro = f'''<p class="usa-intro">{lorem.words(16)}</p>'''
        html_body = f'''
<body>
    {components.header_light_logo()}
  <div class="usa-section">
    <div class="grid-container">
      <div class="grid-row grid-gap">
        <div
          class="usa-layout-docs__sidenav display-none desktop:display-block desktop:grid-col-3"
        >
          <nav aria-label="Secondary navigation">
            <ul class="usa-sidenav">
              <li class="usa-sidenav__item">
                <a href="javascript:void(0);">Parent link</a>
              </li>
              <li class="usa-sidenav__item">
                <a href="javascript:void(0);" class="usa-current"
                  >Current page</a
                >
                <ul class="usa-sidenav__sublist">
                  <li class="usa-sidenav__item">
                    <a href="javascript:void(0);">Child link</a>
                  </li>
                  <li class="usa-sidenav__item">
                    <a href="javascript:void(0);" class="usa-current"
                      >Child link</a
                    >
                    <ul class="usa-sidenav__sublist">
                      <li class="usa-sidenav__item">
                        <a href="javascript:void(0);">Grandchild link</a>
                      </li>
                      <li class="usa-sidenav__item">
                        <a href="javascript:void(0);" class="usa-current"
                          >Grandchild link</a
                        >
                      </li>
                      <li class="usa-sidenav__item">
                        <a href="javascript:void(0);">Grandchild link</a>
                      </li>
                    </ul>
                  </li>
                  <li class="usa-sidenav__item">
                    <a href="javascript:void(0);">Child link</a>
                  </li>
                </ul>
              </li>
              <li class="usa-sidenav__item">
                <a href="javascript:void(0);">Parent link</a>
              </li>
            </ul>
          </nav>
        </div>
        <main class="desktop:grid-col-9 usa-prose" id="main-content">
            {html_h1}
            {html_intro}
          <h2 id="section-heading-h2">Section heading (h2)</h2>
          <p>
            These headings introduce, respectively, sections and subsections
            within your body copy. As you create these headings, follow the same
            guidelines that you use when writing section headings: Be succinct,
            descriptive, and precise.
          </p>
          <h3 id="section-heading-h3">Subsection heading (h3)</h3>
          <p>
            The particulars of your body copy will be determined by the topic of
            your page. Regardless of topic, it’s a good practice to follow the
            inverted pyramid structure when writing copy: Begin with the
            information that’s most important to your users and then present
            information of less importance.
          </p>
          <p>
            Keep each section and subsection focused — a good approach is to
            include one theme (topic) per section.
          </p>
          <h4 id="section-heading-h4">Subsection heading (h4)</h4>
          <p>
            Use the side navigation menu to help your users quickly skip to
            different sections of your page. The menu is best suited to
            displaying a hierarchy with one to three levels and, as we
            mentioned, to display the sub-navigation of a given page.
          </p>
          <p>
            Read the full documentation on our side navigation on the component
            page.
          </p>
        </main>
      </div>
      <div class="usa-layout-docs__sidenav desktop:display-none">
        <nav aria-label="Secondary navigation">
          <ul class="usa-sidenav">
            <li class="usa-sidenav__item">
              <a href="javascript:void(0);">Parent link</a>
            </li>
            <li class="usa-sidenav__item">
              <a href="javascript:void(0);" class="usa-current">Current page</a>
              <ul class="usa-sidenav__sublist">
                <li class="usa-sidenav__item">
                  <a href="javascript:void(0);">Child link</a>
                </li>
                <li class="usa-sidenav__item">
                  <a href="javascript:void(0);" class="usa-current"
                    >Child link</a
                  >
                  <ul class="usa-sidenav__sublist">
                    <li class="usa-sidenav__item">
                      <a href="javascript:void(0);">Grandchild link</a>
                    </li>
                    <li class="usa-sidenav__item">
                      <a href="javascript:void(0);" class="usa-current"
                        >Grandchild link</a
                      >
                    </li>
                    <li class="usa-sidenav__item">
                      <a href="javascript:void(0);">Grandchild link</a>
                    </li>
                  </ul>
                </li>
                <li class="usa-sidenav__item">
                  <a href="javascript:void(0);">Child link</a>
                </li>
              </ul>
            </li>
            <li class="usa-sidenav__item">
              <a href="javascript:void(0);">Parent link</a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
  <footer class="usa-footer">
    <div class="grid-container usa-footer__return-to-top">
      <a href="#">Return to top</a>
    </div>
    <div class="usa-footer__primary-section">
      <nav class="usa-footer__nav" aria-label="Footer navigation">
        <ul class="grid-row grid-gap">
          <li
            class="mobile-lg:grid-col-4 desktop:grid-col-auto usa-footer__primary-content"
          >
            <a class="usa-footer__primary-link" href="javascript:void(0);"
              >&lt;Primary link&gt;</a
            >
          </li>
          <li
            class="mobile-lg:grid-col-4 desktop:grid-col-auto usa-footer__primary-content"
          >
            <a class="usa-footer__primary-link" href="javascript:void(0);"
              >&lt;Primary link&gt;</a
            >
          </li>
          <li
            class="mobile-lg:grid-col-4 desktop:grid-col-auto usa-footer__primary-content"
          >
            <a class="usa-footer__primary-link" href="javascript:void(0);"
              >&lt;Primary link&gt;</a
            >
          </li>
          <li
            class="mobile-lg:grid-col-4 desktop:grid-col-auto usa-footer__primary-content"
          >
            <a class="usa-footer__primary-link" href="javascript:void(0);"
              >&lt;Primary link&gt;</a
            >
          </li>
        </ul>
      </nav>
    </div>
    <div class="usa-footer__secondary-section">
      <div class="grid-container">
        <div class="grid-row grid-gap">
          <div
            class="usa-footer__logo grid-row mobile-lg:grid-col-6 mobile-lg:grid-gap-2"
          >
            <div class="mobile-lg:grid-col-auto">
              <img
                class="usa-footer__logo-img"
                src="/assets/img/logo-img.png"
                alt=""
              />
            </div>
            <div class="mobile-lg:grid-col-auto">
              <p class="usa-footer__logo-heading">&lt;Name of Agency&gt;</p>
            </div>
          </div>
          <div class="usa-footer__contact-links mobile-lg:grid-col-6">
            <div class="usa-footer__social-links grid-row grid-gap-1">
              <div class="grid-col-auto">
                <a class="usa-social-link" href="javascript:void(0);"
                  ><img
                    class="usa-social-link__icon"
                    src="/assets/img/usa-icons/facebook.svg"
                    alt="Facebook"
                /></a>
              </div>
              <div class="grid-col-auto">
                <a class="usa-social-link" href="javascript:void(0);"
                  ><img
                    class="usa-social-link__icon"
                    src="/assets/img/usa-icons/twitter.svg"
                    alt="Twitter"
                /></a>
              </div>
              <div class="grid-col-auto">
                <a class="usa-social-link" href="javascript:void(0);"
                  ><img
                    class="usa-social-link__icon"
                    src="/assets/img/usa-icons/youtube.svg"
                    alt="YouTube"
                /></a>
              </div>
              <div class="grid-col-auto">
                <a class="usa-social-link" href="javascript:void(0);"
                  ><img
                    class="usa-social-link__icon"
                    src="/assets/img/usa-icons/instagram.svg"
                    alt="Instagram"
                /></a>
              </div>
              <div class="grid-col-auto">
                <a class="usa-social-link" href="javascript:void(0);"
                  ><img
                    class="usa-social-link__icon"
                    src="/assets/img/usa-icons/rss_feed.svg"
                    alt="RSS"
                /></a>
              </div>
            </div>
            <p class="usa-footer__contact-heading">
              &lt;Agency Contact Center&gt;
            </p>
            <address class="usa-footer__address">
              <div class="usa-footer__contact-info grid-row grid-gap">
                <div class="grid-col-auto">
                  <a href="tel:1-800-555-5555">&lt;(800) 555-GOVT&gt;</a>
                </div>
                <div class="grid-col-auto">
                  <a href="mailto:info@agency.gov">&lt;info@agency.gov&gt;</a>
                </div>
              </div>
            </address>
          </div>
        </div>
      </div>
    </div>
  </footer>
  <div class="usa-identifier">
    <section
      class="usa-identifier__section usa-identifier__section--masthead"
      aria-label="Agency identifier"
    >
      <div class="usa-identifier__container">
        <div class="usa-identifier__logos">
          <a href="javascript:void(0)" class="usa-identifier__logo"
            ><img
              class="usa-identifier__logo-img"
              src="/assets/img/circle-gray-20.svg"
              alt="&lt;Parent agency&gt; logo"
              role="img"
          /></a>
        </div>
        <section
          class="usa-identifier__identity"
          aria-label="Agency description"
        >
          <p class="usa-identifier__identity-domain">domain.gov</p>
          <p class="usa-identifier__identity-disclaimer">
            <span aria-hidden="true">An </span>official website of the
            <a href="">&lt;Parent agency&gt;</a>
          </p>
        </section>
      </div>
    </section>
    <nav
      class="usa-identifier__section usa-identifier__section--required-links"
      aria-label="Important links"
    >
      <div class="usa-identifier__container">
        <ul class="usa-identifier__required-links-list">
          <li class="usa-identifier__required-links-item">
            <a
              href="javascript:void(0)"
              class="usa-identifier__required-link usa-link"
              >About &lt;Parent shortname&gt;</a
            >
          </li>
          <li class="usa-identifier__required-links-item">
            <a href="" class="usa-identifier__required-link usa-link"
              >Accessibility support</a
            >
          </li>
          <li class="usa-identifier__required-links-item">
            <a href="" class="usa-identifier__required-link usa-link"
              >FOIA requests</a
            >
          </li>
          <li class="usa-identifier__required-links-item">
            <a href="" class="usa-identifier__required-link usa-link"
              >No FEAR Act data</a
            >
          </li>
          <li class="usa-identifier__required-links-item">
            <a href="" class="usa-identifier__required-link usa-link"
              >Office of the Inspector General</a
            >
          </li>
          <li class="usa-identifier__required-links-item">
            <a href="" class="usa-identifier__required-link usa-link"
              >Performance reports</a
            >
          </li>
          <li class="usa-identifier__required-links-item">
            <a href="" class="usa-identifier__required-link usa-link"
              >Privacy policy</a
            >
          </li>
        </ul>
      </div>
    </nav>
    <section
      class="usa-identifier__section usa-identifier__section--usagov"
      aria-label="U.S. government information and services"
    >
      <div class="usa-identifier__container">
        <div class="usa-identifier__usagov-description">
          Looking for U.S. government information and services?
        </div>
        <a href="https://www.usa.gov/" class="usa-link">Visit USA.gov</a>
      </div>
    </section>
  </div>
</body>
        '''

        html = f''' 
            <!DOCTYPE html>
            <html lang="it">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>{meta_title}</title>

                <!-- USWDS initializer -->
                <script src="/assets/uswds/dist/js/uswds-init.min.js"></script>

                <!-- USWDS -->
                <link rel="stylesheet" href="/assets/uswds/dist/css/uswds.min.css">

                <link rel="stylesheet" href="/styles-custom.css">

            </head>
            {html_body}
            </html>
        '''.strip()

        ###
        html_folderpath = f'{g.website_folderpath}/{url_slug}'
        io.folders_recursive_gen(html_folderpath)
        html_filepath = f'{g.website_folderpath}/{url_slug}/index.html'
        with open(html_filepath, 'w') as f: f.write(html)
        print(html_filepath)

def run():
    shutil.copy2(f'styles.css', f'{g.WEBSITE_FOLDERPATH}/styles.css')
    shutil.copy2(f'styles-custom.css', f'{g.WEBSITE_FOLDERPATH}/styles-custom.css')

    output_folderpath = f'{g.WEBSITE_FOLDERPATH}/settori'
    try: shutil.rmtree(output_folderpath)
    except: pass
    io.folders_recursive_gen(output_folderpath)
    ###

    render_sectors_html()
    ###
    render_sector_html()

run()
