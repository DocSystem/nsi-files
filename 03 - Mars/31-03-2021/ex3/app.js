function remplirTableau() {
  numList = [];
  document.querySelectorAll("td.case").forEach((i) => {
    num = Math.trunc(Math.random()*2);
    i.innerText = num;
    numList.push(num);
  });
  console.log(numList);
}

remplirTableau();
