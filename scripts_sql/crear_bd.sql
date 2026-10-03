CREATE DATABASE IF NOT EXISTS viajes_turismo
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'viajes_user'@'localhost'
  IDENTIFIED BY 'ClaveViajes2026';

GRANT ALL PRIVILEGES ON viajes_turismo.* TO 'viajes_user'@'localhost';
FLUSH PRIVILEGES;
