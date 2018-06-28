// 实现级联删除
function change(){
    var area = document.getElementById("area");
    var countrys = document.getElementById("country");
    var index = area.value;                 
    var selects = data[index-1];            //通过选中下拉的选单value值获取数据
    
    var oldOptions = countrys.children;     //用children，数组内不会有多余属性(换行符)
    var length = oldOptions.length;         //！！注意，提前记录length原因：
                                            //如果在遍历删除过程中记录length，则length值会改变，删除会出错。
    for(var i=0;i<length;i++){              //删除原先选项的过程，若不删除，选项会一直堆积。
        countrys.removeChild(oldOptions[0]);//一直第一个元素，因为清除第一个以后，后面的元素会前移。如果按正常的i遍历，会出错！
    }
    
    if(index==0) return;                    //如果选中的是"请选择"，就不再添加数据，避免报错（因为脚标是-1）
    
    for(var i=0;i<selects.length;i++){      //增加选项过程
        var option = document.createElement("option");
        option.innerHTML = selects[i];
        country.appendChild(option);
    }
}