// First try
// const faqs = document.querySelectorAll('.faq');

// faqs.forEach((faq) => {
//   const btn = faq.querySelector('.faq-toggle');
//   btn.addEventListener('click', () => faq.classList.toggle('active'));
// });

// Based on hint
const buttons = document.querySelectorAll('.faq-toggle');

buttons.forEach((btn) => {
  btn.addEventListener('click', () => btn.parentNode.classList.toggle('active'));
});
