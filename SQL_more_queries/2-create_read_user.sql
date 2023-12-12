-- Creacion de la database hbtn_0d_2 y el usario user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- La contraseña user_0d_2 debe ser user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
