// admire.js

//表单提交　　因为会跳转　　所以舍弃
    // function poost(URL,id,num) {
    //     var temp = document.createElement("form");
    //     temp.action =URL;
    //     temp.method = "post";
    //     temp.style.display = "none";
      
    //     var opt1 = document.createElement("input");
    //     opt1.type = "text"
    //     opt1.name = "INPUT";
    //     opt1.value = num;
    //     temp.appendChild(opt1);
    //     var opt2 = document.createElement("input");
    //     opt2.type = "text"
    //     opt2.name = "ID";
    //     opt2.value = id;
    //     temp.appendChild(opt2);
    //     document.body.appendChild(temp);
    //     temp.submit();
    //     return temp;
    // }

//点赞
    /*点赞的数量：good, good,*/
    function sendGood(id){
        goodnum = $("#goodnum"+id);//赞的个数
        num1=parseInt(goodnum.text());//转为int类型

        img1 = document.getElementById("goodimg"+id).src.split('/');
        name1 = img1[img1.length-1];
        if (name1 != "like_aft.png"){
            document.getElementById("goodimg"+id).src="../static/img/like_aft.png"
            num1 +=1;
            goodnum.text(num1)
        }
        else{
            document.getElementById("goodimg"+id).src="../static/img/like_bef.png"
            num1 -=1;
            goodnum.text(num1)
        }
        $.post("show_Admirenum/",{'goodINPUT':num1, 'goodID':id},function(result){});
    }
//踩
    /*踩的数量：*/
    function sendBad(id){
        badnum = $("#badnum"+id);//差评的个数
        num2=parseInt(badnum.text());//转为int类型

        img = document.getElementById("badimg"+id).src.split('/');
        name = img[img.length-1];
        if (name != "like_aft.png"){
            document.getElementById("badimg"+id).src="../static/img/like_aft.png"
            num2 +=1;
            badnum.text(num2)
        }
        else{
            document.getElementById("badimg"+id).src="../static/img/like_bef.png"
            num2 -=1;
            badnum.text(num2)
        }
        $.post("show_Admirenum/",{'badINPUT':num2, 'badID':id},function(result){});
    }