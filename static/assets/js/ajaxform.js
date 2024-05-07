$(document).ready(function() {
    $('#ajax-form').submit(function(e) {
        e.preventDefault(); // Prevent form submission

        var form = $(this);
        var url = form.attr('action');
        var formData = form.serialize();

        $.ajax({
            type: 'POST',
            url: url,
            data: formData,
            dataType: 'json',
            success: function(response) {
                $('#result').text(response.message);
                $('#result').removeClass('text-red-500').addClass('text-green-500');
            },
            error: function(xhr, status, error) {
                var errorMessage = xhr.responseJSON.message;
                $('#result').text(errorMessage);
                $('#result').removeClass('text-green-500').addClass('text-red-500');
            }
        });
    });
});
