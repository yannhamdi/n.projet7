


let form = document.querySelector("#question-form");
function postFormData(url, data){
	return fetch(url, {
		method : "POST",
		body : data
	})
	.then(response => response.json())
    .catch(error => console.log(error));
}


form.addEventListener("submit", function(event){
	event.preventDefault();
	var nom = document.getElementById("question").value;
	let b = document.querySelector("#question-form");
	var newElt = document.createElement("h5");
	newElt.textContent = nom;
    b.appendChild(newElt);

	postFormData("/sendingServer",  new FormData(form))
	.then(
	       function initMap(parentElt){
         console.log("lololo")
    	 let mapElt = document.createElement("div");
         mapElt.classList.add("map");
         let map = new google.maps.Map(mapElt,{
        center :{lat: response.latitude, lng : response.longitude}, 
    	zoom: 8
    		})();
        b.appendChild(mapElt);

    
})

})
    




