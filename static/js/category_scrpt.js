const navbarVertical = document.getElementById('navbar-vertical');
const navbarHorizontal = document.getElementById('navbar-horizontal');
const btnToggleVertical = document.querySelector('[href="#navbar-vertical"]');
const btnToggleHorizontal = document.querySelector('[href="#navbar-horizontal"]');

btnToggleVertical.addEventListener('click', function() {
  if (navbarVertical.classList.contains('show')) {
    navbarVertical.classList.remove('show');
  } else {
    navbarVertical.classList.add('show');
    navbarHorizontal.classList.remove('show');
  }
});

btnToggleHorizontal.addEventListener('click', function() {
  if (navbarHorizontal.classList.contains('show')) {
    navbarHorizontal.classList.remove('show');
  } else {
    navbarHorizontal.classList.add('show');
  }
});
