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
            $('.cross').addClass('cross-transf')
            $('#filter-name').removeClass('name-not-fixed')
            $('#filter-comm').text('COMMERCIALS')
            $('#filter-comm').addClass('fs-name-s')
            $('#filter-mus').text('MUSIC VIDEOS')
            $('#filter-doc').text('DOCUMENTARIES')
            $('#filter-shf').text('SHORT FILMS')
            $('#filter-dop').text('DOP WORKS')
            $('.menu-button').each (function () {
                $(this).addClass('menu-show')
            });
            $('.cross-name').addClass('cross-name-transform')
            // filter-mus
            $('#background').css('display', 'none')
            $('.video-name').css('display', 'none')
        } else if ($(window).scrollTop() < top){
            $('#nav').removeClass('fixed');
            $('#cross').addClass('cross-not-fixed')
            $('#cross').height(cross)
            $('.cross').removeClass('cross-transf')
            $('#filter-name').addClass('name-not-fixed')
            $('#filter-comm').text('KISS')
            $('#filter-comm').removeClass('fs-name-s')
            $('#filter-doc').text('')
            $('#filter-mus').text('')
            $('#filter-shf').text('')
            $('#filter-dop').text('')
            $('#background').css('display', 'flex')
            $('.video-name').css('display', 'inline-flex')
            $('.menu-button').each (function () {
                $(this).removeClass('menu-show')
            });
            $('.cross-name').removeClass('cross-name-transform')
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
    // $(window).scroll(function(event) { 
      
    //   if(scrollLock) {
    //     $(window).scrollTop(previousScrollTop); 
    //   }
    //   previousScrollTop = $(window).scrollTop();
  
    //   console.log(scrollLock)
    // });
    $('.menu').hide();
  
  
    $(".menu-button").click(function() {
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
    });
  });
// Get the navbar
// var navbar = $("#nav");

// Get the offset position of the navbar
// var sticky = $("window").height();

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
