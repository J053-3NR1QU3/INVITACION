// Fecha objetivo para el conteo regresivo
var fechaObjetivo = new Date("2023-06-10").getTime();

// Actualizar el contador cada segundo
var intervalo = setInterval(function() {
  // Fecha actual
  var fechaActual = new Date().getTime();
  
  // Diferencia entre la fecha objetivo y la fecha actual
  var diferencia = fechaObjetivo - fechaActual;

  // Cálculos para obtener días, horas, minutos y segundos
  var dias = Math.floor(diferencia / (1000 * 60 * 60 * 24));
  var horas = Math.floor((diferencia % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutos = Math.floor((diferencia % (1000 * 60 * 60)) / (1000 * 60));
  var segundos = Math.floor((diferencia % (1000 * 60)) / 1000);

  // Mostrar el conteo regresivo en el elemento HTML
  document.getElementById("countdown").innerHTML = dias + " días, " + horas + ":" + minutos + ":" + segundos + " Horas.";

  // Si el conteo regresivo ha terminado, mostrar un mensaje
  if (diferencia < 0) {
    clearInterval(intervalo);
    document.getElementById("countdown").innerHTML = "¡Hoy es el gran día!";
  }
}, 1000);
