function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
var csrftoken = $.cookie('csrftoken');
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// Enable pusher logging - don't include this in production
Pusher.log = function(message) {
  if (window.console && window.console.log) {
    window.console.log(message);
  }
};

var pusher = new Pusher('0e0c5944e77aaa1238f8', {'encrypted': true});
var channel;
function connect(name) {
    channel = pusher.subscribe(name);
    channel.bind('new_message', function(data) {
        $('#chat-lines').append('<li>' + data.message + '</li>');
    });
}

function doSubmit(submitUrl) {
    $.post(submitUrl, {'text': $('#new-line').val()});
    $('#new-line').val('');
}
