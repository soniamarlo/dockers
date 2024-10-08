CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;

-- Crear la tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    CP VARCHAR(10),
    localidad VARCHAR(100)
);

-- Crear la tabla de perros
CREATE TABLE IF NOT EXISTS perros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    raza VARCHAR(50) NOT NULL,
    idUsuario INT DEFAULT 0,
    FOREIGN KEY (idUsuario) REFERENCES usuarios(id) ON DELETE SET NULL
);

-- Crear la tabla de historial de adopciones
CREATE TABLE IF NOT EXISTS historialAdopciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    idUsuario INT,
    idPerro INT,
    FOREIGN KEY (idUsuario) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (idPerro) REFERENCES perros(id) ON DELETE CASCADE
);
