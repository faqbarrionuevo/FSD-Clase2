

let temperatura = document.getElementById("btn").value;
let elemento = document.getElementById("temp");

if(temperatura < 15)
{
    elemento.innerHTML = "Hace frio";
} else if (temperatura > 15 && temperatura <= 20)
{
    elemento.innerHTML = "Temperatura perfecta";
} else if (temperatura > 20 && temperatura <= 25)
{
    elemento.innerHTML = "Temperatura aceptable";
} else
{
    elemento.innerHTML = "Demasiado calor";
}

/*Falta manejo de eventos en JS para que la pag siempre refresque cuando se toca el botón (lo vemos prox clase)*/