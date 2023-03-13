$(document).ready(function() {
  $('.dropdown-toggle').click(function() {
    $(this).toggleClass('collapsed');
    $(this).parent().toggleClass('show');
    $(this).next('.dropdown-menu').toggleClass('show');
    $(this).attr('aria-expanded', $(this).attr('aria-expanded') === 'false' ? 'true' : 'false');
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

  // получаем все элементы списка подкатегорий
  var subItems = document.querySelectorAll(".dropdown-submenu .dropdown-item");

  // при наведении на элемент списка скрываем предыдущий открытый список
  subItems.forEach(function(item) {
    item.addEventListener("mouseleave", function() {
      var previousMenu = this.closest(".dropdown-submenu").querySelector(".dropdown-menu.show");
      if (previousMenu) {
        previousMenu.classList.remove("show");
      }
    });
  });

  // при клике на элемент списка закрываем открытый список
  subItems.forEach(function(item) {
    item.addEventListener("click", function() {
      var currentMenu = this.closest(".dropdown-menu");
      if (currentMenu) {
        currentMenu.classList.remove("show");
      }
    });
  });
});
