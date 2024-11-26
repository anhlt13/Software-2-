
  const number = parseInt(prompt("Enter a number of dice: "));
  const sum = parseInt(prompt("Enter the sum of eye numbers of interest: "));
  const numTrials = 10000;
  let successfulTrials = 0;
  for (let i = 0; i< numTrials; i++){
    let rollSum = 0;
    for (let j=0; j< number; j++){
      rollSum += Math.floor(Math.random() * 6) + 1;
    }
    if (rollSum === sum){
      successfulTrials++;
    }
  }
  const probability = (successfulTrials/numTrials)*100;
  target.innerHTML =`Probability to get sum ${sum} with ${number} dice is ${probability.toFixed(2)} %`
