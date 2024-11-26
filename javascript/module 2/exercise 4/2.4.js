const Listnum = [];
while (true){
  const user = parseInt(prompt("Please enter a number: "));
  if(user===0) {
    break;
  }
  Listnum.push(user);
  Listnum.sort((a,b) => b-a);
  console.log(Listnum);
}
