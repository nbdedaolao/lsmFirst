var pattern = /[a-z]+,[\u4e00-\u9fa5]+/;


function checkInput(inputString) {
	if (!pattern.test(inputString)) {
		alert('格式不正确！')
	}

}

function buttonBInd() {
	var submit = document.querySelector("body > form > p:nth-child(2) > input[type=submit]");
	submit.addEventListener('click', checkInput, false)
}

window.addEventListener('load', buttonBInd, false)