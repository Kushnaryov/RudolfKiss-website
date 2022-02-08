// When the user scrolls the page, execute myFunction

$(document).ready(function() {
    fitty('.fit-size')
    var top = $('#nav').offset().top
    var cross = $('#cross').height()

    $(window).resize(function() {
        cross = $('#cross').height()
        top = $('#nav').offset().top
    });

    $(window).scroll(function() {
        
        if ($(window).scrollTop() >= top) {
            $('#nav').addClass('fixed');
            $('#cross').removeClass('cross-show')
            $('#cross').addClass('cross-hide')
            // $('.cross').addClass('cross-transf')
            // $('#filter-name').removeClass('name-not-fixed')
            $('#filter-comm').text('COMMERCIALS')
            $('#filter-comm').addClass('fs-name-s')
            // $('#filter-mus').text('MUSIC VIDEOS')
            // $('.music').css('display', 'none')
            $('#filter-doc').removeClass('opac-filter-name')
            $('#filter-shf').text('SHORT FILMS')
            $('#filter-dop').removeClass('opac-filter-name')
            $('.menu-button').each (function () {
                $(this).addClass('menu-show')
            });
            $('.cross-name-wrapper').addClass('cross-name-transform')
            $('#background').css('display', 'none')
            if ($(window).scrollTop() >= $(window).height()/3) {
                $('.video-name').css('display', 'none')
            } else {
                $('.video-name').css('display', 'block')
            }
            fitty('.fit-size')
            
        } else if ($(window).scrollTop() < top){
            $('#nav').removeClass('fixed');
            $('#cross').addClass('cross-show')
            $('#cross').removeClass('cross-hide')
            // $('.cross').removeClass('cross-transf')
            // $('#filter-name').addClass('name-not-fixed')
            $('#filter-comm').text('KISS')
            $('#filter-comm').removeClass('fs-name-s')
            $('#filter-doc').addClass('opac-filter-name')
            // $('#filter-doc').text('')
            // $('.music').css('display', 'flex')
            // $('#filter-mus').text('')
            $('#filter-shf').text('')
            $('#filter-dop').addClass('opac-filter-name')
            // $('#filter-dop').text('')
            $('#background').css('display', 'flex')
            $('.video-name').css('display', 'inline-flex')
            $('.menu-button').each (function () {
                $(this).removeClass('menu-show')
            });
            $('.cross-name-wrapper  ').removeClass('cross-name-transform')
            
        };
        if ($(window).scrollTop() >= top) {
            // console.log($(window).scrollTop());
            $('#page-title').addClass('page-fixed');
        } else if ($(window).scrollTop() < top){
            $('#page-title').removeClass('page-fixed');
        };
    });
});

// MENU FOR MOBILE VERSION
$(document).ready(function(){
    var previousScrollTop = 0, scrollLock = false;
    $('.menu').hide();
    $(".menu-button").click(function() {
        fitty('.fit-size')
        $('.menu').fadeIn("fast");
        scrollLock = true;
        $(".burger-bar").css('background', '#fdbebe');
        $(".burger-bar:first-child").css('-webkit-transform', 'rotate(-135deg) translate(-2px, -1px)');
        $(".burger-bar:nth-child(2)").addClass('turn-off')
        $(".burger-bar:nth-child(3)").css('-webkit-transform', 'rotate(-45deg) translate(2px, -1px)');
        $(".menu-header").addClass('menu-show')
        $('#nav').fadeOut("fast");
    }); 
    $(".close-button").click(function() {
        scrollLock = false;
        $(".burger-bar").css('background', 'white');
        $(".burger-bar:first-child").css('-webkit-transform', 'translateY(-10px)');
        $(".burger-bar:nth-child(2)").removeClass('turn-off')
        $(".burger-bar:nth-child(3)").css('-webkit-transform', 'translateY(10px)');
        $(".menu-header").removeClass('menu-show')
        $('.menu').fadeOut("fast");
        $('#nav').fadeIn("fast");
        fitty('.fit-size')
    });
  });

