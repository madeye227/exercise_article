$(function() {
    get_article_list();
});

function up_vote(article_id) {
        var form = new FormData();
        form.append("article_id", article_id);

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": `/up_vote_article`,
            "method": "POST",
            "headers": {
                "cache-control": "no-cache",
                "postman-token": "88bbaf1a-539d-1c7a-c507-bb84df84f765"
            },
            "processData": false,
            "contentType": false,
            "mimeType": "multipart/form-data",
            "data": form
        }

        $.ajax(settings).done(function(response) {
          response = $.parseJSON(response);
          window.location.replace("/");
    });
}

function get_article_list() {
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": `/article_ordered_list`,
        "method": "GET",
        "headers": {
            "cache-control": "no-cache",
            "postman-token": "b067b515-9215-9c06-c035-0c68579f45cb"
        },
    }
    $.ajax(settings).done(function(response) {
            response = $.parseJSON(response);
            $.each(response, function(index, value) {
                var markup =
                    `<li id=${value.id}>
                    <div><b>Title: </b>${value.title}</div>
                    <div><b>Article: </b>${value.article}</div>
                    <div><b>- Author: </b>${value.author}</div>
                    <div><b>Votes: </b>${value.votes} <button onclick="up_vote(${value.id})">Up vote</button></div>
                    <div></div>
                    <br/>
                </li>`;
                console.log(markup)
                $('#article_list').append(markup);
            });
        })
        .fail(function() {
            console.log('Article list fetch failed!');
        });
}
