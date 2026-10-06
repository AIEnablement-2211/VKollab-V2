# VKollab Technologies — website

Production-ready static site. **HTML5 + CSS3 + vanilla JavaScript only** — no frameworks, no build step required to deploy, no runtime third-party requests (fonts are self-hosted).

```
vkollab/
├── index.html               Home
├── about.html               About
├── services.html            Services hub (ten services)
├── services/                Ten service pages
│   ├── sap-application-development.html · sap-fiori-ui5.html · sap-migration-upgrades.html · sap-s4hana.html
│   ├── track-trace-compliancewire.html · sap-ibp-eppds.html · sap-application-management.html
│   └── workday.html · sap-successfactors.html · sap-ai.html
├── industries.html          Seven industries (anchored sections)
├── careers.html
├── contact.html             Contact form (see "Form endpoint")
├── privacy-policy.html · terms-and-conditions.html
├── 404.html
├── robots.txt · sitemap.xml · site.webmanifest
├── assets/
│   ├── css/      style.css (tokens, type, header, hero, buttons, forms, footer)
│   │             pages.css (editorial layouts and page components)
│   │             responsive.css (1920 · 1280 · 1024 · 768 · 480 · 360 · print)
│   ├── js/       main.js · navigation.js · animations.js · forms.js · components.js  (all deferred, vanilla)
│   ├── fonts/    Lexend 500/600/700 (headings) · DM Sans 400–700 (body) — woff2, OFL
│   ├── logos/    vkollab-logo-white.png · vkollab-logo-color.png · vkollab-mark.png
│   ├── images/   19 photographs (all local, ≤1600 px, ≤200 KB except industry-tech.jpg) · og-default.jpg
│   ├── favicon.ico · favicon-*.png · apple-touch-icon.png
├── deploy/  _redirects (Netlify / Cloudflare Pages) · .htaccess (Apache) · nginx-redirects.conf
└── tools/   build.py · content.py · assets_svg.py   ← optional page assembler, see below
```

## Photos

Every photograph is local in `assets/images/`; nothing is loaded from the old site. The mapping from page to file is the `LOCAL_PHOTOS` dict in `tools/build.py` — swap any file, keep the key, rebuild. The photography is stock office imagery extracted from the design files; replacing it progressively with photographs of VKollab's own offices and teams is the single biggest remaining visual upgrade.

## Company facts on the site

The home and About pages state: founded 2020; four offices (Parsippany NJ, Hyderabad, Guntur, Vijayawada); 90+ consultants; clients in the United States, Europe and Japan. They live in `FACTS` and in the prose in `tools/content.py`. Verify them before launch and change them in that one file. No clients, case studies, certifications or statistics are claimed anywhere; when you can name them, the natural place is a "proof" section on the home page after "Why VKollab", and a one-line "Where we have done this" on each service page.

## Deploy

Upload everything except `tools/` to the web root (`index.html`, the other pages, `services/`, `assets/`, `robots.txt`, `sitemap.xml`, `site.webmanifest`, and the matching file from `deploy/`). Works unchanged on Apache, Nginx, GitHub Pages, Netlify, Vercel (static), Cloudflare Pages or any static host.

1. **404 page** — point the server's not-found handler at `/404.html`. Netlify and GitHub Pages pick it up automatically; Apache and Nginx snippets are in `deploy/`.
2. **Old URLs** — the previous site used flat URLs such as `/sap-s4-hana.html`. Redirect maps for all of them are in `deploy/` (`_redirects`, `.htaccess`, `nginx-redirects.conf`). Install the one that matches your host so inbound links and search rankings carry over.
3. **Canonical domain** — all canonical/OG URLs are `https://vkollab.com/…`. If you serve from `www.`, redirect it to the apex (or search-and-replace the domain in the HTML).
4. **Caching** — fonts, CSS, JS and images are safe to cache for a year; HTML should be short-lived. Example headers are in `deploy/.htaccess`.

## Alumni Portal and HR App links

Both buttons (contact banner on every page, footer Quick Links) are wired to two constants at the top of `tools/build.py`:

```python
ALUMNI_URL = "https://vkonnect.vkollab.com/"
HR_APP_URL = "https://vkollab.hrapp.co/v3/"
```

Change them and run `python3 tools/build.py` (or search-and-replace in the HTML). Office map links for Guntur and Vijayawada are in the `OFFICES` list in the same file.

## Careers

The careers page has no job listings; it asks candidates to email `careers@vkollab.com` (`CAREERS_EMAIL` in `tools/build.py`). If you later want listings, the role cards and Apply Now popup are still supported by `css/pages.css` and `js/components.js`.

## 404 page — making it actually work

`404.html` is a normal page; the **server** has to be told to serve it for unknown URLs, otherwise visitors get the host's default error page:

- **Apache / cPanel / shared hosting:** copy `deploy/.htaccess` to the web root (it contains `ErrorDocument 404 /404.html`).
- **Nginx:** add `error_page 404 /404.html;` to the server block (see `deploy/nginx-redirects.conf`).
- **Netlify / Cloudflare Pages / GitHub Pages / Vercel:** a root-level `404.html` is picked up automatically.

Test after deploying by opening `https://vkollab.com/this-does-not-exist`.

## Form endpoint

`js/forms.js` has one constant at the top:

```js
var FORM_ENDPOINT = ""; /* e.g. "https://formspree.io/f/xxxxxxx" */
```

- The same constant drives the home-page conversation form, the Contact page form and the Careers "Apply Now" popup. With an endpoint set, the application form posts `multipart/form-data` (including the CV file); without one, it falls back to email and asks the applicant to attach the CV.
- **Empty (default):** submitting opens the visitor's mail client with the message pre-filled to `info@vkollab.com`. No data is sent anywhere else.
- **Set to a URL:** the form POSTs JSON `{name, company, email, phone, topic, message, consent, page}` with `fetch`, expects a 2xx response, and shows loading / success / error states. Formspree, Netlify Forms (with their JSON endpoint), a Cloudflare Worker, Power Automate HTTP trigger or your own API all work. Never put private API keys in this file — use an endpoint that accepts anonymous POSTs and validates server-side.

A honeypot field (`website`) is included; discard submissions where it is non-empty.

## Editing content

Pages are plain HTML and can be edited directly. Because the header, footer, mega menu and icon sprite are repeated on every page, an optional assembler is included so they never drift:

```
python3 tools/build.py        # regenerates all HTML, sitemap.xml, robots.txt
```

- `tools/content.py` — all copy: service definitions (problem → capabilities → approach → deliverables → outcomes), industries, values, method, roles.
- `tools/build.py` — site constants (phone, email, offices, social links), navigation structure, head/footer templates, JSON-LD.
- `tools/assets_svg.py` — icon sprite and diagrams.

Python 3.8+ with no dependencies. If you prefer to hand-edit the HTML and never run the assembler, delete `tools/`.

## Design system (summary)

The visual language is deliberately restrained: one blue, one navy, two type families, text columns separated by rules, numbered lists and split layouts. The chamfered tile is used only for the service catalogue; the diagonal accent only at the bottom of page heroes. There is no glassmorphism, no watermark text and no decorative gradient.

| Token | Value | Use |
|---|---|---|
| `--blue` | `#2582e7` | buttons, links, eyebrow labels, hero accent |
| `--navy` / `--navy-footer` | `#003869` / `#0c3a68` | headlines, top bar, dark sections, footer |
| `--sky` | `#e8f2fc` | service tiles, menu icon tiles; `#f3f7fc` for light sections and form panels |
| `--ink` / `--ink-2` / `--muted` | `#1f2d3d` / `#44556a` / `#6b7a8c` | body text |
| Headings | Lexend 600/700 | rounded geometric, as in the design |
| Body / UI | DM Sans 400–700 | paragraphs, nav, chips, buttons |

Components: `.topbar`, `.site-header` (transparent over the hero, solid white once scrolled), `.hero` with `.hero__diag`, `.facts`, `.split`, `.cols` (text columns with rules), `.numlist`, `.steps4`, `.tile` (services only), `.svc` switcher, `.tabs`, `.convo` form, `.leader`, `.offices`, `.industry-block`, `.service-layout` with sticky `.aside-card`, `.cta`, `.site-footer`.

Icons: 24-px grid, 1.5-px stroke, round joins, `currentColor`. Add new ones to `ICONS` in `tools/assets_svg.py` and reference with `<svg><use href="#i-name"></use></svg>`.

## Accessibility & performance notes

- Semantic landmarks, one `h1` per page, logical heading order, skip link, visible focus rings, `aria-current` on navigation, keyboard-operable mega menu and mobile drawer (Escape closes, focus is trapped while open, background scroll locked).
- Motion: a short hero entrance, scroll reveals and hover states only — all CSS/vanilla JS. `prefers-reduced-motion` disables all of it; the site is fully usable with JavaScript disabled (links work, menus fall back to the Services hub page, form falls back to `mailto:`).
- No third-party scripts or font services. Two font files are preloaded; scripts are deferred; photos are lazy-loaded.

## Things deliberately left out

`privacy-policy.html` and `terms-and-conditions.html` contain standard, plain-English policies that describe what the site actually does (contact form, applications by email, no tracking cookies). Have them reviewed by whoever handles legal matters at VKollab before launch; the copy lives in `privacy()` and `terms()` in `tools/content.py`.

The previous site carried claims that could not be verified from public information ("100 % success ratio", "15+ years", "24/7"). They have not been carried over. If you have verifiable client names, certifications or partnership status, the natural places to add them are the `hero__proof` strip on the home page and a new section after "Who we are".

## Licences

Lexend and DM Sans are licensed under the SIL Open Font License 1.1 (see `assets/fonts/LICENSE-*.txt`). Everything else in this repository is the property of VKollab Technologies.
