package cl.duoc.MicroservicioFiestas.model;

import java.time.LocalDate;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.PositiveOrZero;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Fiesta {
    @NotBlank
    private int id;

    @NotBlank
    private String name;

    @NotBlank
    private String type;

    @NotBlank
    private String location;

    @NotNull
    private LocalDate date;

    @PositiveOrZero
    private int guests;
}
