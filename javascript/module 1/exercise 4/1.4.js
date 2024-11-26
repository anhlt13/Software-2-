name = prompt("Enter your name: ");
function randomNumber() {
  return Math.ceil(Math.random() * 4);
}
switch(randomNumber()){
  case 1:
    target.innerHTML = `${name} ,you are Gryffindor`;
    break;
  case 2:
    target.innerHTML = `${name} ,"Slytherin"`;
    break;
  case 3:
    target.innerHTML = `${name} ,"Hufflepuff"`;
    break;
  case 4:
    target.innerHTML = `${name} ,"Ravenclaw"`;
    break;
  default:
    console.log("invalid number")
}