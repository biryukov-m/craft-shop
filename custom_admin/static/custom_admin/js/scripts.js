$(document).ready(function () {
    var opened_orders_shortcut = $('.opened-orders-shortcut');
    var new_orders_shortcut = $('.new-orders-shortcut');

    var status_waiting_for_accept_checkbox = $('#id_status_0');
    var status_verified = $('#id_status_1');
    var status_paid = $('#id_status_2');
    var status_in_delivery = $('#id_status_3');
    var status_delivered = $('#id_status_4');
    var status_closed = $('#id_status_5');

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
        })
    }

    opened_orders_shortcut.on('click', function (e) {
        e.preventDefault();
        clear_form();
        status_verified.prop('checked', true);
        status_paid.prop('checked', true);
        status_in_delivery.prop('checked', true);
        status_delivered.prop('checked', true);
        orders_search_submit_button.click();
    });

    new_orders_shortcut.on('click', function (e) {
        e.preventDefault();
        clear_form();
        status_waiting_for_accept_checkbox.prop('checked', true);
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
    })
});