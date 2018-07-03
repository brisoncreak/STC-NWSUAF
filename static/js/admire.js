// admire.js

    /*点赞的数量：*/
    document.getElementById("good").innerText = "";
    var good = document.getElementById("good").textContent;
     
    document.getElementById("bad").innerText  = "";
    var bad = document.getElementById("bad").textContent;

    // 初始化
    window.onload = function(){
        if (good == "") {
            good = 0;
            document.getElementById("good").innerText = 0;
        }
        if (bad == "") {
            bad = 0;
            document.getElementById("bad").innerText = 0;
        }              
    }

    /*点赞的数量：*/
    function sendGood(){
        good = parseInt(good) + 1;
        document.getElementById("good").innerText = good%2;
        if(good%2!=0){
             window.document.getElementById("goodimg").src="../static/img/like_aft.png"
        }
        else{
             window.document.getElementById("goodimg").src="../static/img/like_bef.png"
        }
    }
    
    /*踩的数量：*/
    function sendBad(){
        bad = parseInt(bad) + 1;
        document.getElementById("bad").innerText = bad%2;
        if(bad%2!=0){
             window.document.getElementById("badimg").src="../static/img/like_aft.png"
        }
        else{
             window.document.getElementById("badimg").src="../static/img/like_bef.png"
        }
    }