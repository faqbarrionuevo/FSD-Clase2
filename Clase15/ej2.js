let contenido = document.querySelector("#hora");
let intervalo;
function play()
{
    intervalo = setInterval(() =>
    {
        let fecha = new Date();
        let minutos = fecha.getMinutes();
        let horas = fecha.getHours();
        let segundos = fecha.getSeconds();
        contenido.innerHTML=`<p>${horas}:${minutos}:${segundos}</p>`
    }, 1000);
}

function stop ()
{
    clearInterval(intervalo);
}

//Agregar alarma, el usuario ingresa horas min y segs y a esa hora aparece un alert o algo avisando