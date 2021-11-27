var regionButton;
var paisButton;
function recursive(){
	var but1=document.getElementsByClassName("regionButton");
	var but2=document.getElementsByClassName("paisButton");
	if(!but1.length||!but2.length){
		setTimeout(recursive,100);

	}
	else{
		regionButton=but1[0];
		paisButton=but2[0];
		regionButton.onclick = function(){document.querySelector(".porRegion").style.display='block';document.querySelector(".porPais").style.display='none'};
		paisButton.onclick = function(){document.querySelector(".porPais").style.display='block';document.querySelector(".porRegion").style.display='none'};
	}
}
recursive();
