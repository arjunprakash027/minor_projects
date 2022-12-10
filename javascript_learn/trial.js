//let a = 100;
//console.log(a)
import fetch from "node-fetch";


// function getdata(theUrl) 
// {   
//     var request = new XMLHttpRequest();
//     request.addEventListener("load", function() {
//         initialArray = JSON.parse(request.response);
//     }, false);
//     request.open("GET",theUrl,false);
//     request.send(null);
//     var data = request.responseText;
//     console.log(data);  
// };

async function getdatas()
{
    const url = 'https://arjunro.herokuapp.com/get_stock/INFY';
    let response = await fetch(url);
    let data = await response.json();
    console.log(data)
}

getdatas()