const List = [];
for (let i = 0; i <5 ; i++) {
  const userNumbers = parseInt(prompt("Enter five random numbers: "));
  console.log(userNumbers);
  List.push(userNumbers);
}
console.log("Numbers in reverse order: ");
for(let i = List.length - 1; i >= 0; i--){
  console.log(List[i]);
}
