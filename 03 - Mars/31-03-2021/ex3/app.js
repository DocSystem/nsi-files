function remplirTableau() {
  numList = [];
  document.querySelectorAll("td.case").forEach((i) => {
    num = Math.trunc(Math.random()*2);
    i.innerText = num;
    i.className = "nbr" + num;
    i.setAttribute("onclick", "changerNbr(this)");
    numList.push(num);
  });
  //console.log(numList);
}

function changerNbr(elem) {
  if (elem.className == "nbr1") {
    elem.className = "nbr0";
    elem.innerText = "0";
  }
  else {
    elem.className = "nbr1";
    elem.innerText = "1";
  }
}

remplirTableau();
