$(document).ready(function () {
    var form = $('#buying-product');
    var container = $('#basket-container');
    var button_remove = $('.item_remove');
    var decrease_item_quantity = $('.decrease_item_quantity');
    var increase_item_quantity = $('.increase_item_quantity');
    // Функция для пересчета общей цены корзины на клиентской стороне после аякса
    function recalculate_basket_price(){
        var basket_price = 0;
        $('.item-total-price').each(function(i,elem) {
            var price = $(elem).text().replace(',','.');
            basket_price += parseFloat(price);
        });
        basket_price = basket_price.toFixed(2).replace('.', ',');
        $('.basket-total-price').text(basket_price);
    }
    function recalculate_basket_items_count(){
        var count = 0;
        var counter = $('#circle-counter');
        $('.item-total-price').each(function() {
            count += 1;
        });
        counter.text(count);
        if (count < 1) { counter.addClass('hidden');}
        else {counter.removeClass('hidden');}
    }
    function toggle_basket () {
        if ($('#circle-counter').hasClass('hidden')) {
            container.addClass('hidden');
        } else {
            container.toggleClass('hidden');
        }
    }
    form.on('submit', function (e) {
        e.preventDefault();
        // Обработка нажатия submit на форме - отдача ajax с данными товара бэкэнду
        // Считываем все данные, что висят на кнопке
        var button = $('#add-to-cart');
        var item_quantity = Number($('#quantity-selector').val());
        var item_size = $('#size-selector').val();
        var item_id = Number(button.data('item_id'));
        var item_name = button.data('item_name');
        var item_price = button.data('item_price');
        var item_image = button.data('item_image');
        // Сначала отдача на бэкэнд желаемого товара в корзину
        // Считываем url, что генерится в шаблоне для ajax
        var url = form.attr('action');
        var csrf_token = $('#csrf-token [name="csrfmiddlewaretoken"]').val();
        // Подготовка словаря дата для передачи в ajax
        var data = {};
        data.item_id = item_id;
        data.item_quantity = item_quantity;
        data['csrfmiddlewaretoken']=csrf_token;
        data.item_size = item_size;
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log('OK ajax');
                // Далее мгновенная отрисовка в корзине этого товара
                // Топорный хак для убрания нулей из Decimal числа Django, чтобы получить целое число
                item_price = Number(item_price.replace(',', '.'));
                $('#basket-container ul').append
                ("<li class=\"item new\">\n" +
                    "                        <div class=\"image-container\">\n" +
                    "                            <img class=\"\"  src=\"" +
                    item_image +
                    "\">\n" +
                    "                        </div>\n" +
                    "                        <div class=\"text-container\">\n" +
                    "                            <div class=\"name\">" +
                    item_name +
                    "</div>\n" +
                    "                            <div class=\"size\">"+ item_size +"</div>\n" +
                    "                            <div class=\"price\">" +
                    item_price.toFixed(2).replace('.', ',') +
                    "</div>\n" +
                    "                        </div>\n" +
                    "                        <div class=\"horizontal-text-container\">\n" +
                    "                            <span class=\"count\">x "+ item_quantity +"</span>\n" +
                    "                            <span class=\"item-total-price\">"+ (item_price*item_quantity).toFixed(2) +"</span>\n" +
                    "                        </div>\n" +
                    '                    </li>');
                recalculate_basket_price();
                recalculate_basket_items_count();
                toggle_basket();
            },
            error: function () {
                console.log('Error ajax');
            }
        });

    });
    // Обработка ajax запроса на удаление товара из корзины
    button_remove.on('click', function (e) {
        var item_id = $(this).data('item_id');
        var item_size = $(this).data('item_size');
        var url = $(this).data('url');
        var csrf_token = $('#csrf-token [name="csrfmiddlewaretoken"]').val();
        // Подготовка словаря дата для передачи в ajax
        var data = {};
        var target = e.target;
        data.item_id = item_id;
        data.item_size = item_size;
        data['csrfmiddlewaretoken']=csrf_token;
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log('OK remove item ajax');
                // remove сработает и для встроенной корзины в топ меню и для корзины на странице чекаута
                target.closest('.item').remove();
                recalculate_basket_price();
                recalculate_basket_items_count();
            },
            error: function () {
                console.log('Error remove item ajax');
            }
        });

    });
    // Показать/скрыть корзину по клику
    $('#basket-icon').on('click', toggle_basket);
    // Скрыть корзину, если курсор мыши сьехал
    container.on('mouseleave', toggle_basket);
    decrease_item_quantity.on('click', function (e) {
        e.preventDefault();
        var target = $(e.target);
        var quantity = target.parent().find('.number').val();
        if (quantity < 2) {
            console.log('Quantity =', quantity);
            return
        }
        var item_price = target.closest('.item').find("td.text-container div.price").text();
        // item_price = Number(item_price.split(',', '.')[0]);
        item_price = parseFloat(item_price.replace(',','.'));
        // item_price = item_price.toFixed(2);
        console.log(item_price, "Item_price");
        console.log(quantity, "quantity");
        var quantity_sel = target.parent().find('.number');
        var item_total_price_sel = target.closest('.item').find('td.total span.item-total-price');
        var new_quantity = quantity - 1;
        console.log(new_quantity);
        var new_total_price = (item_price*new_quantity).toFixed(2);
        console.log(new_total_price);
        quantity_sel.val(new_quantity);
        item_total_price_sel.text(new_total_price.replace('.',','));
        recalculate_basket_price();
    });
    increase_item_quantity.on('click', function (e) {
        e.preventDefault();
        var target = $(e.target);
        var quantity = Number(target.parent().find('.number').val());
        var item_price = target.closest('.item').find("td.text-container div.price").text();
        item_price = parseFloat(item_price.replace(',','.'));
        // item_price = item_price.toFixed(2);
        console.log(item_price, "Item_price");
        console.log(quantity, "quantity");
        var quantity_sel = target.parent().find('.number');
        var item_total_price_sel = target.closest('.item').find('td.total span.item-total-price');
        var new_quantity = quantity + 1;
        console.log(new_quantity);
        var new_total_price = (item_price*new_quantity).toFixed(2);
        console.log(new_total_price);
        quantity_sel.val(new_quantity);
        item_total_price_sel.text(new_total_price.replace('.',','));
        recalculate_basket_price();
    })
});