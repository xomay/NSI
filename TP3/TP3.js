< script >
  function visible() {
    const bouton = document.getElementById("valider");
    const password_input = document.getElementById("password");
    if (password_input != "") {
      bouton.disabled = true;
    }
  }
