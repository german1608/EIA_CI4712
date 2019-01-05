function buscar(){
	//elemento a buscar
	var texto = document.getElementById("buscar-plan")
	var restar = 0
	// Validacion de seleccion
	if (texto.value != ""){
		var tbody = document.getElementById("contenido")
		var tr = tbody.getElementsByTagName("tr")
		//Iteracion sobre la tabla
		for (var i = tr.length - 1; i >= 0; i--) {
			var td = tr[i].getElementsByTagName("td")
			//match
			if ((td[0].innerText == texto.value) || (td[1].innerText == texto.value) || (td[2].innerText == texto.value) ||
				(td[3].innerText == texto.value) || (td[4].innerText == texto.value) || (td[5].innerText == texto.value)){
				tr[i].style.display = "";
			}
			else {
				tr[i].style.display = "none";
				restar += parseInt(td[5].innerText)
			}
		}
	}
	calcularTotal(restar)
}
function teclado(){
	var input = document.getElementById("buscar-plan")
	input.addEventListener('keydown', presionaEnter)
}
function presionaEnter(evento){
	if (evento.keyCode == 13) {buscar()}
}

function calcularTotal(restar){
	//elemento a buscar
	var texto = document.getElementById("total")
	var suma = 0
	var tbody = document.getElementById("contenido")
	var tr = tbody.getElementsByTagName("tr")
	//Iteracion sobre la tabla
	for (var i = tr.length - 1; i >= 0; i--) {
		var td = tr[i].getElementsByTagName("td")
		//realizar suma
		suma += parseInt(td[5].innerText)
	}
	texto.value = suma-restar
}

window.addEventListener('load', calcularTotal(0))