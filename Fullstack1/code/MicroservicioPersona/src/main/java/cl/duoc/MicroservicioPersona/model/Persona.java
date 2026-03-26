package cl.duoc.MicroservicioPersona.model;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Positive;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Persona {
	@Positive(message = "El campo rut debe ser un positivo valido.")
    private int rut;

	@Pattern(regexp = "[0-9kK]")
    private char dv;

	@NotBlank(message = "El campo nombre es obligatorio")
    private String nombre;
}
