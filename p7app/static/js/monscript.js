


let form = document.querySelector("#question-form");
form.addEventListener("submit", function(event){
	event.preventDefault();
	console.log("ok")



    fetch("/sendingServer", {
	     method: "POST",
	     body: new FormData(form)

})
    .then(response => response.json())
    .catch(error => console.log(error));
    

})
console.log(response);



