document.addEventListener('DOMContentLoaded', function () {
    const floatingDivs = document.querySelectorAll('.animate');

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

document.addEventListener('DOMContentLoaded', function () {
    const floatingDivs = document.querySelectorAll('.animate-z');

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

document.addEventListener('DOMContentLoaded', function () {
    const floatingDivs = document.querySelectorAll('.animate-h3');

    const observerOptions = {
        root: null, // Use the viewport as the container
        rootMargin: '0px',
        threshold: 0.9 // Trigger when 10% of the element is visible
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

document.addEventListener('DOMContentLoaded', function () {
    const floatingDivs = document.querySelectorAll('.animate2');

    const observerOptions = {
        root: null, // Use the viewport as the container
        rootMargin: '0px',
        threshold: 0.1 // Trigger when 10% of the element is visible
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