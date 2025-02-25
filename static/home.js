const adImages = document.querySelector('.ad-images');
const nextButton = document.getElementById('nextBtn');
const ads = document.querySelectorAll('.ad'); 
let currentIndex = 0;
ads[currentIndex].classList.add('active');
function nextAd() {

  ads[currentIndex].classList.remove('active');
  currentIndex++;
  if (currentIndex >= ads.length) {
    currentIndex = 0;
  }
  ads[currentIndex].classList.add('active');
}
nextButton.addEventListener('click', nextAd);
setInterval(nextAd, 1000);
