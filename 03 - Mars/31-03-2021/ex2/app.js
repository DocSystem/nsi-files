function changerFond() {
  var elem = document.querySelector("div");
  elem.className = "autrecouleur";
}

let myButton = document.querySelector("button#btn1");

myButton.addEventListener("click", function () {
  changerFond();
});

let myButton2 = document.querySelector("button#btn2");

myButton2.addEventListener("click", function () {
  document.location.reload();
});

var allElems = {}

document.querySelectorAll("li").forEach((i) => {
  if (typeof allElems[i.className] == "undefined") {
    allElems[i.className] = [];
  }
  allElems[i.className].push(i.innerText);
});

for (var color in allElems) {
  newLi = document.createElement("li");
  newLi.innerText = color + " : " + allElems[color].length;
  document.querySelector("#colorquantities").appendChild(newLi);
}
