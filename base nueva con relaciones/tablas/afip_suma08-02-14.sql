# ************************************************************
# Sequel Pro SQL dump
# Versión 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 192.168.10.08 (MySQL 5.5.32-0ubuntu0.12.04.1)
# Base de datos: os111308_old
# Tiempo de Generación: 2014-02-08 15:41:38 -0300
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Volcado de tabla afip_suma
# ------------------------------------------------------------

DROP TABLE IF EXISTS `afip_suma`;

CREATE TABLE `afip_suma` (
  `renos` varchar(6) DEFAULT NULL,
  `periodo` varchar(6) DEFAULT NULL,
  `cant_benef` varchar(15) DEFAULT NULL,
  `importe_tranf` varchar(15) DEFAULT NULL,
  `capita` varchar(15) DEFAULT NULL,
  `art_2_inc_a` varchar(15) DEFAULT NULL,
  `art_2_inc_b` varchar(15) DEFAULT NULL,
  `art_2_inc_c` varchar(15) DEFAULT NULL,
  `art_3_ajuste` varchar(16) DEFAULT NULL,
  `total_subsidio` varchar(15) DEFAULT NULL,
  `area_reservada` varchar(26) DEFAULT NULL,
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `afip_suma` WRITE;
/*!40000 ALTER TABLE `afip_suma` DISABLE KEYS */;

INSERT INTO `afip_suma` (`renos`, `periodo`, `cant_benef`, `importe_tranf`, `capita`, `art_2_inc_a`, `art_2_inc_b`, `art_2_inc_c`, `art_3_ajuste`, `total_subsidio`, `area_reservada`, `id`)
VALUES
	(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1);

/*!40000 ALTER TABLE `afip_suma` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
