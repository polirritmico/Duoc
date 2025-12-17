/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 * Author:  Jazna
 */

DROP DATABASE dsyapp;
CREATE DATABASE IF NOT EXISTS dsyapp;
USE dsyapp;

CREATE TABLE espada (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    material VARCHAR(25) NOT NULL,
    longitud INTEGER NOT NULL,
    PRIMARY KEY (id)
);

/*
Agrega algunos registros
*/
INSERT INTO espada(material, longitud) VALUES ('Zarpa rápida', 60);
INSERT INTO espada(material, longitud) VALUES ('Rebanavientos', 70);
INSERT INTO espada(material, longitud) VALUES ('Filo tempestuoso', 35);
INSERT INTO espada(material, longitud) VALUES ('RompeJuramentos', 27);


