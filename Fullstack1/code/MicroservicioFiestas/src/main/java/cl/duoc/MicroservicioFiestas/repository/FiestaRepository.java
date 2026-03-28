package cl.duoc.MicroservicioFiestas.repository;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;

import cl.duoc.MicroservicioFiestas.model.Fiesta;

@Repository
public class FiestaRepository {
    private List<Fiesta> data = new ArrayList<>();

    public List<Fiesta> getFiestas() {
        return new ArrayList<>(data);
    }

    public Fiesta getById(int id) {
        for (Fiesta fiesta : data) {
            if (fiesta.getId() == id) {
                return fiesta;
            }
        }
        return null;
    }

    public Fiesta createFiesta(Fiesta newFiesta) {
        Fiesta fiestaInDB = getById(newFiesta.getId());
        if (fiestaInDB != null) {
            throw new RuntimeException("Ya existe la fiesta.");
        }
        data.add(newFiesta);
        return newFiesta;
    }

    public Fiesta updateFiesta(Fiesta updatedFiesta) {
        for (Fiesta fiesta : data) {
            if (fiesta.getId() == updatedFiesta.getId()) {
                // TODO: probar. si no funciona actualizar cada atributo
                fiesta = updatedFiesta;
                return fiesta;
            }
        }
        throw new RuntimeException("Fiesta no encontrada.");
    }

    public Fiesta deleteFiesta(Fiesta targetFiesta) {
        Fiesta matchFiesta = getById(targetFiesta.getId());
        if (matchFiesta != null) {
            data.remove(targetFiesta);
            return targetFiesta;
        } else {
            throw new RuntimeException("Fiesta no encontrada");
        }
    }
}
