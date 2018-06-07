CREATE DATABASE agenda;
USE agenda;

CREATE TABLE Contato (
  cId int(11) NOT NULL AUTO_INCREMENT,
  nome varchar(100) DEFAULT NULL,
  email varchar(100) DEFAULT NULL,
  PRIMARY KEY (cId)
);