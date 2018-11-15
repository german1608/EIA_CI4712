function buscar(){
		//elemento a buscar
		var texto = document.getElementById("busqueda")
		// Validacion de seleccion
		if (texto.value != ""){
			var tbody = document.getElementById("contenido")
			var tr = tbody.getElementsByTagName("tr")
			//Iteracion sobre la tabla
			for (var i = tr.length - 1; i >= 0; i--) {
				var td = tr[i].getElementsByTagName("td")
				//match
				if ((td[0].innerText == texto.value) || (td[1].innerText == texto.value) || (td[2].innerText == texto.value) || (td[3].innerText == texto.value)){
					tr[i].style.display = "";
				}
				else {
					tr[i].style.display = "none";
				}
			}
		}	
	}