// When the user scrolls the page, execute myFunction

$(document).ready(function() {
    // var top = $('.main-background').height()
    var top = $('#nav').offset().top
    // var bottom = $('.main-background').height()
    var cross = $('#cross').height()
    $(window).scroll(function() {
        
        if ($(window).scrollTop() >= top) {
            $('#nav').addClass('fixed');
            $('#cross').removeClass('cross-not-fixed')
            $('#cross').height('7vh')
            $('#filter-name').removeClass('name-not-fixed')
            $('#filter-comm').text('COMMERCIALS')
            $('#filter-comm').addClass('fs-name-s')
            $('#filter-mus').text('MUSIC VIDEOS')
            $('#filter-doc').text('DOCUMENTARIES')
            $('#filter-shf').text('SHORT FILMS')
            $('#filter-dop').text('DOP WORKS')
            
            filter-mus
            $('#background').css('display', 'none')
            $('.video-name').css('display', 'none')
        } else if ($(window).scrollTop() < top){
            $('#nav').removeClass('fixed');
            $('#cross').addClass('cross-not-fixed')
            $('#cross').height(cross)
            $('#filter-name').addClass('name-not-fixed')
            $('#filter-comm').text('KISS')
            $('#filter-comm').removeClass('fs-name-s')
            $('#filter-doc').text('')
            $('#filter-mus').text('')
            $('#filter-shf').text('')
            $('#filter-dop').text('')
            $('#background').css('display', 'flex')
            $('.video-name').css('display', 'inline-flex')
        };

        if ($(window).scrollTop() >= top) {
            // console.log($(window).scrollTop());
            $('#page-title').addClass('page-fixed');
        } else if ($(window).scrollTop() < top){
            $('#page-title').removeClass('page-fixed');
        };
    });
});
// Get the navbar
// var navbar = $("#nav");

// Get the offset position of the navbar
// var sticky = $("window").height();

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
