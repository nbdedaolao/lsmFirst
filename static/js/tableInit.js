function initTable(word,interpretation){
	var table = document.querySelector("body > table >tbody");
	var wordCell = document.createElement('td');
	var interpretationCell = document.createElement('td');
	var aRow = document.createElement('tr');
	wordCell.setAttribute('class','en');
	interpretationCell.setAttribute('class','zh');
	wordCell.innerText = word;
	interpretationCell.innerText = interpretation;
	aRow.appendChild(wordCell);
	aRow.appendChild(interpretationCell);
	table.appendChild(aRow)
}

function readFile() {
	var wordMap;
	var fileReader = new FileReader();
	fileReader.readAsText(this.files[0],'utf-8');
	fileReader.onload = ()=>{
	     var wordList = fileReader.result.split('\n');
		 var wordMap = wordList.map(item=>{return item.split(',')})
		 for (var i = 0; i < wordMap.length; i++) {
			initTable(wordMap[i][0],wordMap[i][1])
		 }
	    };
	document.querySelector("body > input[type=file]").remove()
	}
	
function inputFileBind() {
	var inputFile = document.querySelector("body > input[type=file]");
	inputFile.addEventListener('change',readFile,false)
}

window.addEventListener('load',inputFileBind,false)