var id_categoria = "";

function abrir_modal(nombre, id) {
	id_categoria = id;
	$("#aNombre").text(nombre);
    $('#exampleModalCenter').modal('show');

}

function elimina(){
	$('#'+ id_categoria).submit();
}