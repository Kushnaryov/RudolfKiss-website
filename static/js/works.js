function work_wrapper_big(elem) {
    elem.addClass('work-wrapper-big')
}

function work_wrapper_small(elem) {
    elem.addClass('work-wrapper-small')
}

function work_wrapper_one(elem) {
    elem.addClass('work-wrapper-one')
}

function frame_big_all(elem) {
    elem.addClass('work-frame chamfer-20-all')
}

function frame_big_left(elem) {
    elem.addClass('work-frame chamfer-20-left')
}

function frame_big_right(elem) {
    elem.addClass('work-frame chamfer-20-right')
}

function frame_small(elem) {
    elem.addClass('work-frame frame-small chamfer-10-all')
}

function frame_one(elem) {
    elem.addClass('work-frame frame-one no-chamfer')
}

function title_big(elem) {
    elem.addClass('work-title title-big')
}

function title_small(elem) {
    elem.addClass('work-title title-small')
}

function title_one(elem) {
    elem.addClass('work-title title-one')
}

function three_cols(elem1, elem2, elem3) {
    elem1.each(function(i) {
        if ((i+1)%2 == 1) {
            work_wrapper_small($(this))
        }
        else {
            work_wrapper_big($(this))
        }
    });
    elem2.each(function(i) {
        if (parseInt(i/3,10) % 2 == 0) {
            if ((i+1)%2 == 1) {
                frame_small($(this))
            }
            else {
                frame_big_all($(this))
            }
        } else {
            if ((i+1)%2 == 1) {
                frame_small($(this))
            }
            else {
                if (i%3 == 0) {
                    frame_big_right($(this))
                } else {
                    frame_big_left($(this))
                }
            }
        }
    });
    elem3.each(function(i) {
        if ((i+1)%2 == 1) {
            title_small($(this))
        }
        else {
            title_big($(this))
        }
    });
}

function two_cols(elem1, elem2, elem3) {
    elem1.each(function(i) {
        work_wrapper_big($(this))
    });
    elem2.each(function(i) {
        if (i%2 == 1) {
            frame_big_left($(this))
        } else {
            frame_big_right($(this))
        }
    });
    elem3.each(function(i) {
        title_big($(this))
    });
};

function one_col(elem1, elem2, elem3) {
    elem1.each(function(i) {
        work_wrapper_one($(this))
    });
    elem2.each(function(i) {
        frame_one($(this))
    });
    elem3.each(function(i) {
        title_one($(this))
    });
};

function give_classes(n_cols, elem1, elem2, elem3) {
    
    if (n_cols == 3) {
        three_cols(elem1, elem2, elem3)
    } else if (n_cols == 2) {
        two_cols(elem1, elem2, elem3)
    } else if (n_cols == 1) {
        one_col(elem1, elem2, elem3)
    } 

};

function clean_classes() {
    $('.work').each(function() {
        $(this).removeClass($(this).attr('class')).addClass('work')
    });
    $('.frame').each(function() {
        $(this).removeClass($(this).attr('class')).addClass('frame')
    });
    $('.title').each(function() {
        $(this).removeClass($(this).attr('class')).addClass('title')
    });
}



$(document).ready(function() {
    var n_cols = $('.works-container').css('grid-template-columns').split(' ').length
    give_classes(n_cols, $('.work'), $('.frame'), $('.title'))
    $( window ).resize(function() {
        var new_n_cols = $('.works-container').css('grid-template-columns').split(' ').length
        if (new_n_cols != n_cols) {
            clean_classes()
            n_cols = new_n_cols
            give_classes(n_cols, $('.work'), $('.frame'), $('.title'))
            
            // console.log('n changed')
        }
    });
});