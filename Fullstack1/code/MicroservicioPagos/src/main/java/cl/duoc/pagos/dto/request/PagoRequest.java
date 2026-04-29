package cl.duoc.pagos.dto.request;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import lombok.Data;

@Data
public class PagoRequest {
    @NotNull
    private Integer montoPagado;
    private String estadoPago;
    private Integer idFiesta;
}
