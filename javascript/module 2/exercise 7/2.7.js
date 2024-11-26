function dice(sides){
  return Math.floor(Math.random() * sides) + 1;
}
function main(){
  const user = parseInt(prompt("Enter the maximum number of dice: "));
  let roll;
  let html = `<ul>`;
  while (true){
    roll = dice(user);
    html += `<li>${roll}</li>`;
    if (roll===user){
      break;
    }
  }
  html += `</ul>`;
  document.body.innerHTML += html
}
main();