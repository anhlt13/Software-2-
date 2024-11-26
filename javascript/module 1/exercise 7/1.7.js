
function rollDice(numRolls){
  let sum = 0;
  for (let i = 0; i<numRolls; i++){
    sum += Math.floor(Math.random()*6)+1;
  }
  return sum;
}
const numRolls = parseInt(prompt("Enter a number of dice you would like to roll: "));
const diceSum = rollDice(numRolls);
console.log("The sum of the dice rolls is: ", diceSum);
target.innerHTML = `The sum of the dice rolls is: ${diceSum}`;