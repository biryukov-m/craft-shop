$(document).ready(function () {
    var clipboard = new ClipboardJS('.to-clipboard');
    clipboard.on('success', function(e) {
        console.log(e);
        $('.event-result .ok').removeClass('hidden');
    });
    clipboard.on('error', function(e) {
        console.log(e);
        $('.event-result .error').removeClass('hidden');
    });
});
