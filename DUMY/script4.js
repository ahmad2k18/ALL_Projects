document.addEventListener('DOMContentLoaded', function () {
    animate();
  });
  
  function animate() {
    var leftArm = document.getElementById('left-arm');
    var rightArm = document.getElementById('right-arm');
    var leftLeg = document.getElementById('left-leg');
    var rightLeg = document.getElementById('right-leg');
  
    leftArm.style.transform = 'rotate(-20deg)';
    rightArm.style.transform = 'rotate(20deg)';
    leftLeg.style.transform = 'rotate(20deg)';
    rightLeg.style.transform = 'rotate(-20deg)';
  }
  