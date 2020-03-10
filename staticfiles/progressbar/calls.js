function getStuff(elem) {
    const id = $(elem).attr('id');

    $.ajax({
        url: window.location.pathname + id,
        type: 'GET',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function (result) {
            alert('ok');
            $('#something').prepend(
                "<p>" + result.item + "</p>"
            );
        }
    });
}