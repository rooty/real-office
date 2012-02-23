var formErrors = [];
var fancyboxDefaultOpts = {
    transitionIn: 'fade',
    transitionOut: 'fade',
    titleShow: false,
    showCloseButton: false,
    hideOnOverlayClick: false,
    hideOnContentClick: false,
    overlayShow: true,
    padding: 8,
    width: 400,
    height: 450,
    overlayColor: '#000000',
    overlayOpacity: 0.4
};

$.fn.fancybox.defaults.onClosed = function() { formErrors = [] }

jQuery.fn.indexOf = function (e) {
    for (var i = 0; i < this.length; i++) {
        if (this[i] == e) return i;
    }
    return -1;
};

var djForm = function(data, callback) {

    function processForm(data, callback) {
        // 'data' is the json object or html returned from the server
        if (typeof data == 'string') {
            if (callback) {
                callback(data);
            }
        } else if (typeof data == 'object') {
            processFormErrors(data);
        }
    }

    function processFormErrors(data) {
        if (data.success) {
            $.fancybox.close();
        } else {
            $.each(data['errors'], function (k, v) {
                if ($(formErrors).indexOf(k) == -1) {
                    formErrors.push(k);
                    $('<div class="error">' + v + '</div>').appendTo($('#' + k));
                } else {
                    $('#' + k + " > div.error").text(v);
                }
            });

            $.each(formErrors, function (i) {
                if (!(formErrors[i] in data['errors'])) {
                    $('#' + formErrors[i] + " > div.error").remove();
                    formErrors.splice(i, 1);
                }
            });
        }
    }

    processForm(data, callback);
};

(function($) {
    $.fn.remote_popup_form = function(callback) {
        var selector = 'form[data-remote=true]';
        $(document).off('submit', selector);
        $(document).on('submit', selector, {callback: callback}, function (e) {
            e.preventDefault();
            $(this).ajaxSubmit({
                success: function (data) {
                    djForm(data, e.data.callback);
                }
            });
            e.stopImmediatePropagation();
        });
    };

    $.fn.ajaxPaginate = function(options) {
        return this.each(function() {
          var defaults = {
              container: '.wide_column', // set container
              paginatorLink:  '.more_block a' // set link for paginator
          };
          var opts = $.extend(defaults, options);
          var $container = $(this);
          $(opts.container).on('click', opts.paginatorLink, function(e) {
              e.preventDefault();
              var $elem = $(this);
              $.get($elem.attr('href'), function(data) {
                  $elem.parents('tr').remove();
                  $(data).appendTo($container);
              });
          });
        });
    };
})(jQuery)


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ajaxSend(function (event, xhr, settings) {

    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
                !(/^(\/\/|http:|https:).*/.test(url));
    }

    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

/**
 * Show custom confirm popup
 * @param elem jQuery wrapped set
 * @param callback function
 */
function actionConfirm(elem, callback) {
    jConfirm(elem.data('confirmNotice'), '', function(r) {
        if (r) {
            callback();
        }
    });
}

$(function () {
    $('input[placeholder], textarea[placeholder]').placeholder();

    $(document).on('click', 'a[data-method=post]', function(e) {
        e.preventDefault();
        var $elem = $(this);
        var path = $elem.attr('href');

        actionConfirm($elem, function () {
          var href = path,
            form = $('<form method="post" action="' + href + '"></form>'),
            metadata_input = '<input name="csrfmiddlewaretoken" value="' + getCookie('csrftoken') + '" type="hidden" />';

          form.hide().append(metadata_input).appendTo('body');
          form.submit();
        });
    });

    $(document).on('click', "a.popup", function(e) {
        e.preventDefault();
        $.fancybox(
          $.extend(
            {href: $(this).attr('href')},
            fancyboxDefaultOpts
          )
        );
    });

    $('textarea[data-remote=true]').change(function () {
        $.ajax({
            type: 'POST',
            url: $(this).data('url'),
            data: {description: $(this).val()}
        });
    });

    $('.quotes_list, .messages_list').ajaxPaginate();

    $(".gallery").fancybox();

    $("a[rel=edit_avatar]").fancybox(fancyboxDefaultOpts);
    $("a[rel=edit_group]").fancybox(fancyboxDefaultOpts);

    $(".month li.curr").parent().toggle();
});
