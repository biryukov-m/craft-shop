$(document).ready(function () {

    // Функция для пересчета общей цены корзины на клиентской стороне после аякса
    function recalculate_basket_price(){
        var basket_price = 0;
        $('.total-price').each(function(i,elem) {
            // Топорный хак для убрания нулей из Decimal числа Django, чтобы получить целое число
            basket_price += Number($(elem).text().split(',', 1));
        });
        $('#basket-total-price').text(basket_price.toFixed(2));
    }

    var form = $('#buying-product');
    var container = $('#basket-container');

    form.on('submit', function (e) {
        e.preventDefault();
        // Обработка нажатия submit на форме - отдача ajax с данными товара бэкэнду

        // Считываем все данные, что висят на кнопке
        var button = $('#add-to-cart');
        var item_quantity = Number($('#quantity-selector').val());
        var item_id = Number(button.data('item_id'));
        var item_name = button.data('item_name');
        var item_price = button.data('item_price');
        var item_image = button.data('item_image');


        // Сначала отдача на бэкэнд желаемого товара в корзину
        // Считываем url, что генерится в шаблоне для ajax
        var url = form.attr('action');
        var csrf_token = $('#buying-product [name="csrfmiddlewaretoken"]').val();
        // Подготовка словаря дата для передачи в ajax
        var data = {};
        data.item_id = item_id;
        data.item_quantity = item_quantity;
        data['csrfmiddlewaretoken']=csrf_token;
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log('OK ajax');
            },
            error: function () {
                console.log('Error ajax');
            }
        });

        // Далее мгновенная отрисовка в корзине этого товара

        // Топорный хак для убрания нулей из Decimal числа Django, чтобы получить целое число
        item_price = Number(item_price.split(',', 1));

        $('#basket-container ul').append
        ("<li class=\"item\">\n" +
            "                        <div class=\"image-container\">\n" +
            "                            <img class=\"\"  src=\"" +
            item_image +
            "\">\n" +
            "                        </div>\n" +
            "                        <div class=\"text-container\">\n" +
            "                            <div class=\"name\">" +
            item_name +
            "</div>\n" +
            "                            <div class=\"size\">XL</div>\n" +
            "                            <div class=\"price\">" +
            item_price +
            "</div>\n" +
            "                        </div>\n" +
            "                        <div class=\"horizontal-text-container\">\n" +
            "                            <span class=\"count\">x "+ item_quantity +"</span>\n" +
            "                            <span class=\"total-price\">"+ item_price*item_quantity + ',00' +"</span>\n" +
            "                        </div>\n" +
            '                    </li>');

        recalculate_basket_price();

    });





    // Показать/скрыть корзину по клику
    $('#basket-icon').on('click', function (e) {
        e.preventDefault();
        container.toggleClass('hidden');
    });

    // Скрыть корзину, если курсор мыши сьехал
    // container.on('mouseleave', function (e) {
    //     e.preventDefault();
    //     container.addClass('hidden');
    // });

    // Обработка ajax запроса на удаление товара из корзины

    var button_remove = $('.item_remove');
    button_remove.on('click', function () {
        var item_id = $(this).data('item_id');
        var url = $(this).data('url');
        var csrf_token = $('#basket-list [name="csrfmiddlewaretoken"]').val();
        // Подготовка словаря дата для передачи в ajax
        var data = {};
        data.item_id = item_id;
        data['csrfmiddlewaretoken']=csrf_token;
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log('OK remove item ajax');
            },
            error: function () {
                console.log('Error remove item ajax');
            }
        });

        $(this).closest('li.item').remove();

        recalculate_basket_price();

    });

});