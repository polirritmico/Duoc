Funcion numero <- generarNumero(min, max)
	Definir numero Como Entero;
	numero = Azar(max + 1 - min) + min;
	numero = 3;
FinFuncion

Funcion numero <- pedirNumeroAlUsuario(min, max)
	Definir numero Como Entero;
	Escribir "Escribe un número entre ", min, " y ", max;
	Leer numero;
FinFuncion

Funcion adivino <- revisarSiAdivino(objetivo, conjetura)
	Definir adivino Como Logico;
	Si objetivo == conjetura Entonces
		adivino = Verdadero;
	SiNo
		adivino = Falso;
	FinSi
FinFuncion

Funcion mensajeIntentos(intentos)
	Escribir "";
	Escribir "-----------------------";
	
	Si intentos > 1 Entonces
		Escribir "Te quedan ", intentos, " intentos";
	SiNo
		Escribir "¡Cuidado, solo te queda un intento!";
	FinSi
	
	Escribir "";
FinFuncion

Funcion anuncioBienvenida(menor, mayor)
	Escribir "== Bienvenido ==";
	Escribir "";
	Escribir "Adivina el número entre ", menor, " y ", mayor, ".";
FinFuncion

Funcion mensajeFinal(aGanado, numeroSecreto)
	Si aGanado Entonces
		Escribir "¡Felicidades, ese era el número! ¡Has adivinado!";
	SiNo
		Escribir "Te has quedado sin intentos";
		Escribir "Has perdido...";
		Escribir "El número era ", numeroSecreto;
	FinSi
FinFuncion

Funcion aGanado <- adivinar(numeroSecreto, intentos, min, max)
	Definir numeroUsuario Como Entero;
	Definir sinIntentos Como Logico;
	Definir aGanado Como Logico;
	
	aGanado = Falso;
	sinIntentos = Falso;
	
	Repetir
		mensajeIntentos(intentos);
		
		numeroUsuario = pedirNumeroAlUsuario(min, max);
		aGanado = revisarSiAdivino(numeroSecreto, numeroUsuario);
		
		intentos = intentos - 1;
		Si intentos < 1 Entonces
			sinIntentos = Verdadero;
		FinSi
	Hasta Que aGanado O sinIntentos;
FinFuncion

// ----------------------------------------------------------------------------------------

Proceso Main
	Definir cantidadDeIntentos Como Entero;
	Definir numeroSecreto Como Entero;
	Definir numeroMenor Como Entero;
	Definir numeroMayor Como Entero;
	Definir aGanado Como Logico;
	
	cantidadDeIntentos = 3;
	numeroMenor = 1;
	numeroMayor = 3;

	numeroSecreto = generarNumero(numeroMenor, numeroMayor);
	anuncioBienvenida(numeroMenor, numeroMayor);
	aGanado = adivinar(numeroSecreto, cantidadDeIntentos, numeroMenor, numeroMayor);
	mensajeFinal(aGanado, numeroSecreto);
FinProceso
