$(document).ready(function () {
    fitty('.fit-size')
    $("#background-v").on('play', function () {
        fitty('.fit-size')
        $('.fit-size').each (function (){
            $(this).css('lineHeight', parseInt($(this).css('fontSize'))*0.8+'px')
        });
    });
    $(window).resize(function () { 
        fitty('.fit-size')
        $('.fit-size').each (function (){
            $(this).css('lineHeight', parseInt($(this).css('fontSize'))*0.8+'px')
        });
    });
});