# Practice

## JS 使用
- underfined、null、0、false、NaN、空字符串的逻辑结果均为false 
 
- 使用对象构造器  
 
	  function Person(firstName, lastName){
    	this.firstName =  firstName;
    	this.lastName = lastName;
	  }
	  var Saad = new Person("Saad", "Mousliki");
		
- 使用自调用函数  
	
	  (function(){
    	// 置于此处的代码将自动执行
	  })();  
	  (function(a,b){
    	var result = a+b;
    	return result;
	  })(10,20)
		 
- 从数组中随机获取成员  

	  var items = [12, 548 , 'a' , 2 , 5478 , 'foo' , 8852, , 'Doe' , 2145 , 119];
	  var randomItem = items[Math.floor(Math.random() * items.length)];  

- 获取指定范围内的随机数  

	  var x = Math.floor(Math.random() * (max - min + 1)) + min;  

- 生成从0到指定值的数字数组  

	  var numbersArray = [] , max = 100;
	  for( var i=1; numbersArray.push(i++) < max;);