const formulario = document.getElementById("formLogin");

formulario.addEventListener("submit", function (ev) {
  ev.preventDefault();
  const mail = document.getElementById("inputMail").value;
  const password = document.getElementById("inputPassword").value;

  if (mail === "admin@duoc.cl" && password === "123456") {
    alert("Ingreso correcto");
    window.location.href = "pages/principal.html";
  } else {
    alert("Usuario o contraseña incorrectos.");
  }
});
