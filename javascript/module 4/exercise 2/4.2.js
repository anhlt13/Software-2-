const search = document.querySelector("#search");
search.addEventListener("submit", function(event) {
  event.preventDefault();
  const queryInput = document.querySelector("#query");
  const value = queryInput.value;
  const url = `https://api.tvmaze.com/search/shows?q=${value}`;
  fetch(url).then(response => response.json()).then(data => {
    console.log("Results", data);
  }).catch(error => {
    console.error("Error fetching data", error);
  })
})