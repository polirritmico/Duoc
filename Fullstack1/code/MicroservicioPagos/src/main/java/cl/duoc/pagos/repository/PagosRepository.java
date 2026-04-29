package cl.duoc.pagos.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import cl.duoc.pagos.model.Pago;

public interface PagosRepository extends JpaRepository<Pago, Long> {

}
