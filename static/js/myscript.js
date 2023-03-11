// get references to the carousel elements
var carousel = $('#header-carousel');
var indicators = carousel.find('.carousel-indicators li');
var items = carousel.find('.carousel-item');

// add click event listeners to the indicators
indicators.click(function() {
  var index = $(this).index();
  var activeIndex = carousel.find('.active').index();

  // update the active indicator
  indicators.eq(activeIndex).removeClass('active');
  indicators.eq(index).addClass('active');

  // update the active slide and its neighboring slides
  items.eq(activeIndex).removeClass('position-relative active');
  items.eq(index).addClass('position-relative active');
  if (index > activeIndex) {
    items.slice(activeIndex + 1, index).addClass('position-relative carousel-item-next');
    items.slice(index).removeClass('carousel-item-next carousel-item-left');
  } else if (index < activeIndex) {
    items.slice(index + 1, activeIndex).addClass('position-relative carousel-item-left');
    items.slice(0, index).removeClass('carousel-item-left carousel-item-next');
    items.slice(activeIndex).removeClass('carousel-item-left');
  }
});

// set the initial active slide
indicators.eq(0).addClass('active');
items.eq(0).addClass('position-relative active');
items.slice(1).addClass('position-relative carousel-item-next');


