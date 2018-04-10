package SensorDB;

import org.springframework.data.repository.CrudRepository;

import SensorDB.Sensortable;

public interface SensorRepository extends CrudRepository<Sensortable, Long> {

}
