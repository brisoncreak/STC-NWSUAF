 function check(){
 				if (document.myForm.email.value == "" || document.myForm.password.value == "") {
 					//alert("Please input your email and password!");
					Showbo.Msg.alert("Please input your email and password!");
 					document.myForm.reset();
 				} else if((document.myForm.email.value=="cxr@qq.com"&& document.myForm.password.value =="123") || (document.myForm.email.value=="lm@qq.com"&& document.myForm.password.value=="321")){
 					//alert("Success!");
					Showbo.Msg.alert("Success");
 					document.myForm.reset();
 				}else{
                Showbo.Msg.alert("The user name or password you entered is incorrect!"); 
                 document.myForm.reset();              
             } 
  }