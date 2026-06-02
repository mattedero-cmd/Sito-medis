# Sito personale · Portfolio

Sito web personale realizzato in **HTML, CSS e JavaScript** (nessun framework, nessuna dipendenza).
Design pulito, professionale e completamente responsive.

## Struttura

```
.
├── index.html    # Contenuto e struttura delle pagine
├── styles.css    # Stile e layout (responsive)
├── script.js     # Menu mobile, validazione form, interazioni
└── README.md
```

## Come visualizzarlo in locale

Apri semplicemente `index.html` nel browser, oppure avvia un piccolo server locale:

```bash
# Con Python 3
python3 -m http.server 8000
# poi apri http://localhost:8000
```

## Come personalizzarlo

Tutti i contenuti sono in `index.html`. Sostituisci i testi segnaposto:

- **Nome e ruolo** — cerca `Matteo Cognome` e `Professione / Ruolo`
- **Chi sono** — sezione `#about`
- **Competenze** — sezione `#skills`
- **Esperienza** — sezione `#experience` (timeline)
- **Progetti** — sezione `#projects`
- **Contatti e link social** — sezione `#contact` (LinkedIn, GitHub, email)

I colori si modificano dalle variabili CSS in cima a `styles.css` (`:root`).

## Pubblicazione gratuita su GitHub Pages

1. Vai su **Settings → Pages** del repository
2. In *Source* seleziona il branch (es. `main`) e la cartella `/ (root)`
3. Salva: il sito sarà online su `https://<utente>.github.io/<repo>/`

> Nota: il form contatti apre il client di posta dell'utente. Per ricevere i
> messaggi direttamente via email senza backend puoi usare un servizio come
> [Formspree](https://formspree.io) o [Netlify Forms](https://docs.netlify.com/forms/setup/).
