function remplirTableau() {
  numList = [];
  const tds = document.querySelectorAll("td.case");

  for (var i = 0; i < tds.length; i++) {
    if (i < 3) {
      num = 1;
    }
    else {
      num = Math.trunc(Math.random()*2);
    }
    tds[i].innerText = num;
    tds[i].className = "nbr" + num;
    tds[i].setAttribute("onclick", "afficherNbr(this)");
    numList.push(num);
  }
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

var nombresAffiches = [];

function afficherNbr(elem) {
  elem.classList.add("clicked");
  var contenu = parseInt(elem.innerText);
  nombresAffiches.push(contenu);
  if (nombresAffiches.length == 3) { afficherResultat() };
}

function afficherResultat() {
  const logsElem = document.getElementById('logs');
  if ((nombresAffiches[0] == 0 && nombresAffiches[1] == 0 && nombresAffiches[2] == 0) || (nombresAffiches[0] == 1 && nombresAffiches[1] == 1 && nombresAffiches[2] == 1)) {
    logsElem.innerText = "Bravo, tu as gagné !";
  }
  else {
    logsElem.innerText = "Il faut cliquer sur trois mêmes nombres d'affilée. Essaie à nouveau !";
    logsElem.appendChild(document.createElement("br"));
    var rel = document.createElement("a");
    rel.href = "javascript:reload();";
    rel.innerText = "Réessayer"
    logsElem.appendChild(rel);
  }
}

function reload() {
  document.location.reload();
}

remplirTableau();
