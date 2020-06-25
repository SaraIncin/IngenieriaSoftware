function modificar_estado(id_orden) {
    $.ajax({
    	url: "/administrador/ver-pedidos/cambiar-estado/" + id_orden.toString(),
        method: "POST",
        success: function (result) {
            location.reload();
        }
    });
}

function goBack() {
  window.history.back();
}
