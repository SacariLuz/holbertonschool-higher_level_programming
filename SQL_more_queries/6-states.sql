-- Creacion de la base de datos hbtn_0d_usa y la tabla states en la database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (PRIMARY KEY (id), id INT AUTO_INCREMENT NOT NULL, name VARCHAR(256) NOT NULL);
