
function ajaxRequest(text) {
    if (text.length==0)
    {
        document.getElementById("txtAntwort").innerHTML="";
        return;
    }
    else{
        $.ajax({
            type: "POST",
            url: "/ml",
            data: { text: text },
            success: function(response) {
                document.getElementById("txtAntwort").innerHTML = response.msg;
            }
        });
}
}
