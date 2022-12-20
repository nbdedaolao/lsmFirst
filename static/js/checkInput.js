var pattern = /[a-z]+,[\u4e00-\u9fa5]+/;

function getInput() {
	var inputTag = document.querySelector("body > form > p:nth-child(1) > input[type=text]")
	return inputTag.value
}


function checkInput() {

	if (!pattern.test(getInput())) {
		alert('格式不正确！')
	}
}


function buttonBInd() {
	var submit = document.querySelector("body > form > p:nth-child(2) > input[type=submit]");
	submit.addEventListener('click', checkInput, false)
}

window.addEventListener('load', buttonBInd, false)