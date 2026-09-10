-- Base de datos: adoptaya

CREATE DATABASE IF NOT EXISTS adoptaya;
USE adoptaya;

CREATE TABLE IF NOT EXISTS refugios (
    id_refugio INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ciudad VARCHAR(80) NOT NULL,
    contacto VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS mascotas (
    id_mascota INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    tipo VARCHAR(30) NOT NULL,
    edad VARCHAR(20) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    id_refugio INT,
    FOREIGN KEY (id_refugio) REFERENCES refugios(id_refugio)
);