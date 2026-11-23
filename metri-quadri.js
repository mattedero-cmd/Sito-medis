/*
 * METRI QUADRI PULITI QUEST'ANNO
 *
 * Il totale arriva dal gestionale Medis (pulizie chiuse a registro, facce pulite contate: lo stesso
 * numero delle Statistiche). Il gestionale lo tiene in cache un'ora, quindi il sito non pesa sul
 * database qualunque sia il numero di visite.
 *
 * Il totale viene accostato a una superficie vera e conosciuta, scelta a caso fra quelle
 * «alla portata» del numero: a ogni visita può uscire un paragone diverso, e il pulsante ne
 * propone un altro. La foto arriva da Wikipedia/Wikimedia Commons al momento della visita, con
 * autore e licenza; se non arriva resta un riquadro senza foto e la pagina non si rompe.
 *
 * Se il gestionale non risponde la sezione resta nascosta: meglio niente che un numero inventato.
 */
(() => {
  'use strict';

  const API = 'https://medis-zeta.vercel.app/api/pubblico/mq-puliti';

  /*
   * Le superfici di confronto. `mq` è la superficie, `nome` la forma singolare con l'articolo,
   * `plurale` (se c'è) fa dire «12 campi da tennis» invece di «12 volte un campo da tennis».
   * `wiki` sono le voci di it.wikipedia da cui prendere la foto, in ordine di preferenza.
   * `nota` dice da dove viene il numero: le fonti sono in README.md.
   */
  const SUPERFICI = [
    { mq: 4.18, nome: 'un tavolo da ping pong', plurale: 'tavoli da ping pong', wiki: ['Tennistavolo'], nota: '2,74 × 1,525 m, misure ufficiali' },
    { mq: 128, nome: 'un campo da beach volley', plurale: 'campi da beach volley', wiki: ['Beach volley'], nota: '16 × 8 m' },
    { mq: 162, nome: 'un campo da pallavolo', plurale: 'campi da pallavolo', wiki: ['Pallavolo'], nota: '18 × 9 m' },
    { mq: 200, nome: 'un campo da padel', plurale: 'campi da padel', wiki: ['Padel'], nota: '20 × 10 m' },
    { mq: 261, nome: 'un campo da tennis', plurale: 'campi da tennis', wiki: ['Tennis'], nota: '23,77 × 10,97 m, quello del doppio' },
    { mq: 420, nome: 'un campo da basket', plurale: 'campi da basket', wiki: ['Pallacanestro'], nota: '28 × 15 m, misure FIBA' },
    { mq: 800, nome: 'un campo da calcetto', plurale: 'campi da calcetto', wiki: ['Calcio a 5'], nota: '40 × 20 m' },
    { mq: 1250, nome: 'una piscina olimpionica', plurale: 'piscine olimpioniche', wiki: ['Piscina olimpionica', 'Nuoto'], nota: '50 × 25 m' },
    { mq: 1800, nome: 'una pista da hockey su ghiaccio', plurale: 'piste da hockey', wiki: ['Hockey su ghiaccio'], nota: '60 × 30 m, misure internazionali' },
    { mq: 2000, nome: 'tutto il vetro della Piramide del Louvre', wiki: ['Piramide del Louvre'], nota: 'circa 2.000 m² di vetro sulle quattro facce' },
    { mq: 2600, nome: 'l’arena dell’Arena di Verona', wiki: ['Arena di Verona'], nota: 'l’ellisse centrale di 75 × 44 m' },
    { mq: 3000, nome: 'il vetro della cupola del Reichstag di Berlino', wiki: ['Cupola del Reichstag', 'Palazzo del Reichstag'], nota: '3.000 m² di vetro' },
    { mq: 5350, nome: 'un campo da football americano', plurale: 'campi da football americano', wiki: ['Football americano'], nota: '109,7 × 48,8 m, mete comprese' },
    { mq: 7140, nome: 'il prato di San Siro', wiki: ['Stadio Giuseppe Meazza'], nota: '105 × 68 m' },
    { mq: 9000, nome: 'il tetto di vetro della Galleria Vittorio Emanuele II', wiki: ['Galleria Vittorio Emanuele II'], nota: 'oltre 9.000 m² di vetro, posati nel 1867' },
    { mq: 17000, nome: 'Piazza del Duomo a Milano', wiki: ['Piazza del Duomo (Milano)', 'Duomo di Milano'], nota: 'circa 17.000 m²' },
    { mq: 22000, nome: 'la Basilica di San Pietro', wiki: ['Basilica di San Pietro in Vaticano'], nota: 'circa 22.000 m² di superficie interna' },
    { mq: 24000, nome: 'il Colosseo', wiki: ['Colosseo'], nota: 'circa 24.000 m² di pianta, un’ellisse di 188 × 156 m' },
    { mq: 47600, nome: 'Piazza San Pietro', wiki: ['Piazza San Pietro'], nota: 'circa 47.600 m²' },
    { mq: 53000, nome: 'la base della Piramide di Cheope', wiki: ['Piramide di Cheope'], nota: 'circa 230 × 230 m' },
    { mq: 56000, nome: 'tutto il vetro dello Shard di Londra', wiki: ['The Shard'], nota: '56.000 m² di facciata in vetro, 11.000 lastre' },
    { mq: 103000, nome: 'tutto il vetro del Burj Khalifa', wiki: ['Burj Khalifa'], nota: '103.000 m² di vetro, il grattacielo più alto del mondo' },
    { mq: 208879, nome: 'tutti i pavimenti dell’Empire State Building', wiki: ['Empire State Building'], nota: '102 piani, 6.514 finestre' },
    { mq: 440000, nome: 'la Città del Vaticano', wiki: ['Città del Vaticano', 'Basilica di San Pietro in Vaticano'], nota: '0,44 km², lo stato più piccolo del mondo' },
    { mq: 1164000, nome: 'il Lago di Levico', wiki: ['Lago di Levico'], nota: '1,16 km²' },
    { mq: 2020000, nome: 'il Principato di Monaco', wiki: ['Monte Carlo', 'Principato di Monaco'], nota: '2,02 km²' },
    { mq: 3410000, nome: 'Central Park a New York', wiki: ['Central Park'], nota: '341 ettari' },
    { mq: 5380000, nome: 'il Lago di Caldonazzo', wiki: ['Lago di Caldonazzo'], nota: '5,38 km², il lago più grande tutto trentino' },
  ];

  /* Un paragone è «alla portata» se il totale ci sta almeno una volta e al massimo 12 volte. */
  const MAX_VOLTE = 12;

  // `useGrouping: 'always'`: in italiano 7140 si scriverebbe senza il punto delle migliaia.
  const fmt = (n, dec = 0) => n.toLocaleString('it-IT', { maximumFractionDigits: dec, minimumFractionDigits: 0, useGrouping: 'always' });

  /** Quali superfici si possono accostare al totale (le più grandi se nessuna è nel range). */
  function candidati(totale) {
    const sotto = SUPERFICI.filter((s) => s.mq <= totale);
    const vicini = sotto.filter((s) => totale / s.mq <= MAX_VOLTE);
    if (vicini.length) return vicini;
    return sotto.length ? [sotto[sotto.length - 1]] : [SUPERFICI[0]];
  }

  /** «quanto il Colosseo», «2,3 volte il Colosseo», «12 campi da tennis», «mezzo tavolo…». */
  function frase(totale, s) {
    const r = totale / s.mq;
    if (r < 0.9) return `${fmt(Math.round(r * 100))}% di ${s.nome}`;
    if (r < 1.15) return `quanto ${s.nome}`;
    if (s.plurale) return `${fmt(r, r < 10 ? 1 : 0)} ${s.plurale}`;
    return `${fmt(r, r < 10 ? 1 : 0)} volte ${s.nome}`;
  }

  // ── Foto da Wikipedia / Commons (CORS aperto con origin=*) ──
  const fotoCache = new Map();
  const isFoto = (file) => /\.(jpe?g|webp)$/i.test(file || '');
  const testo = (html) => {
    const d = document.createElement('div');
    d.innerHTML = html || '';
    return (d.textContent || '').replace(/\s+/g, ' ').trim();
  };

  async function fotoDi(s) {
    if (fotoCache.has(s)) return fotoCache.get(s);
    let out = null;
    try {
      const q = new URLSearchParams({ action: 'query', format: 'json', origin: '*', prop: 'pageimages', piprop: 'name', redirects: '1', titles: s.wiki.join('|') });
      const pagine = Object.values((await (await fetch(`https://it.wikipedia.org/w/api.php?${q}`)).json()).query?.pages || {});
      // Nell'ordine di preferenza di `wiki`, la prima voce che ha come immagine una FOTO
      // (non una bandiera, uno stemma o una mappa, che sono SVG o PNG).
      const perTitolo = new Map(pagine.map((p) => [p.title, p.pageimage]));
      const file = s.wiki.map((t) => perTitolo.get(t)).find(isFoto) || pagine.map((p) => p.pageimage).find(isFoto);
      if (file) {
        const c = new URLSearchParams({ action: 'query', format: 'json', origin: '*', prop: 'imageinfo', iiprop: 'url|extmetadata', iiurlwidth: '960', titles: `File:${file}` });
        const info = Object.values((await (await fetch(`https://commons.wikimedia.org/w/api.php?${c}`)).json()).query?.pages || {})[0]?.imageinfo?.[0];
        if (info?.thumburl) {
          const m = info.extmetadata || {};
          out = {
            src: info.thumburl,
            pagina: info.descriptionurl,
            autore: testo(m.Artist?.value) || 'Wikimedia Commons',
            licenza: testo(m.LicenseShortName?.value),
          };
        }
      }
    } catch (_) { /* senza foto si mostra lo stesso il paragone */ }
    fotoCache.set(s, out);
    return out;
  }

  // ── Interfaccia ──
  const sez = document.getElementById('mq');
  if (!sez) return;
  const el = (id) => document.getElementById(id);
  const numero = el('mqNumero');
  const anno = el('mqAnno');
  const quanto = el('mqQuanto');
  const nota = el('mqNota');
  const img = el('mqImg');
  const fig = el('mqFoto');
  const credito = el('mqCredito');
  const prossimo = el('mqProssimo');
  const altro = el('mqAltro');
  const agg = el('mqAgg');
  const da = el('mqDa');
  const sempreBox = el('mqSempre');
  const sempreNum = el('mqSempreNum');
  const dal = el('mqDal');
  const tragLista = el('mqTraguardi');
  const tragTitolo = el('mqTragTitolo');
  const tutti = el('mqTutti');
  const REDUCE = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  let totale = 0;
  let lista = [];
  let indice = 0;
  let giro = 0;

  function contaFino(n) {
    if (REDUCE || n <= 0) { numero.textContent = fmt(n); return; }
    const t0 = performance.now();
    const durata = 1600;
    const passo = (t) => {
      const k = Math.min(1, (t - t0) / durata);
      numero.textContent = fmt(Math.round(n * (1 - Math.pow(1 - k, 3))));
      if (k < 1) requestAnimationFrame(passo);
    };
    requestAnimationFrame(passo);
  }

  async function mostra(s) {
    const mio = ++giro;
    quanto.textContent = frase(totale, s);
    nota.textContent = `${s.nome.charAt(0).toUpperCase()}${s.nome.slice(1)}: ${s.nota}.`;
    fig.classList.add('is-loading');
    fig.classList.remove('no-foto');
    const f = await fotoDi(s);
    if (mio !== giro) return; // nel frattempo è stato chiesto un altro paragone
    if (f) {
      img.onload = () => fig.classList.remove('is-loading');
      img.onerror = () => { fig.classList.remove('is-loading'); fig.classList.add('no-foto'); credito.hidden = true; };
      img.src = f.src;
      img.alt = s.nome.replace(/^(un|una|il|la|lo|l’|tutto il|tutti i)\s?/i, '');
      credito.innerHTML = '';
      const a = document.createElement('a');
      a.href = f.pagina; a.target = '_blank'; a.rel = 'noopener';
      a.textContent = `Foto: ${f.autore}${f.licenza ? ` · ${f.licenza}` : ''} · Wikimedia Commons`;
      credito.appendChild(a);
      credito.hidden = false;
    } else {
      img.removeAttribute('src');
      fig.classList.remove('is-loading');
      fig.classList.add('no-foto');
      credito.hidden = true;
    }
  }

  function traguardo() {
    const s = SUPERFICI.find((x) => x.mq > totale);
    if (!s) { prossimo.hidden = true; return; }
    prossimo.hidden = false;
    prossimo.textContent = `Prossimo traguardo: ${s.nome}. Mancano ${fmt(Math.ceil(s.mq - totale))}\u00a0m².`;
  }

  /**
   * «il 3 marzo 2026», «l’8 marzo 2026», «il 1° maggio 2026» da «2026-03-03», senza passare per i
   * fusi orari. `art` è la preposizione da accordare: «il» → «l’», «dal» → «dall’» davanti a 8 e 11.
   */
  const MESI = ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre'];
  const giorno = (iso, art) => {
    const [a, m, g] = String(iso).split('-').map(Number);
    const data = `${g === 1 ? '1°' : g} ${MESI[m - 1]} ${a}`;
    const elisa = g === 8 || g === 11;
    return `${elisa ? `${art}l’` : `${art} `}${data}`.replace(/^ill’/, 'l’');
  };

  /**
   * I TRAGUARDI: per ogni superficie superata dal totale di sempre, il giorno in cui è successo
   * (il primo punto del progressivo che la raggiunge). Dal più recente.
   */
  function traguardiRaggiunti(progressivo) {
    const out = [];
    for (const s of SUPERFICI) {
      const p = progressivo.find((x) => x.mq >= s.mq);
      if (p) out.push({ s, data: p.data });
    }
    return out.reverse();
  }

  const SPUNTA = '<svg aria-hidden="true" focusable="false" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></svg>';
  const VISIBILI = 5;

  function mostraSempre(sempre, annoCorrente) {
    if (!sempre || typeof sempre.mq !== 'number' || !sempre.dal) return;
    // L'anno parte dal primo intervento a registro se è di quest'anno: prima non si contava.
    if (String(sempre.dal).startsWith(`${annoCorrente}-`) && sempre.dal !== `${annoCorrente}-01-01`) {
      const d = giorno(sempre.dal, 'dal');
      da.textContent = `${d.charAt(0).toUpperCase()}${d.slice(1)}, primo intervento registrato, ho pulito`;
    }
    sempreBox.hidden = false;
    sempreNum.textContent = fmt(sempre.mq);
    dal.textContent = `Il conteggio parte ${giorno(sempre.dal, 'dal')}, giorno del primo intervento registrato nel mio registro di lavoro.`;
    const trag = traguardiRaggiunti(Array.isArray(sempre.progressivo) ? sempre.progressivo : []);
    tragLista.innerHTML = '';
    if (!trag.length) { tragTitolo.hidden = true; return; }
    trag.forEach((t, i) => {
      const li = document.createElement('li');
      li.innerHTML = SPUNTA;
      const nome = document.createElement('span');
      nome.textContent = `${t.s.nome.charAt(0).toUpperCase()}${t.s.nome.slice(1)} (${fmt(t.s.mq, 2)}\u00a0m²)`;
      const quando = document.createElement('time');
      quando.dateTime = t.data;
      quando.textContent = `superato ${giorno(t.data, 'il')}`;
      li.append(nome, quando);
      if (i >= VISIBILI) li.hidden = true;
      tragLista.appendChild(li);
    });
    tutti.hidden = trag.length <= VISIBILI;
    tutti.textContent = `Mostra tutti i ${trag.length} traguardi`;
  }

  tutti.addEventListener('click', () => {
    tragLista.querySelectorAll('li[hidden]').forEach((li) => { li.hidden = false; });
    tutti.hidden = true;
  });

  function avvia(dati) {
    totale = Math.max(0, Number(dati.mq) || 0);
    anno.textContent = String(dati.anno);
    const d = new Date(dati.aggiornato);
    if (!isNaN(d)) agg.textContent = `Aggiornato al ${d.toLocaleDateString('it-IT', { day: 'numeric', month: 'long', year: 'numeric' })}.`;
    sez.hidden = false;
    mostraSempre(dati.sempre, dati.anno);

    if (totale === 0) {
      numero.textContent = '0';
      quanto.textContent = 'anno nuovo, vetri nuovi: il contatore è appena ripartito!';
      fig.hidden = true; altro.hidden = true; nota.hidden = true;
      traguardo();
      return;
    }

    // Ordine casuale dei paragoni possibili: ogni visita parte da uno diverso.
    lista = candidati(totale).slice();
    for (let i = lista.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [lista[i], lista[j]] = [lista[j], lista[i]];
    }
    indice = 0;
    altro.hidden = lista.length < 2;
    traguardo();
    mostra(lista[0]);

    // Il numero conta da zero quando la sezione entra nello schermo.
    if ('IntersectionObserver' in window && !REDUCE) {
      numero.textContent = '0';
      const io = new IntersectionObserver(([e]) => {
        if (e.isIntersecting) { contaFino(totale); io.disconnect(); }
      }, { threshold: 0.1 });
      io.observe(numero);
    } else {
      numero.textContent = fmt(totale);
    }
  }

  altro.addEventListener('click', () => {
    if (lista.length < 2) return;
    indice = (indice + 1) % lista.length;
    mostra(lista[indice]);
  });

  fetch(API, { mode: 'cors' })
    .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
    .then((d) => { if (typeof d?.mq === 'number' && typeof d?.anno === 'number') avvia(d); })
    .catch(() => { /* gestionale non raggiungibile: la sezione resta nascosta */ });

  // Per le prove automatiche: le funzioni pure, senza toccare la pagina.
  window.__mqMedis = { SUPERFICI, candidati, frase, traguardiRaggiunti };
})();
