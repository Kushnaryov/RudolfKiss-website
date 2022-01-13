
$(document).ready(function() {
    $(".video-png").click(function(e) {
        $(".iframe-wrapper").addClass('show'); 
        $("#vimeo").attr('src', $(this).attr('name'));
    });

    // hide i frame if iframe-background is clicked
    $('.iframe-background').click(function(e) {
        $(".iframe-wrapper").removeClass('show');
        $("#vimeo").attr('src', '')
    });
});