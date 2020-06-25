function agregar_alimento(valor) {
    $.ajax({
    	url: "/usuarios/cliente/menu/" + valor.toString(),
        method: "POST",
        success: function (result) {
            console.log(result)
        }
    });
}


function modificar_cantidad(valor) {
    $.ajax({
    	url: "/usuarios/cliente/menu/" + valor.toString(),
        method: "POST",
        success: function (result) {
            location.reload();
        }
    });
}

function eliminar_articulo(id) {
	$.ajax({
		url: "/usuarios/cliente/carrito/" + id.toString(),
		method:"POST",
		success: function (result) {
			location.reload();
		}
	})
}


function eliminar(id) {
	$.ajax({
		url: "/usuarios/cliente/carrito/articulo/" + id.toString(),
		method:"POST",
		success: function (result) {
			location.reload();
		}
	})
}


function suma(){
	sum = 0;
	var tabla = document.getElementById("tabla");
	for(var i = 1; i < tabla.rows.length-1; i++){
        sum = sum + parseInt(tabla.rows[i].cells[4].innerHTML);
    }
	return sum
}
	document.getElementById("Resultado").innerHTML = suma();


function modificar_estado(id_orden) {
    $.ajax({
    	url: "/administrador/ver-pedidos/cambiar-estado/" + id_orden.toString(),
        method: "POST",
        success: function (result) {
            location.reload();
        }
    });
}