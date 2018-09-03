
$( function() {
    $( "#slider-size-range" ).slider({
        range: true,
        min: 0,
        max: 500,
        values: [ 75, 300 ],
        slide: function( event, ui ) {
            $( "#size-amount" ).val( ui.values[ 0 ] + " - " + ui.values[ 1 ] );
        }
    });
    $( "#size-amount" ).val( $( "#slider-size-range" ).slider( "values", 0 ) +
        " - " + $( "#slider-size-range" ).slider( "values", 1 ) );
} );