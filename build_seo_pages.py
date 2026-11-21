#!/usr/bin/env python3
"""Genera le pagine per città di MediS (pulizia vetrate per aziende in Trentino),
le pagine di rimando per gli indirizzi non più usati e la sitemap.

Esegui:  python3 build_seo_pages.py
"""
import json
from datetime import date

SITE = "https://medistn.it"
TODAY = date.today().isoformat()

WA = "https://wa.me/393519878991?text=Ciao%20Matteo%2C%20vorrei%20un%20preventivo%20per%20la%20pulizia%20delle%20vetrate%20della%20mia%20attivit%C3%A0."

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
  <meta property="og:image" content="__SITE__/og-image.png" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="zone.css" />
  <script type="application/ld+json">__JSONLD__</script>
</head>
<body>
  <div class="wrap">
    <header class="top">
      <a class="brand" href="/"><img src="logo.png" alt="" width="42" height="38" /><span>MediS</span></a>
      <a class="top__home" href="/">Torna alla home</a>
    </header>

    <div class="hero">
      <span class="hero__badge">__BADGE__</span>
      <h1>__H1__</h1>
      <p class="lead">__LEAD__</p>
      <div class="cta">
        <a class="btn btn--primary" href="tel:+393519878991">Chiama 351 987 8991</a>
        <a class="btn" href="__WA__" target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn" href="mailto:info@medistn.it?subject=Richiesta%20preventivo%20vetrate">Email</a>
      </div>
    </div>

__BODY__

    <section>
      <h2>In tutto il Trentino</h2>
      <p>__OTHER__</p>
      <div class="zones">__ZONES__</div>
    </section>

    <footer>
      <p>MediS di Deromedis Matteo, Altopiano della Vigolana (TN)<br />
      P. IVA 02581560220<br />
      <a href="/">medistn.it</a> <span aria-hidden="true">|</span> <a href="https://www.instagram.com/8_medis_9/" target="_blank" rel="noopener">Instagram</a></p>
    </footer>
  </div>
</body>
</html>
"""

REDIRECT = """<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="refresh" content="0; url=/" />
  <link rel="canonical" href="__SITE__/" />
  <meta name="robots" content="noindex, follow" />
  <title>MediS: pulizia vetrate per aziende in Trentino</title>
</head>
<body>
  <p>Questa pagina è stata spostata. Vai a <a href="/">MediS, pulizia vetrate per aziende in Trentino</a>.</p>
</body>
</html>
"""


def section(title, html):
    return f"    <section>\n      <h2>{title}</h2>\n{html}\n    </section>"


def p(text):
    return f"      <p>{text}</p>"


def ul(items):
    lis = "\n".join(f"        <li>{i}</li>" for i in items)
    return f'      <ul class="list">\n{lis}\n      </ul>'


METODO = (
    p("Per le vetrate esterne uso aste telescopiche in carbonio con acqua demineralizzata: "
      "l’acqua passa attraverso resine a scambio ionico che tolgono calcare e minerali, così il vetro "
      "asciuga da solo, senza aloni e senza residui di detergente. Fino al secondo piano lavoro da terra, "
      "senza cestello e senza scale davanti all’ingresso.") + "\n" +
    p("Le aste non sono la soluzione per tutto: servono spazio a terra e un accesso libero. Con tettoie, "
      "tende, balconi, vetrate più alte o sporco ostinato come silicone e residui di cantiere servono "
      "altri strumenti e il lavoro a mano. Quando ci incontriamo valutiamo insieme come procedere.")
)

PREVENTIVO = p(
    'Chiamami al <a href="tel:+393519878991">351 987 8991</a> oppure scrivimi '
    '<a href="' + WA + '" target="_blank" rel="noopener">su WhatsApp</a>: organizziamo un incontro per conoscerci '
    'e valutare insieme l’intervento, poi ti preparo un preventivo chiaro e senza impegno.'
)

PAGES = [
    {
        "slug": "lavavetri-trento",
        "place": "Trento",
        "h1": "Pulizia vetrate per aziende a Trento",
        "badge": "Trento e dintorni",
        "title": "Pulizia vetrate per aziende a Trento | MediS",
        "desc": "Pulizia di vetrate, vetrine e facciate in vetro per negozi, showroom, hotel e aziende a Trento. Fino al 2° piano da terra, anche fuori orario.",
        "lead": "Vetrine di negozi, vetrate di showroom, ingressi di hotel e facciate di sedi aziendali: a Trento pulisco le grandi superfici vetrate delle attività, con acqua demineralizzata e un risultato senza aloni.",
        "sections": [
            ("Vetrate pulite per le attività di Trento",
             p("In una città dove tanti negozi si affacciano sulla strada, la vetrina è la prima cosa che un cliente vede. "
               "Un vetro opaco o rigato dà un’impressione trascurata anche al negozio più curato; una vetrata trasparente "
               "fa entrare luce e mette in risalto quello che vendi.") + "\n" +
             p("Parto dall’Altopiano della Vigolana e raggiungo Trento in poco tempo: per questo posso seguire con "
               "regolarità le attività della città, con passaggi programmati e orari concordati.")),
            ("Cosa pulisco a Trento", ul([
                "Vetrine e porte a vetro di negozi",
                "Grandi vetrate di showroom e concessionarie",
                "Ingressi, sale e dehors in vetro di hotel, bar e ristoranti",
                "Facciate vetrate e ingressi di rappresentanza di sedi aziendali",
                "Telai e profili, lavati insieme al vetro",
            ])),
            ("Il metodo", METODO),
            ("Anche prima dell’apertura", p(
                "Per non disturbare i tuoi clienti posso lavorare prima dell’apertura, la sera o nel giorno di chiusura: "
                "basta programmare insieme l’intervento. Puoi scegliere un passaggio singolo oppure una frequenza fissa, "
                "per esempio ogni mese o a ogni cambio di stagione.")),
            ("Non solo vetri", p(
                "Per migliorare l’immagine del tuo negozio mi occupo anche di riqualificazione interni, con pellicole "
                "decorative che rinnovano banconi, porte, pareti e reception senza smontare nulla, e di pellicole per vetri "
                "a controllo solare. <a href=\"/#cosa-faccio\">Scopri tutti i servizi</a>.")),
            ("Conosciamoci", PREVENTIVO),
        ],
        "other": "Oltre a Trento lavoro con le attività di tutta la provincia, dalla Vallagarina alla Valsugana.",
    },
    {
        "slug": "lavavetri-rovereto",
        "place": "Rovereto",
        "h1": "Pulizia vetrate per aziende a Rovereto",
        "badge": "Rovereto e Vallagarina",
        "title": "Pulizia vetrate per aziende a Rovereto | MediS",
        "desc": "Pulizia di vetrate e vetrine per negozi, showroom, hotel e aziende a Rovereto e in Vallagarina. Acqua demineralizzata, anche fuori orario.",
        "lead": "A Rovereto e in Vallagarina curo le superfici vetrate di negozi, showroom, attività ricettive e aziende: vetrine trasparenti e ingressi in ordine, con interventi singoli o programmati.",
        "sections": [
            ("Per le attività di Rovereto e della Vallagarina",
             p("Dalle vetrine del centro alle grandi vetrate delle zone commerciali, ogni attività ha esigenze diverse: "
               "c’è chi ha bisogno di una vetrina sempre perfetta per i clienti e chi di una pulizia periodica di superfici "
               "ampie, anche su più livelli.") + "\n" +
             p("Per le attività di Rovereto organizzo volentieri passaggi programmati: concordiamo una volta la frequenza "
               "e gli orari, e poi penso io a tutto, senza che tu debba chiamarmi ogni volta.")),
            ("Le superfici che curo", ul([
                "Vetrine su strada e ingressi di negozi",
                "Vetrate di showroom, concessionarie e spazi espositivi",
                "Vetrate di hotel, ristoranti e palestre",
                "Facciate e ingressi di sedi aziendali, fino al secondo piano da terra",
                "Telai e profili, insieme al vetro",
            ])),
            ("Acqua pura, senza detergenti", METODO),
            ("Orari che non disturbano", p(
                "Posso intervenire prima dell’apertura, la sera o nel giorno di chiusura: il lavoro si fa quando il "
                "negozio è vuoto e i tuoi clienti trovano le vetrate già pulite.")),
            ("Rinnovare l’immagine del negozio", p(
                "Oltre alla pulizia propongo la riqualificazione interni con pellicole decorative effetto legno, pietra, "
                "metallo o colore, e pellicole per vetri a controllo solare per gli spazi esposti al sole. "
                "<a href=\"/#cosa-faccio\">Vedi tutti i servizi</a>.")),
            ("Conosciamoci", PREVENTIVO),
        ],
        "other": "Oltre a Rovereto e alla Vallagarina lavoro con le attività di tutta la provincia di Trento.",
    },
]

# Indirizzi non più usati: rimandano alla home
REDIRECTS = [
    "lavavetri-pergine-valsugana",
    "lavavetri-altopiano-della-vigolana",
    "pulizia-pannelli-fotovoltaici-trentino",
]


def jsonld(page):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "Pulizia vetrate per aziende",
        "name": page["h1"],
        "description": page["desc"],
        "areaServed": [
            {"@type": "City", "name": page["place"]},
            {"@type": "AdministrativeArea", "name": "Trentino"},
        ],
        "audience": {"@type": "BusinessAudience", "name": "Negozi, showroom, hotel, ristoranti e aziende"},
        "url": f'{SITE}/{page["slug"]}.html',
        "provider": {"@id": f"{SITE}/#business", "@type": "LocalBusiness", "name": "MediS",
                     "telephone": "+39 351 987 8991", "email": "info@medistn.it", "url": f"{SITE}/",
                     "image": f"{SITE}/og-image.png", "areaServed": "Trentino"},
    }, ensure_ascii=False, indent=2)


def zones_links(current):
    links = ['<a href="/">Home: tutti i servizi</a>']
    for q in PAGES:
        if q["slug"] != current:
            links.append(f'<a href="{q["slug"]}.html">{q["h1"]}</a>')
    return "\n        ".join(links)


def render(page):
    body = "\n\n".join(section(t, h) for t, h in page["sections"])
    repl = {
        "__TITLE__": page["title"], "__DESC__": page["desc"], "__SITE__": SITE, "__SLUG__": page["slug"],
        "__PLACE__": page["place"], "__BADGE__": page["badge"], "__H1__": page["h1"], "__LEAD__": page["lead"],
        "__BODY__": body, "__ZONES__": zones_links(page["slug"]), "__OTHER__": page["other"],
        "__JSONLD__": jsonld(page), "__WA__": WA,
    }
    html = TEMPLATE
    for k, v in repl.items():
        html = html.replace(k, v)
    return html


def main():
    for page in PAGES:
        with open(f'{page["slug"]}.html', "w", encoding="utf-8") as f:
            f.write(render(page))
        print("scritta", page["slug"] + ".html")
    for slug in REDIRECTS:
        with open(f"{slug}.html", "w", encoding="utf-8") as f:
            f.write(REDIRECT.replace("__SITE__", SITE))
        print("rimando", slug + ".html")

    urls = [(f"{SITE}/", "1.0")] + [(f'{SITE}/{p["slug"]}.html', "0.8") for p in PAGES]
    items = "\n".join(
        f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>monthly</changefreq>\n"
        f"    <priority>{pr}</priority>\n  </url>" for u, pr in urls)
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                f"{items}\n</urlset>\n")
    print("scritta sitemap.xml")


if __name__ == "__main__":
    main()
