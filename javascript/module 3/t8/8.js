const num1_input = document.querySelector('#num1');
const num2_input = document.querySelector('#num2');
const button = document.querySelector('#start');
let select_Operation = document.querySelector("#operation");
const Total_result = document.querySelector("#result")
button.addEventListener("click", () => {
  const num1 = parseInt(num1_input.value);
  const num2 = parseInt(num2_input.value);
  const Operation = select_Operation.value;
  let result;
  if (Operation === "add"){
    result = num1 + num2;
  }else if(Operation === "sub"){
    result = num1 - num2;
  }else if(Operation === "multi"){
    result = num1 * num2;
  }else if(Operation === "div"){
    result = num1 / num2;
    }
  Total_result.textContent = result
});

