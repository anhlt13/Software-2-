const participants = parseInt(prompt("Enter a number of participants: "));
const ListName = [];
for( let i = 0; i<participants; i++) {
  const names = prompt("Enter names of participants: ");
  ListName.push(names);
}
  ListName.sort();
  let html="<ol>";
  for (let i=0; i< ListName.length; i++) {
  html+=`<li>${ListName[i]}</li>`;
}
html+= "</ol>";
document.body.innerHTML += html;



