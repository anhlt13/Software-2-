const answer = confirm('Should I calculate the square root? ');
target.innerHTML = `${answer}`;

if (answer) {
  number = parseInt(prompt("Enter a number: "));
  if (number > 0) {
    calculate = Math.sqrt(number);
    target.innerHTML = `Your result is ${calculate}`;
  } else {
    target.innerHTML = `The square root of a negative number is not defined`;
  }
} else {
  target.innerHTML = "The square root is not calculated.";
}
