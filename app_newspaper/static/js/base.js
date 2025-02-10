const cloud = document.getElementById("cloud");
const barralateral = document.querySelector(".barra-lateral");
const spans = document.querySelectorAll("span");
const palanca = document.querySelector(".switch");
const circulo = document.querySelector(".circulo");
const menu = document.querySelector(".menu");
const main = document.querySelector("main");
const searchLink = document.getElementById("search-link"); // Botón en la barra lateral
const searchContainer = document.getElementById("buscar"); // Contenedor de la barra de búsqueda
const closeSearch = document.querySelector(".close-search"); // Icono de cierre
const mainContent = document.querySelector(".contenido"); // Contenedor del contenido principal

menu.addEventListener("click", () => {
    barralateral.classList.toggle("max-barra-lateral");
    if (barralateral.classList.contains("max-barra-lateral")) {
        menu.children[0].style.display = "none";
        menu.children[1].style.display = "block";
    } 
    else {
        menu.children[0].style.display = "block";
        menu.children[1].style.display = "none";
    }

    if (window.innerWidth <=320){
        barralateral.classList.add("mini-barra-lateral");
        main.classList.add("min-main");
        spans.forEach((span) => {
            span.classList.add("oculto");
        })
    }
});

// Al cargar el DOM, aplica el modo oscuro si estaba activo
document.addEventListener("DOMContentLoaded", () => {
    if (localStorage.getItem("dark-mode") === "true") {
      document.documentElement.classList.add("dark-mode");
      palanca.classList.add("activo");
      circulo.classList.add("prendido");
    } else {
      document.documentElement.classList.remove("dark-mode");
      palanca.classList.remove("activo");
      circulo.classList.remove("prendido");
    }
  });

// Evento para alternar el modo oscuro
palanca.addEventListener("click", () => {
    // Alterna la clase en el elemento <html>
    document.documentElement.classList.toggle("dark-mode");
  
    // Actualiza el estado en localStorage y ajusta las clases de los controles visuales
    if (document.documentElement.classList.contains("dark-mode")) {
      localStorage.setItem("dark-mode", "true");
      palanca.classList.add("activo");
      circulo.classList.add("prendido");
    } else {
      localStorage.setItem("dark-mode", "false");
      palanca.classList.remove("activo");
      circulo.classList.remove("prendido");
    }
  });

cloud.addEventListener("click", () => {
    barralateral.classList.toggle("mini-barra-lateral");
    main.classList.toggle("min-main");
    spans.forEach((span) => {;
        span.classList.toggle("oculto");
    })
});


// Evento para ocultar la barra de búsqueda
searchLink.addEventListener("click", (e) => {
    e.preventDefault();
    // Si la barra ya está activa, la cierra; de lo contrario, la abre
    if (searchContainer.classList.contains("active")) {
      searchContainer.classList.remove("active");
      mainContent.classList.remove("search-active");
    } else {
      searchContainer.classList.add("active");
      mainContent.classList.add("search-active");
    }
  });


closeSearch.addEventListener("click", (e) => {
    // Siempre cierra la barra
    searchContainer.classList.remove("active");
    mainContent.classList.remove("search-active");
});