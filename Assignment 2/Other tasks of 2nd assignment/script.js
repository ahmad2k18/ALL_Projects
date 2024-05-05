function changeColor() {
    var button = document.querySelector('.button');
    button.classList.toggle('clicked');
  }

  // color picker js 
  function changeBackgroundColor(color) {
    var targetElement = document.getElementById('targetElement');
    targetElement.style.backgroundColor = color;
  }

  // img enlarger

  function enlargeImage() {
    var image = document.getElementById('image');
    var currentWidth = image.offsetWidth;
    var newWidth = currentWidth * 1.2; // Increase width by 20%
    image.style.width = newWidth + 'px';
  }