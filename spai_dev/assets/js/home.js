const heroPics = document.querySelectorAll('.hero-pic img');
const heroTexts = document.querySelectorAll('.hero-text');
let currentPic = 0;

setInterval(() => {
    heroPics[currentPic].classList.remove('active');
    heroTexts[currentPic].classList.remove('active');
    currentPic = (currentPic + 1) % heroPics.length;
    heroPics[currentPic].classList.add('active');
    heroTexts[currentPic].classList.add('active');
}, 3000); /* Change the image and text every 3 seconds */

heroPics[currentPic].classList.add('active');
heroTexts[currentPic].classList.add('active');

function nextImage() {
    heroPics[currentPic].classList.remove('active');
    heroTexts[currentPic].classList.remove('active');
    currentPic = (currentPic + 1) % heroPics.length;
    heroPics[currentPic].classList.add('active');
    heroTexts[currentPic].classList.add('active');
}

function prevImage() {
    heroPics[currentPic].classList.remove('active');
    heroTexts[currentPic].classList.remove('active');
    currentPic = (currentPic - 1 + heroPics.length) % heroPics.length;
    heroPics[currentPic].classList.add('active');
    heroTexts[currentPic].classList.add('active');
}
