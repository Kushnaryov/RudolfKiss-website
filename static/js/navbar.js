// When the user scrolls the page, execute myFunction

$(document).ready(function() {
    var vh = $(window).height()
    var vw = $(window).width()
    $(window).scroll(function() {
        if ($(window).scrollTop() >= (0.75 + 0.074)*vh) {
            console.log($(window).scrollTop());
            $("#nav").addClass("sticky")
        } else {
            $("#nav").removeClass("sticky");
        };

        if ($(window).scrollTop() >= 0.75*vh-0.25*vw) {
            P
        } else {

        };

    });
});
// Get the navbar
// var navbar = $("#nav");

// Get the offset position of the navbar
// var sticky = $("window").height();

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
