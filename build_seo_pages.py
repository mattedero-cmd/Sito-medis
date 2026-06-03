#!/usr/bin/env python3
"""Genera le pagine SEO per zona di MediS (lavavetri in Trentino) + sitemap.
Esegui:  python3 build_seo_pages.py
"""
import json

SITE = "https://medistn.it"

TEMPLATE = """<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>__TITLE__</title>
  <meta name="description" content="__DESC__" />
  <link rel="canonical" href="__SITE__/__SLUG__.html" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="theme-color" content="#07100f" />
  <meta name="geo.region" content="IT-TN" />
  <meta name="geo.placename" content="__PLACE__" />
  <link rel="icon" href="logo.png" />
  <link rel="apple-touch-icon" href="logo.png" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="MediS" />
  <meta property="og:locale" content="it_IT" />
  <meta property="og:url" content="__SITE__/__SLUG__.html" />
  <meta property="og:title" content="__TITLE__" />
  <meta property="og:description" content="__DESC__" />
  <meta property="og:image" content="__SITE__/logo.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Caveat:wght@700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="zone.css" />
  <script type="application/ld+json">__JSONLD__</script>
</head>
<body>
  <div class="wrap">
    <header class="top">
      <a class="brand" href="/"><img src="logo.png" alt="MediS" /><span>M<b>e</b>diS</span></a>
      <a class="top__home" href="/">← Home</a>
    </header>

    <div class="hero">
      <span class="hero__badge">📍 __BADGE__</span>
      <h1>__H1__</h1>
      <p class="lead">__LEAD__</p>
      <div class="cta">
        <a class="btn btn--primary" href="tel:+393519878991">Chiama 351 987 8991</a>
        <a class="btn" href="https://wa.me/393519878991" target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn" href="mailto:info@medistn.it">Email</a>
      </div>
    </div>

__BODY__

    <section>
      <h2>Altre zone servite</h2>
      <div class="zones">__ZONES__</div>
    </section>

    <footer>
      <p>MediS di Deromedis Matteo — Altopiano della Vigolana (TN) · P. IVA 02581560220<br />
      <a href="/">medistn.it</a> · <a href="https://www.instagram.com/8_medis_9/" target="_blank" rel="noopener">Instagram</a></p>
    </footer>
  </div>
</body>
</html>
"""

# Sezioni di contenuto riutilizzabili
def section(title, html):
    return f"    <section>\n      <h2>{title}</h2>\n{html}\n    </section>"

def p(text):
    return f"      <p>{text}</p>"

def ul(items):
    lis = "\n".join(f"        <li>{i}</li>" for i in items)
    return f'      <ul class="list">\n{lis}\n      </ul>'

INCLUSI = ul([
    "Vetrine, ingressi e porte a vetro di negozi e showroom",
    "Finestre e vetrate di abitazioni, uffici e condomini",
    "Pannelli fotovoltaici: pulizia per recuperare resa ed efficienza",
    "Superfici esposte, telai e davanzali",
    "Interventi singoli oppure programmati nel tempo",
])

PERCHE = ul([
    "Risultato senza aloni, con attrezzatura professionale",
    "Lavoro preciso, puntuale e curato nei dettagli",
    "Preventivo chiaro e concordato in anticipo",
    "Servizio per privati e attività commerciali",
])

PAGES = [
    {
        "slug": "lavavetri-trento",
        "place": "Trento",
        "area_type": "City",
        "h1": "Lavavetri a Trento",
        "badge": "Trento e dintorni",
        "title": "Lavavetri a Trento — MediS | Pulizia vetri, vetrine e fotovoltaico",
        "desc": "Lavavetri professionale a Trento: pulizia di vetrate, vetrine, finestre e pannelli fotovoltaici per case e attività. Preventivo rapido con MediS.",
        "lead": "Cerchi un lavavetri a Trento? MediS si occupa della pulizia professionale di vetri, vetrine e pannelli fotovoltaici per privati e aziende, in città e nei comuni vicini.",
        "body_intro": "A Trento curo vetrine di negozi, finestre di abitazioni e uffici, vetrate di showroom e condomini. Un vetro pulito dà subito un'immagine migliore alla tua casa o alla tua attività, e dei pannelli fotovoltaici puliti rendono di più.",
    },
    {
        "slug": "lavavetri-rovereto",
        "place": "Rovereto",
        "area_type": "City",
        "h1": "Lavavetri a Rovereto",
        "badge": "Rovereto e Vallagarina",
        "title": "Lavavetri a Rovereto — MediS | Pulizia vetri e vetrine",
        "desc": "Lavavetri a Rovereto e in Vallagarina: pulizia di vetrate, vetrine, finestre e pannelli fotovoltaici. Risultato senza aloni con MediS.",
        "lead": "Servizio di lavavetri a Rovereto e in Vallagarina: pulizia professionale di vetrine, finestre e pannelli fotovoltaici per abitazioni e attività commerciali.",
        "body_intro": "A Rovereto pulisco vetrine di negozi e showroom, finestre di case e uffici, oltre ai pannelli fotovoltaici. Interventi una tantum o programmati, per avere sempre vetri brillanti.",
    },
    {
        "slug": "lavavetri-pergine-valsugana",
        "place": "Pergine Valsugana",
        "area_type": "City",
        "h1": "Lavavetri a Pergine Valsugana",
        "badge": "Pergine e Valsugana",
        "title": "Lavavetri a Pergine Valsugana — MediS | Pulizia vetri e fotovoltaico",
        "desc": "Lavavetri a Pergine Valsugana e in Valsugana: pulizia di vetrate, vetrine, finestre e pannelli fotovoltaici. Preventivo rapido con MediS.",
        "lead": "Lavavetri a Pergine Valsugana e dintorni: pulizia di vetri, vetrine e pannelli fotovoltaici per privati e imprese, con risultato senza aloni.",
        "body_intro": "A Pergine e in Valsugana mi occupo di vetrine, finestre, vetrate e moduli fotovoltaici. Spazi più luminosi per la tua casa e una vetrina curata per la tua attività.",
    },
    {
        "slug": "lavavetri-altopiano-della-vigolana",
        "place": "Altopiano della Vigolana",
        "area_type": "City",
        "h1": "Lavavetri all'Altopiano della Vigolana",
        "badge": "Altopiano della Vigolana",
        "title": "Lavavetri Altopiano della Vigolana — MediS | Pulizia vetri",
        "desc": "Lavavetri all'Altopiano della Vigolana: pulizia di vetrate, vetrine, finestre e pannelli fotovoltaici. MediS è del posto: chiama per un preventivo.",
        "lead": "MediS è dell'Altopiano della Vigolana: lavavetri professionale per case e attività della zona, con pulizia di vetri, vetrine e pannelli fotovoltaici.",
        "body_intro": "Essendo del posto, raggiungo rapidamente abitazioni e attività dell'Altopiano della Vigolana per la pulizia di finestre, vetrine, vetrate e moduli fotovoltaici.",
    },
    {
        "slug": "pulizia-pannelli-fotovoltaici-trentino",
        "place": "Trentino",
        "area_type": "AdministrativeArea",
        "h1": "Pulizia pannelli fotovoltaici in Trentino",
        "badge": "Tutto il Trentino",
        "title": "Pulizia pannelli fotovoltaici in Trentino — MediS",
        "desc": "Pulizia professionale di pannelli fotovoltaici in tutto il Trentino: rimuove sporco e depositi per ripristinare resa ed efficienza dell'impianto. MediS.",
        "lead": "La sporcizia sui pannelli fotovoltaici riduce la produzione di energia. MediS offre la pulizia professionale dei moduli in tutto il Trentino, per ripristinare resa ed efficienza.",
        "body_intro": "Polvere, polline, foglie e depositi calcarei abbassano il rendimento dell'impianto. Con una pulizia regolare i pannelli tornano a produrre al massimo: un piccolo intervento che si ripaga in energia.",
        "fotovoltaico": True,
    },
]

def build_body(page):
    parts = []
    parts.append(section("Il servizio", p(page["body_intro"])))
    if page.get("fotovoltaico"):
        parts.append(section("Cosa comprende", ul([
            "Pulizia dei moduli con acqua pura, senza detergenti aggressivi",
            "Rimozione di polvere, polline, foglie e depositi",
            "Controllo visivo dello stato dei pannelli",
            "Interventi singoli o programmati (consigliato 1–2 volte l'anno)",
            "Impianti residenziali e aziendali",
        ])))
    else:
        parts.append(section("Cosa pulisco", INCLUSI))
    parts.append(section("Perché scegliere MediS", PERCHE))
    parts.append(section("Richiedi un preventivo", p(
        'Scrivimi o chiamami al <a href="tel:+393519878991">351 987 8991</a> '
        'oppure <a href="https://wa.me/393519878991" target="_blank" rel="noopener">su WhatsApp</a>: '
        'ti do un preventivo chiaro, senza impegno.')))
    return "\n\n".join(parts)

def jsonld(page):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "Lavavetri" if not page.get("fotovoltaico") else "Pulizia pannelli fotovoltaici",
        "name": page["h1"],
        "description": page["desc"],
        "areaServed": {"@type": page["area_type"], "name": page["place"]},
        "url": f'{SITE}/{page["slug"]}.html',
        "provider": {
            "@type": "LocalBusiness",
            "name": "MediS",
            "telephone": "+39 351 987 8991",
            "email": "info@medistn.it",
            "url": f"{SITE}/",
            "image": f"{SITE}/logo.png",
            "areaServed": "Trentino",
        },
    }, ensure_ascii=False, indent=2)

def zones_links(current):
    links = []
    for q in PAGES:
        if q["slug"] == current:
            continue
        label = q["h1"].replace("Lavavetri ", "").replace("all'", "").replace("a ", "").strip()
        links.append(f'<a href="{q["slug"]}.html">{q["h1"]}</a>')
    return "\n        ".join(links)

def render(page):
    html = TEMPLATE
    repl = {
        "__TITLE__": page["title"],
        "__DESC__": page["desc"],
        "__SITE__": SITE,
        "__SLUG__": page["slug"],
        "__PLACE__": page["place"],
        "__BADGE__": page["badge"],
        "__H1__": page["h1"],
        "__LEAD__": page["lead"],
        "__BODY__": build_body(page),
        "__ZONES__": zones_links(page["slug"]),
        "__JSONLD__": jsonld(page),
    }
    for k, v in repl.items():
        html = html.replace(k, v)
    return html

def main():
    for page in PAGES:
        fn = f'{page["slug"]}.html'
        with open(fn, "w", encoding="utf-8") as f:
            f.write(render(page))
        print("scritta", fn)

    # Sitemap con home + tutte le pagine zona
    urls = [f"{SITE}/"] + [f'{SITE}/{p["slug"]}.html' for p in PAGES]
    items = "\n".join(
        f"  <url>\n    <loc>{u}</loc>\n    <changefreq>monthly</changefreq>\n"
        f"    <priority>{'1.0' if u.endswith('/') else '0.8'}</priority>\n  </url>"
        for u in urls
    )
    sm = ('<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          f"{items}\n</urlset>\n")
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sm)
    print("scritta sitemap.xml")

if __name__ == "__main__":
    main()
