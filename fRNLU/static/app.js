$(document).ready(function() {

    $('button#btnsend').click(function() {
        var value = $('input#inputdata').val();

        if(value == '') {
            alert('No values entered!');
            return;
        }

        var apiurl = 'http://52.170.40.190:5000/fetchentityintent/' + value;

        $.ajax({
            url: apiurl,
            method: 'GET',
            datatype: 'json'
        }).done(function(data, textStatus, jqXHR) {
            $('div#response').append(renderjson(data));

        }).fail(function(jqXHR, textStatus, errorThrown) {
             $('div#response').text(textStatus + ' -- ' + errorThrown);
        });

    });
});