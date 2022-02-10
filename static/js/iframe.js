
$(document).ready(function() {
    $(".video").click(function(e) {
        $(".iframe-wrapper").addClass('show'); 
        $("#vimeo").attr('src', $(this).attr('name'));
    });
    $(".video-name").click(function(e) {
        console.log('clicked')
        $(".iframe-wrapper").addClass('show'); 
        $("#vimeo").attr('src', $(this).attr('name'));
    });

    // hide i frame if iframe-background is clicked
    $('.iframe-background').click(function(e) {
        $(".iframe-wrapper").removeClass('show');
        $("#vimeo").attr('src', '')
    });
});
