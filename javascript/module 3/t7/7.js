
const targetImage = document.querySelector("#target");
const trigger = document.querySelector("#trigger");
trigger.addEventListener('mouseover', ()=> {
  targetImage.src="img/picB.jpg";
});
trigger.addEventListener('mouseout', () => {
  targetImage.src="img/picA.jpg";
});
