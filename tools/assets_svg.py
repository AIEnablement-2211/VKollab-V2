"""SVG icon sprite + diagrams, inlined into every page by build.py.

Icon language: 24x24 viewBox, 1.5px stroke, round joins, no fills.
Diagrams: hand-drawn enterprise landscape / ecosystem / delivery visuals in brand tokens.
"""

ICONS = {
    "arrow-right": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "chevron-down": '<path d="M6 9l6 6 6-6"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "external": '<path d="M14 4h6v6M20 4l-9 9M19 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h5"/>',
    "linkedin": '<path d="M6.5 9.5v8M6.5 6.5v.01M10.5 17.5v-8M10.5 13a3 3 0 0 1 6 0v4.5"/><rect x="3" y="3" width="18" height="18" rx="2"/>',
    "facebook": '<path d="M14 8h2V5h-2a3 3 0 0 0-3 3v2H9v3h2v7h3v-7h2l1-3h-3V8z"/>',
    "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5v.01"/>',
    "youtube": '<rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="M10 9l5 3-5 3z"/>',
    # Practice / service icons
    "layers": '<path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 12l9 5 9-5M3 16l9 5 9-5"/>',
    "migrate": '<path d="M4 7h11M12 4l3 3-3 3M20 17H9M12 14l-3 3 3 3"/>',
    "shield": '<path d="M12 3l8 3v6c0 4.5-3.2 8-8 9-4.8-1-8-4.5-8-9V6l8-3z"/><path d="M9 12l2 2 4-4"/>',
    "core": '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 4v5M15 4v5M9 15v5M15 15v5M4 9h5M4 15h5M15 9h5M15 15h5"/>',
    "window": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M8 13h4M8 16h8"/>',
    "chart": '<path d="M4 20V4M4 20h16"/><path d="M8 15l4-5 3 3 5-7"/>',
    "schedule": '<rect x="3" y="5" width="18" height="15" rx="2"/><path d="M3 10h18M7 3v4M17 3v4M7 14h4M13 17h4"/>',
    "barcode": '<path d="M4 6v12M8 6v12M11 6v12M15 6v12M18 6v12M20 6v12M6 6v8M13 6v8"/>',
    "book": '<path d="M4 5a2 2 0 0 1 2-2h12v16H6a2 2 0 0 0-2 2V5z"/><path d="M4 19a2 2 0 0 0 2 2h12M8 7h7"/>',
    "people": '<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0M16 4a3 3 0 0 1 0 6M17 14a6 6 0 0 1 4 6"/>',
    "cloud": '<path d="M7 18a4 4 0 0 1-.5-8A6 6 0 0 1 18 9a4.5 4.5 0 0 1 0 9H7z"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "building": '<path d="M4 21V5a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v16M15 10h4a1 1 0 0 1 1 1v10M3 21h18M8 8h2M8 12h2M8 16h2"/>',
    # Industry icons
    "car": '<path d="M4 15l1.5-5A2 2 0 0 1 7.4 8.5h9.2a2 2 0 0 1 1.9 1.5L20 15M3 15h18v3H3zM6 18v2M18 18v2"/><circle cx="7.5" cy="15" r=".5"/><circle cx="16.5" cy="15" r=".5"/>',
    "factory": '<path d="M3 21V10l5 3v-3l5 3v-3l5 3V5h3v16H3z"/><path d="M7 17h2M12 17h2M17 17h2"/>',
    "truck": '<path d="M3 7h11v9H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="17.5" r="1.5"/><circle cx="17" cy="17.5" r="1.5"/>',
    "heart": '<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/><path d="M8 11h2l1-2 2 4 1-2h2"/>',
    "bank": '<path d="M3 10l9-6 9 6M5 10v8M9 10v8M15 10v8M19 10v8M3 18h18M3 21h18"/>',
    "blueprint": '<rect x="3" y="4" width="18" height="16" rx="1"/><path d="M3 9h18M8 9v11M14 9v4h7"/>',
    "pill": '<rect x="3.5" y="9" width="17" height="6" rx="3" transform="rotate(-45 12 12)"/><path d="M8.5 15.5l7-7"/>',
    # Method icons
    "search": '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>',
    "plan": '<path d="M4 5h16v14H4zM4 10h16M9 10v9"/>',
    "build": '<path d="M14 6l4 4-9 9H5v-4l9-9zM12 8l4 4"/>',
    "run": '<path d="M5 4l14 8-14 8V4z"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    "handshake": '<path d="M3 9l4-3 5 3 5-3 4 3-4 7-5 4-5-4-4-7z"/><path d="M12 9l-3 3 2 2 3-2"/>',
    "scale": '<path d="M12 3v18M5 7h14M5 7l-3 7a3 3 0 0 0 6 0L5 7zM19 7l-3 7a3 3 0 0 0 6 0l-3-7zM8 21h8"/>',
    "document": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
}


def sprite():
    out = ['<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true" focusable="false">']
    for name, body in ICONS.items():
        out.append(
            f'<symbol id="i-{name}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{body}</symbol>'
        )
    out.append("</svg>")
    return "\n".join(out)


def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} aria-hidden="true" focusable="false"><use href="#i-{name}"></use></svg>'


# ---------------------------------------------------------------------------
# Diagrams
# ---------------------------------------------------------------------------

_T = 'font-family="Manrope, Helvetica, Arial, sans-serif"'
_S = 'font-family="Manrope, Helvetica, Arial, sans-serif"'


def hero_landscape():
    """An SAP-centred enterprise landscape: core in the middle, planning / people /
    compliance tiers around it, integration lines, cloud + non-SAP edges."""
    navy = "#1d3770"
    acc = "#2e5aac"
    ink = "#171b26"
    mut = "#5f6577"
    bd = "#dcd9d1"
    paper = "#ffffff"
    return f'''<svg viewBox="0 0 640 520" role="img" aria-labelledby="hero-d-title hero-d-desc" xmlns="http://www.w3.org/2000/svg">
<title id="hero-d-title">Enterprise landscape centred on SAP S/4HANA</title>
<desc id="hero-d-desc">A diagram of an enterprise landscape: SAP S/4HANA at the core, surrounded by supply-chain planning, serialization, HR systems and compliance training, with integration to cloud platforms and non-SAP applications, and managed services underneath.</desc>
<defs>
  <marker id="m-dot" viewBox="0 0 8 8" refX="4" refY="4" markerWidth="5" markerHeight="5"><circle cx="4" cy="4" r="3" fill="{acc}"/></marker>
  <pattern id="p-grid" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="{bd}" stroke-width=".5" opacity=".6"/></pattern>
</defs>
<rect x="0" y="0" width="640" height="520" fill="url(#p-grid)"/>

<!-- frame label -->
<text x="20" y="28" {_T} font-size="11" letter-spacing="2" fill="{mut}">ENTERPRISE LANDSCAPE</text>
<line x1="20" y1="38" x2="620" y2="38" stroke="{bd}"/>

<!-- Integration lines (drawn first, under boxes) -->
<g fill="none" stroke="{acc}" stroke-width="1.25">
  <path d="M320 212V160"/>
  <path d="M320 308v52"/>
  <path d="M232 260H150"/>
  <path d="M408 260h82"/>
  <path d="M258 212L170 160"/>
  <path d="M382 212l88-52"/>
  <path d="M258 308l-88 52"/>
  <path d="M382 308l88 52"/>
</g>
<g fill="{acc}"><circle cx="320" cy="160" r="3"/><circle cx="320" cy="360" r="3"/><circle cx="150" cy="260" r="3"/><circle cx="490" cy="260" r="3"/><circle cx="170" cy="160" r="3"/><circle cx="470" cy="160" r="3"/><circle cx="170" cy="360" r="3"/><circle cx="470" cy="360" r="3"/></g>

<!-- Core -->
<rect x="232" y="212" width="176" height="96" fill="{navy}"/>
<text x="320" y="248" text-anchor="middle" {_S} font-size="20" fill="#fff">SAP S/4HANA</text>
<text x="320" y="270" text-anchor="middle" {_T} font-size="11" letter-spacing="1.5" fill="#b9c3dc">DIGITAL CORE</text>
<text x="320" y="292" text-anchor="middle" {_T} font-size="10.5" fill="#b9c3dc">FI/CO · MM · SD · PP · QM · EWM</text>

<!-- Top: planning -->
<rect x="60" y="70" width="220" height="90" fill="{paper}" stroke="{bd}"/>
<text x="76" y="94" {_T} font-size="10" letter-spacing="1.5" fill="{mut}">PLANNING</text>
<text x="76" y="116" {_S} font-size="15" fill="{ink}">SAP IBP</text>
<text x="76" y="138" {_T} font-size="11.5" fill="{mut}">S&amp;OP · Demand · Inventory · Response</text>
<text x="76" y="152" {_T} font-size="11.5" fill="{mut}">Embedded PP/DS (ePPDS)</text>

<rect x="360" y="70" width="220" height="90" fill="{paper}" stroke="{bd}"/>
<text x="376" y="94" {_T} font-size="10" letter-spacing="1.5" fill="{mut}">SERIALIZATION</text>
<text x="376" y="116" {_S} font-size="15" fill="{ink}">Advanced Track &amp; Trace</text>
<text x="376" y="138" {_T} font-size="11.5" fill="{mut}">Pharma serialization · Country packs</text>
<text x="376" y="152" {_T} font-size="11.5" fill="{mut}">Regulatory reporting (EPCIS)</text>

<!-- Sides -->
<rect x="20" y="222" width="130" height="76" fill="{paper}" stroke="{bd}"/>
<text x="34" y="244" {_T} font-size="10" letter-spacing="1.5" fill="{mut}">EXPERIENCE</text>
<text x="34" y="266" {_S} font-size="14" fill="{ink}">SAP Fiori / UI5</text>
<text x="34" y="284" {_T} font-size="11" fill="{mut}">Role-based apps</text>

<rect x="490" y="222" width="130" height="76" fill="{paper}" stroke="{bd}"/>
<text x="504" y="244" {_T} font-size="10" letter-spacing="1.5" fill="{mut}">NON-SAP</text>
<text x="504" y="266" {_S} font-size="14" fill="{ink}">Third-party apps</text>
<text x="504" y="284" {_T} font-size="11" fill="{mut}">APIs · Connectors</text>

<!-- Bottom: people & compliance -->
<rect x="60" y="360" width="220" height="90" fill="{paper}" stroke="{bd}"/>
<text x="76" y="384" {_T} font-size="10" letter-spacing="1.5" fill="{mut}">PEOPLE</text>
<text x="76" y="406" {_S} font-size="15" fill="{ink}">SuccessFactors · Workday</text>
<text x="76" y="428" {_T} font-size="11.5" fill="{mut}">Core HR · Payroll · Talent</text>
<text x="76" y="442" {_T} font-size="11.5" fill="{mut}">Integrations to ERP and benefits</text>

<rect x="360" y="360" width="220" height="90" fill="{paper}" stroke="{bd}"/>
<text x="376" y="384" {_T} font-size="10" letter-spacing="1.5" fill="{mut}">COMPLIANCE TRAINING</text>
<text x="376" y="406" {_S} font-size="15" fill="{ink}">ComplianceWire LMS</text>
<text x="376" y="428" {_T} font-size="11.5" fill="{mut}">GxP · 21 CFR Part 11 · Audit trails</text>
<text x="376" y="442" {_T} font-size="11.5" fill="{mut}">Role-based curricula</text>

<!-- Foundation band -->
<rect x="20" y="474" width="600" height="30" fill="#eeece6"/>
<text x="34" y="493" {_T} font-size="10.5" letter-spacing="1.5" fill="{ink}">MANAGED SERVICES</text>
<text x="606" y="493" text-anchor="end" {_T} font-size="10.5" fill="{mut}">Monitoring · Upgrades · Support · Cloud (AWS / Azure / GCP / private)</text>
</svg>'''


def ecosystem_diagram():
    """Navy-band diagram: how SAP, data, cloud, automation and non-SAP connect."""
    line = "rgba(255,255,255,.28)"
    txt = "#ffffff"
    mut = "#b9c3dc"
    acc = "#9db5e6"
    return f'''<svg viewBox="0 0 720 420" role="img" aria-labelledby="eco-t eco-d" xmlns="http://www.w3.org/2000/svg">
<title id="eco-t">How the pieces connect</title>
<desc id="eco-d">Layered diagram: experience layer on top, SAP core and extensions in the middle connected to non-SAP systems through integration, with data, cloud and automation as the foundation.</desc>
<g {_T} font-size="10.5" letter-spacing="1.5" fill="{mut}">
  <text x="24" y="40">EXPERIENCE</text>
  <text x="24" y="150">APPLICATIONS</text>
  <text x="24" y="282">INTEGRATION</text>
  <text x="24" y="368">FOUNDATION</text>
</g>
<g stroke="{line}"><line x1="24" y1="52" x2="696" y2="52"/><line x1="24" y1="162" x2="696" y2="162"/><line x1="24" y1="294" x2="696" y2="294"/><line x1="24" y1="380" x2="696" y2="380"/></g>

<!-- Experience -->
<g fill="none" stroke="{txt}" stroke-width="1">
  <rect x="140" y="64" width="150" height="56"/><rect x="310" y="64" width="150" height="56"/><rect x="480" y="64" width="150" height="56"/>
</g>
<g {_T} font-size="12" fill="{txt}" text-anchor="middle">
  <text x="215" y="88">SAP Fiori apps</text><text x="385" y="88">Portals &amp; mobile</text><text x="555" y="88">Dashboards</text>
</g>
<g {_T} font-size="10.5" fill="{mut}" text-anchor="middle">
  <text x="215" y="106">Role-based, UI5</text><text x="385" y="106">Employee / partner</text><text x="555" y="106">Analytics &amp; KPIs</text>
</g>

<!-- Applications -->
<rect x="140" y="176" width="275" height="98" fill="{txt}"/>
<text x="156" y="200" {_S} font-size="16" fill="#1d3770">SAP S/4HANA</text>
<text x="156" y="220" {_T} font-size="11" fill="#3d4352">Finance · Procurement · Sales · Manufacturing</text>
<g {_T} font-size="10.5" fill="#1d3770"><text x="156" y="246">+ IBP</text><text x="200" y="246">+ ePPDS</text><text x="254" y="246">+ ATTP</text><text x="306" y="246">+ SuccessFactors</text></g>
<text x="156" y="264" {_T} font-size="10.5" fill="#5f6577">Extensions, custom ABAP, Business One</text>

<g fill="none" stroke="{txt}" stroke-width="1"><rect x="430" y="176" width="200" height="44"/><rect x="430" y="230" width="200" height="44"/></g>
<text x="446" y="196" {_T} font-size="12" fill="{txt}">Non-SAP systems</text>
<text x="446" y="212" {_T} font-size="10" fill="{mut}">Workday · CRM · MES</text>
<text x="446" y="250" {_T} font-size="12" fill="{txt}">Compliance &amp; LMS</text>
<text x="446" y="266" {_T} font-size="10" fill="{mut}">ComplianceWire · EDMS</text>

<!-- Integration connectors -->
<g stroke="{acc}" stroke-width="1.25" fill="none">
  <path d="M415 198h15"/><path d="M415 252h15"/>
  <path d="M215 120v56"/><path d="M385 120v56"/><path d="M555 120v56"/>
  <path d="M270 274v30"/><path d="M530 274v30"/>
</g>
<g fill="{acc}"><circle cx="422" cy="198" r="2.5"/><circle cx="422" cy="252" r="2.5"/></g>
<g fill="none" stroke="{txt}" stroke-width="1" stroke-dasharray="3 3"><rect x="140" y="304" width="490" height="60"/></g>
<g {_T} font-size="11.5" fill="{txt}">
  <text x="156" y="330">APIs &amp; OData</text><text x="276" y="330">IDoc / RFC</text><text x="376" y="330">Middleware &amp; connectors</text><text x="546" y="330">File &amp; EDI</text>
</g>
<text x="156" y="350" {_T} font-size="10.5" fill="{mut}">Process-to-process · On-premise to cloud · Third-party applications</text>

<!-- Foundation -->
<g {_T} font-size="11.5" fill="{txt}">
  <text x="140" y="404">Data &amp; master data</text><text x="310" y="404">Cloud (AWS · Azure · GCP · private)</text><text x="548" y="404">Automation &amp; monitoring</text>
</g>
</svg>'''


def method_diagram():
    """Small horizontal delivery flow for the About page."""
    return f'''<svg viewBox="0 0 720 120" role="img" aria-label="Delivery flow: assess, design, build and migrate, run and improve" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="40" x2="690" y2="40" stroke="#dcd9d1"/>
<g fill="#f7f6f2" stroke="#2e5aac" stroke-width="2"><circle cx="30" cy="40" r="6"/><circle cx="250" cy="40" r="6"/><circle cx="470" cy="40" r="6"/><circle cx="690" cy="40" r="6"/></g>
<g {_S} font-size="15" fill="#171b26"><text x="30" y="76">Assess</text><text x="250" y="76">Design</text><text x="470" y="76">Build &amp; migrate</text><text x="690" y="76" text-anchor="end">Run &amp; improve</text></g>
<g {_T} font-size="11" fill="#5f6577"><text x="30" y="96">Landscape, risks, sizing</text><text x="250" y="96">Blueprint, scope, plan</text><text x="470" y="96">Configure, develop, test</text><text x="690" y="96" text-anchor="end">Support, upgrades, AMS</text></g>
</svg>'''


def industry_mini(kind):
    """Tiny schematic per industry (restrained line drawings)."""
    base = 'viewBox="0 0 240 120" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#1d3770" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"'
    shapes = {
        "automotive": '<path d="M20 80h200M40 80l16-26h78l30 26"/><circle cx="70" cy="86" r="8"/><circle cx="160" cy="86" r="8"/><path d="M60 54v26M110 54v26M150 60l8 20"/><path d="M190 40h30M200 30h20M210 20h10" stroke="#2e5aac"/>',
        "manufacturing": '<path d="M20 100V60l30 18V60l30 18V60l30 18V30h20v70H20z"/><path d="M40 90h8M70 90h8M100 90h8"/><path d="M160 100V50h60v50"/><path d="M170 70h40M170 85h40" stroke="#2e5aac"/><path d="M180 50V30h20v20"/>',
        "logistics": '<path d="M20 90h140V50H20zM160 62h30l20 20v8h-50z"/><circle cx="50" cy="96" r="7"/><circle cx="185" cy="96" r="7"/><path d="M60 70h60" stroke="#2e5aac"/><path d="M60 60h30M60 80h40"/>',
        "healthcare": '<path d="M40 100V40h60v60M100 60h50v40M20 100h200"/><path d="M70 55v20M60 65h20" stroke="#2e5aac"/><path d="M160 30c10-12 30-8 30 6 0 12-30 30-30 30s-30-18-30-30c0-14 20-18 30-6z" stroke="#2e5aac"/>',
        "banking": '<path d="M30 100h180M40 92h160M50 50v42M80 50v42M120 50v42M160 50v42M190 50v42M30 50l90-30 90 30H30z"/><path d="M110 70h20M100 80h40" stroke="#2e5aac"/>',
        "realestate": '<path d="M30 100V40l40-20 40 20v60M70 100V70h20v30M140 100V60h70v40M150 75h10M170 75h10M190 75h10M150 88h10M170 88h10"/><path d="M20 100h200"/><path d="M30 40h80" stroke="#2e5aac" stroke-dasharray="3 3"/>',
        "pharma": '<rect x="30" y="40" width="90" height="40" rx="20" transform="rotate(-30 75 60)"/><path d="M58 70l34-20" stroke="#2e5aac"/><path d="M150 30v70M165 30v70M180 30v70M195 30v70M210 30v70M158 30v40M188 30v40M203 30v40" stroke="#1d3770"/>',
    }
    return f"<svg {base}>{shapes[kind]}</svg>"


def service_diagram(kind):
    """Per-service schematic shown in the service header's right column."""
    b = 'xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true"'
    n, a, bd, mut, ink, paper = "#1d3770", "#2e5aac", "#dcd9d1", "#5f6577", "#171b26", "#ffffff"
    box = lambda x, y, w, h, t, s="", fill=paper, col=ink: (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{bd}"/>'
        f'<text x="{x+12}" y="{y+22}" {_T} font-size="12" fill="{col}">{t}</text>'
        + (f'<text x="{x+12}" y="{y+38}" {_T} font-size="10.5" fill="{mut if fill==paper else "#b9c3dc"}">{s}</text>' if s else "")
    )
    d = {
        "development": f'''<svg viewBox="0 0 420 240" {b}>
{box(20,20,170,50,"Business requirement","Process gap or new capability")}
{box(230,20,170,50,"Design &amp; prototype","Fiori / ABAP / BTP")}
{box(20,110,170,50,"Build &amp; test","Unit · integration · UAT")}
{box(230,110,170,50,"Transport &amp; release","Change control")}
{box(20,190,380,36,"Operate in S/4HANA","",n,"#fff")}
<g stroke="{a}" stroke-width="1.25" fill="none"><path d="M190 45h40"/><path d="M315 70v40"/><path d="M230 135h-40"/><path d="M105 160v30"/></g>
<g fill="{a}"><circle cx="230" cy="45" r="2.5"/><circle cx="315" cy="110" r="2.5"/><circle cx="190" cy="135" r="2.5"/><circle cx="105" cy="190" r="2.5"/></g></svg>''',
        "migration": f'''<svg viewBox="0 0 420 240" {b}>
{box(20,30,150,60,"Source landscape","ECC · AnyDB · OS")}
{box(250,30,150,60,"Target landscape","S/4HANA · HANA · cloud")}
<g stroke="{a}" stroke-width="1.25" fill="none"><path d="M170 60h80"/><path d="M243 54l7 6-7 6"/></g>
<g {_T} font-size="10.5" fill="{mut}"><text x="20" y="130">OS layer</text><text x="20" y="160">Database layer</text><text x="20" y="190">Application layer</text><text x="20" y="220">Custom code &amp; data</text></g>
<g stroke="{bd}"><line x1="130" y1="126" x2="400" y2="126"/><line x1="130" y1="156" x2="400" y2="156"/><line x1="130" y1="186" x2="400" y2="186"/><line x1="130" y1="216" x2="400" y2="216"/></g>
<g fill="{a}"><rect x="130" y="122" width="90" height="8"/><rect x="130" y="152" width="150" height="8"/><rect x="130" y="182" width="220" height="8"/><rect x="130" y="212" width="270" height="8"/></g></svg>''',
        "management": f'''<svg viewBox="0 0 420 240" {b}>
<circle cx="210" cy="120" r="78" fill="none" stroke="{bd}"/>
<circle cx="210" cy="120" r="44" fill="{n}"/>
<text x="210" y="116" text-anchor="middle" {_T} font-size="11" fill="#fff">SAP</text><text x="210" y="131" text-anchor="middle" {_T} font-size="11" fill="#b9c3dc">landscape</text>
<g {_T} font-size="11" fill="{ink}" text-anchor="middle"><text x="210" y="30">Monitor</text><text x="330" y="124">Support</text><text x="210" y="222">Patch &amp; upgrade</text><text x="90" y="124">Enhance</text></g>
<g fill="{a}"><circle cx="210" cy="42" r="3"/><circle cx="288" cy="120" r="3"/><circle cx="210" cy="198" r="3"/><circle cx="132" cy="120" r="3"/></g>
<text x="20" y="235" {_T} font-size="10.5" fill="{mut}">Continuous application management, SLA-driven</text></svg>''',
        "s4hana": f'''<svg viewBox="0 0 420 240" {b}>
<g {_T} font-size="10.5" fill="{mut}"><text x="20" y="34">Assess &amp; size</text><text x="20" y="84">Choose path</text><text x="20" y="134">Clean &amp; convert</text><text x="20" y="184">Go-live &amp; adopt</text></g>
<g stroke="{bd}"><line x1="130" y1="40" x2="400" y2="40"/><line x1="130" y1="90" x2="400" y2="90"/><line x1="130" y1="140" x2="400" y2="140"/><line x1="130" y1="190" x2="400" y2="190"/></g>
<g fill="{a}"><rect x="130" y="24" width="60" height="10"/><rect x="190" y="74" width="80" height="10"/><rect x="270" y="124" width="90" height="10"/><rect x="360" y="174" width="40" height="10"/></g>
<g {_T} font-size="10" fill="{ink}"><text x="196" y="33">Greenfield · Brownfield · Selective</text></g>
<text x="20" y="226" {_T} font-size="10.5" fill="{mut}">Phased conversion with data reduction before migration</text></svg>''',
        "fiori": f'''<svg viewBox="0 0 420 240" {b}>
<rect x="20" y="20" width="380" height="200" fill="{paper}" stroke="{bd}"/>
<rect x="20" y="20" width="380" height="32" fill="{n}"/>
<text x="34" y="41" {_T} font-size="11" fill="#fff">My Approvals</text>
<g fill="#eeece6"><rect x="36" y="68" width="100" height="56"/><rect x="152" y="68" width="100" height="56"/><rect x="268" y="68" width="116" height="56"/><rect x="36" y="140" width="216" height="64"/><rect x="268" y="140" width="116" height="64"/></g>
<g {_T} font-size="10.5" fill="{ink}"><text x="46" y="88">Purchase orders</text><text x="162" y="88">Leave requests</text><text x="278" y="88">Invoices</text><text x="46" y="160">Open items</text><text x="278" y="160">KPIs</text></g>
<g fill="{a}"><rect x="46" y="100" width="40" height="6"/><rect x="162" y="100" width="28" height="6"/><rect x="278" y="100" width="60" height="6"/></g></svg>''',
        "ibp": f'''<svg viewBox="0 0 420 240" {b}>
<path d="M30 200V30M30 200h370" stroke="{bd}"/>
<path d="M40 160l40-20 40 10 40-40 40 15 40-35 40 20 40-30 40 10" fill="none" stroke="{n}" stroke-width="1.5"/>
<path d="M40 170l40-10 40 5 40-30 40 8 40-28 40 12 40-22 40 4" fill="none" stroke="{a}" stroke-width="1.25" stroke-dasharray="4 3"/>
<g {_T} font-size="10.5" fill="{mut}"><text x="40" y="222">Demand</text><text x="160" y="222">Supply</text><text x="280" y="222">Inventory</text><text x="360" y="222">Response</text></g>
<g {_T} font-size="10.5"><text x="300" y="40" fill="{n}">— Actual</text><text x="300" y="56" fill="{a}">- - Plan</text></g></svg>''',
        "eppds": f'''<svg viewBox="0 0 420 240" {b}>
<g {_T} font-size="10.5" fill="{mut}"><text x="20" y="48">Line 1</text><text x="20" y="98">Line 2</text><text x="20" y="148">Line 3</text><text x="20" y="198">Bottleneck</text></g>
<g stroke="{bd}"><line x1="90" y1="54" x2="400" y2="54"/><line x1="90" y1="104" x2="400" y2="104"/><line x1="90" y1="154" x2="400" y2="154"/><line x1="90" y1="204" x2="400" y2="204"/></g>
<g fill="{n}"><rect x="90" y="36" width="90" height="14"/><rect x="200" y="36" width="60" height="14"/><rect x="110" y="86" width="140" height="14"/><rect x="90" y="136" width="50" height="14"/><rect x="160" y="136" width="120" height="14"/></g>
<g fill="{a}"><rect x="280" y="36" width="100" height="14"/><rect x="270" y="86" width="110" height="14"/><rect x="300" y="136" width="80" height="14"/><rect x="90" y="186" width="310" height="14" opacity=".35"/></g>
<text x="20" y="232" {_T} font-size="10.5" fill="{mut}">Finite scheduling against resource capacity</text></svg>''',
        "attp": f'''<svg viewBox="0 0 420 240" {b}>
<g fill="{n}"><rect x="30" y="40" width="4" height="60"/><rect x="38" y="40" width="2" height="60"/><rect x="44" y="40" width="6" height="60"/><rect x="54" y="40" width="2" height="60"/><rect x="60" y="40" width="4" height="60"/><rect x="68" y="40" width="2" height="60"/><rect x="74" y="40" width="6" height="60"/><rect x="84" y="40" width="2" height="60"/><rect x="90" y="40" width="4" height="60"/></g>
<text x="30" y="120" {_T} font-size="10.5" fill="{mut}">GTIN · Serial · Lot · Expiry</text>
{box(140,30,120,44,"Unit","serial number")}
{box(140,100,120,44,"Case","aggregation")}
{box(140,170,120,44,"Pallet","SSCC")}
<g stroke="{a}" stroke-width="1.25"><path d="M200 74v26M200 144v26"/></g>
{box(290,30,110,44,"Regulators","EPCIS reports")}
{box(290,100,110,44,"Partners","3PL · wholesalers")}
{box(290,170,110,44,"ERP","order &amp; delivery")}
<g stroke="{a}" stroke-width="1.25" fill="none"><path d="M260 52h30M260 122h30M260 192h30"/></g></svg>''',
        "compliancewire": f'''<svg viewBox="0 0 420 240" {b}>
{box(20,20,120,44,"Role","Job function")}
{box(150,20,120,44,"Curriculum","SOPs · modules")}
{box(280,20,120,44,"Assignment","Automated")}
<g stroke="{a}" stroke-width="1.25" fill="none"><path d="M140 42h10M270 42h10"/></g>
{box(20,100,380,44,"Training record · e-signature · audit trail","21 CFR Part 11 · EU Annex 11",n,"#fff")}
<g {_T} font-size="10.5" fill="{mut}"><text x="20" y="180">Completion</text><text x="20" y="206">Overdue</text></g>
<g stroke="{bd}"><line x1="110" y1="176" x2="400" y2="176"/><line x1="110" y1="202" x2="400" y2="202"/></g>
<g fill="{a}"><rect x="110" y="171" width="240" height="8"/><rect x="110" y="197" width="40" height="8" opacity=".5"/></g>
<text x="20" y="232" {_T} font-size="10.5" fill="{mut}">Dashboards configured for inspection readiness</text></svg>''',
        "workday": f'''<svg viewBox="0 0 420 240" {b}>
<rect x="150" y="90" width="120" height="60" fill="{n}"/>
<text x="210" y="116" text-anchor="middle" {_T} font-size="12" fill="#fff">Workday HCM</text><text x="210" y="134" text-anchor="middle" {_T} font-size="10.5" fill="#b9c3dc">Core HR · Payroll · Talent</text>
{box(20,20,120,44,"Studio","Complex, high volume")}
{box(280,20,120,44,"Cloud Connect","Pre-packaged")}
{box(20,176,120,44,"EIB","File-based")}
{box(280,176,120,44,"Web services","SOAP · REST")}
<g stroke="{a}" stroke-width="1.25" fill="none"><path d="M140 42l40 48M280 42l-40 48M140 198l40-48M280 198l-40-48"/></g></svg>''',
        "successfactors": f'''<svg viewBox="0 0 420 240" {b}>
{box(20,20,380,44,"Employee Central","Core HR · Payroll · Time",n,"#fff")}
{box(20,84,120,52,"Recruiting","&amp; Onboarding")}
{box(150,84,120,52,"Performance","&amp; Goals")}
{box(280,84,120,52,"Learning","&amp; Succession")}
<g stroke="{a}" stroke-width="1.25" fill="none"><path d="M80 64v20M210 64v20M340 64v20"/></g>
<g {_T} font-size="10.5" fill="{mut}"><text x="20" y="170">Integrates with</text></g>
<g {_T} font-size="11" fill="{ink}"><text x="20" y="196">S/4HANA</text><text x="110" y="196">Payroll providers</text><text x="240" y="196">Identity</text><text x="320" y="196">Benefits</text></g>
<line x1="20" y1="206" x2="400" y2="206" stroke="{bd}"/></svg>''',
    }
    return d[kind]
