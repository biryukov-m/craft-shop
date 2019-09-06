$(document).ready(function () {
//
// Обработка корзины
//
    var basket_form = $('#buying-product');
    var basket_container = $('#basket-container');
    var button_remove = $('.item_remove');
    var basket_decrease_item_quantity_button = $('.decrease_item_quantity');
    var basket_increase_item_quantity_button = $('.increase_item_quantity');
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
            basket_container.addClass('hidden');
        } else {
            basket_container.toggleClass('hidden');
        }
    }
    basket_form.on('submit', function (e) {
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
        var url = basket_form.attr('action');
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
                basket_container.removeClass('hidden');
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
    basket_container.on('mouseleave', toggle_basket);
    // Кнопка уменьшения количества
    basket_decrease_item_quantity_button.on('click', function (e) {
        function decrease_item_quantity(target) {
            var quantity = Number($('.spinner-selector .number').val());
            console.log('quantity is - ', quantity);
            if (quantity < 2) {
                console.log('Error because quantity is less than 2, cant decrease more', quantity);
                return
            }
            var item_price = target.closest('.item').find("td.text-container div.price").text();
            item_price = parseFloat(item_price.replace(',','.'));
            console.log("Item_price is - ", item_price);
            var quantity_sel = $('.spinner-selector .number');
            var item_total_price_sel = target.closest('.item').find('td.total span.item-total-price');
            var new_quantity = quantity - 1;
            console.log("New quantity is- ", new_quantity);
            var new_total_price = (item_price*new_quantity).toFixed(2);
            console.log("New total price is - ", new_total_price);
            quantity_sel.val(new_quantity);
            item_total_price_sel.text(new_total_price.replace('.',','));
            recalculate_basket_price();
        }
        e.preventDefault();
        var target = $(e.target);
        // AJAX Handling
        var data_holder = $(this).closest('tr.item');
        var item_id = data_holder.data('item_id');
        console.log('AJAX item_id is - ', item_id);
        var item_size = data_holder.data('item_size');
        console.log('AJAX item_size is - ', item_size);
        // var item_quantity = data_holder.data('item_quantity');
        var item_quantity = Number($('.spinner-selector .number').val());
        console.log('AJAX item_quantity is - ', item_quantity);
        var method = $(this).data('method');
        console.log('AJAX method is - ', method);
        var url = data_holder.data('url');
        console.log('AJAX url is - ', url);
        var csrf_token = $('#csrf-token [name="csrfmiddlewaretoken"]').val();
        // Подготовка словаря дата для передачи в ajax
        var data = {};
        data.item_id = item_id;
        data.item_size = item_size;
        data.item_quantity = item_quantity;
        data.method = method;
        data['csrfmiddlewaretoken']=csrf_token;
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log('OK decrease quantity in checkout ajax');
                decrease_item_quantity(target);
            },
            error: function () {
                console.log('Error decrease quantity in checkout ajax');
            }
        });
    });
    // Кнопка увеличения количества
    basket_increase_item_quantity_button.on('click', function (e) {
        function increase_item_quantity(target) {
            var quantity = Number($('.spinner-selector .number').val());
            var item_price = target.closest('.item').find("td.text-container div.price").text();
            item_price = parseFloat(item_price.replace(',','.'));
            console.log(item_price, "Item_price");
            console.log(quantity, "quantity");
            var quantity_sel = $('.spinner-selector .number');
            var item_total_price_sel = target.closest('.item').find('td.total span.item-total-price');
            var new_quantity = quantity + 1;
            console.log(new_quantity);
            var new_total_price = (item_price*new_quantity).toFixed(2);
            console.log(new_total_price);
            quantity_sel.val(new_quantity);
            item_total_price_sel.text(new_total_price.replace('.',','));
            recalculate_basket_price();
        }
        e.preventDefault();
        var target = $(e.target);

        // AJAX Handling
        var data_holder = $(this).closest('tr.item');
        var item_id = data_holder.data('item_id');
        console.log('AJAX item_id is - ', item_id);
        var item_size = data_holder.data('item_size');
        console.log('AJAX item_size is - ', item_size);
        console.log('target is ', target);
        console.log('Trying to find from parent value of class .number', target);

        var item_quantity = Number($('.spinner-selector .number').val());
        console.log('AJAX item_quantity is - ', item_quantity);
        var method = $(this).data('method');
        console.log('AJAX method is - ', method);
        var url = data_holder.data('url');
        console.log('AJAX url is - ', url);
        var csrf_token = $('#csrf-token [name="csrfmiddlewaretoken"]').val();
        // Подготовка словаря дата для передачи в ajax
        var data = {};
        data.item_id = item_id;
        data.item_size = item_size;
        data.item_quantity = item_quantity;
        data.method = method;
        data['csrfmiddlewaretoken']=csrf_token;
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log('OK increase quantity in checkout ajax');
                increase_item_quantity(target);
            },
            error: function () {
                console.log('Error increase quantity in checkout ajax');
            }
        });

    });
//
// Обработка кликов user-interface в top menu магазина
//
    var user_icon = $('#user-topmenu-icon');
    var user_menu = $('#drop-user-menu');
    function toggle_user_menu() {
        user_menu.toggleClass('hidden');
        // в css аттрибут active дает цвет, нужный для подсветки
        user_icon.toggleClass('active');
    }
    // Показать/скрыть юзер-меню по клику
    user_icon.on('click mouseenter' , toggle_user_menu);
    // Скрыть меню, если курсор мыши сьехал
    user_menu.on('mouseleave', toggle_user_menu);
    // Обработка клика в user-interface на поиск заказа
    var find_order_button = $('#find-order');
    var hidden_search_order_input = $('#hidden-search-order-input');
    find_order_button.on('click', function (e) {
        hidden_search_order_input.toggle();
    });
});