Funcion mensajeBienvenida
	Escribir "== Cajero ==";
	Escribir "Bienvenido al cajero automático.";
FinFuncion


Funcion mensajeSalida
	Escribir "Sesión cerrada correctamente.";
	Escribir "Que tenga buen día.";
FinFuncion


Funcion verSaldo(saldo)
	Escribir "Su saldo actual es de $", saldo, " pesos.";
FinFuncion


Funcion cantidad <- pedirMonto(mensaje, menorBillete)
	Definir operacionValida Como Logico;
	Definir cantidad Como Entero;
	
	operacionValida = Falso;
	Mientras No operacionValida Hacer
		Escribir mensaje;
		Leer cantidad;
		Si cantidad >= menorBillete Y cantidad % menorBillete == 0 Entonces
			operacionValida = Verdadero;
		SiNo
			Escribir "Monto inválido. Ingrese un valor múltiplo de ", menorBillete, " mayor que 0.";
		FinSi
		Escribir "";
	FinMientras
FinFuncion


Funcion saldo <- realizarGiro(saldo, menorBillete)
	Definir fondosSuficientes Como Logico;
	Definir giro Como Entero;
	
	fondosSuficientes = Verdadero;
	Si saldo < menorBillete Entonces
		fondosSuficientes = Falso;
		Escribir "Fondos insuficientes para realizar un giro.";
	FinSi
	
	Si fondosSuficientes Entonces
		giro = pedirMonto("Ingrese el monto a retirar:", menorBillete);
		
		Si giro > saldo Entonces
			Escribir "Fondos insuficientes para realizar el giro.";
		SiNo
			Escribir "Ha realizado un giro por $", giro, " pesos.";
			saldo = saldo - giro;
		FinSi
	FinSi
FinFuncion


Funcion saldo <- realizarDeposito(saldo, menorBillete)
	Definir deposito Como Entero;
	
	deposito = pedirMonto("Ingrese el monto a depositar:", menorBillete);
	Escribir "Ha realizado un depósito por $", deposito, " pesos.";
	saldo = saldo + deposito;
FinFuncion


Funcion seleccion <- pedirSeleccionAUsuario(cantidadOperaciones)
	Definir seleccion Como Entero;
	Definir inputValido Como Logico;
	
	inputValido = Falso;
	Escribir "Seleccione una operación:";
	Mientras No inputValido Hacer
		Leer seleccion;
		Si seleccion < 1 O seleccion > cantidadOperaciones Entonces
			Escribir "Opción no válida. Seleccione una opción correcta:";
		SiNo
			inputValido = Verdadero;
			seleccion = seleccion - 1; // 1-index a 0-index
		FinSi
	FinMientras
	Escribir "";
FinFuncion


Funcion mostrarMenu(operaciones, cantidadOperaciones)
	Escribir "";
	Escribir "------------------";
	Escribir "Menú de selección:";
	Escribir "------------------";
	Escribir "";
	
	Definir i Como Entero;
	Para i = 0 Hasta cantidadOperaciones - 1 Hacer
		Escribir i + 1, ". ", operaciones[i];
	FinPara
	Escribir "";
FinFuncion


Funcion ejecutarSesion(operaciones, cantidadOperaciones, menorBillete, saldo)
	Definir seleccionUsuario Como Entero;
	Definir salir Como Logico;
	Definir operacion Como Caracter;
	
	salir = Falso;
	Repetir
		mostrarMenu(operaciones, cantidadOperaciones);
		seleccionUsuario = pedirSeleccionAUsuario(cantidadOperaciones);
		
		operacion = operaciones[seleccionUsuario];
		Si operacion == "Saldo" Entonces
			verSaldo(saldo);
		FinSi
		Si operacion == "Depósito" Entonces
			saldo = realizarDeposito(saldo, menorBillete);
		FinSi
		Si operacion == "Giro" Entonces
			saldo = realizarGiro(saldo, menorBillete);
		FinSi
		Si operacion == "Salir" Entonces
			salir = Verdadero;
		FinSi
	Hasta Que salir
FinFuncion

//----------------------------------------------------------------

Proceso Main
	Definir saldo Como Entero;
	Definir menorBillete Como Entero;
	Definir cantidadOperaciones Como Entero;
	Definir operaciones Como Caracter;
	Dimension operaciones[4];
	
	cantidadOperaciones = 4;
	operaciones[0] = "Saldo";
	operaciones[1] = "Depósito";
	operaciones[2] = "Giro";
	operaciones[3] = "Salir";
	
	menorBillete = 1000;
	saldo = 10000;
	
	mensajeBienvenida();
	ejecutarSesion(operaciones, cantidadOperaciones, menorBillete, saldo);
	mensajeSalida();
FinProceso
