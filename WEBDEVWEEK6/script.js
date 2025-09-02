// --- Part 1: Event Handling ---
// Get the button element from the DOM
const myButton = document.getElementById('myButton');

// Add a click event listener
myButton.addEventListener('click', () => {
    alert('Button was clicked!');
});

// --- Part 2: Interactive Elements: Light/Dark Mode Toggle ---
// Get the toggle button and the body element
const themeToggle = document.getElementById('themeToggle');
const body = document.body;

// Add a click event listener to the toggle button
themeToggle.addEventListener('click', () => {
    // Toggle the 'dark-theme' class on the body
    body.classList.toggle('dark-theme');
});

// --- Part 3: Form Validation ---
// Get form elements
const myForm = document.getElementById('myForm');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');

// Get error message elements
const nameError = document.getElementById('nameError');
const emailError = document.getElementById('emailError');
const passwordError = document.getElementById('passwordError');
const successMessage = document.getElementById('successMessage');

// Add a submit event listener to the form
myForm.addEventListener('submit', (event) => {
    // Prevent the default form submission
    event.preventDefault();

    let formIsValid = true;

    // Reset all previous error messages
    nameError.textContent = '';
    emailError.textContent = '';
    passwordError.textContent = '';
    successMessage.textContent = '';

    // Validate Name
    if (nameInput.value.trim() === '') {
        nameError.textContent = 'Name is required.';
        formIsValid = false;
    }

    // Validate Email using a regular expression
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(emailInput.value)) {
        emailError.textContent = 'Please enter a valid email address.';
        formIsValid = false;
    }

    // Validate Password (e.g., min length of 8)
    if (passwordInput.value.length < 8) {
        passwordError.textContent = 'Password must be at least 8 characters long.';
        formIsValid = false;
    }

    // If all fields are valid, show a success message
    if (formIsValid) {
        successMessage.textContent = 'Form submitted successfully!';
        myForm.reset(); // Optional: Clear the form
    }
});