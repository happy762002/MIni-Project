// Theme Toggle
const themeToggle = document.getElementById('theme-toggle');
themeToggle.addEventListener('change', () => {
    document.body.classList.toggle('dark-mode');
    // Save theme preference to localStorage
    localStorage.setItem('theme', document.body.classList.contains('dark-mode') ? 'dark' : 'light');
});

// Load theme preference on page load
window.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        themeToggle.checked = true;
    }
});

// Form Validation and Submission Handling
const form = document.getElementById('user-form');
const emailInput = document.getElementById('email');
const emailError = document.getElementById('email-error');



// form.addEventListener('submit', (e) => {
//     e.preventDefault();
//     let isValid = true;

//     // Email validation
//     const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//     if (!emailPattern.test(emailInput.value)) {
//         emailError.classList.add('active');
//         isValid = false;
//     } else {
//         emailError.classList.remove('active');
//     }

//     if (isValid) {
//         setTimeout(() => {
//             alert('Form submitted!');
//             form.reset();         // Clear form fields
//             location.reload();    // Reload to reset state
//         }, 500);
//     }
// });

