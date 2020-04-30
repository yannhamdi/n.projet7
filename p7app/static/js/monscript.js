
let form = document.querySelector("#question-form");
let b = document.querySelector("#question-form");
function postFormData(url, data){
	return fetch(url, {
		method : "POST",
		body : data
	})
	.then(response => response.json())
    .catch(error => console.log(error));
}
function initMap(latitude, longitude){
    	let mapElt = document.createElement("div");
    	
    	let myLatLng = {lat: latitude, lng: longitude};
         mapElt.classList.add("map");
         let map = new google.maps.Map(mapElt,{
         center : myLatLng,
         zoom: 12
    	})
        
        b.appendChild(mapElt);
        var marker = new google.maps.Marker({position: myLatLng, map: map});
    }
function processPotAnswer(response){
	var nom = document.getElementById("question").value;
	var newElt = document.createElement("h5");
	newElt.textContent = nom ;
    b.appendChild(newElt);
    let latitude = response.latitude;
    let longitude = response.longitude;
    initMap(latitude, longitude);
}

form.addEventListener("submit", function(event){
	event.preventDefault();
	
	postFormData("/sendingServer",  new FormData(form))
	.then(response => processPotAnswer(response)
	       );
})





