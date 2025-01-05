// const heroPics = document.querySelectorAll('.hero-pic img');
// const heroTexts = document.querySelectorAll('.hero-text');
// let currentPic = 0;

// setInterval(() => {
//     heroPics[currentPic].classList.remove('active');
//     heroTexts[currentPic].classList.remove('active');
//     currentPic = (currentPic + 1) % heroPics.length;
//     heroPics[currentPic].classList.add('active');
//     heroTexts[currentPic].classList.add('active');
// }, 3000); /* Change the image and text every 3 seconds */

// heroPics[currentPic].classList.add('active');
// heroTexts[currentPic].classList.add('active');


document.addEventListener("DOMContentLoaded", function () {
    const heroPics = document.querySelectorAll('.hero-pic img');
    const heroTexts = document.querySelectorAll('.hero-text');
    let currentPic = 0;
    let interval = 3000; // Change interval time here if needed
    let index = 0;

    // Initially activate the first image and text
    heroPics[currentPic].classList.add('active');
    heroTexts[index].classList.add('active');

    // Function to cycle through images and texts
    function cycleHeroContent() {
        // Remove 'active' class from the current items
        heroPics[currentPic].classList.remove('active');
        heroTexts[index].classList.remove('active');

        // Update index
        currentPic = (currentPic + 1) % 5;
        index = (index + 1) % 5;
        // Add 'active' class to the new items
        heroPics[currentPic].classList.add('active');
        heroTexts[index].classList.add('active');
    }

    // Start the interval for cycling
    setInterval(cycleHeroContent, interval);
});


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
        879: {
            slidesPerView: 2.3
        },
        980: {
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
    speed: 400,
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

document.querySelector('.menu-icon').addEventListener('click', function () {
    document.querySelector('.navbar').classList.toggle('active');
});

/****messages */
/*MESGAGE*******************************************/
document.addEventListener("DOMContentLoaded", () => {
    const messages = document.querySelectorAll('.message'); // Select all message containers

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible'); // Add class when visible
            } else {
                entry.target.classList.remove('visible'); // Optional: Remove when not visible
            }
        });
    }, { threshold: 0.2 }); // Trigger when 20% of the element is visible

    // Observe each message container
    messages.forEach(message => observer.observe(message));
});
/*****************************testinoms */
document.addEventListener('DOMContentLoaded', function () {
    // Select all test-content elements
    const contents = document.querySelectorAll('.test-content');
    
    // Select the back and next arrows
    const backArrow = document.querySelector('.test-arrows img:first-child');
    const nextArrow = document.querySelector('.test-arrows img:last-child');
    
    // Initialize the index to track the current content
    let currentIndex = 0;

    // Function to update the active content
    function updateActiveContent(newIndex) {
        // Remove the active class from the current content
        contents[currentIndex].classList.remove('active');

        // Update the index (loop around using modulo)
        currentIndex = (newIndex + contents.length) % contents.length;

        // Add the active class to the new content
        contents[currentIndex].classList.add('active');
    }

    // Initialize: Show the first content
    contents[currentIndex].classList.add('active');

    // Event listener for the back arrow
    backArrow.addEventListener('click', function () {
        updateActiveContent(currentIndex - 1); // Move to the previous content
    });

    // Event listener for the next arrow
    nextArrow.addEventListener('click', function () {
        updateActiveContent(currentIndex + 1); // Move to the next content
    });
});
document.addEventListener("DOMContentLoaded", () => {
    const messages = document.querySelectorAll('.testimonals'); // Select all message containers

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible'); // Add class when visible
            } else {
                entry.target.classList.remove('visible'); // Optional: Remove when not visible
            }
        });
    }, { threshold: 0.3 }); // Trigger when 20% of the element is visible

    // Observe each message container
    messages.forEach(message => observer.observe(message));
});
document.addEventListener("DOMContentLoaded", () => {
    const messages = document.querySelectorAll('.contact-us'); // Select all message containers

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible'); // Add class when visible
            } else {
                entry.target.classList.remove('visible'); // Optional: Remove when not visible
            }
        });
    }, { threshold: 0.2 }); // Trigger when 20% of the element is visible

    // Observe each message container
    messages.forEach(message => observer.observe(message));
});