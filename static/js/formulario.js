//Actualiza el combo provincias con los datos obtenidos del ajax
function actualizar_combo_provincia(data)
{
    $('#combo_provincia').empty(); //elimino el cotenido actual del combo

    // agrego los tipos obtenidos por ajax
    $.each(data, function(index, provincia){
      $('<option value="' + provincia['id'] + '">' +
                            provincia['nombre'] + '</option>')
      .appendTo('#combo_provincia')     
   });
}

//Actualizar provincia segun la region elegida 
//al terminar actualiza tambien distrito
function actualizar_provincia()
{
    $.getJSON('/miubigeo/obtener_provincias_region/'+ 
                   document.getElementById('combo_region').value,
               function(data){ actualizar_combo_provincia(data); 
                               actualizar_distrito();
                              });
}

//Actualiza el combo distritos con los datos obtenidos del ajax
function actualizar_combo_distrito(data)
{
    $('#combo_distrito').empty(); //elimino el cotenido actual del combo

    // agrego los tipos obtenidos por ajax
    $.each(data, function(index, distrito){
      $('<option value="' + distrito['id'] + '">' +
                            distrito['nombre'] + '</option>')
      .appendTo('#combo_distrito')     
   });
}

//Actualiza distrito segun la provincia elegida
function actualizar_distrito()
{
    $.getJSON('/miubigeo/obtener_distritos_provincia/'+ 
                    document.getElementById('combo_provincia').value,
               function(data){ actualizar_combo_distrito(data) });
}

//funcion que se ejecuta al cargar la pagina
$(function(){
     // Actualizamos los selects, se hace esto
     // pues al recargar la pagina los selects pueden tener
     // un inicio distinto del por defecto
     actualizar_provincia();
})
