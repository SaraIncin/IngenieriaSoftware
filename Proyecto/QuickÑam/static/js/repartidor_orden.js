function seleccionar(id_orden) {
    $.ajax({
    	url: "/usuarios/repartidor/seleccionar/" + id_orden.toString(),
        method: "POST",
        success: function (result) {
            location.reload();
        }
    });
}

function modificar_estado(id_orden) {
    $.ajax({
    	url: "/usuarios/repartidor/cambiar-estado/" + id_orden.toString(),
        method: "POST",
        success: function (result) {
            location.reload();
        }
    });
}

function goBack() {
  window.history.back();
}