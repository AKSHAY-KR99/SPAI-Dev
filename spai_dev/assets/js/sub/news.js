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

  document.addEventListener('DOMContentLoaded', function () {
    const deleteLinks = document.querySelectorAll('.delete-link');
    
    deleteLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            const url = this.getAttribute('href');
            if (confirm('Do you want to delete this item?')) {
                window.location.href = url;
            }
        });
    });
});
  