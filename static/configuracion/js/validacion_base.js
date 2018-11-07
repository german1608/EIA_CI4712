//Funcionalidad de validacion
function validar(){
	//Constantes
	var constantes = {};
	constantes.limite_pond = 100;
	constantes.inputs = {};
	constantes.inputs.intensidad = [];
	constantes.inputs.extension = [];
	constantes.inputs.duracion = [];
	constantes.inputs.reversibilidad = [];
	constantes.inputs.probabilidad = [];
	constantes.inputs.importancia = [];
	
	// Value + i ... i donde empieza los inputs de una tabla
	constantes.limites = [1,13,17,21,25,29]
	
	//Sub limites de la tabla intensidad
	
	constantes.limites_sub = [1,5,9]
	//1:Creciente : El de mas arriba es el de mayor valor
	//0:Decreciente: el de más arriba es el de menor valor
	constantes.tablas_orden = [1,1,0,1,1,1]	
	
	constantes.submit = document.getElementsByName("submit")[0];
	

	var cantidad_inputs = 32;	
	var type = "intensidad";
	//Obtener los inputs segun el tipo
	for (var i = 1; i <= cantidad_inputs; i++) {
		if(i==constantes.limites[1]){
			type = "extension";
		}else if(i==constantes.limites[2]){	
			type = "duracion";				
		}else if(i==constantes.limites[3]){	
			type = "reversibilidad";	
		}else if(i==constantes.limites[4]){	
			type = "probabilidad";	
		}else if(i==constantes.limites[5]){	
			type = "importancia";	
		}

		constantes.inputs[type].push(document.getElementsByName("valor"+i)[0])
	}
	
	//Funciones para validacion de tipos
	
	//Funcion que revisa si el input esta vacio
	function esVacio(input){
		return input.value.length == 0;
	};	

	//Funcion que revisa si es un numero
	function noEsNumero(valor){
		return isNaN(Number(valor))
	};		

	function esta_entre(valor){
		return valor >= 0 && valor <=10; 
	}			
	
	function input_pertenece(numero){
		for (var i = 0; i < constantes.limites.length-1; i++) { 
			if(numero>=constantes.limites[i] && numero<constantes.limites[i+1]){
				return i;
			}
		}
		return constantes.limites.length-1;
	}
	
	function input_pertenece_intensidad(numero){
		for (var i = 0; i < constantes.limites.length-1; i++) { 
			if(numero>=constantes.limites_sub[i] && numero<constantes.limites_sub[i+1]){
				return i;
			}
		}
		return constantes.limites_sub.length-1;
	}	
	
	function esta_en_borde_izquierdo(numero,tabla){
		return numero == constantes.limites_sub[tabla]
	}	
	
	function esta_en_borde_derecho(numero,tabla){
		if(numero==constantes.limites[1]-1){
			return true;
		}		
		return numero == constantes.limites_sub[tabla+1]-1
	}
	
	function esta_en_borde_superior(numero,tabla){
		return numero == constantes.limites[tabla]
	}

	function esta_en_borde_inferior(numero,tabla){
		if(numero==cantidad_inputs){
			return true;
		}
		return numero == constantes.limites[tabla+1]-1;
	}	
	
	function promedio_intensidad(number,tabla){
		var number = Number(number)
		var valor1,valor2;
		if(esta_en_borde_izquierdo(number,tabla)){
			valor1 = 10;
			valor2 = document.getElementsByName("valor"+(number+1).toString())[0].value;		

		}else if(esta_en_borde_derecho(number,tabla)){
			valor1 = document.getElementsByName("valor"+(number-1).toString())[0].value;
			valor2 = 0;
		}else{
			valor1 = document.getElementsByName("valor"+(number-1).toString())[0].value;
			valor2 = document.getElementsByName("valor"+(number+1).toString())[0].value;	
		}
		valor1 = Number(valor1);
		valor2 = Number(valor2);
		return (valor1 + valor2)/2		
	}

	function promedio(number,tabla,crecimiento){
		var number = Number(number)
		var valor1,valor2;
		if(esta_en_borde_superior(number,tabla)){
			if(crecimiento==1){
				valor1 = 10;
			}else{
				valor1 = 0;			
			}
			valor2 = document.getElementsByName("valor"+(number+1).toString())[0].value;		

		}else if(esta_en_borde_inferior(number,tabla)){
			valor1 = document.getElementsByName("valor"+(number-1).toString())[0].value;
			if(crecimiento==1){
				valor2 = 0;
			}else{
				valor2 = 10;			
			}
		}else{
			valor1 = document.getElementsByName("valor"+(number-1).toString())[0].value;
			valor2 = document.getElementsByName("valor"+(number+1).toString())[0].value;	
		}
		valor1 = Number(valor1);
		valor2 = Number(valor2);
		return (valor1 + valor2)/2
	};
	
	function set_correct_value(input){
		var tag = input.name;
		var numero = Number(tag.substring(5, tag.length));
	
		if(numero<constantes.limites[1]){
			//El de mayor valor es el de arriba:
			var tabla = input_pertenece_intensidad(numero);
			return promedio_intensidad(numero,tabla)		
		}else{
			//El de mayor valor es el de arriba:
			var tabla = input_pertenece(numero);
			return promedio(numero,tabla,constantes.tablas_orden[tabla])
		}
	}
	

	function esta_entre_al_lado(input){
		var tag = input.name;
		var number = Number(tag.substring(5, tag.length));
		var valorEntre = Number(input.value);
		if(number<constantes.limites[1]){
	
			//El de mayor valor es el de arriba:
			var tabla = input_pertenece_intensidad(number);
			var valor1,valor2
			
			if(esta_en_borde_izquierdo(number,tabla)){
				valor1 = 10;
				valor2 = document.getElementsByName("valor"+(number+1).toString())[0].value;		
			}else if(esta_en_borde_derecho(number,tabla)){
				valor1 = document.getElementsByName("valor"+(number-1).toString())[0].value;
				valor2 = 0;			
			}else{
				valor1 = document.getElementsByName("valor"+(number-1).toString())[0].value;
				valor2 = document.getElementsByName("valor"+(number+1).toString())[0].value;	
			}
			console.log(tabla)
			console.log(valor1)
			console.log(valor2)
			console.log(valorEntre<=valor1 && valorEntre>=valor2)
			valor1 = Number(valor1);
			valor2 = Number(valor2);
			return valorEntre<=valor1 && valorEntre>=valor2;
			
		}else{
			//El de mayor valor es el de arriba:
			var tabla = input_pertenece(number);
			var crecimiento = constantes.tablas_orden[tabla];
			var valor1,valor2
			
			if(esta_en_borde_superior(number,tabla)){
				if(crecimiento==1){
					valor1 = 10;
				}else{
					valor1 = 0;			
				}
				valor2 = document.getElementsByName("valor"+(number+1).toString())[0].value;		

			}else if(esta_en_borde_inferior(number,tabla)){
				valor1 = document.getElementsByName("valor"+(number-1).toString())[0].value;
				if(crecimiento==1){
					valor2 = 0;
				}else{
					valor2 = 10;			
				}
			}else{
				valor1 = document.getElementsByName("valor"+(number-1).toString())[0].value;
				valor2 = document.getElementsByName("valor"+(number+1).toString())[0].value;	
			}
			valor1 = Number(valor1);
			valor2 = Number(valor2);		
			if(valor1<valor2){
				var temp = valor2;
				valor2=valor1;
				valor1=temp;
			}
			return valorEntre<=valor1 && valorEntre>=valor2;
		}		
	}
	
	function validacion_tipos(elmnt){
		var numero = Number(elmnt.value);
		if(noEsNumero(elmnt.value)){
			alert("El valor ingresado no es un numero.");
			elmnt.value = set_correct_value(elmnt);
			return false;			
		}
		
		if(!esta_entre(numero)){
			alert("El valor no está entre 0 y 10");
			elmnt.value = set_correct_value(elmnt);
			return false;				
		}
		
		if(esVacio(elmnt)){
			alert("El valor no puede ser vacio");
			elmnt.value = set_correct_value(elmnt);
			return false;					
		}
		
		if(!esta_entre_al_lado(elmnt)){
			alert("El valor no está entre sus adyacentes");
			elmnt.value = set_correct_value(elmnt);
			return false;			
		}		
		
		
		return true;
	};
	
	//Se agrega a cada uno de los campos la validacion al cambiar el contenido del input
	type = "intensidad";
	for (var i = 0; i <= cantidad_inputs; i++) { 
		if(i==constantes.limites[1]){
			type = "extension";
		}else if(i==constantes.limites[2]){	
			type = "duracion";				
		}else if(i==constantes.limites[3]){	
			type = "reversibilidad";	
		}else if(i==constantes.limites[4]){	
			type = "probabilidad";	
		}else if(i==constantes.limites[5]){	
			type = "importancia";	
		}
		for (var j = 0; j < constantes.inputs[type].length; j++) { 
			constantes.inputs[type][j].onchange = function(){
				validacion_tipos(this);
			}
		
		}
	}
	
	
};

//Al cargar la pagina se activa la funcionalidad de validacion
window.onload = function() {
	validar();
};
