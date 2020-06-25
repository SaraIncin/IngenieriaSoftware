var id_alimento = "";

function abrir_modal(nombre, id) {
	id_alimento = id;
	$("#aNombre").text(nombre);
    $('#exampleModalCenter').modal('show');

}

function elimina(){
	$('#'+ id_alimento).submit();
}

