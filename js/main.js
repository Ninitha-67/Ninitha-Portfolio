const navToggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.nav');
if (navToggle && nav) {
  navToggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(open));
  });
}

const siteHeader = document.querySelector('.site-header');
window.addEventListener('scroll', () => {
  if (!siteHeader) return;
  siteHeader.classList.toggle('scrolled', window.scrollY > 50);
});

const texts = ['cat profile.txt', 'whoami', 'ls -la skills/', 'grep "cybersecurity" *'];
let textIndex = 0;
let charIndex = 0;
const typedTextElement = document.querySelector('.typed-text');

function type() {
  if (!typedTextElement) return;
  if (charIndex < texts[textIndex].length) {
    typedTextElement.textContent += texts[textIndex].charAt(charIndex);
    charIndex++;
    setTimeout(type, 100);
  } else {
    setTimeout(erase, 2000);
  }
}

function erase() {
  if (!typedTextElement) return;
  if (charIndex > 0) {
    typedTextElement.textContent = texts[textIndex].substring(0, charIndex - 1);
    charIndex--;
    setTimeout(erase, 50);
  } else {
    textIndex = (textIndex + 1) % texts.length;
    setTimeout(type, 500);
  }
}
setTimeout(type, 1000);

const roles = ['SOC Analyst', 'Threat Researcher', 'GRC Specialist', 'Penetration Tester', 'Security Engineer'];
let roleIndex = 0;
const roleElement = document.querySelector('.rotating-roles');
if (roleElement) {
  roleElement.textContent = roles[0];
  roleElement.style.transition = 'opacity 0.5s';
  setInterval(() => {
    roleElement.style.opacity = 0;
    setTimeout(() => {
      roleIndex = (roleIndex + 1) % roles.length;
      roleElement.textContent = roles[roleIndex];
      roleElement.style.opacity = 1;
    }, 500);
  }, 3000);
}

const canvas = document.getElementById('matrix-canvas');
if (canvas) {
  const ctx = canvas.getContext('2d');
  const resizeMatrix = () => {
    canvas.width = window.innerWidth;
    canvas.height = Math.max(window.innerHeight, document.documentElement.scrollHeight);
  };
  resizeMatrix();
  const matrix = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%^&*()*&^%+-/~{[|`]}';
  const matrixArray = matrix.split('');
  const fontSize = 16;
  let drops = [];
  const setupDrops = () => {
    const columns = Math.floor(canvas.width / fontSize);
    drops = Array.from({ length: columns }, () => Math.random() * -100);
  };
  setupDrops();
  function drawMatrix() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.04)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#00d4ff';
    ctx.font = fontSize + 'px monospace';
    for (let i = 0; i < drops.length; i++) {
      const text = matrixArray[Math.floor(Math.random() * matrixArray.length)];
      ctx.fillText(text, i * fontSize, drops[i] * fontSize);
      if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
      drops[i]++;
    }
  }
  setInterval(drawMatrix, 35);
  window.addEventListener('resize', () => { resizeMatrix(); setupDrops(); });
}

const progressBars = document.querySelectorAll('.progress-bar[data-progress]');
if (progressBars.length) {
  const progressObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const bar = entry.target;
      bar.style.width = bar.dataset.progress + '%';
    });
  }, { threshold: 0.35 });
  progressBars.forEach((bar) => progressObserver.observe(bar));
}

const revealItems = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.12 });
revealItems.forEach((el) => observer.observe(el));

const contactForm = document.getElementById('contactForm');
const formNote = document.getElementById('formNote');
if (contactForm && formNote) {
  contactForm.addEventListener('submit', (event) => {
    event.preventDefault();
    formNote.textContent = 'Thanks. This form is ready for integration with email or backend handling.';
    contactForm.reset();
  });
}

function scrollToSection(sectionId) {
  const el = document.getElementById(sectionId);
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}

function downloadResume() {
  window.location.hash = '#contact';
}

// Terminal-style helpers used by hero buttons
window.scrollToSection = scrollToSection;
window.downloadResume = downloadResume;
