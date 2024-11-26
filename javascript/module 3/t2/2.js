const result = document.querySelector(`#target`);
const l = document.createElement("li")
const t = document.createElement("li")
const o = document.createElement("li")

result.appendChild(l).innerHTML= "First Item"
result.appendChild(t).innerHTML= "Second Item"
result.appendChild(o).innerHTML= "Third Item"

result.setAttribute('class', 'my-list')