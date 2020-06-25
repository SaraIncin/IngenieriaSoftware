var id_repartidor = "";

function abrir_modal(nombre, apellido, id) {
	id_repartidor = id;
	$("#aNombre").text(nombre);
	$("#apellido").text(apellido);
    $('#exampleModalCenter').modal('show');

}

function elimina(){
	$('#'+ id_repartidor).submit();
}

