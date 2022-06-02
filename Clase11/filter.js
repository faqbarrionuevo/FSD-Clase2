function myFilter(arr, funcion) {

    let nuevoArr = [];

    for (let elemento of arr) 
    {
        if (funcion(elemento)) 
        {
            nuevoArr.push(elemento);
        }
    }
    return nuevoArr;
}

let arr = [1, 2, 67, 12, 100];

function esPar(elemento) {

    return ((elemento % 2) == 0);

}

let nuevoArr = myFilter(arr, esPar);
let nuevoArr2 = arr.filter(esPar)

console.log(arr);

console.log(nuevoArr);

console.log(nuevoArr2);