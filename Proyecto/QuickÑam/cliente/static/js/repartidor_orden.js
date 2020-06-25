function seleccionar(id_orden) {
    $.ajax({
    	url: "/usuarios/repartidor/seleccionar/" + id_orden.toString(),
        method: "POST",
        success: function (result) {
            location.reload();
        }
    });
}