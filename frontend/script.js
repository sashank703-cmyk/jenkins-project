const api = "http://backend:5000/cars";

function loadCars(){

fetch(api)


.then(res => res.json())

.then(data => {

let output=""

data.forEach(car=>{

output += `<p>${car[1]} - ${car[2]}</p>`

})

document.getElementById("output").innerHTML=output

})

}

function addCar(){

let name=document.getElementById("name").value

let brand=document.getElementById("brand").value

fetch(api,{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

name:name,

brand:brand

})

})

.then(res=>res.json())

.then(data=>{

alert("Car Added Successfully")

loadCars()

})

}

loadCars()