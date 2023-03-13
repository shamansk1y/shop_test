$(document).ready(function() {
  $('.dropdown-toggle').click(function(event) {
    event.stopPropagation(); // отменяем всплытие клика по родительским элементам
    $(this).toggleClass('collapsed');
    $(this).parent().toggleClass('show');
    $(this).next('.dropdown-menu').toggleClass('show');
    $(this).attr('aria-expanded', $(this).attr('aria-expanded') === 'false' ? 'true' : 'false');
  });
});


// получаем кнопку и навигационное меню по ID
var button = document.getElementById("button-vertical");
var menu = document.getElementById("navbar-vertical");

// при клике на кнопку меняем классы и aria-expanded у кнопки и навигационного меню
button.addEventListener("click", function() {
    button.classList.toggle("collapsed");
    button.setAttribute("aria-expanded", button.classList.contains("collapsed") ? "false" : "true");
    menu.classList.toggle("show");
});
