$(document).ready(function() {
    $("#background-v").on('play', function () {
        console.log($("#background-v").parent().parent().attr('class'))
        console.log($("#background-v").parent().attr('class'))
        console.log($("#background-v").attr('class'))
        $(".wrapper").addClass('show')
        // $("#background-v").parent().addClass('show')
        // $("#background-v").addClass('show')
    });
});