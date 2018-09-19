$( function(min, max) {
    $( "#slider-price-range" ).slider({
        range: true,
        min: min,
        max: max,
        values: [ 75, 300 ],
        slide: function( event, ui ) {
            $( "#price-amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
        }
    });
    $( "#price-amount" ).val( "$" + $( "#slider-price-range" ).slider( "values", 0 ) +
        " - $" + $( "#slider-price-range" ).slider( "values", 1 ) );
} );