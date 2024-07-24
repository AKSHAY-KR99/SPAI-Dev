document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.menu-icon').addEventListener('click', function() {
        document.querySelector('.navbar').classList.toggle('active');
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.news-container');
  
    container.addEventListener('mouseover', () => {
      container.style.transform = 'scale(1.02)'; // Zoom in
    });
  
    container.addEventListener('mouseout', () => {
      container.style.transform = 'scale(1)'; // Zoom out
    });
  });
  