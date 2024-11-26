const number = parseInt(prompt("Enter a number you want to check: "))
function CheckNum(number){
  if (number % number === 0 && number % 1 === 0 ) {
    console.log(number, "is a prime number");
    target.innerHTML = `${number} is a prime number`;
  }else{
    target.innerHTML = `${number} is not a prime number`;
    }
}
