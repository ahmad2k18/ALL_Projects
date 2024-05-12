const resultElement = document.getElementById('result');
const lengthElement = document.getElementById('length');
const uppercaseElement = document.getElementById('uppercase');
const lowercaseElement = document.getElementById('lowercase');
const numbersElement = document.getElementById('numbers');
const symbolsElement = document.getElementById('symbols');
const generateElement = document.getElementById('generate');
const clipboardElement = document.getElementById('clipboard');

const randomFunc = {
  lower: getRandomLower,
  upper: getRandomUpper,
  number: getRandomNumber,
  symbol: getRandomSymbol,
};

clipboardElement.addEventListener('click', () => {
  const textarea = document.createElement('textarea');
  const password = resultElement.innerText;

  if (!password) {
    return;
  }
  textarea.value = password;
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand('copy');
  textarea.remove();
  alert('Password copied to clipboard');
});

generateElement.addEventListener('click', () => {
  const length = +lengthElement.value;
  const hasLower = lowercaseElement.checked;
  const hasUpper = uppercaseElement.checked;
  const hasNumber = numbersElement.checked;
  const hasSymbol = symbolsElement.checked;

  resultElement.innerText = generatePassword(length, hasLower, hasUpper, hasNumber, hasSymbol);
});

function generatePassword(length, lower, upper, number, symbol) {
  let generatedPassword = '';

  const typesCount = lower + upper + number + symbol;
  const typesArr = [{ lower: lower }, { upper: upper }, { number: number }, { symbol: symbol }].filter(
    (item) => Object.values(item)[0]
  );
  // Object.values() example:
  //   const object1 = { a: 'somestring', b: 42, c: false, };
  //   console.log(Object.values(object1));
  //         expected output: Array ["somestring", 42, false]

  if (typesCount === 0) {
    return '';
  }

  for (let i = 0; i < length; i++) {
    const randomType = typesArr[Math.floor(Math.random() * typesArr.length)];
    const randomFuncName = Object.keys(randomType)[0];
    generatedPassword += randomFunc[randomFuncName]();
  }

  console.log(generatedPassword);

  return generatedPassword;
}

function getRandomLower() {
  return String.fromCharCode(97 + Math.floor(Math.random() * 26));
}

function getRandomUpper() {
  return String.fromCharCode(65 + Math.floor(Math.random() * 26));
}

function getRandomNumber() {
  return String.fromCharCode(48 + Math.floor(Math.random() * 10));
}

function getRandomSymbol() {
  const symbols = '"' + "!#$%&'()*+,-./:;<=>?@[]^_`{|}~";
  return symbols.charAt(Math.floor(Math.random() * symbols.length));
}
