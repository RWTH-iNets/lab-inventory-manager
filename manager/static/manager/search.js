$( "form" ).submit(function( event ) {
    event.preventDefault();
    $.ajax({
        method: "POST",
        url: $("form").attr('action'),
        data: $("form").serialize(),
        success: function (data) {
            alert("Success!");
        }
    });
});
