$(document).ready(function () {
    $('label#add-comment').on('click', function () {
        $('#id_customer_comment').toggle();
        if ($(this).text() === 'Додати коментар') {
            $(this).html("Приховати коментар");
            return
        }
        if ($(this).text() === 'Приховати коментар') {
            $(this).html("Додати коментар");
        }
    })
});