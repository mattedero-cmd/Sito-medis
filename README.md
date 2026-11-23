# MediS — Sito web

Sito vetrina di **MediS** di Matteo Deromedis: lavavetri, wrapping
e riqualificazione interni nell'Altopiano della Vigolana (TN).

Realizzato in **HTML, CSS e JavaScript** puro, senza framework né dipendenze.
Tema scuro con accento turchese, coerente con il logo e il biglietto da visita.

## Struttura

```
.
├── index.html              # Sito completo (servizi, chi sono, contatti)
├── contatto.html           # Biglietto da visita digitale (target del tag NFC)
├── matteo-deromedis.vcf    # vCard scaricabile ("Salva il contatto")
├── styles.css              # Stile (tema scuro brand MediS, responsive)
├── script.js               # Menu mobile, validazione form, interazioni
└── README.md
```

## Biglietto da visita digitale (NFC)

La pagina `contatto.html` è pensata come destinazione del **tag NFC**: si apre
su smartphone con i pulsanti rapidi (Salva contatto, Chiama, WhatsApp, Email,
Indicazioni). Il pulsante **"Salva il contatto"** scarica `matteo-deromedis.vcf`,
che si aggiunge in rubrica con un tap — senza bisogno del QR code.

Una volta online, l'indirizzo da impostare sul tag NFC sarà:
`https://mattedero-cmd.github.io/Sito-medis/contatto.html`

## Contenuti del sito (index.html)

Posizionamento: **pulizia di grandi vetrate per aziende** (negozi, showroom, hotel,
ristoranti, palestre, sedi aziendali) in tutto il Trentino, più **riqualificazione
interni** e **pellicole per vetri**.

- Schermata iniziale: logo, nome, pulsanti Chiama, WhatsApp, Email, Salva contatto
- Pulito nel …: metri quadri puliti nell'anno dal gestionale, con paragoni e traguardi (vedi sotto)
- Cosa faccio: Pulizia vetrate, Riqualificazione interni, Controllo solare (testi nell'HTML, dettagli in finestra)
- Per chi lavoro, Il mio metodo (aste ad acqua demineralizzata fino al 2° piano), Come lavoro
- Chi sono, Domande frequenti, zone (Trento, Rovereto, Trentino)
- Pagine città: `lavavetri-trento.html`, `lavavetri-rovereto.html` (generate da `build_seo_pages.py`)
- `og-image.png`: immagine per le anteprime dei link (1200x630)

Il pulsante recensioni si attiva inserendo il link in `REVIEW_URL` (nello script in fondo a `index.html`).
La cartella `prove/` contiene le proposte alternative e non viene pubblicata.

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

## Metri quadri puliti quest'anno (`metri-quadri.js`)

La sezione «Pulito nel …» mostra i m² di vetro puliti nell'anno (dal primo intervento a registro,
se è di quest'anno) e quelli **di sempre**, con la data in cui è stato superato ogni traguardo,
letti dal gestionale
(`https://medis-zeta.vercel.app/api/pubblico/mq-puliti`: anno, totale, ora del calcolo, data del
primo intervento e totale progressivo per giornata, senza clienti; cache di un'ora). Se il gestionale non risponde la sezione resta nascosta.

Il totale viene accostato a caso a una superficie conosciuta fra quelle che ci stanno da 1 a 12
volte (il pulsante ne propone un'altra), più il «prossimo traguardo». La foto è quella principale
della voce di it.wikipedia, presa al momento della visita con autore e licenza da Wikimedia
Commons; bandiere, stemmi e mappe (SVG/PNG) sono scartati e senza foto resta un riquadro neutro.

Fonti delle superfici (ricerca del 23 novembre 2026):
- campi sportivi, piscina e pista da hockey: misure regolamentari (calcio 105 × 68 m, come il
  [campo di San Siro](https://en.wikipedia.org/wiki/San_Siro));
- Piramide del Louvre: 1.800–2.000 m² di vetro secondo le fonti ([Geopop](https://www.geopop.it/piramide-louvre-significato-vetro-perche/));
- cupola del Reichstag: 3.000 m² di vetro ([Bundestag](https://webarchiv.bundestag.de/archive/2006/0908/htdocs_e/virtuelle_rundgaenge/hotspot75.html));
- Arena di Verona: arena centrale 75 × 44 m (ellisse ≈ 2.600 m²);
- Galleria Vittorio Emanuele II: oltre 9.000 m² di vetro ([Lombardia Beni Culturali](https://lombardiabeniculturali.it/fotografie/schede-complete/IMM-3a120-0000014));
- Piazza del Duomo di Milano: 17.000 m² ([Barceló](https://www.barcelo.com/guia-turismo/es/italia/milan/que-ver/piazza-del-duomo/));
- Basilica di San Pietro: 22.067 m² ([italia.it](https://www.italia.it/it/lazio/roma/basilica-di-san-pietro));
- Colosseo: circa 24.000 m² ([Turismo Roma](https://www.turismoroma.it/it/luoghi/lanfiteatro-flavio-colosseo));
- Piazza San Pietro: circa 47.600 m² ([idealista](https://www.idealista.it/news/node/285843));
- Piramide di Cheope: lato 230,3 m ([Britannica](https://www.britannica.com/place/Great-Pyramid-of-Giza));
- The Shard: 56.000 m² di vetro ([RIBA Journal](https://ribaj.com/buildings/database-the-shard-london));
- Burj Khalifa: 103.000 m² di vetro ([scheda ufficiale](https://www.burjkhalifa.ae/en/assets/FACT-SHEET.pdf));
- Empire State Building: 208.879 m² di pavimenti, 6.514 finestre ([Wikipedia](https://en.wikipedia.org/wiki/Empire_State_Building));
- Città del Vaticano 0,44 km², Principato di Monaco 2,02 km² ([Britannica](https://www.britannica.com/topic/list-of-the-smallest-countries-by-area));
- Lago di Levico 1,16 km², Lago di Caldonazzo 5,38 km² ([Wikipedia](https://en.wikipedia.org/wiki/Lake_Caldonazzo));
- Central Park: 341 ettari ([Britannica](https://www.britannica.com/print/article/102556)).

Per aggiungere un paragone basta una riga nella lista `SUPERFICI` di `metri-quadri.js`.
