function maFonction() {
  document.querySelector("#monPara").style.color="red";
}



function foncRouge() {
	document.querySelector("#monPara").classList.remove("vert");
	document.querySelector("#monPara").classList.add("rouge");
}
function foncVert() {
	document.querySelector("#monPara").classList.remove("rouge");
	document.querySelector("#monPara").classList.add("vert");
}



function modifMessage() {
	document.querySelector("#monPara").innerHTML = "Bravo, vous avez cliqué sur le bouton !"
}



function foncEntre(){
	document.querySelector("#maDiv").classList.remove("blanc");
	document.querySelector("#maDiv").classList.add("rouge");
}
function foncQuitte() {
	document.querySelector("#maDiv").classList.remove("rouge");
	document.querySelector("#maDiv").classList.add("blanc");
}
