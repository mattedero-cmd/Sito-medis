// Anno corrente nel footer
document.getElementById('year').textContent = new Date().getFullYear();

// Menu mobile
const toggle = document.querySelector('.nav__toggle');
const menu = document.querySelector('.nav__menu');

if (toggle && menu) {
  toggle.addEventListener('click', () => {
    const isOpen = menu.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(isOpen));
  });

  // Chiudi il menu quando si clicca un link
  menu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      menu.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
}

// Gestione form contatti (validazione lato client)
const form = document.getElementById('contactForm');
const feedback = document.getElementById('formFeedback');

if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = form.name.value.trim();
    const email = form.email.value.trim();
    const phone = form.phone ? form.phone.value.trim() : '';
    const service = form.service ? form.service.value : '';
    const message = form.message.value.trim();
    const emailValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

    if (!name || !email || !message) {
      showFeedback('Per favore compila i campi obbligatori (nome, email, messaggio).', 'error');
      return;
    }
    if (!emailValid) {
      showFeedback('Inserisci un indirizzo email valido.', 'error');
      return;
    }

    // Nota: per ricevere davvero le richieste senza aprire il client di posta
    // si può collegare un servizio come Formspree/Netlify Forms.
    const subject = encodeURIComponent(`Richiesta preventivo${service ? ' · ' + service : ''} — ${name}`);
    const body = encodeURIComponent(
      `Nome: ${name}\nEmail: ${email}\nTelefono: ${phone || '—'}\nServizio: ${service || '—'}\n\n${message}`
    );
    window.location.href = `mailto:info@medistn.it?subject=${subject}&body=${body}`;

    showFeedback('Grazie! Si aprirà il tuo client di posta per inviare il messaggio.', 'success');
    form.reset();
  });
}

function showFeedback(text, type) {
  if (!feedback) return;
  feedback.textContent = text;
  feedback.className = `form-feedback ${type}`;
}

// Evidenzia la voce di menu attiva durante lo scroll
const sections = document.querySelectorAll('main section[id]');
const navLinks = document.querySelectorAll('.nav__menu a');

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach((link) => {
          link.style.color = link.getAttribute('href') === `#${id}` ? '' : '';
          link.classList.toggle('is-active', link.getAttribute('href') === `#${id}`);
        });
      }
    });
  },
  { rootMargin: '-40% 0px -55% 0px' }
);

sections.forEach((section) => observer.observe(section));
