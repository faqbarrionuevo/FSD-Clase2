function calculadora (num1, num2, funcion)
{
    return funcion (num1, num2)
}

let resultado = calculadora(2, 3, (x, y) => 
{
    return x + y
})

console.log(resultado)