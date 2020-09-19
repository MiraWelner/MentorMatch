$document.ready(function(){
    // jQuery methods go here...
    //.click for when button is clicked?
    $("#id_selector").click(function(){
        const url = "";
        const postInfo = {
            title: "New Title",
            description: "jquery description"
        };

        //Allows us to make requests (call functions?) as we were doing before with postman
        $.ajax({
            url: url,
            type: "POST",
            data: JSON.stringify(postInfo),
            processData: false, 
            contentType: "application/json: charset=UTF-8",
            complete: function(){
                console.log("request complete");
                window.location.reload();
            }
        })
    });
});