window.onload=function(){
    setInterval(myFunction, 1000);
}

function myFunction()
{
//$("#chatarea-box").load("/market/paying/"+order_id+" #chatarea", function(){
    $("#refresh-nav").load("/ #header-bottom-right");
    //document.getElementById("chatbottom").scrollIntoView();
}