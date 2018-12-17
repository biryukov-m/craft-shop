$(document).ready(function () {
    var form = $('#buying-product');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
        console.log('123123123123123');
        var quantity = $('quantity-selector').val();
        var size = $('size-selector').val();
        var button = $('#add-to-cart');
        var item_id = button.data('item_id');
        var item_name = button.data('item_name');
        console.log(item_id, item_name);
    })
});