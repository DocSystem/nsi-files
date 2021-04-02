function verifiernom() {
  var message = document.getElementById('reponse');

  if (this.value.length < 5) {
    message.innerText = "Le nom doit comporter au moins 5 caractères";
  }
  else {
    message.innerText = "";
  }
}

var nomutilisateur = document.getElementById('utilisateur');
nomutilisateur.addEventListener("blur", verifiernom);
