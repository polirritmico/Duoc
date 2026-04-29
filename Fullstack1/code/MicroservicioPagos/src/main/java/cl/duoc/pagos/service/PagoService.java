package cl.duoc.pagos.service;

import org.springframework.stereotype.Service;

import cl.duoc.pagos.dto.request.PagoRequest;
import cl.duoc.pagos.dto.response.PagoResponse;
import cl.duoc.pagos.repository.PagosRepository;
import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class PagoService {
    private final PagosRepository repo;

    public PagoResponse savePago(PagoRequest pago) {
        PagoResponse res = PagoResponse();
    }
}
