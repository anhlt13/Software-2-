function dice() {
  return Math.floor(Math.random() * 6) + 1;
}
function main(){
  let roll;
  let html = `<ul>`;
  do {
    roll = dice();
    html += `<li>${roll}</li>`;
  }
  while(roll!==6);
html += `</ul>`;
document.body.innerHTML += html;
}
main();