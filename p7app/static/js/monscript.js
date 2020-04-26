


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
	postFormData("/sendingServer",  new FormData(form))
	.then(response => {
		console.log(response.latitude)
    })
})



