$(function() {
    $("a.video_popup").fancybox({
        onComplete: function() {
            window.location.hash = "/" + $(".video_popup_outer").find("span").attr("id");
        }
    });
});

$(function() {
    var fragment = window.location.href.split("#/");
    var video_id = '';
    if (fragment) {
        if (fragment.length > 1){
                    video_id = fragment[1];
                    if (video_id.length > 0) {
                        $.fancybox({
                            href: '/videos/show/'+ video_id + '/'
                        });
                    }
        }
    }
});
