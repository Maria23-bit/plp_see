// Part 1: Mastering JavaScript Basics

// 1. Declare a variable to store the user's age.
// We'll assume the user's age is 19 for this example.
let userAge = 19;

// 2. Use a conditional statement to check if the user is 18 or older.
if (userAge >= 18) {
    console.log("You are old enough to vote! ");
} else {
    console.log("You are not yet old enough to vote. ");
}

// 3. You can also get input from the user using a prompt.
// let userAgeInput = prompt("Please enter your age:");
// if (userAgeInput >= 18) {
//     console.log("You are old enough to vote!");
// } else {
//     console.log("You are not yet old enough to vote.");
// }

// To display the output on the webpage, you can modify a DOM element (see Part 4).
// Part 2: JavaScript Functions

// 1. Function to calculate the area of a rectangle.
// This function takes two parameters: width and height.
function calculateRectangleArea(width, height) {
    return width * height;
}

// 2. Function to format a user's name.
// This function takes a name and returns it with a greeting.
function greetUser(name) {
    return `Hello, ${name}! Welcome to the page. `;
}

// You can call these functions and use their returned values.
let area = calculateRectangleArea(10, 5);
console.log(`The area of the rectangle is: ${area}`); // Output: The area of the rectangle is: 50

let greeting = greetUser("Alice");
console.log(greeting); // Output: Hello, Alice! Welcome to the page. 
// Part 3: JavaScript Loops

// 1. Using a 'for' loop to iterate through an array of numbers.
const numbers = [2, 4, 6, 8, 10];
console.log("Listing even numbers:");
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}

// 2. Using a 'while' loop to create a simple countdown.
let countdown = 5;
console.log("Starting countdown:");
while (countdown > 0) {
    console.log(countdown);
    countdown--;
}
console.log("Blast off! ");

// 3. You could also use a forEach loop for arrays.
console.log("Listing even numbers with forEach:");
numbers.forEach(number => {
  console.log(number);
});
// Part 4: Mastering the DOM

// 1. Select an element and change its text content.
// This happens after the button is clicked.
const messageElement = document.getElementById("message");
const myButton = document.getElementById("myButton");

myButton.addEventListener("click", () => {
    messageElement.textContent = "You clicked the button! The text has changed.";
    messageElement.classList.add("highlight "); // Add a CSS class
});

// 2. Create and append new elements to the page.
const shoppingList = document.getElementById("shoppingList");
const items = ["Apples ", "Milk ", "Bread "];

// Use a loop to create list items dynamically.
items.forEach(itemText => {
    const li = document.createElement("li");
    li.textContent = itemText;
    shoppingList.appendChild(li);
});

// 3. Respond to another event, like a mouseover.
// This example could change the background color of the shopping list.
shoppingList.addEventListener("mouseover", () => {
    shoppingList.style.backgroundColor = "#f0f0f0";
});

shoppingList.addEventListener("mouseout", () => {
    shoppingList.style.backgroundColor = "transparent";
});