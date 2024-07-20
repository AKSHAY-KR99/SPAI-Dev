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

/*****news*************************** */
document.addEventListener('DOMContentLoaded', function () {
    const floatingDivs = document.querySelectorAll('.news-containers');

    const observerOptions = {
        root: null, // Use the viewport as the container
        rootMargin: '0px',
        threshold: 0.2 // Trigger when 10% of the element is visible
    };

    function handleIntersection(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    }

    const observer = new IntersectionObserver(handleIntersection, observerOptions);

    floatingDivs.forEach(div => {
        observer.observe(div);
    });
});

/************************************************/

/**********associa*/
document.addEventListener('DOMContentLoaded', function () {
    const floatingDivs = document.querySelectorAll('.associate-containers');

    const observerOptions = {
        root: null, // Use the viewport as the container
        rootMargin: '0px',
        threshold: 0.2 // Trigger when 10% of the element is visible
    };

    function handleIntersection(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    }

    const observer = new IntersectionObserver(handleIntersection, observerOptions);

    floatingDivs.forEach(div => {
        observer.observe(div);
    });
});

/****************about********/
document.addEventListener('DOMContentLoaded', function () {
    const floatingDivs = document.querySelectorAll('.about-content');

    const observerOptions = {
        root: null, // Use the viewport as the container
        rootMargin: '0px',
        threshold: 0.2 // Trigger when 10% of the element is visible
    };

    function handleIntersection(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    }

    const observer = new IntersectionObserver(handleIntersection, observerOptions);

    floatingDivs.forEach(div => {
        observer.observe(div);
    });
});

/*********executive**** */
document.addEventListener('DOMContentLoaded', function () {
    const floatingDivs = document.querySelectorAll('.executie-containers');

    const observerOptions = {
        root: null, // Use the viewport as the container
        rootMargin: '0px',
        threshold: 0.2 // Trigger when 10% of the element is visible
    };

    function handleIntersection(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    }

    const observer = new IntersectionObserver(handleIntersection, observerOptions);

    floatingDivs.forEach(div => {
        observer.observe(div);
    });
});

document.querySelector('.menu-icon').addEventListener('click', function() {
    document.querySelector('.navbar').classList.toggle('active');
});

