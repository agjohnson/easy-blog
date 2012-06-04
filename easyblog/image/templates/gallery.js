/* gallery.js */

$(document).ready(function () {
    var images={{ images|safe }};
    
    var gallery = $(".gallery-{{ gallery.slug }}");
    gallery.addClass("gallery-{{ gallery.style }}")
    
    for (i in images) {
        var elem = $("<img />");
        elem.attr({
            src: images[i],
        });
        gallery.append(elem);
    }
});

