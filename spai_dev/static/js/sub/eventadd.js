document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.menu-icon').addEventListener('click', function() {
        document.querySelector('.navbar').classList.toggle('active');
    });
});
document.getElementById('eventForm').addEventListener('submit', function(event) {
    let isValid = true;

    // Clear previous errors
    document.querySelectorAll('.error-message').forEach(el => el.textContent = '');

    // Title validation
    const title = document.getElementById('title').value.trim();
    if (title.length === 0) {
        document.getElementById('titleError').textContent = 'Title is required.';
        isValid = false;
    }

    // Image validation
    const image = document.getElementById('image').files[0];
    if (!image) {
        document.getElementById('imageError').textContent = 'Image is required.';
        isValid = false;
    } else if (!['image/jpeg', 'image/png', 'image/gif'].includes(image.type)) {
        document.getElementById('imageError').textContent = 'Only JPEG, PNG, and GIF images are allowed.';
        isValid = false;
    }

    // Date and Time validation
    const datetime = document.getElementById('datetime').value;
    if (!datetime) {
        document.getElementById('datetimeError').textContent = 'Date and time are required.';
        isValid = false;
    }

    // // Location validation
    // const location = document.getElementById('location').value.trim();
    // if (location.length === 0) {
    //     document.getElementById('locationError').textContent = 'Location is required.';
    //     isValid = false;
    // }

    // Description validation
    const description = document.getElementById('description').value.trim();
    if (description.length === 0) {
        document.getElementById('descriptionError').textContent = 'Description is required.';
        isValid = false;
    }

    // Registration Link validation
    const registrationLink = document.getElementById('registration_link').value.trim();
    if (registrationLink.length > 0 && !/^https?:\/\/[^\s]+$/.test(registrationLink)) {
        document.getElementById('registrationLinkError').textContent = 'Invalid URL format.';
        isValid = false;
    }

    // Prevent form submission if not valid
    if (!isValid) {
        event.preventDefault();
    }
});
function previewImage(event) {
    const file = event.target.files[0];
    const preview = document.getElementById('preview');
    const imagePreview = document.getElementById('imagePreview');

    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result;
            preview.style.display = 'block'; // Ensure the image is visible
            imagePreview.style.display = 'block'; // Show the preview container
            imagePreview.style.backgroundImage = `url(${e.target.result})`;
        }
        reader.readAsDataURL(file);
    } else {
        preview.style.display = 'none'; // Hide the image if no file is selected
        imagePreview.style.display = 'none'; // Hide the preview container if no file is selected
    }
}
