document.querySelector("#searchFrom").addEventListener("submit", function(event){
  event.preventDefault();
  const query = document.querySelector("#query").value;
  fetch(`https://api.tvmaze.com/search/shows?q=${query}`)
      .then(response => response.json())
      .then(data =>{
        console.log(data);
  })
      .catch(error => {
        console.error("Error fetching data", error);
  })
})