$(document).ready(function() {
    $(".background-v").on("loadeddata", function() {
        $(window).scroll(function() {
            if ($(window).scrollTop() >= 5) {
                $('.pink-background').css('background-color', '#fdbebe')
            } else {
                $('.pink-background').css('background-color', 'black')
            }
        });
    });
});

