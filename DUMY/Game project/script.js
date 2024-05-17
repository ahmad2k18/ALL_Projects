document.addEventListener("DOMContentLoaded", function() {
    // Start the game
    startGame();

    // Event listeners for the choices
    document.getElementById("leftChoice").addEventListener("click", function() {
        makeChoice("left");
    });
    document.getElementById("rightChoice").addEventListener("click", function() {
        makeChoice("right");
    });
});

function startGame() {
    var storyElement = document.getElementById("story");
    storyElement.innerText = "Welcome to the Adventure Game! You find yourself in a mysterious forest...";

    var choicesElement = document.getElementById("choices");
    choicesElement.style.display = "none";
}

function makeChoice(choice) {
    var storyElement = document.getElementById("story");
    var choicesElement = document.getElementById("choices");

    switch (choice) {
        case "left":
            storyElement.innerText = "You chose the left path... You find a hidden treasure! Congratulations! You win!";
            break;
        case "right":
            storyElement.innerText = "You chose the right path... You encounter a hungry bear... You were eaten by the bear. Game over!";
            break;
    }

    // Hide the choices after making a choice
    choicesElement.style.display = "none";
}
