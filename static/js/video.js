$(document).ready(function() {
    $(".video").each(function() {
        $(this).hover(
            function () {
                $(this).get(0).play();
            }, 
            function() {
                $(this).get(0).pause();
            });
    });
});