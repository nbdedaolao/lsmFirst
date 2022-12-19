//背景反转
function bgReverse(flag,status1,status2){
	if (flag === status1) {
		return status2;
	} else{
		return status1;
	}
}

//锁定事件发生标签，判断标签是否为zh，为zh点击后背景反转
function hideOrShow(e){
	if(e.target.getAttribute('class') == 'zh'){
		e.target.style.backgroundColor = bgReverse(e.target.style.backgroundColor,'white','black')
	}		
}

// 给table绑定点击事件（事件委托）
function clickBind(){
	var table = document.querySelector("body > table");
	table.addEventListener("click",hideOrShow,false);
}

window.addEventListener('load',clickBind,false)


