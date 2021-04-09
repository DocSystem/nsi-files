document.querySelectorAll("img").forEach((i) => {
  i.setAttribute("onmouseover", "changerOrange(this)");
});

function changerOrange(i) {
  i.src = "img/orange.png";
}
