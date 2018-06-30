obj1 = document.getElementById("s_1");
str1 = obj1.value;
obj2 = document.getElementById("s_2"); 

function change_1()//主分类改变函数
{
    nongkecolleges = {{nongkes|safe}}
    gongkecolleges = {{gongkes|safe}}
    likecolleges = {{likes|safe}}
    wenkecolleges = {{wenkes|safe}}
    if(str1=="农科")
        createSelect(nongkecolleges)
    else if(str1=="工科")
        createSelect(gongkecolleges)
    else if(str1=="理科")
        createSelect(likecolleges)
    else if(str1=="文科")
        createSelect(wenkecolleges)
}

function createSelect(colleges)
{
    obj2.innerHTML = ""; //删除
    colleges.forEach(function(college)
    {
        op = document.createElement("option");
        //创建option元素
        op_text = document.createTextNode(college);
        //创建文本节点
        op.appendChild(op_text);
        //为option添加文本节点
        op.setAttribute("value",college);
        //设置value属性
        obj2.appendChild(op);
        //为obj2添加子节点
    })
} 
