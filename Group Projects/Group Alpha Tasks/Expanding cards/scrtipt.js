const panels = document.querySelectorAll('.expanding-cards-panel');

panels.forEach((panel) => {
  panel.addEventListener('click', (event) => {
    removeActiveClasses();
    panel.classList.add('active');
  });
});

function removeActiveClasses() {
  panels.forEach((panel) => {
    panel.classList.remove('active');
  });
}
