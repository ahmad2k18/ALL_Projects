function animateButton() {
    var button = document.querySelector('.btn');
    var span = document.createElement('span');
    span.classList.add('circle');
    button.appendChild(span);
  
    var diameter = Math.max(button.clientWidth, button.clientHeight);
    var radius = diameter / 2;
  
    span.style.width = span.style.height = diameter + 'px';
    span.style.left = event.clientX - button.getBoundingClientRect().left - radius + 'px';
    span.style.top = event.clientY - button.getBoundingClientRect().top - radius + 'px';
  
    span.classList.add('ripple');
    
    setTimeout(() => {
      span.remove();
    }, 1000);
  }
  