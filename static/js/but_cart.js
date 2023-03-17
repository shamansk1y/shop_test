document.querySelectorAll('.btn-minus').forEach(function(button) {
  button.addEventListener('click', function(event) {
    event.preventDefault();
    var input = button.closest('.quantity').querySelector('input');
    var quantity = parseInt(input.value);
    if (quantity > 1) {
      quantity--;
      input.value = quantity;
      var productId = input.getAttribute('id').replace('quantity_', '');
      // Send an AJAX request to update the quantity in the server-side cart object
      fetch('/cart/update/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          product_id: productId,
          quantity: quantity
        })
      });
    }
  });
});