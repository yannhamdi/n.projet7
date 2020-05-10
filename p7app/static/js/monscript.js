
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
    var myImg = new Image();
    myImg.src = '/static/img/ajax-loader.gif';
    myImg.classList.add("icone");
    b.appendChild(myImg);
    const loader = document.querySelector(".icone");
    loader.classList += "waiting";
    try{
        var nom = document.getElementById("question").value;
        var newElt = document.createElement("h5");
        newElt.classList.add("answer");
        newElt.textContent = nom ;
        b.appendChild(newElt);
        var adAsked = document.createElement("h5");
        adAsked.classList.add("answer")
        adAsked.textContent = "Voici l'addresse demandée: " + response.addresse ;
        loader.className = "icone";
        b.appendChild(adAsked);
        var infoAsked = document.createElement("h5");
        infoAsked.classList.add("answer")
        infoAsked.textContent = "T'ai je dèja raconté mon petit loup ce qui se trouve aux alentours? " + response.inquiries ;
        b.appendChild(infoAsked);
        let latitude = response.latitude;
        let longitude = response.longitude;
        initMap(latitude, longitude);
        var textChat = document.createElement("h5");
        textChat.classList.add("answer");
        textChat.textContent = "Mon petit lapin si tu en veux savoir plus, je t'invite à visiter la page wikipedia en visitant le lien ci dessous:";
        b.appendChild(textChat);
        var urlAsked = document.createElement("a");
        var linkText = document.createTextNode(response.weblink);
        urlAsked.appendChild(linkText);
        urlAsked.classList.add("answer");
        urlAsked.title = "lien" ;
        urlAsked.href = response.weblink ;
        b.appendChild(urlAsked);
}
    catch(error){
        var messageError = document.createElement("h5");
        messageError.classList.add("answer");
        loader.className = "icone";
        messageError.textContent = "Je sais que je suis un dinosaure et que je connais énormèment de choses mais là je dois avouer que tu m'as posé une colle... Désolé mon petit canard";
        b.appendChild(messageError);
    }
}
function sendingErrorMessage(){
    var myImg = new Image();
    myImg.src = '/static/img/ajax-loader.gif';
    myImg.classList.add("icone");
    var load = document.getElementById("loader");
    load.appendChild(myImg);
    const loader = document.querySelector(".icone");
    loader.classList += "waiting";
    var messageError = document.createElement("h5");
    messageError.classList.add("answer");
    loader.className = "icone";
    messageError.textContent = "Je sais que je suis un dinosaure et que je connais énormèment de choses mais là je dois avouer que tu m'as posé une colle... Désolé mon petit canard";
    b.appendChild(messageError);


}
form.addEventListener("submit", function(event){
    event.preventDefault();
    
    postFormData("/sendingServer",  new FormData(form))
    .then(response => processPotAnswer(response)
           )
    .catch(error => console.log(error))
})