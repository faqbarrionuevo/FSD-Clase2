function getBalanceTotal()
{
    let caja = Number(document.getElementById("caja").value);
    let corriente = Number(document.getElementById("corriente").value);
    let sueldo = Number(document.getElementById("sueldo").value);

    let saldoTotal = document.getElementById("saldo");
    saldoTotal.innerHTML = parseInt(caja + corriente + sueldo);
    
    
}