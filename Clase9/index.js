const textarea = document.getElementById('textarea');
const dibujar = document.getElementById('div1');
//const dibujar = document.getElementById('dibujar');
const btnDibujar = document.getElementById('btn-dibujar');



btnDibujar.onclick = function()
{
    //let textoFix = textarea.value.replaceAll('\n','<br>');
    console.log(textarea.value);
    //dibujar.innerText = textarea.value;
    //dibujar.innerHTML = textoFix;
    let jsCreate = document.createElement("p");
    //jsCreate.innerHTML =  textoFix;
    //dibujar.appendChild(jsCreate);

    let indexPesos = textarea.value.indexOf('$'); //Saco el ínidce donde esta $
    let pesos = textarea.value.slice(indexPesos + 1, indexPesos + 3); //Suponemos solo numeros de 2 digitos
    jsCreate.innerHTML = pesos;
    dibujar.appendChild(jsCreate);
}