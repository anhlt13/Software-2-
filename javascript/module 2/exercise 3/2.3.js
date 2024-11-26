const Listnames = []
for (let i = 0; i< 6; i++){
  const names = prompt("Enter the names of six dogs: ")
  Listnames.push(names)
}
Listnames.reverse()
let html="<ul>";
for (let i = 0; i<Listnames.length; i++){
  html+=`<li>${Listnames[i]}</li>`;
}
html+=`</ul>`;
document.body.innerHTML +=html;
