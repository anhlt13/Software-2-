const Listnum = [];
while(true){
  const numbers = parseInt(prompt("Enter numbers: "));
  if(Listnum.includes(numbers)) {
    console.log("the has already been given");
    break;
  }
Listnum.push(numbers);
Listnum.sort((a, b) => a - b);
console.log("Entered numbers in ascending order:", Listnum);
}
