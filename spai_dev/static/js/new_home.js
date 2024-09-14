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
var swiper = new Swiper('.news-containers', {
    slidesPerView: 1.2, // You can set this to 'auto' for responsive slides
    spaceBetween: 2,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        478: {
        slidesPerView: 1.5, // 2 slides on tablets
        
        },
        580: {
        slidesPerView: 1.8, // 2 slides on tablets
        
        },
        680: {
        slidesPerView: 2.2, // 2 slides on tablets
        
        },
        768: {
        slidesPerView: 2, // 2 slides on tablets
        
        },
        879:{
            slidesPerView: 2.3
        },
        980:{
            slidesPerView: 2.6
        },
        1110: {
        slidesPerView: 3.2, // 3 slides on desktops
        
        },
    },
    autoplay: {
        delay: 3000, // Time between slides (in milliseconds)
        disableOnInteraction: false, // Keeps autoplay active even after user interaction
        
    },
    speed:400,
    loop: true, // Enable loop mode if required
});

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
