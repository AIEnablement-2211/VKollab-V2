#!/usr/bin/env python3
"""
VKollab static site assembler.

Produces plain HTML files from shared chrome (head, header, footer, icon sprite)
plus per-page content. The output in the project root is the deliverable; this
script only exists so the navigation and footer never drift between pages.

Run:  python3 tools/build.py
"""
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from assets_svg import sprite, icon, hero_landscape, ecosystem_diagram, method_diagram, industry_mini, service_diagram  # noqa: E402
import content  # noqa: E402

SITE_URL = "https://vkollab.com"
SITE_NAME = "VKollab Technologies"
PHONE_DISPLAY = "+1 908 300 1548"
PHONE_HREF = "tel:+19083001548"
EMAIL = "info@vkollab.com"
CAREERS_EMAIL = "careers@vkollab.com"
ALUMNI_URL = "https://vkonnect.vkollab.com/"   # Alumni Portal (former employees)
HR_APP_URL = "https://vkollab.hrapp.co/v3/"   # HR App (current employees)

def ext(url):
    return url if url else "#"
SOCIAL = {
    "linkedin": "https://www.linkedin.com/company/vkollab-technologies",
    "facebook": "https://www.facebook.com/vkollabtechnologies",
    "instagram": "https://www.instagram.com/vkollabtechnologies",
    "youtube": "https://www.youtube.com/@vkollabtechnologies",
}
OFFICES = [
    ("Head office", "Parsippany, New Jersey", "8 Campus Dr, Suite 105<br>Parsippany, NJ 07054<br>United States", "https://www.google.com/maps/search/?api=1&query=8+Campus+Dr+Suite+105+Parsippany+NJ+07054"),
    ("Branch office", "Hyderabad, Telangana", "H.No. 6-3-852/2 &amp; 3, Ameerpet<br>Hyderabad, Telangana 500016<br>India", "https://www.google.com/maps/search/?api=1&query=6-3-852+Ameerpet+Hyderabad+500016"),
    ("Branch office", "Guntur, Andhra Pradesh", "87-18-3361/1/A, Mahatma Gandhi Nagar<br>Revenue Ward 41, Guntur<br>Andhra Pradesh 522003, India", "https://maps.app.goo.gl/n38xgfJ69fRrMbMw5"),
    ("Branch office", "Vijayawada, Andhra Pradesh", "Plot No 1, Vijaya Dairy Colony<br>Salipeta Road, Poranki, Vijayawada<br>NTR District, Andhra Pradesh 521137, India", "https://maps.app.goo.gl/dSXx5opm4GUPHA458"),
]

# ---------------------------------------------------------------------------
# Service catalogue (single source of truth for nav, hub, footer, sitemap)
# ---------------------------------------------------------------------------
SERVICE_ORDER = [
    "sap-application-development", "sap-fiori-ui5", "sap-migration-upgrades", "sap-s4hana",
    "track-trace-compliancewire", "sap-ibp-eppds", "sap-application-management", "workday", "sap-successfactors", "sap-ai",
]
PRACTICES = [{"id": "services", "icon": "core", "title": "Services", "services": SERVICE_ORDER}]
SERVICES = content.SERVICES  # dict slug -> definition
INDUSTRIES = content.INDUSTRIES

# ---------------------------------------------------------------------------
# Chrome
# ---------------------------------------------------------------------------

def head(page, root):
    title = page["title"]
    desc = page["description"]
    path = page["path"]
    canonical = SITE_URL + "/" + ("" if path == "index.html" else path)
    og_image = SITE_URL + "/assets/images/og-default.jpg"
    jsonld = page.get("jsonld", "")
    noindex = '<meta name="robots" content="noindex, follow">' if page.get("noindex") else ""
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{noindex}<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#003869">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="VKollab Technologies — SAP consulting and application services">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_image}">
<link rel="icon" href="{root}assets/favicon.ico" sizes="32x32">
<link rel="icon" href="{root}assets/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="{root}assets/apple-touch-icon.png">
<link rel="manifest" href="{root}site.webmanifest">
<link rel="preload" href="{root}assets/fonts/lexend-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}assets/fonts/dm-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/css/style.css">
<link rel="stylesheet" href="{root}assets/css/pages.css">
<link rel="stylesheet" href="{root}assets/css/responsive.css">
{jsonld}
</head>
<body>
{sprite()}
<a class="skip-link" href="#main">Skip to main content</a>
'''


def header(root, current):
    def nav_link(href, label, key):
        cur = ' aria-current="page"' if current == key else ""
        return f'<li class="site-nav__item"><a class="site-nav__link" href="{root}{href}"{cur}>{label}</a></li>'

    half = (len(SERVICE_ORDER) + 1) // 2
    cols = []
    for chunk in (SERVICE_ORDER[:half], SERVICE_ORDER[half:]):
        items = "".join(
            f'<li><a class="mega__link" href="{root}services/{sl}.html"><i>{icon(SERVICES[sl]["icon"])}</i><span>{SERVICES[sl]["name"]}<small>{SERVICES[sl]["tag"]}</small></span></a></li>'
            for sl in chunk
        )
        cols.append(f'<div class="mega__group"><ul role="list">{items}</ul></div>')
    mega = (
        f'<div class="mega mega--2" id="mega-services">{"".join(cols)}'
        f'<div class="mega__foot"><span>Ten services: SAP platform, planning, serialization and compliance, HR systems and AI.</span>'
        f'<a class="link-arrow" href="{root}services.html">All services {icon("arrow-right")}</a></div></div>'
    )
    services_cur = ' is-current' if current in ("services", "service") else ""
    home_cur = ' aria-current="page"' if current == "home" else ""
    return f'''<div class="topbar">
<div class="container container--wide topbar__inner">
<div class="topbar__left">SAP consulting and managed services &middot; Parsippany, NJ &middot; Hyderabad, India</div>
<div class="topbar__right"><a href="mailto:{EMAIL}">{icon("mail")} {EMAIL}</a><a href="{PHONE_HREF}">{icon("phone")} {PHONE_DISPLAY}</a></div>
</div>
</div>
<header class="site-header">
<div class="container container--wide site-header__inner">
<a class="brand" href="{root}index.html" aria-label="VKollab Technologies — home">
<img class="brand__light" src="{root}assets/logos/vkollab-logo-white.png" alt="VKollab Technologies" width="373" height="81">
<img class="brand__dark" src="{root}assets/logos/vkollab-logo-color.png" alt="VKollab Technologies" width="374" height="81">
</a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu"><span class="nav-toggle__bars"></span></button>
<nav class="site-nav" id="site-nav" aria-label="Primary">
<ul class="site-nav__list" role="list">
<li class="site-nav__item"><a class="site-nav__link" href="{root}index.html"{home_cur}>Home</a></li>
{nav_link("about.html", "About", "about")}
<li class="site-nav__item site-nav__item--has-menu{services_cur}"><a class="site-nav__link" href="{root}services.html" aria-expanded="false" aria-controls="mega-services" aria-haspopup="true">Services {icon("chevron-down")}</a>{mega}</li>
{nav_link("industries.html", "Industries", "industries")}
{nav_link("careers.html", "Careers", "careers")}
{nav_link("contact.html", "Contact", "contact")}
</ul>
<div class="site-nav__cta"><a class="site-nav__phone" href="{PHONE_HREF}">{icon("phone")}<span>{PHONE_DISPLAY}</span></a><a class="btn btn--primary" href="{root}contact.html">Talk to a consultant</a></div>
</nav>
</div>
</header>
<main id="main" tabindex="-1">
'''


def footer(root):
    svc_links = "".join(
        f'<li><a href="{root}services/{s}.html">{SERVICES[s]["name"]}</a></li>'
        for s in SERVICE_ORDER
    )
    socials = "".join(
        f'<a href="{url}" aria-label="VKollab on {name.capitalize()}">{icon(name)}</a>' for name, url in SOCIAL.items()
    )
    return f'''</main>
<footer class="site-footer">
<div class="container container--wide">
<div class="site-footer__top">
<div class="site-footer__brand">
<a href="{root}index.html" aria-label="VKollab Technologies — home"><img src="{root}assets/logos/vkollab-logo-white.png" alt="VKollab Technologies" width="373" height="81" loading="lazy"></a>
<p>SAP consulting and managed services for manufacturers and regulated industries. Founded 2020. Head office in Parsippany, New Jersey; delivery centres in Hyderabad, Guntur and Vijayawada, India.</p>
<div class="social">{socials}</div>
</div>
<div>
<h2>Services</h2>
<ul role="list">{svc_links}</ul>
</div>
<div>
<h2>Company</h2>
<ul role="list">
<li><a href="{root}about.html">About VKollab</a></li>
<li><a href="{root}industries.html">Industries</a></li>
<li><a href="{root}careers.html">Careers</a></li>
<li><a href="{root}contact.html">Contact</a></li>
<li><a href="{root}privacy-policy.html">Privacy Policy</a></li>
<li><a href="{root}terms-and-conditions.html">Terms and Conditions</a></li>
</ul>
<h3 class="site-footer__sub">Employee links</h3>
<ul role="list" class="site-footer__emp">
<li><a href="{ext(HR_APP_URL)}" data-pending-link>HR App</a><small>Current employees</small></li>
<li><a href="{ext(ALUMNI_URL)}" data-pending-link>Alumni Portal</a><small>Former employees</small></li>
</ul>
</div>
<div>
<h2>Contact</h2>
<address>
<div><strong>Head office</strong><a href="{OFFICES[0][3]}">8 Campus Dr, Suite 105<br>Parsippany, NJ 07054, United States</a></div>
<div><strong>India</strong>{" &middot; ".join(f'<a href="{o[3]}">{o[1].split(",")[0]}</a>' for o in OFFICES[1:])}</div>
<div><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div>
<div><strong>Phone</strong><a href="{PHONE_HREF}">{PHONE_DISPLAY}</a></div>
</address>
</div>
</div>
</div>
<div class="site-footer__bottom">
<div class="container container--wide">
<p>&copy; <span data-year>{date.today().year}</span> VKollab Technologies. All rights reserved.</p>
<div class="site-footer__legal"><a href="{root}privacy-policy.html">Privacy Policy</a><span aria-hidden="true">|</span><a href="{root}terms-and-conditions.html">Terms and Conditions</a></div>
</div>
</div>
</footer>
<script src="{root}assets/js/main.js" defer></script>
<script src="{root}assets/js/navigation.js" defer></script>
<script src="{root}assets/js/animations.js" defer></script>
<script src="{root}assets/js/forms.js" defer></script>
<script src="{root}assets/js/components.js" defer></script>
</body>
</html>
'''


def cta_band(root, heading="Talk to an SAP consultant, not a sales desk", body="Describe your landscape and the question you are trying to answer. A consultant from the relevant practice replies within one working day.", primary=("Talk to a consultant", "contact.html"), secondary=None):
    sec = f'<a class="btn btn--outline" href="{root}{secondary[1]}">{secondary[0]}</a>' if secondary else ""
    return f'''<section class="cta" aria-labelledby="cta-h">
<div class="container container--wide cta__inner">
<div class="cta__text">
<h2 id="cta-h">{heading}</h2>
<p>{body}</p>
<div class="cluster"><a class="btn btn--primary btn--lg" href="{root}{primary[1]}">{primary[0]} {icon("arrow-right")}</a>{sec}</div>
</div>
<div class="cta__contact">
<a class="cta__phone" href="{PHONE_HREF}"><small>Call the US office</small>{PHONE_DISPLAY}</a>
<a class="cta__mail" href="mailto:{EMAIL}"><small>Email</small>{EMAIL}</a>
</div>
</div>
</section>
'''


def breadcrumb(items):
    lis = []
    for i, (label, href) in enumerate(items):
        if href is None:
            lis.append(f'<li aria-current="page">{label}</li>')
        else:
            lis.append(f'<li><a href="{href}">{label}</a></li>')
    return f'<nav aria-label="Breadcrumb"><ol class="breadcrumb" role="list">{"".join(lis)}</ol></nav>'


def jsonld_breadcrumb(items):
    els = []
    for i, (name, path) in enumerate(items, 1):
        els.append(f'{{"@type":"ListItem","position":{i},"name":"{name}","item":"{SITE_URL}/{path}"}}')
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{",".join(els)}]}}</script>'


ORG_JSONLD = f'''<script type="application/ld+json">{{
"@context":"https://schema.org","@type":"Organization","name":"VKollab Technologies","url":"{SITE_URL}/","logo":"{SITE_URL}/assets/logos/vkollab-logo-color.png",
"email":"{EMAIL}","telephone":"+1-908-300-1548",
"founder":{{"@type":"Person","name":"Venkat Makke","jobTitle":"Founder & CEO","sameAs":"https://www.linkedin.com/in/venkatmakke/"}},
"address":[
 {{"@type":"PostalAddress","streetAddress":"8 Campus Dr, Suite 105","addressLocality":"Parsippany","addressRegion":"NJ","postalCode":"07054","addressCountry":"US"}},
 {{"@type":"PostalAddress","streetAddress":"H.No. 6-3-852/2 and 3, Ameerpet","addressLocality":"Hyderabad","addressRegion":"Telangana","postalCode":"500016","addressCountry":"IN"}},
 {{"@type":"PostalAddress","streetAddress":"87-18-3361/1/A, Mahatma Gandhi Nagar, Revenue Ward 41","addressLocality":"Guntur","addressRegion":"Andhra Pradesh","postalCode":"522003","addressCountry":"IN"}},
 {{"@type":"PostalAddress","streetAddress":"Plot No 1, Vijaya Dairy Colony, Salipeta Road, Poranki","addressLocality":"Vijayawada","addressRegion":"Andhra Pradesh","postalCode":"521137","addressCountry":"IN"}}
],
"sameAs":["{SOCIAL['linkedin']}","{SOCIAL['facebook']}","{SOCIAL['instagram']}","{SOCIAL['youtube']}"]
}}</script>'''


# Photos (all local, assets/images). Keys are what content.py asks for.
LOCAL_PHOTOS = {
    "hero": "hero-office.jpg", "home": "hero-home.jpg", "about-hero": "about-hero.jpg", "office": "office-meeting.jpg",
    "team": "team-meeting.jpg", "team2": "team-boardroom.jpg", "about-trio": "about-trio.jpg", "about-board": "about-boardroom.jpg",
    "faq1": "about-faq-1.jpg", "faq2": "about-faq-2.jpg", "faq3": "about-faq-3.jpg", "process": "team-process.jpg",
    "cutout": "team-cutout.webp", "contact": "contact-consultant.jpg", "ceo": "ceo-venkat-makke.jpg",
    "industry-tech": "industry-tech.jpg", "ai": "ai-hands.jpg", "network": "network-bg.jpg",
    # industries
    "pharma": "industry-tech.jpg", "automotive": "about-faq-2.jpg", "manufacturing": "team-process.jpg", "logistics": "about-faq-1.jpg",
    "healthcare": "about-trio.jpg", "banking": "about-boardroom.jpg", "real-estate": "about-faq-3.jpg",
    # service heroes
    "development": "team-meeting.jpg", "migration": "team-boardroom.jpg", "management": "office-meeting.jpg", "s4hana": "hero-office.jpg",
    "fiori": "about-faq-2.jpg", "attp-cw": "industry-tech.jpg", "ibp-eppds": "about-trio.jpg", "workday": "about-boardroom.jpg",
    "successfactors": "about-faq-1.jpg", "careers": "team-meeting.jpg",
}


_ROOT = {"root": ""}


def photo(key, alt="", extra="", eager=False):
    src = f'{_ROOT["root"]}assets/images/{LOCAL_PHOTOS[key]}'
    load = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img src="{src}" alt="{alt}" {load} decoding="async" data-photo {extra}>'


# ---------------------------------------------------------------------------
# Page builders
# ---------------------------------------------------------------------------

def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    # collapse runs of blank lines
    html = re.sub(r"\n{3,}", "\n\n", html)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)


def page(path, title, description, current, body, jsonld="", noindex=False):
    root = "../" if "/" in path else ""
    p = {"path": path, "title": title, "description": description, "jsonld": jsonld, "noindex": noindex}
    html = head(p, root) + header(root, current) + body + footer(root)
    write(path, html)


def ctx(root):
    """Helper bundle passed into content templates."""
    _ROOT["root"] = root
    return {
        "root": root, "icon": icon, "PRACTICES": PRACTICES, "SERVICES": SERVICES, "INDUSTRIES": INDUSTRIES,
        "OFFICES": OFFICES, "PHONE_DISPLAY": PHONE_DISPLAY, "PHONE_HREF": PHONE_HREF, "EMAIL": EMAIL, "CAREERS_EMAIL": CAREERS_EMAIL,
        "cta_band": cta_band, "breadcrumb": breadcrumb, "hero_landscape": hero_landscape,
        "ecosystem_diagram": ecosystem_diagram, "method_diagram": method_diagram,
        "industry_mini": industry_mini, "service_diagram": service_diagram, "SOCIAL": SOCIAL,
        "photo": photo, "SERVICE_ORDER": SERVICE_ORDER, "ALUMNI_URL": ext(ALUMNI_URL), "HR_APP_URL": ext(HR_APP_URL),
    }


def build():
    # Home
    page("index.html",
         "VKollab Technologies — SAP consulting and managed services for manufacturers and regulated industries",
         "S/4HANA implementation and migration, application management, IBP and PP/DS planning, serialization with SAP Advanced Track & Trace, ComplianceWire, SuccessFactors and Workday. Founded 2020; offices in New Jersey and India.",
         "home", content.home(ctx("")), jsonld=ORG_JSONLD)

    # About
    page("about.html",
         "About VKollab Technologies — who we are, where we work and how we deliver",
         "VKollab Technologies is an SAP consulting and managed-services firm founded in 2020, with a head office in Parsippany, NJ and delivery centres in Hyderabad, Guntur and Vijayawada. Leadership, values and how we work.",
         "about", content.about(ctx("")), jsonld=jsonld_breadcrumb([("Home", ""), ("About", "about.html")]))

    # Services hub
    page("services.html",
         "Services — SAP platform, planning, serialization, HR systems and AI | VKollab Technologies",
         "Ten services: SAP application development, Fiori/UI5, migration and upgrades, S/4HANA, Advanced Track & Trace with ComplianceWire, IBP with ePPDS, application management, Workday, SuccessFactors and SAP AI.",
         "services", content.services_hub(ctx("")), jsonld=jsonld_breadcrumb([("Home", ""), ("Services", "services.html")]))

    # Service detail pages
    for slug in SERVICE_ORDER:
        if True:
            s = SERVICES[slug]
            path = f"services/{slug}.html"
            jl = jsonld_breadcrumb([("Home", ""), ("Services", "services.html"), (s["name"], path)]) + f'''
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Service","name":"{s['name']}","serviceType":"{s['name']}","provider":{{"@type":"Organization","name":"VKollab Technologies","url":"{SITE_URL}/"}},"areaServed":["US","IN","AE","EU","JP"],"description":"{s['description']}","url":"{SITE_URL}/{path}"}}</script>'''
            page(path, f"{s['name']} services | VKollab Technologies", s["description"], "service",
                 content.service_page(ctx("../"), slug, None), jsonld=jl)

    # Industries
    page("industries.html",
         "Industries — pharmaceutical, automotive, manufacturing, logistics, healthcare, banking and construction | VKollab",
         "Where VKollab works: pharmaceutical and life sciences, automotive, manufacturing, logistics and transport, healthcare, banking and financial services, real estate and infrastructure construction.",
         "industries", content.industries(ctx("")), jsonld=jsonld_breadcrumb([("Home", ""), ("Industries", "industries.html")]))

    # Careers
    page("careers.html",
         "Careers at VKollab Technologies — SAP consulting roles in India and the US",
         "Work on S/4HANA, planning, serialization and HR-platform programmes for US clients from Hyderabad, Guntur, Vijayawada or New Jersey. Send your CV to careers@vkollab.com.",
         "careers", content.careers(ctx("")), jsonld=jsonld_breadcrumb([("Home", ""), ("Careers", "careers.html")]))

    # Contact
    page("contact.html",
         "Contact VKollab Technologies — Parsippany NJ, Hyderabad, Guntur and Vijayawada",
         "Talk to a VKollab consultant about an SAP programme, migration, managed service or HR-systems project. Phone +1 908 300 1548 or email info@vkollab.com; replies within one working day.",
         "contact", content.contact(ctx("")), jsonld=jsonld_breadcrumb([("Home", ""), ("Contact", "contact.html")]))

    # Legal
    page("privacy-policy.html", "Privacy Policy | VKollab Technologies",
         "How VKollab Technologies collects, uses and protects personal information submitted through vkollab.com.",
         "", content.privacy(ctx("")), jsonld=jsonld_breadcrumb([("Home", ""), ("Privacy Policy", "privacy-policy.html")]))
    page("terms-and-conditions.html", "Terms and Conditions | VKollab Technologies",
         "Terms governing the use of the vkollab.com website and its content.",
         "", content.terms(ctx("")), jsonld=jsonld_breadcrumb([("Home", ""), ("Terms and Conditions", "terms-and-conditions.html")]))

    # 404
    page("404.html", "Page not found | VKollab Technologies",
         "The page you were looking for does not exist or has moved.", "", content.not_found(ctx("")), noindex=True)

    # Supporting files
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {SITE_URL}/sitemap.xml\n")

    today = date.today().isoformat()
    urls = ["", "about.html", "services.html", "industries.html", "careers.html", "contact.html", "privacy-policy.html", "terms-and-conditions.html"] + [
        f"services/{s}.html" for s in SERVICE_ORDER
    ]
    pri = {"": "1.0", "services.html": "0.9", "about.html": "0.8", "contact.html": "0.8"}
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.w3.org/1999/xhtml" xmlns:x="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{SITE_URL}/{u}</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq><priority>{pri.get(u, '0.7')}</priority></url>")
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")

    write("site.webmanifest", '''{
  "name": "VKollab Technologies",
  "short_name": "VKollab",
  "icons": [
    { "src": "/assets/favicon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/assets/favicon-512.png", "sizes": "512x512", "type": "image/png" }
  ],
  "theme_color": "#003869",
  "background_color": "#ffffff",
  "display": "browser",
  "start_url": "/"
}
''')


if __name__ == "__main__":
    build()
