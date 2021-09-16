CREATE DATABASE IF NOT EXISTS `VILLES` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `VILLES`;

CREATE TABLE `CLIENTS` (
  `num_client` VARCHAR(42),
  `nom` VARCHAR(42),
  `adresse` VARCHAR(42),
  `num_commande` VARCHAR(42),
  PRIMARY KEY (`num_client`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `COMMANDES` (
  `num_commande` VARCHAR(42),
  `poids` VARCHAR(42),
  `volume` VARCHAR(42),
  `numtransporteur` VARCHAR(42),
  PRIMARY KEY (`num_commande`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `VILLES` (
  `num_ville` VARCHAR(42),
  `adresse` VARCHAR(42),
  `num_client` VARCHAR(42),
  `num_ville_1` VARCHAR(42),
  PRIMARY KEY (`num_ville`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `LIVRE` (
  `numtransporteur` VARCHAR(42),
  `num_ville` VARCHAR(42),
  PRIMARY KEY (`numtransporteur`, `num_ville`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `TRANSPORTEURS` (
  `numtransporteur` VARCHAR(42),
  `nom_transporteur` VARCHAR(42),
  `adresse` VARCHAR(42),
  `tarif` VARCHAR(42),
  `num_ville` VARCHAR(42),
  PRIMARY KEY (`numtransporteur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `CLIENTS` ADD FOREIGN KEY (`num_commande`) REFERENCES `COMMANDES` (`num_commande`);
ALTER TABLE `COMMANDES` ADD FOREIGN KEY (`numtransporteur`) REFERENCES `TRANSPORTEURS` (`numtransporteur`);
ALTER TABLE `VILLES` ADD FOREIGN KEY (`num_ville_1`) REFERENCES `VILLES` (`num_ville`);
ALTER TABLE `VILLES` ADD FOREIGN KEY (`num_client`) REFERENCES `CLIENTS` (`num_client`);
ALTER TABLE `LIVRE` ADD FOREIGN KEY (`num_ville`) REFERENCES `VILLES` (`num_ville`);
ALTER TABLE `LIVRE` ADD FOREIGN KEY (`numtransporteur`) REFERENCES `TRANSPORTEURS` (`numtransporteur`);
ALTER TABLE `TRANSPORTEURS` ADD FOREIGN KEY (`num_ville`) REFERENCES `VILLES` (`num_ville`);