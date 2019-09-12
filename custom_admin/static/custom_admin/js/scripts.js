$(document).ready(function () {
    // Обработка фильтров на странице main__sidebar_orders.html
    var opened_orders_shortcut = $('.opened-orders-shortcut');
    var new_orders_shortcut = $('.new-orders-shortcut');
    var removed_orders_shortcut = $('.removed-orders-shortcut');
    var all_orders_shortcut = $('.all-orders-shortcut');
    var status_waiting_for_accept_checkbox = $('#id_status_0');
    var status_verified = $('#id_status_1');
    var status_paid = $('#id_status_2');
    var status_in_delivery = $('#id_status_3');
    var status_delivered = $('#id_status_4');
    var status_closed = $('#id_status_5');
    var filter_is_removed = $('#id_is_removed');
    var orders_search_submit_button = $('.orders-search-submit');

    function clear_form() {
        var form = $('form.filters')[0];
        form.reset();
        status_waiting_for_accept_checkbox.prop('checked', false);
        status_verified.prop('checked', false);
        status_paid.prop('checked', false);
        status_in_delivery.prop('checked', false);
        status_delivered.prop('checked', false);
        status_closed.prop('checked', false);
        $('#id_delivery_method_0').prop('checked', false);
        $('#id_delivery_method_1').prop('checked', false);
        $('#id_delivery_method_2').prop('checked', false);
        var inputs_list = [];
        inputs_list.push($('#id_customer_name'));
        inputs_list.push($('#id_code'));
        inputs_list.push($('#id_customer_email'));
        inputs_list.push($('#id_customer_phone'));
        $.each(inputs_list, function (index, element) {
            element.val('');
        });
        filter_is_removed.val('');
    }

    opened_orders_shortcut.on('click', function (e) {
        e.preventDefault();
        clear_form();
        status_verified.prop('checked', true);
        status_paid.prop('checked', true);
        status_in_delivery.prop('checked', true);
        status_delivered.prop('checked', true);
        filter_is_removed.val('3');
        orders_search_submit_button.click();
    });

    new_orders_shortcut.on('click', function (e) {
        e.preventDefault();
        clear_form();
        status_waiting_for_accept_checkbox.prop('checked', true);
        filter_is_removed.val('3');
        orders_search_submit_button.click();
    });

    removed_orders_shortcut.on('click', function (e) {
        e.preventDefault();
        clear_form();
        filter_is_removed.val('2');
        orders_search_submit_button.click();
    });

    all_orders_shortcut.on('click', function (e) {
        e.preventDefault();
        clear_form();
        filter_is_removed.val('3');
        orders_search_submit_button.click();
    });

    // При клике на кнопке поиска, встроенной в каждый инпут - очищаются все остальные поля
    $('button.find-order').on('click', function (e) {
        e.preventDefault();
        var input_field = $(this).prev('input');
        var current_val = input_field.val();
        clear_form();
        input_field.val(current_val);
        orders_search_submit_button.click();
    });

    // В таблице заказов при нажатии на строку заказа - переход на его детальное отображение
    $('.orders-table-content table tbody tr').on('click', function () {
        window.location = this.getAttribute('data-url');
    });

    //  Скрипты сайдбара   main__sidebar_products.html
    $('#id_item_type a.parent').on('click', function () {
        $(this).toggleClass('opened');
        $(this).siblings('ul').slideToggle();
    });


    // Обработка отмеченых чекбоксов в фильтре.
    // При клике переносится в локал сторадж состояние "checked"
    $('.item_type_checkbox').click(function(e){
        if (e.target.checked) {
            localStorage.setItem('admin_sidebar_'+this.id, 'yes');
        } else {
            localStorage.setItem('admin_sidebar_'+this.id, 'no');
        }
    });
    // При загрузке страницы, у каждого чекбокса запрашивает из локал стораджа информацию
    // о предыдущем состоянии, и согласно этому ставит или удаляет атрибут checked
    $('.item_type_checkbox').each(
        function () {
            if (localStorage.getItem('admin_sidebar_'+this.id)==='yes'){
                this.setAttribute('checked', '');
                $(this).closest('a').addClass('opened');
                // Тут надо придумать способ сменить ближайшей ссылке "а" класс на opened
                console.log($(this).closest('a'));
            }
            else {
                this.removeAttribute('checked');
            }
        }
    )
});