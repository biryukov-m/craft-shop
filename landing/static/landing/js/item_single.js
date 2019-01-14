$(document).ready(function () {
    var hovered_image = $('.extra-images .image-wrapper img');
    var main_image = $('.main-image-wrapper img');
    var main_image_src = $('.main-image-wrapper img').attr('src');
    function change_image() {
        var target = $(this);
        var target_image_src = target.attr('src');
        main_image.attr('src', target_image_src);
    }
    function set_base_image() {
        main_image.attr('src', main_image_src);
    }
    hovered_image.on('click mouseenter', change_image);
    var extra_images_row = $('.extra-images');
    extra_images_row.on('mouseleave', set_base_image);
});
