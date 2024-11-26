'use strict';


  const num1 = parseInt(prompt("Enter the 1st number: "));
  const num2= parseInt(prompt("Enter the 2nd number: "));
  const num3 = parseInt(prompt("Enter the 3rd number: "));

document.querySelector('#sum').innerHTML = `The sum is ${num1 + num2 + num3}`;
document.querySelector('#product').innerHTML = `The product is ${num1 * num2 * num3}`;
document.querySelector('#average').innerHTML = `The average is ${(num1 + num2 + num3)/3}`;




