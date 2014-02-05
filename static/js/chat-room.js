// Enable pusher logging - don't include this in production
Pusher.log = function(message) {
  if (window.console && window.console.log) {
    window.console.log(message);
  }
};

var pusher = new Pusher('0e0c5944e77aaa1238f8');
var channel;
function connect(name) {
    channel = pusher.subscribe('test_channel');
    channel.bind('new_message', function(data) {
        $('#chat-lines').append('<li>' + data.message + '</li>');
    });
};
