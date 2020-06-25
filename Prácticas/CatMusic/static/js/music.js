window.onload = init;



function init () {
    reproductor = new Audio();
    prev = document.getElementById("prev");
    art = document.getElementById("art");
    play = document.getElementById("play");
    next = document.getElementById("next");
    title = document.getElementById("title");
    artist = document.getElementById("artist");
    isPlay = false;
    canciones = [
        {
            title: 'Drive my car',
            artist: 'Beatles',
            url: 'http://abarcarodriguez.com/365/files/rainbow.mp3',
            art: 'https://lh3.googleusercontent.com/CrIHeXpJPoZz63YneLoWOjUGswBEa5LHVoUEPYu9hvA2CJMZz2f8X6V4fve7hti5ww7GUvtYYA=s1024-c-e100-rwu-v1'
        },
            
        {
            title: 'Come together',
            artist: 'Beatles',
            url: 'http://abarcarodriguez.com/365/files/rainbow.mp3',
            art: 'https://lh3.googleusercontent.com/QXdqujkQXwuQzgpxSP8nzrOqq6i0NQnE_iD3XFkRNs9-3yC4jigcFTB94bn8BOVlFNnx2VztmQ=s1024-c-e100-rwu-v1'
        },
        {
            title: 'The Primordial Booze',
            artist: 'Rainbowdragoneyes',
            url: 'http://abarcarodriguez.com/365/files/rainbow.mp3',
            art: 'https://lh4.ggpht.com/QqjbOo_bnoKjsrpZlQSGoACKQYpQpbT6pPIkDl6UuTWvc4jrJgu4XaSY8_Lomb73l_JjuDtkUBM=s1024-c-e100-rwu-v1'
    }];
    indexMusic = 0;
    NUMCAN = canciones.length;
    reprodIndex(0);
    play.addEventListener('click',playEvt,true);
    prev.addEventListener('click',prevEvt,true);
    next.addEventListener('click',nextEvt,true);
}

function prevEvt(e){
    indexMusic = Math.abs((indexMusic-1)%NUMCAN);
    reprodIndex(indexMusic);
}
function nextEvt(e){
    indexMusic = Math.abs((indexMusic+1)%NUMCAN);
    reprodIndex(indexMusic);
}
function playEvt(e){
    if (!isPlay) {
        play.childNodes[1].setAttribute("src", "static/img/pause.png");
        reproductor.play();
    }else{
        play.childNodes[1].setAttribute("src", "static/img/play.png");
        
        reproductor.pause();
    }
    isPlay = !isPlay;
}


function reprodIndex(index){
    var track = canciones[index];
    //cargar datos de la cancion
    title.innerHTML = track.title;
    artist.innerHTML = track.artist;
    art.setAttribute("src",track.art);
    reproductor.src = track.url;
    //reproducir cancion 
    reproductor.onloadeddata = function() {
        art.onload = function() {
            reproductor.play();
        }
    }
}
