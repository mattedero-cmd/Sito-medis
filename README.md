# MediS — Sito web

Sito vetrina di **MediS** di Matteo Deromedis: lavavetri, wrapping
e riqualificazione interni nell'Altopiano della Vigolana (TN).

Realizzato in **HTML, CSS e JavaScript** puro, senza framework né dipendenze.
Tema scuro con accento turchese, coerente con il logo e il biglietto da visita.

## Struttura

```
.
├── index.html                  # Home: scheda contatti (pulsanti rapidi + servizi)
├── lavavetri-*.html            # Pagine SEO per zona (generate)
├── pulizia-pannelli-fotovoltaici-trentino.html  # Pagina SEO fotovoltaico (generata)
├── build_seo_pages.py          # Genera le pagine SEO per zona + sitemap.xml
├── zone.css                    # Stile delle pagine SEO e della 404
├── 404.html                    # Pagina "non trovata"
├── contatto.html               # Redirect alla home (vecchio indirizzo del tag NFC)
├── sito.html                   # Vecchio sito completo (noindex, non collegato)
├── styles.css / script.js      # Stile e script di sito.html
├── matteo-deromedis.vcf        # vCard scaricabile ("Salva contatto")
├── logo.png
├── sitemap.xml / robots.txt / CNAME
└── GUIDA-SEO.md
```

Le pagine per zona **non vanno modificate a mano**: modifica `build_seo_pages.py`
e rigenera con `python3 build_seo_pages.py`.

## Biglietto da visita digitale (NFC)

La home (`index.html`) è la scheda contatti ed è la destinazione del **tag NFC**:
si apre su smartphone con i pulsanti rapidi (Chiama, WhatsApp, Email, Salva contatto).
Il pulsante **"Salva contatto"** scarica `matteo-deromedis.vcf`, che si aggiunge
in rubrica con un tap.

Indirizzo da impostare sul tag NFC: `https://medistn.it/`
(il vecchio `https://medistn.it/contatto.html` reindirizza comunque alla home).

## Contenuti del sito

- **Hero** — presentazione dell'attività e call-to-action
- **Servizi** — Lavavetri · Wrapping · Riqualificazione interni
- **Chi sono** — presentazione di Matteo Deromedis
- **Perché MediS** — i punti di forza
- **Contatti** — form di richiesta preventivo + contatti diretti e WhatsApp

## Dati attività

- **Titolare:** Deromedis Matteo
- **Zona:** Altopiano della Vigolana (TN)
- **Telefono:** 351 987 8991
- **Email:** info@medistn.it
- **P. IVA:** 02581560220 · **C.F.:** DRMMTT89T15L378F · **SDI:** USAL8PV

## Come visualizzarlo in locale

Apri `index.html` nel browser, oppure avvia un server locale:

```bash
python3 -m http.server 8000
# poi apri http://localhost:8000
```

## Personalizzazione

- I **colori** si modificano dalle variabili CSS in cima a `styles.css` (`:root`).
  L'accento turchese è `--color-accent`.
- Il **logo** è realizzato come testo (font Caveat). Per usare il logo reale,
  inserisci il file immagine (es. `logo.png`) e sostituisci `.brand__mark` con un `<img>`.
- I **testi** sono tutti in `index.html`.

## Pubblicazione gratuita su GitHub Pages

1. **Settings → Pages** del repository
2. In *Source* seleziona il branch e la cartella `/ (root)`
3. Salva: il sito sarà online su `https://<utente>.github.io/<repo>/`

> Il form contatti apre il client di posta verso `info@medistn.it`. Per ricevere
> le richieste direttamente via email senza client, si può collegare
> [Formspree](https://formspree.io) o [Netlify Forms](https://docs.netlify.com/forms/setup/).
