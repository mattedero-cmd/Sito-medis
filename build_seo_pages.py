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
                "Per migliorare l’immagine del tuo negozio mi occupo anche di <a href=\"riqualificazione-interni-trento.html\">riqualificazione interni</a>, con pellicole "
                "decorative che rinnovano banconi, porte, pareti e reception senza smontare nulla, e di "
                "<a href=\"pellicole-per-vetri-trento.html\">pellicole per vetri</a> solari, privacy e di sicurezza. "
                "<a href=\"/#cosa-faccio\">Scopri tutti i servizi</a>.")),
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
                "Oltre alla pulizia propongo la <a href=\"riqualificazione-interni-trento.html\">riqualificazione interni</a> con pellicole decorative effetto legno, pietra, "
                "metallo o colore, e <a href=\"pellicole-per-vetri-trento.html\">pellicole per vetri</a>: a controllo solare "
                "per gli spazi esposti al sole, privacy e di sicurezza. <a href=\"/#cosa-faccio\">Vedi tutti i servizi</a>.")),
            ("Conosciamoci", PREVENTIVO),
        ],
        "other": "Oltre a Rovereto e alla Vallagarina lavoro con le attività di tutta la provincia di Trento.",
    },
    {
        "slug": "pellicole-per-vetri-trento",
        "place": "Trento",
        "h1": "Pellicole per vetri a Trento e in Trentino",
        "badge": "Solari, privacy, sicurezza e grafiche",
        "title": "Pellicole per vetri a Trento: solari, privacy e sicurezza | MediS",
        "desc": "Pellicole per vetrate di negozi, showroom e aziende in Trentino: controllo solare, privacy, sicurezza e applicazione di grafiche per vetrine.",
        "service_type": "Applicazione pellicole per vetri",
        "offers": ["Pellicole a controllo solare", "Pellicole privacy", "Pellicole di sicurezza", "Applicazione grafiche per vetrine"],
        "lead": "Una pellicola applicata sul vetro esistente cambia il modo in cui una vetrata lavora per la tua attività: meno calore, più riservatezza, più sicurezza o una vetrina che comunica. Senza sostituire il vetro e senza lavori di muratura.",
        "sections": [
            ("Pellicole a controllo solare", p(
                "Sulle vetrate esposte al sole riducono il calore che entra e l’abbagliamento, e filtrano i raggi solari "
                "che con il tempo fanno scolorire prodotti in vetrina, arredi e pavimenti. Gli ambienti restano più "
                "luminosi e piacevoli anche d’estate, per chi ci lavora e per i clienti.") + "\n" +
             ul([
                "Vetrine e showroom esposti a sud o a ovest",
                "Sale, ingressi e reception con grandi vetrate",
                "Spazi dove il sole sugli schermi o sui banconi dà fastidio",
             ])),
            ("Pellicole privacy", p(
                "Satinate, con l’effetto di un vetro smerigliato: tengono riservati gli spazi senza "
                "togliere luce. Si possono applicare su tutta la superficie o solo in una fascia, così chi passa non vede "
                "dentro ma la vetrata resta luminosa.") + "\n" +
             ul([
                "Vetrate su strada di studi, ambulatori e spazi di consulenza",
                "Zone riservate, retro del negozio, spogliatoi e servizi",
                "Pareti vetrate interne che dividono gli ambienti",
             ])),
            ("Pellicole di sicurezza", p(
                "Se il vetro si rompe, la pellicola di sicurezza trattiene i frammenti invece di lasciarli cadere: un "
                "aiuto concreto dove passano clienti e personale, su vetrine, porte a vetro e vetrate ad altezza "
                "d’uomo.")),
            ("Grafiche per vetrine", p(
                "Applico vetrofanie e grafiche adesive con logo, orari, scritte e promozioni. Tu, la tua agenzia o la tua "
                "tipografia mi fornite la grafica pronta; io la applico con cura e senza difetti, così la "
                "vetrina comunica in modo pulito e professionale.")),
            ("Interno o esterno?", p(
                "Dipende dal tipo di vetro, da come è esposto e dalla pellicola scelta: alcune vanno applicate sul lato "
                "interno, altre funzionano meglio all’esterno. Lo valutiamo insieme caso per caso, durante il sopralluogo.")),
            ("Il vantaggio di chi pulisce vetri", p(
                "Una pellicola dura e si vede bella solo se il vetro sotto è perfettamente pulito: polvere, calcare o "
                "residui restano intrappolati per sempre. Pulire vetrate è il mio lavoro di tutti i giorni, per questo "
                "preparo il vetro con la stessa cura che metto nella pulizia, prima di ogni applicazione.") + "\n" +
             p("Posso lavorare anche prima dell’apertura, la sera o nel giorno di chiusura, per non fermare la tua attività.")),
            ("Conosciamoci", PREVENTIVO),
        ],
        "other": "Applico pellicole per vetri a Trento, Rovereto e in tutta la provincia. Mi occupo anche di pulizia vetrate e di <a href=\"riqualificazione-interni-trento.html\">riqualificazione interni</a>.",
    },
    {
        "slug": "riqualificazione-interni-trento",
        "place": "Trento",
        "h1": "Riqualificazione interni per negozi a Trento e in Trentino",
        "badge": "Pellicole decorative per arredi e superfici",
        "title": "Riqualificazione interni per negozi a Trento | MediS",
        "desc": "Rinnova banconi, porte, pareti e arredi del tuo negozio con pellicole decorative effetto legno, pietra, metallo, pelle e tessuto. Trento e Trentino.",
        "service_type": "Riqualificazione interni con pellicole decorative",
        "offers": ["Rivestimento di banconi e reception", "Rivestimento di porte e pareti", "Rivestimento di arredi ed espositori", "Rivestimento di cucine e banconi bar", "Rivestimento di ascensori, colonne e soffitti"],
        "lead": "Il tuo negozio ha un bancone segnato, porte superate o arredi che non rispecchiano più la tua immagine? Con le pellicole decorative li rinnovo senza smontarli e senza cantiere: cambiano aspetto in poco tempo, restano al loro posto.",
        "sections": [
            ("Perché riqualificare con le pellicole", p(
                "Sostituire un bancone, rifare una parete o cambiare le porte significa demolire, smaltire, aspettare e "
                "spesso chiudere. Le pellicole decorative si applicano direttamente sulle superfici esistenti: "
                "un’alternativa pulita e veloce alla sostituzione, con pochi disagi per la tua attività.") + "\n" +
             p("È il modo più semplice per dare un volto nuovo al negozio, adeguarlo a un nuovo marchio o semplicemente "
               "farlo sembrare curato come merita.")),
            ("Cosa posso rinnovare", ul([
                "Banconi, casse e reception",
                "Porte, infissi e pareti, anche in cartongesso",
                "Mobili, espositori, scaffali e tavoli",
                "Cucine, banconi bar, frigoriferi e vetrine refrigerate",
                "Interni e porte di ascensori",
                "Colonne, pilastri e soffitti",
            ])),
            ("Le finiture", ul([
                "<strong>Legno</strong>, nelle diverse essenze e tonalità",
                "<strong>Pietra e marmo</strong>, compreso l’effetto cemento",
                "<strong>Metallo</strong>: acciaio, ottone, finiture spazzolate",
                "<strong>Tinta unita</strong>, opaca o lucida",
                "<strong>Pelle e tessuto</strong>, per superfici calde al tatto e alla vista",
            ]) + "\n" + p("Al primo incontro ti mostro il catalogo delle finiture, così scegli quella giusta per il tuo locale.")),
            ("Per chi lavoro", ul([
                "Negozi e boutique che vogliono rinnovare l’immagine",
                "Bar, ristoranti e hotel: banconi, reception, sale",
                "Showroom e spazi espositivi",
                "Palestre, studi e spazi aperti al pubblico",
            ])),
            ("Come lavoro", ul([
                "<strong>Ci incontriamo</strong>: vedo il locale, capisco cosa vuoi ottenere e ti mostro il catalogo",
                "<strong>Scegliamo insieme</strong> superfici e finiture",
                "<strong>Preventivo chiaro</strong>, senza impegno",
                "<strong>Applicazione</strong>: preparo le superfici e applico le pellicole con cura e senza difetti",
            ])),
            ("Vetrine e interni, un solo referente", p(
                "Oltre alla riqualificazione mi occupo di <a href=\"/#cosa-faccio\">pulizia vetrate</a> e di "
                "<a href=\"pellicole-per-vetri-trento.html\">pellicole per vetri</a>: puoi affidare a una sola persona "
                "tutto quello che i clienti vedono del tuo negozio, dalla vetrina al bancone.")),
            ("Conosciamoci", PREVENTIVO),
        ],
        "other": "Rinnovo negozi e locali a Trento, Rovereto e in tutta la provincia.",
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
        "serviceType": page.get("service_type", "Pulizia vetrate per aziende"),
        "name": page["h1"],
        "description": page["desc"],
        "areaServed": [
            {"@type": "City", "name": page["place"]},
            {"@type": "AdministrativeArea", "name": "Trentino"},
        ],
        "audience": {"@type": "BusinessAudience", "name": "Negozi, showroom, hotel, ristoranti e aziende"},
        "url": f'{SITE}/{page["slug"]}.html',
        **({"hasOfferCatalog": {"@type": "OfferCatalog", "name": page["h1"], "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": o}} for o in page["offers"]]}}
           if page.get("offers") else {}),
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
