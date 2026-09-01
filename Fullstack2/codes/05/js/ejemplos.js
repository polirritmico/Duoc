const nombreUno = "Camila";
const altura = 1.68;
let edadUno = 19;
const estudiante = true;
let curso;

edadUno = edadUno + 1;
console.log("Edad", edadUno);

if (edadUno >= 19) {
  console.log("Es mayor de edad");
} else {
  console.log("Es menor de edad");
}

function sumar(num1, num2) {
  return num1 + num2;
}

const total = sumar(1, 3);
console.log("Return función sumar: " + total);

const titulo = document.getElementById("titulo");
console.log("Valor de titulo definido en el html", titulo);

const parrafo = document.querySelector(".description");
console.log("Valor del parrafo definido en el html", parrafo);

const btnUno = document.getElementById("btnSaludar");
const saludo = document.getElementById("msgSaludar");

btnUno.addEventListener("click", function () {
  saludo.textContent = "Hola choro";
});

const tarjeta = document.getElementById("tarjeta");
tarjeta.addEventListener("mouseover", function () {
  tarjeta.style.backgroundColor = "red";
  tarjeta.textContent = "El mouse activó la función";
});
tarjeta.addEventListener("mouseout", function () {
  tarjeta.style.backgroundColor = "white";
  tarjeta.textContent = "Pasar el mouse sobre este elemento";
});

const btnMostrar = document.getElementById("btnMostrar");
const txtInput = document.getElementById("txtNombre");
const salidaParrafo = document.getElementById("textoSalida");

btnMostrar.addEventListener("click", function () {
  let texto = txtInput.value.trim();
  if (texto === "") {
    salidaParrafo.textContent = "Debes escribir algo en el input";
  } else {
    salidaParrafo.textContent = `Escribiste esto: '${texto}'`;
  }
});

const btnTextoACambiar = document.getElementById("btnTextoACambiar");
const txtTitulo = document.getElementById("textoCambiar");
btnTextoACambiar.addEventListener("click", function () {
  txtTitulo.textContent = "Nuevo título";
  btnTextoACambiar.textContent = "Acción realizada";
  btnTextoACambiar.disabled = true;
});

const btnAgregarTarea = document.getElementById("btnAgregarTarea");
const inputNuevaTarea = document.getElementById("nuevaTarea");
const listaTareas = document.getElementById("listaTareas");
btnAgregarTarea.addEventListener("click", function () {
  const texto = inputNuevaTarea.value.trim();
  if (texto === "") {
    return;
  }

  const item = document.createElement("li");
  item.textContent = texto;
  item.addEventListener("click", function () {
    item.remove();
  });
  listaTareas.appendChild(item);

  inputNuevaTarea.textContent = "";
});
