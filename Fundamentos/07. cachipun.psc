Funcion mostrarOpciones(reglas, jugadasPosibles)
	Definir i Como Entero;
	Para i = 0 Hasta jugadasPosibles - 1 Hacer // 0-index
		Escribir i + 1, ". ", reglas[i,0]; // 1-index
	FinPara
	Escribir "";
FinFuncion

Funcion jugada <- jugarUsuario(reglas, jugadasPosibles)
	Definir jugada Como Entero;
	Definir jugadaValida Como Logico;
	
	Escribir "Elige una opción:";
	Repetir
		Leer jugada;
		Si jugada < 1 O jugada > jugadasPosibles Entonces
			jugadaValida = Falso;
			Escribir "Opción inválida. Elige una opción correcta";
		SiNo
			jugadaValida = Verdadero;
			jugada = jugada - 1; // 1-index a 0-index
		FinSi
	Hasta Que jugadaValida
	
	Escribir "Has elegido jugar: ", reglas[jugada,0];
FinFuncion

Funcion jugada <- jugarMaquina(reglas, jugadasPosibles)
	Definir jugada Como Entero;
	jugada = Azar(jugadasPosibles);
	Escribir "Tu oponente ha jugado: ", reglas[jugada,0];
FinFuncion

Funcion hayEmpate <- resolverEmpate(jugadaUsuario, jugadaMaquina)
	Definir hayEmpate Como Logico;
	Si jugadaUsuario == jugadaMaquina Entonces
		hayEmpate = Verdadero;
		Escribir "";
		Escribir "¡Empate! Nadie gana esta ronda";
		Escribir "";
	SiNo
		hayEmpate = Falso;
	FinSi
FinFuncion

Funcion ganaUsuario <- resolverGanador(jugadaUsuario, jugadaMaquina, reglas)
	Definir ganaUsuario Como Logico;
	
	Si reglas[jugadaUsuario,1] == reglas[jugadaMaquina,0] Entonces
		ganaUsuario = Verdadero;
		Escribir reglas[jugadaUsuario,0], " vence a ", reglas[jugadaMaquina,0] , ". ¡Has ganado la ronda!";
	SiNo
		ganaUsuario = Falso;
		Escribir reglas[jugadaMaquina,0], " vence a ", reglas[jugadaUsuario,0] , ". Has perdido la ronda...";
	FinSi
FinFuncion

Funcion anunciarGanador(ganaUsuario)
	Si ganaUsuario Entonces
		Escribir "¡Felicidades, has ganado!";
	SiNo
		Escribir "¡Mala suerte, has perdido!";
	FinSi
FinFuncion

Funcion mostrarPuntuacion(puntosUsuario, puntosMaquina)
	Escribir "";
	Escribir "Puntaje usuario: ", puntosUsuario;
	Escribir "Puntaje rival: ", puntosMaquina;
	Escribir "";
FinFuncion

Funcion ronda <- incrementarYAnunciarRonda(ronda)
	ronda = ronda + 1;
	Escribir "--------------";
	Escribir " Ronda N.° ", ronda;
	Escribir "--------------";
	Escribir "";
FinFuncion

Funcion mostrarBienvenida
	Limpiar Pantalla;
	Escribir "== Cachipún ==";
FinFuncion

//---------------------------------------------------------------------

Funcion ganaUsuario <- jugar(reglas, jugadasPosibles, rondasAGanar)
	Definir jugadaUsuario Como Entero;
	Definir jugadaMaquina Como Entero;
	Definir puntosUsuario Como Entero;
	Definir puntosMaquina Como Entero;
	Definir ronda Como Entero;
	
	Definir hayEmpate Como Logico;
	Definir hayGanador Como Logico;
	Definir ganaUsuario Como Logico;
	
	hayGanador = Falso;
	puntosUsuario = 0;
	puntosMaquina = 0;
	
	ronda = 0;
	Mientras No hayGanador Hacer
		ronda = incrementarYAnunciarRonda(ronda);
		
		mostrarOpciones(reglas, jugadasPosibles);
		jugadaUsuario = jugarUsuario(reglas, jugadasPosibles);
		jugadaMaquina = jugarMaquina(reglas, jugadasPosibles);
		
		hayEmpate = resolverEmpate(jugadaUsuario, jugadaMaquina);
		Si No hayEmpate Entonces
			ganaUsuario = resolverGanador(jugadaUsuario, jugadaMaquina, reglas);
			
			Si ganaUsuario Entonces
				puntosUsuario = puntosUsuario + 1;
			SiNo
				puntosMaquina = puntosMaquina + 1;
			FinSi
			
			mostrarPuntuacion(puntosUsuario, puntosMaquina);
			
			Si puntosUsuario == rondasAGanar Entonces
				hayGanador = Verdadero;
				ganaUsuario = Verdadero;
			FinSi
			Si puntosMaquina == rondasAGanar Entonces
				hayGanador = Verdadero;
				ganaUsuario = Falso;
			FinSi
		FinSi
	FinMientras
FinFuncion

//---------------------------------------------------------------------

Proceso Main
	Definir reglas Como Caracter;
	Dimension reglas[3,3];
	
	Definir jugadasPosibles Como Entero;
	Definir rondasAGanar Como Entero;
	Definir ganaUsuario Como Logico;

	jugadasPosibles = 3;
	reglas[0,0] = "Piedra"; // Piedra:
	reglas[0,1] = "Tijera"; // vence a
	reglas[0,2] = "Papel";  // pierde contra
	
	reglas[1,0] = "Papel";  // Papel:
	reglas[1,1] = "Piedra"; // vence a
	reglas[1,2] = "Tijera"; // pierde contra
	
	reglas[2,0] = "Tijera"; // Tijera
	reglas[2,1] = "Papel";  // vence a
	reglas[2,2] = "Piedra"; // pierde contra
	
	rondasAGanar = 3;
	
	mostrarBienvenida();
	ganaUsuario = jugar(reglas, jugadasPosibles, rondasAGanar);
	anunciarGanador(ganaUsuario);
FinProceso
