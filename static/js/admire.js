// admire.js


//点赞
    /*点赞的数量：good, good,*/
    function sendGood(id,str,userID){
        crsfvalue = $("input[name='csrfmiddlewaretoken']").val()
        goodnum = $("#goodnum"+id);//赞的个数
        num1=parseInt(goodnum.text());//转为int类型
        isAdd1 = 1
        img = document.getElementById("badimg"+id).src.split('/');
        name = img[img.length-1];
        img1 = document.getElementById("goodimg"+id).src.split('/');
        name1 = img1[img1.length-1];
        //点赞
        if (name1 != "like_aft.png" && name != "like_aft.png" ){   
            document.getElementById("goodimg"+id).src="../static/img/like_aft.png"
            num1 +=1;
            goodnum.text(num1)
            isAdd1 = 1
        }
        else if(name1 != "like_aft.png" && name=="like_aft.png"){
            isAdd1 = 0
        }
        //取消点赞
        else{
            document.getElementById("goodimg"+id).src="../static/img/like_bef.png"
            num1 -=1;
            goodnum.text(num1)
            isAdd1 = 0
        }
        //isGood代表的是　是好评还是取消好评
        $.post(admire_pathG,{'goodINPUT':num1, 'goodID':id , 'admireType':str,'csrfmiddlewaretoken':crsfvalue,'userID':userID,'isAdd':isAdd1},function(result){});

    }
//踩
    /*踩的数量：*/
    function sendBad(id,str,userID){
        crsfvalue = $("input[name='csrfmiddlewaretoken']").val()
        badnum = $("#badnum"+id);//差评的个数
        num2=parseInt(badnum.text());//转为int类型
        isAdd2 =1
        img1 = document.getElementById("goodimg"+id).src.split('/');
        name1 = img1[img1.length-1];
        img = document.getElementById("badimg"+id).src.split('/');
        name = img[img.length-1];
        //踩　
        if (name != "like_aft.png" && name1 != "like_aft.png"){
            document.getElementById("badimg"+id).src="../static/img/like_aft.png"
            num2 +=1;
            badnum.text(num2)
            isAdd2 = 1
        }
        else if(name != "like_aft.png" && name1=="like_aft.png"){
            isAdd2 = 0
        }
        //取消踩
        else{
            document.getElementById("badimg"+id).src="../static/img/like_bef.png"
            num2 -=1;
            badnum.text(num2)
            isAdd2 = 0
        }
        // alert(userID)
        $.post(admire_pathB,{'badINPUT':num2, 'badID':id , 'admireType':str,'csrfmiddlewaretoken':crsfvalue,'userID':userID,'isAdd':isAdd2},function(result){});
    }