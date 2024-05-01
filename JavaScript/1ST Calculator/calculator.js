let displayValue = '';

function appendValue(value) {
    displayValue += value;
    document.getElementById('display').value = displayValue;
}

function calculate() {
    try {
        displayValue = eval(displayValue);
        document.getElementById('display').value = displayValue;
    } catch (error) {
        alert('Invalid expression');
    }
}

function clearDisplay() {
    displayValue = '';
    document.getElementById('display').value = '';
}
