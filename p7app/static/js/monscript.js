


let form = document.querySelector("#question-form");
let map = document.createElement('div');
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
	console.log(nom);
	let b = document.querySelector("#question-form");
	var newElt = document.createElement("h5");
	newElt.textContent = nom;
    b.appendChild(newElt);

	postFormData("/sendingServer",  new FormData(form))
	.then(response => {
		console.log(response.latitude)
    })
    .then(function initMap(){

    		map = new google.maps.Map(document.getElementById('map'),{
    			center :{lat: response.latitude, lng : response.longitude}, 
    			zoom: 8
    		});
    initMap();
    	
})



