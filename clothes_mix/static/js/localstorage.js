/*Funcion para guardar los datos*/
$(document).ready(function(){    
    $('#ingresar').click(function(){        
        /*Captura de datos escrito en los inputs*/        
        var email = document.getElementById("correo").value;
        var pass = document.getElementById("contraseña").value;
        var nombre = document.getElementById("nombre").value;
        var apellido = document.getElementById("apellido").value;
        /*var rut = document.getElementById("rut").value;*/
        var fecha = document.getElementById("fecha").value;
        /*Guardando los datos en el LocalStorage*/
        localStorage.setItem("Email", email);
        localStorage.setItem("Pass", pass);
        localStorage.setItem("Nombre", nombre);
        localStorage.setItem("Apellido", apellido);
        /*localStorage.setItem("Rut", rut);*/
        localStorage.setItem("Fecha", fecha);
        /*Limpiando los campos o inputs*/
        document.getElementById("correo").value = "";
        document.getElementById("contraseña").value = "";
        document.getElementById("nombre").value = "";
        document.getElementById("apellido").value = "";
        /*document.getElementById("rut").value = "";*/
        document.getElementById("fecha").value = "";
    });   
});

/*Funcion Cargar y Mostrar datos*/
$(document).ready(function(){    
    $('#mostrar').click(function(){                       
        /*Obtener datos almacenados*/
        var email1 = localStorage.getItem("Email");
        /*var pass1 = localStorage.getItem("Pass");*/
        var nombre1 = localStorage.getItem("Nombre");
        var apellido1 = localStorage.getItem("Apellido");
        /*var rut1 = localStorage.getItem("Rut");*/
        var fecha1 = localStorage.getItem("Fecha");

        /*Mostrar datos almacenados*/      
        document.getElementById("email1").innerHTML = email1;
        /*document.getElementById("pass1").innerHTML = pass1;*/
        document.getElementById("nombre1").innerHTML = nombre1;
        document.getElementById("apellido1").innerHTML = apellido1;
        /*document.getElementById("rut1").innerHTML = rut1;*/
        document.getElementById("fecha1").innerHTML = fecha1;
    });   
});

/*redirecion pag*/
function myFunction() {
    location.replace("datos.html")
}
function volver() {
    location.replace("form.html")
}