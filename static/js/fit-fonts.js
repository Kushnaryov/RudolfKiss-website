$(document).ready(function () {
    fitty('.fit-size')
    $("#background-v").on('play', function () {
        fitty('.fit-size')
        $('.fit-size').each (function (){
            $(this).css('lineHeight', parseInt($(this).css('fontSize'))*0.85+'px')
        });
    });
    $(window).resize(function () { 
        fitty('.fit-size')
        $('.fit-size').each (function (){
            $(this).css('lineHeight', parseInt($(this).css('fontSize'))*0.85+'px')
        });
    });
});