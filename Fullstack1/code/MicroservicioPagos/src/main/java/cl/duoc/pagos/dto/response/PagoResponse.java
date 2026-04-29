package cl.duoc.pagos.dto.response;

import java.time.LocalDate;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PagoResponse {
    private Long id;
    private LocalDate fecha;
    private Integer monto;
    private String estado;
}
