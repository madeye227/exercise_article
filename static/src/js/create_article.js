function submitForm() {
        var form = new FormData();
        title = $('#title').val().trim()
        article = $('#article').val().trim()
        author = $('#author').val().trim()
        console.log(title);
        console.log(article);
        console.log(author);
        form.append("title", title);
        form.append("article_content", article);
        form.append("author", author);

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": `/create_article`,
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
