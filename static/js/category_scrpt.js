$(document).ready(function() {
  // Отображение и скрытие вертикального меню при нажатии на кнопку
  $('[data-toggle="collapse"]').on('click', function() {
    $(this).toggleClass('active');
    $($(this).attr('href')).toggleClass('show');
    $('body').toggleClass('overflow-hidden');
  });

  // Отображение горизонтального выпадающего меню при наведении на элемент
  $('.dropdown').on('mouseenter', function() {
    if($(window).width() > 768) {
      $(this).addClass('show');
      $(this).find('.dropdown-menu').addClass('show');
    }
  });

  // Скрытие горизонтального выпадающего меню при уходе курсора с элемента
  $('.dropdown').on('mouseleave', function() {
    if($(window).width() > 768) {
      $(this).removeClass('show');
      $(this).find('.dropdown-menu').removeClass('show');
    }
  });
});
