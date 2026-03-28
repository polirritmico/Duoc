package cl.duoc.MicroservicioFiestas.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import cl.duoc.MicroservicioFiestas.model.Fiesta;
import cl.duoc.MicroservicioFiestas.repository.FiestaRepository;

@Service
public class FiestaService {
    @Autowired
    private FiestaRepository repository;

    public List<Fiesta> getAllFiestas() {
        return repository.getFiestas();
    }
}
