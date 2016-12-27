function testObj(key, code){
	
	this.key = key;
	this.code = code;
	
	function say(){
		console.log(this.key + '---' + this.code);
	}
	
}