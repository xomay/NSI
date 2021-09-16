function copier() {
  champ_texte = document.getElementById("mon_texte");
  zone = document.getElementById("ma_zone");
  // Ici " champ_texte" est un composant HTML, une zone de texte. // Il faut récupérer son contenu
  texte = champ_texte.value;
  zone.innerText = texte;
}

function apercu() {
  champ_texte = document.getElementById("mon_texte");
  zone = document.getElementById("ma_zone");
  // Ici " champ_texte" est un composant HTML, une zone de texte. // Il faut récupérer son contenu
  texte = champ_texte.value;
  zone.innerText = 'Texte à copier : '+texte+'. Ca te va ?';
}

function changerCouleur(couleur) {
  zone = document.getElementById("ma_zone");
  zone.style.backgroundColor=couleur;
}

function cacher() {
  zone_a_cacher = document.getElementById("ma_zone2");
  bouton3 = document.getElementById("bnt3");
  bouton4 = document.getElementById("bnt4");
  zone_a_cacher.className="invisible";
  bouton3.className="invisible";
  bouton4.className="visible";
}
function montrer() {
  zone_a_monter = document.getElementById("ma_zone2");
  bouton3 = document.getElementById("bnt3");
  bouton4 = document.getElementById("bnt4");
  zone_a_monter.className="visible";
  bouton3.className="visible";
  bouton4.className="invisible";
}
