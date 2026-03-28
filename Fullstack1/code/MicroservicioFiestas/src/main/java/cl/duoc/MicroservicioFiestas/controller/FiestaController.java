package cl.duoc.MicroservicioFiestas.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import cl.duoc.MicroservicioFiestas.model.Fiesta;
import cl.duoc.MicroservicioFiestas.service.FiestaService;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@RestController
@RequestMapping("/api/v1/fiestas")
public class FiestaController {

    @Autowired
    private FiestaService service;

    @GetMapping("/get-all")
    public List<Fiesta> getAllFiestas() {
        return service.getAllFiestas();
    }
}
