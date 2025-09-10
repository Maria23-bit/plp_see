// Check for 'DOMContentLoaded' to ensure the DOM is fully loaded before running script
document.addEventListener("DOMContentLoaded", function() {

    /*
     *  Part 2: JavaScript Functions
     * This section demonstrates functions, parameters, return values, and scope.
     */

    // Function to demonstrate local scope and return value.
    function calculateSum(a, b) {
        // 'sum' is a local variable, accessible only within this function.
        const sum = a + b;
        console.log("Inside calculateSum function, local variable 'sum' is:", sum);
        return sum;
    }

    // A global variable.
    let globalMessage = "The function has been executed.";

    // Function to display the result of the calculation.
    function showResult() {
        // Accessing a global variable from inside a function is allowed.
        console.log("Global message: " + globalMessage);

        // Get values from input fields
        const num1 = document.getElementById("num1").value;
        const num2 = document.getElementById("num2").value;

        // Validate inputs
        if (num1 === "" || num2 === "") {
            // Custom message box to avoid 'alert()'
            const resultText = document.getElementById("resultText");
            resultText.textContent = "Please enter both numbers!";
            resultText.style.color = "red";
            return;
        }

        // Call our reusable function with parameters and store the returned value.
        const total = calculateSum(parseFloat(num1), parseFloat(num2));

        // Update the DOM with the returned value.
        const resultText = document.getElementById("resultText");
        resultText.textContent = "The sum is: " + total;
        resultText.style.color = "inherit"; // Reset color
    }

    // Event listener for the calculation button
    const calculateButton = document.getElementById("calculateButton");
    if (calculateButton) {
        calculateButton.addEventListener("click", showResult);
    }


    /*
     *  Part 3: Combining CSS Animations with JavaScript
     * This section uses JavaScript to dynamically trigger CSS animations.
     */

    // Get the button and the animated box element
    const triggerButton = document.getElementById("triggerAnimation");
    const animatedBox = document.getElementById("animatedBox");
    let isAnimated = false;

    // Function to trigger the slide-in animation
    function triggerSlideIn() {
        if (!isAnimated) {
            // Add the CSS class to trigger the animation.
            animatedBox.classList.add("slide-in");
            isAnimated = true;
        } else {
            // If already animated, remove and re-add the class to re-trigger.
            animatedBox.classList.remove("slide-in");
            // Using a small timeout to allow the browser to remove the class before re-adding.
            setTimeout(() => {
                animatedBox.classList.add("slide-in");
            }, 10);
        }
    }

    // Event listener for the trigger button
    if (triggerButton && animatedBox) {
        triggerButton.addEventListener("click", triggerSlideIn);
    }

    // A function to set up the initial state of the animated box.
    function setupAnimatedBox() {
        // Initially set the box to be invisible.
        animatedBox.style.opacity = '0';
    }

    // Call the setup function when the page loads.
    setupAnimatedBox();
});
