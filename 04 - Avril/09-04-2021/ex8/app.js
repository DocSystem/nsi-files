document.querySelectorAll("td").forEach((i) => {
  i.setAttribute("onmouseenter", "showPrice(this, event)");
  i.setAttribute("onmouseleave", "hidePrice()");
  i.setAttribute("onmousemove", "movePrice(this, event)");
  i.setAttribute("onclick", "addToCart(this)");
});

function showPrice(elem, ev) {
  var name = elem.innerText;
  var popup_price = document.getElementById('popup_price');
  document.getElementById('popup').classList.remove("hidden");
  document.getElementById('popup').setAttribute("style", "top: " + ev.y + "px;left:" + ev.x + "px;");
  document.getElementById('popup_name').innerText = name;
  popup_price.innerText = getPrice(name);
}

function getPrice(name) {
  if (name == "Aubergines") {
    return "1.19";
  }
  else if (name == "Carrotes") {
    return "1.39";
  }
  else if (name == "Courgettes") {
    return "1.59";
  }
  else if (name == "Poivron") {
    return "3.99";
  }
  else if (name == "Tomates") {
    return "3.00";
  }
  else if (name == "Abricots") {
    return "3.18";
  }
}

function hidePrice() {
  document.getElementById('popup').classList.add("hidden");
}

function movePrice(elem, ev) {
  document.getElementById('popup').setAttribute("style", "top: " + ev.y + "px;left:" + ev.x + "px;");
}

cart = {
  "Aubergines": 0,
  "Carrotes": 0,
  "Courgettes": 0,
  "Poivron": 0,
  "Tomates": 0,
  "Abricots": 0
};

function addToCart(elem) {
  var name = elem.innerText;
  var quantity = prompt("Quelle quantité ? (" + name + " coute " + getPrice(name) + "€)", "1");
  if (quantity != null) {
    try {
      quantity = parseInt(quantity);
      cart[name] += quantity;
      updateCart();
    }
    catch {
      alert("La quantité entrée n'est pas valide !");
    }
  }
}

function updateCart() {
  var isEmpty = true;
  var table = document.createElement("table");
  var fTr = document.createElement("tr");
  var th;
  th = document.createElement("th");
  th.innerText = "Objet";
  fTr.appendChild(th);
  th = document.createElement("th");
  th.innerText = "Quantité";
  fTr.appendChild(th);
  th = document.createElement("th");
  th.innerText = "Prix";
  fTr.appendChild(th);
  table.appendChild(fTr);
  var totalQuantity = 0;
  var totalPrice = 0;
  var td;
  for (var objet in cart) {
    if (cart[objet] > 0) {
      isEmpty = false;
      var tr = document.createElement("tr");
      td = document.createElement("td");
      td.innerText = objet;
      tr.appendChild(td);
      td = document.createElement("td");
      td.innerText = cart[objet];
      tr.appendChild(td);
      td = document.createElement("td");
      td.innerText = Math.round(getPrice(objet) * parseFloat(cart[objet]) * 100)/100 + "€";
      tr.appendChild(td);
      table.appendChild(tr);
      totalQuantity += cart[objet];
      totalPrice += getPrice(objet) * cart[objet];
    }
  }
  if (isEmpty) {
    document.getElementById('panier').innerHTML = "Votre panier est vide";
  }
  else {
    var tr = document.createElement("tr");
    td = document.createElement("td");
    td.innerText = "Total";
    tr.appendChild(td);
    td = document.createElement("td");
    td.innerText = totalQuantity;
    tr.appendChild(td);
    td = document.createElement("td");
    td.innerText = Math.round(totalPrice * 100) / 100 + "€";
    tr.appendChild(td);
    table.appendChild(tr);
    document.getElementById('panier').innerHTML = "";
    document.getElementById('panier').appendChild(table);
  }
}

updateCart();
