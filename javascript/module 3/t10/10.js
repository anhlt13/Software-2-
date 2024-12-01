const source = document.querySelector("#source");
const first_name = document.querySelector('input[name = "firstname"]');
const last_name = document.querySelector('input[name="lastname"]');
const sentences = document.querySelector('#target');
source.addEventListener('submit', (event) =>{
  event.preventDefault();
  const firstName = first_name.value;
  const lastName = last_name.value;
  sentences.textContent = `Your name is ${firstName} ${lastName}`;
});
