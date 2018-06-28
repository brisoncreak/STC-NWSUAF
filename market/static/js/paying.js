window.onload=function(){


    document.getElementById("chatbottom").scrollIntoView();
    
    $("#new-message").click(function(){          
　　　　    var content = $("#new-content").val();
        $("#new-content").val("");
        csrf = $("input[name='csrfmiddlewaretoken']").val();
        $.post(url1, {'content':content,'csrfmiddlewaretoken':csrf},
            function(data,status){
                 //window.location.reload();
                 myFunction();

            });

　　})
    setInterval(myFunction, 3000);
}

function myFunction()
{
$("#chatarea-box").load("/market/paying/"+order_id+" #chatarea", function(){document.getElementById("chatbottom").scrollIntoView();});


}


