'use strict'
function checkLeapYear(year) {
  if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    target.innerHTML = `${year} is a leap year`;
  } else {
    target.innerHTML = `${year} is not a leap year`;
  }
}

let year = prompt("Enter a year: ");
checkLeapYear(year);
