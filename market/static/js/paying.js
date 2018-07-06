mouse_not_down = true;

window.onload=function(){


    //document.getElementById("chatbottom").scrollIntoView();
    var div = document.getElementById("chatarea")
    div.scrollTop = div.scrollHeight;
    
    $("#new-message").click(function(){          
　　　　    var content = $("#new-content").val();
        $("#new-content").val("");
        csrf = $("input[name='csrfmiddlewaretoken']").val();
        $.post(url1, {'content':content,'csrfmiddlewaretoken':csrf},
            function(data,status){
                 //window.location.reload();
                 //myFunction();

            });


　　})
    document.onkeydown = function(){
    var oEvent = window.event;
    if (oEvent.keyCode ==13) {
            $("#new-message").click();
    }

}
  
    //setInterval(myFunction, 1000);

    var host_now = window.location.host;

    var wsURI = "ws://"+host_now+"/market/ws/"+order_id+"/"+uid;

    websocket = new WebSocket(wsURI);

    websocket.onopen = function(evt){
        console.log("Connection open ..."); 
        setInterval("if(mouse_not_down){websocket.send('456')}", 1000);
    };
     websocket.onclose = function(evt){
         console.log("Connection closed.");
    };
    websocket.onmessage = function(evt){
        //console.log( "Received Message: " + evt.data);
        
        $('#paycontent').html(evt.data);
        var div = document.getElementById("chatarea")
        div.scrollTop = div.scrollHeight;

    };
    websocket.onerror = function(evt){
        console.log( "Received error: " + evt.data);
    };
}

// function myFunction()
// {
// //$("#chatarea-box").load("/market/paying/"+order_id+" #chatarea", function(){
//     //$("#paycontent").load("/market/paying/"+order_id+" #fresh_area", function(){
//     //document.getElementById("chatbottom").scrollIntoView();
    
// }

function mouseDown()
{
mouse_not_down = false; 
}
 
function mouseUp()
{
mouse_not_down = true; 
}