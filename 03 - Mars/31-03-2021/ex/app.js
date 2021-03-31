const ulElem = document.querySelector("ul");

const elemsData = [
  {
    "text": "Bleu",
    "color": "yellow"
  },
  {
    "text": "Vert",
    "color": "red"
  },
  {
    "text": "Jaune",
    "color": "pink"
  }
];

var i = 12;

for (var newElemData in elemsData) {
  var newLi = document.createElement("li");
  newLi.style.color = elemsData[newElemData]["color"];
  newLi.innerText = elemsData[newElemData]["text"];
  newLi.style.fontSize = i + "px";
  ulElem.appendChild(newLi);
  i+=8;
}
