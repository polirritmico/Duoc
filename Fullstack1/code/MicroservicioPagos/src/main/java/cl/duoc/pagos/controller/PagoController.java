package cl.duoc.pagos.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import cl.duoc.pagos.dto.request.PagoRequest;
import cl.duoc.pagos.dto.response.PagoResponse;
import cl.duoc.pagos.service.PagoService;
import io.swagger.v3.oas.annotations.parameters.RequestBody;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping("/api/v1/pagos")
@RequiredArgsConstructor
public class PagoController {
    private final PagoService service;

    public ResponseEntity<PagoResponse> savePago(@Valid @RequestBody PagoRequest req) {
        PagoResponse res = service.savePago(req);
        return ResponseEntity.ok(res);
    }
}
