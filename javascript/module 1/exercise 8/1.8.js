const start_year = prompt("Enter the start year: ")
const end_year = prompt("Enter the ending year: ")
function checkLeapYear(year) {
  return ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0);
}
let html = "<ul>";
for(let year = start_year; year <= end_year; year++){
  if (checkLeapYear(year)) {
    html += `<li>${year}</li>`;
  }
}
html += "</ul>"
/*html string is not automatically rendered so need to add these sentence below to read */
document.body.innerHTML += html;