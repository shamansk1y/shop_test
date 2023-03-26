
document.getElementById("resetFilters").addEventListener("click", function() {
    // Сбросить все чекбоксы в форме
    var checkboxes = document.getElementsByTagName("input");
    for (var i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].type == "checkbox") {
            checkboxes[i].checked = false;
        }
    }

    // Отправить форму для возврата к изначальному списку товаров
    document.forms[1].submit();
});

