$(document).ready(function(){
    $('#send-button').click(function(){
        sendMessage();
    });

    $('#user-input').keypress(function(e){
        if(e.which == 13) { // Enter key
            sendMessage();
        }
    });

    function sendMessage() {
        let userInput = $('#user-input').val();
        if (userInput.trim() === '') return;

        $('#chat-box').append(`<div class="user-message">${userInput}</div>`);
        $('#user-input').val('');
        $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);

        $.ajax({
            url: '/chat',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ message: userInput }),
            success: function(data){
                $('#chat-box').append(`<div class="bot-message">${data.reply}</div>`);
                $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
            }
        });
    }
});
