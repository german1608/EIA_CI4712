//Funcionalidad de validacion
function validar(){
	//Constantes
	var constantes = {};
	constantes.limite_pond = 100;
	constantes.id_inputs = ["id_pondIntensidad","id_pondExtension","id_pondDuracion","id_pondReversibilidad","id_pondProbabilidad"];
	constantes.inputs = [];
	constantes.submit = document.getElementById("formulario");
	
	//Se obtienen los apuntadores a los objetos DOM (Los inputs) dado sus ID
	for (var i = 0; i < constantes.id_inputs.length; i++) { 
		constantes.inputs.push(document.getElementById(constantes.id_inputs[i]))
	}

	//Funcion que revisa si el input esta vacio
	function esVacio(input){
		return input.value.length == 0;
	}
	
	//Funcion que revisa si es un numero
	function noEsNumero(valor){
		return isNaN(Number(valor))
	};
	
	//Funcion para determinar si la sumatoria esta por debajo del limite
	function sumatoria_debajo(){
		var sumatoria = 0;
		var valor;
		for (var i = 0; i < constantes.id_inputs.length; i++) { 
			if(esVacio(constantes.inputs[i])){
				continue;
			}
				
			valor = constantes.inputs[i].value;
			if(noEsNumero(valor)){
				alert("El valor ingresado no es un numero.");
				return false;
			}
			sumatoria+= Number(valor);
			if(sumatoria > constantes.limite_pond){

				alert("El valor ingresado supera el limite [100%], dada la suma de las ponderaciones: "+sumatoria.toString())
				return false;
			}
		}		
		
		return true;
	};
	
	//Funcion para determinar si la sumatoria da el limite
	function sumatoria_limite(){
		var sumatoria = 0;
		var valor;
		for (var i = 0; i < constantes.id_inputs.length; i++) { 
			if(esVacio(constantes.inputs[i])){
				alert("Existe una ponderacion que está vacia, por favor verificar.");
				return false;
			}
				
			valor = constantes.inputs[i].value;

			if(noEsNumero(valor)){
				alert("Existe una ponderacion que posee un valor no numerico, por favor verificar.");
				return false;
			}
			
			sumatoria+= Number(valor);
		}		
	

		if(sumatoria == constantes.limite_pond){
			return true;
		}
		alert("La ponderacion tiene un valor distinto a 100. Actualmente es :" + sumatoria.toString());
		return false;
	};
	
	//Se agrega la funcion de verificar el 100% al presionar el boton submit
	constantes.submit.onsubmit = function() {
    	return sumatoria_limite();
	};

	//Se agrega a cada uno de los campos la validacion al cambiar el contenido del input
	for (var i = 0; i < constantes.id_inputs.length; i++) { 
		constantes.inputs[i].onchange = function(){

			if(!sumatoria_debajo()){
				this.value = 0;
			}
		}
	}
	
	function esta_entre(valor){
		return valor >= 0 && valor <=10; 
	}
	
	function probabilidad_validado(){
		
		if(noEsNumero(constantes.ponderacion.value)){
			alert("El valor ingresado no es un numero.");
			return false;			
		}
		
		if(!esta_entre(Number(constantes.ponderacion.value))){
			alert("El valor no está entre 0 y 10");
			return false;				
		}
		
		return true;
	};
	
};

//Al cargar la pagina se activa la funcionalidad de validacion
window.onload = function() {
	validar();
};
