-- Base de datos: adoptaya (PostgreSQL)

CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS refugios (
    id_refugio SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ciudad VARCHAR(80) NOT NULL,
    contacto VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS mascotas (
    id_mascota SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    tipo VARCHAR(30) NOT NULL,
    edad VARCHAR(20) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    id_refugio INTEGER REFERENCES refugios(id_refugio)
);

CREATE TABLE IF NOT EXISTS adoptantes (
    id_adoptante SERIAL PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL,
    cedula VARCHAR(10) NOT NULL,
    telefono VARCHAR(15) NOT NULL
);

CREATE TABLE IF NOT EXISTS solicitudes (
    id_solicitud SERIAL PRIMARY KEY,
    id_adoptante INTEGER REFERENCES adoptantes(id_adoptante),
    id_mascota INTEGER REFERENCES mascotas(id_mascota),
    fecha VARCHAR(20) NOT NULL,
    estado VARCHAR(30) NOT NULL
);