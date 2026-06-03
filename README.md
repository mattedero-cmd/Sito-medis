# MediS — Sito web

Sito vetrina di **MediS** di Matteo Deromedis: lavavetri, applicatore pubblicitario
e riqualificatore di interni nell'Altopiano della Vigolana (TN).

Realizzato in **HTML, CSS e JavaScript** puro, senza framework né dipendenze.
Tema scuro con accento turchese, coerente con il logo e il biglietto da visita.

## Struttura

```
.
├── index.html    # Contenuto e struttura del sito
├── styles.css    # Stile (tema scuro brand MediS, responsive)
├── script.js     # Menu mobile, validazione form, interazioni
└── README.md
```

## Contenuti del sito

- **Hero** — presentazione dell'attività e call-to-action
- **Servizi** — Lavavetri · Applicatore pubblicitario · Riqualificatore di interni
- **Chi sono** — presentazione di Matteo Deromedis
- **Perché MediS** — i punti di forza
- **Contatti** — form di richiesta preventivo + contatti diretti e WhatsApp

## Dati attività

- **Titolare:** Deromedis Matteo
- **Indirizzo:** Via Vittoria 11, 38049 Altopiano della Vigolana (TN)
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
