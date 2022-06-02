let nombres = []

let nombresPrint = document.getElementById('list');

function addName ()
{
    nombres.push(document.getElementById("name").value);
}

function deleteName ()
{
    let name = document.getElementById("name").value;
    for (let x in nombres)
    {
        if(nombres[x] == name)
        {
            nombres.splice(x);
        }
    }
}

function printName ()
{
    for (let name of nombres)
    {
        let printNames = document.createElement("li");
        printNames.innerHTML = "Nombre: " + name;
        //printNamea.innerHTML = `Nombre: ${name + "Apellido"}`;
        printNames.classList.add('list-group-item');
        nombresPrint.appendChild(printNames);
    }
}