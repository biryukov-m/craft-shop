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
    }

    opened_orders_shortcut.on('click', function (e) {
        e.preventDefault();
        clear_form();
        status_waiting_for_accept_checkbox.prop('checked', false);
        status_verified.prop('checked', true);
        status_paid.prop('checked', true);
        status_in_delivery.prop('checked', true);
        status_delivered.prop('checked', true);
        status_closed.prop('checked', false);
        orders_search_submit_button.click();
    });

    new_orders_shortcut.on('click', function (e) {
        e.preventDefault();
        clear_form();
        status_waiting_for_accept_checkbox.prop('checked', true);
        status_verified.prop('checked', false);
        status_paid.prop('checked', false);
        status_in_delivery.prop('checked', false);
        status_delivered.prop('checked', false);
        status_closed.prop('checked', false);
        orders_search_submit_button.click();
    });

});