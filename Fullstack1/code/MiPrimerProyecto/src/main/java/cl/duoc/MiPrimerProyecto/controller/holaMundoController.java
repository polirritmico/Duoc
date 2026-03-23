package cl.duoc.MiPrimerProyectoFullStackApplication.controller;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;

@RestController
public class holaMundoController{
    // Agregamos el tipo de la solicitud (GET, POST, PUT, DELETE, etc.)
    @GetMapping("/holaMundo")
    public String getMethodName() {
        return "¡Hola Mundo!";
    }
}