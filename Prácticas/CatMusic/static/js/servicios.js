$(document).ready(function(){
	var grados1 = 1;
	var grados2 = 1;
	var grados3 = 1;

	$(".menu_servicio").mouseover(function(){
		console.log(this);
		$(this).animate({width:100+"%"},50,"swing");
		var a = setInterval(function(){
		$("#engrane1").css({transform:'rotate('+ grados1 + 'deg)'});
		$("#engrane2").css({transform:'rotate('+ grados2 + 'deg)'});
		$("#engrane3").css({transform:'rotate('+ grados3 + 'deg)'});
		grados1++;
		grados2--;
		grados3++;
		if(grados1 % 15 == 0){
			clearInterval(a);
		}
	},50);
	});

	$(".menu_servicio").mouseleave(function(){
		$(this).animate({width:100+"%"},50,"swing");
	});





});


function cambiaContenido(id){
		$(".area_trabajo").animate({opacity: 0},300, function() {
       // $(".area_trabajo").css({'background-image': 'url(img/'+id+'.JPG)'}).
        animate({opacity: 1});});
		$(".servicioDescripcion").addClass("oculto");
		$("#"+id).removeClass("oculto");


	}
/*
function cambiaImagen(id){
		$(".area_trabajo_galeria").animate({opacity: 0},300, function() {
        $(".area_trabajo_galeria").animate({opacity: 1});});
		 document.getElementById("img1").src= id+'.JPG';
	}
*/

 
