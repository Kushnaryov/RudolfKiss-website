// When the user scrolls the page, execute myFunction

$(document).ready(function() {
    var vh = $(window).height()
    var vw = $(window).width()
    $(window).scroll(function() {
        console.log($(window).scrollTop())
        console.log(vh)
        if ($(window).scrollTop() >= (0.8)*vh) {
            // console.log($(window).scrollTop());
            $('#nav').addClass('fixed');
        } else {
            $('#nav').removeClass('fixed');
        };

        if ($(window).scrollTop() >= (1)*vh) {
            // console.log($(window).scrollTop());
            $('#page-title').addClass('page-fixed');
        } else {
            $('#page-title').removeClass('page-fixed');
        };
    });
});
// Get the navbar
// var navbar = $("#nav");

// Get the offset position of the navbar
// var sticky = $("window").height();

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
