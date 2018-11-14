var macros = document.getElementById("macros")
var parrafo = document.getElementById('p')

var actividades = document.getElementById('actividades')
var nuevaFila = actividades.insertRow(-1)

var celda0 = nuevaFila.insertCell(0)
var celda1 = nuevaFila.insertCell(1)
var celda2 = nuevaFila.insertCell(2)

celda0.innerHTML = "Celda0"
celda1.innerHTML = "Celda1"
celda2.innerHTML = "Celda2"

/*console.log(sel.options.length)
for (var i = sel.options.length - 1; i >= 0; i--) {
	parrafo.innerHTML += sel.options[i].text + "<br>"
}
*/
function eleccion_marco() {
	var e = document.getElementById("macros");
	var strUser = e.options[e.selectedIndex].value;
	console.log(strUser)
}
function eleccion_disciplina() {
	var e = document.getElementById("disciplinas");
	var strUser = e.options[e.selectedIndex].value;
	console.log(strUser)
}