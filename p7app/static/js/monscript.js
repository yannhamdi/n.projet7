


let form = document.querySelector("#question-form");

form.addEventListener("submit", function(event){
	event.preventDefault();
fetch("/sendingServer", {
	 method: "POST",
	 body: new FormData(form)
});







})