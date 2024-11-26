'use strict';
const names = ['John', 'Paul', 'Jones'];
const result = document.querySelector('#target');
const l = document.createElement("li")
const t = document.createElement("li")
const o = document.createElement("li")

for ( let name of names){
    result.appendChild(l).innerHTML= names[0];
    result.appendChild(t).innerHTML= names[1];
    result.appendChild(o).innerHTML= names[2];

}
