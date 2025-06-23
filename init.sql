CREATE DATABASE IF NOT EXISTS appdb;
USE appdb;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  password VARCHAR(255)
);

INSERT IGNORE INTO users (first_name, last_name, email, password) VALUES (
  'Loise', 'Fenoll', 'loise.fenoll@ynov.com', 'PvdrTAzTeR247sDnAZBr'
);
