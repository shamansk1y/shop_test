function addToCart(productId) {
    var sizeSelect = document.getElementById("size-select");
    var size = sizeSelect.options[sizeSelect.selectedIndex].value;
    location.href = "{% url 'cart:cart_add' product.id %}?size=" + encodeURIComponent(size);
}