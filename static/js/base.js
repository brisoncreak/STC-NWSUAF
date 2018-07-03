window.onload=function(){
    //轮询方式
    //setInterval(myFunction, 1000);

    //查看浏览器是否支持WebSocket
    // if(window.WebSocket){
    //     alert('support WebSocket');
    // }
    // else{
    //     alert('not support WebSocket');
    // }

    var wsURI = "ws://172.29.7.232:8000/ws/"

    websocket = new WebSocket(wsURI);

    websocket.onopen = function(evt){
        console.log("Connection open ..."); 
        setInterval("websocket.send('123')", 1000);
    };
     websocket.onclose = function(evt){
         console.log("Connection closed.");
    };
    websocket.onmessage = function(evt){
        //console.log( "Received Message: " + evt.data);
        $('#header-bottom-right').html(evt.data);
    };
    websocket.onerror = function(evt){
        console.log( "Received error: " + evt.data);
    };
}

function myFunction()
{
    $("#refresh-nav").load("/ #header-bottom-right");
}
