
/* Crea una base de datos SQL en su local host con estas premisas */
CREATE DATABASE IF NOT EXISTS hotel;
USE hotel;
CREATE TABLE `nuevo_hotel` (
	`Hora_de_entrada` TIME NOT NULL,
	`Fecha` DATE NOT NULL,
	`Marca_de_vehiculo` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`Patente` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`Habitacion` INT(10) NULL DEFAULT NULL,
	`Cantidad_de_horas` INT(10) NULL DEFAULT NULL,
	`Importe` INT(10) NOT NULL
)
COLLATE='utf8mb4_0900_ai_ci'
ENGINE=InnoDB
;
CREATE TABLE `registro_hotel` (
	`FECHA` DATE NOT NULL,
	`HORA` TIME NOT NULL,
	`MARCA_VEHICULO` CHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`PATENTE` CHAR(50) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`cantidad_horas` INT(10) NOT NULL,
	`HABITACION` INT(10) NOT NULL DEFAULT '0',
	`IMPORTE` INT(10) NOT NULL
)
COLLATE='utf8mb4_0900_ai_ci'
ENGINE=InnoDB
;
