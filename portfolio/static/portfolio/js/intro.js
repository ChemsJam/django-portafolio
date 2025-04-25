let intro = document.querySelector('.intro');
let logoSpan = document.querySelectorAll('.logo-parts');

// ⏱ Ajustes de velocidad
let appearDelay = 100;  // cada letra aparece más rápido
let fadeDelay = 30;     // y también desaparecen más rápido
let bufferTime = 500;   // tiempo extra antes de iniciar el fade
let endDelay = 1500;    // tiempo final antes de ocultar la intro

window.addEventListener('DOMContentLoaded', () => {
    logoSpan.forEach((span, idx) => {
        setTimeout(() => {
            span.classList.add('active');
        }, (idx + 1) * appearDelay);
    });

    let totalAppearTime = logoSpan.length * appearDelay;

    setTimeout(() => {
        logoSpan.forEach((span, idx) => {
            setTimeout(() => {
                span.classList.remove('active');
                span.classList.add('fade');
            }, (idx + 1) * fadeDelay);
        });
    }, totalAppearTime + bufferTime);

    setTimeout(() => {
        intro.style.top = '-100vh';
    }, totalAppearTime + bufferTime + endDelay);
});
