$(document).ready(function() {
  $('.dropdown-toggle').click(function() {
    $(this).toggleClass('collapsed');
    $(this).parent().toggleClass('show');
    $(this).next('.dropdown-menu').toggleClass('show');
    $(this).attr('aria-expanded', $(this).attr('aria-expanded') === 'false' ? 'true' : 'false');
  });
});