// получаем кнопку и навигационное меню по ID
var button = document.getElementById("button-vertical");
var menu = document.getElementById("navbar-vertical");

// при клике на кнопку меняем классы и aria-expanded у кнопки и навигационного меню
button.addEventListener("click", function() {
    button.classList.toggle("collapsed");
    button.setAttribute("aria-expanded", button.classList.contains("collapsed") ? "false" : "true");
    menu.classList.toggle("show");
});