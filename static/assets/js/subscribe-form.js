$(document).ready(function() {
    $('#subscribe-form').submit(function(event) {
        // Prevent default form submission
        event.preventDefault();

        // Get form data
        var formData = $(this).serialize();

        // Send AJAX request
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: formData,
            dataType: 'json',
            success: function(response) {
                // Display response message
                $('#result1').text(response.message);
                if (response.success) {
                    $('#result1').removeClass('text-red-500').addClass('text-green-500');
                } else {
                    $('#result1').removeClass('text-green-500').addClass('text-red-500');
                }
            },
            error: function(xhr, status, error) {
                console.error('AJAX request failed: ' + status + ', ' + error);
            }
        });
    });
});
