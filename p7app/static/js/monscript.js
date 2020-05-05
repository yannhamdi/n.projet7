
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
	newElt.classList.add("chat")
	newElt.textContent = nom ;
    b.appendChild(newElt);
    var adAsked = document.createElement("h5");
    adAsked.classList.add("chat")
    adAsked.textContent = "Voici l'addresse demandée: " + response.addresse ;
    b.appendChild(adAsked);
    var infoAsked = document.createElement("h5");
    infoAsked.classList.add("answer")
    infoAsked.textContent = "T'ai je dèja raconté mon petit loup ce qui se trouve aux alentours? " + response.inquiries ;
    b.appendChild(infoAsked);
    let latitude = response.latitude;
    let longitude = response.longitude;
    initMap(latitude, longitude);
    var urlAsked = document.createElement("a");
    var linkText = document.createTextNode(response.weblink)
    urlAsked.appendChild(linkText);
    urlAsked.classList.add("answer");
    urlAsked.title = "lien" ;
    urlAsked.href = response.weblink ;
    b.appendChild(urlAsked);
}
function sendingErrorMessage(){
    var messageError = document.createElement("h5");
    messageError.classList.add("chat");
    messageError.textContent = "Je sais que je suis un dinosaure et que je connais énormèment de choses mais là je dois avouer que tu m'as posé une colle... Désolé mon petit canard";
    b.appendChild(messageError);


}
form.addEventListener("submit", function(event){
	event.preventDefault();
	
	postFormData("/sendingServer",  new FormData(form))
	.then(response => processPotAnswer(response)
	       )
	.catch(error => sendingErrorMessage());
})






