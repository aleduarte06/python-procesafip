# ************************************************************
# Sequel Pro SQL dump
# Versión 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 192.168.10.08 (MySQL 5.5.32-0ubuntu0.12.04.1)
# Base de datos: os111308_old
# Tiempo de Generación: 2014-02-08 14:38:44 -0300
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Volcado de tabla afip_nomina
# ------------------------------------------------------------

DROP TABLE IF EXISTS `afip_nomina`;

CREATE TABLE `afip_nomina` (
  `codosoc` varchar(6) DEFAULT NULL,
  `periodo` varchar(4) DEFAULT NULL,
  `cuit` varchar(11) DEFAULT NULL,
  `cuil` varchar(11) DEFAULT NULL,
  `remosimp` varchar(12) DEFAULT NULL,
  `imposad` varchar(8) DEFAULT NULL,
  `zona` varchar(2) DEFAULT NULL,
  `grpfam` varchar(2) DEFAULT NULL,
  `nogrpfam` varchar(2) DEFAULT NULL,
  `secoblig` varchar(2) DEFAULT NULL,
  `condcuil` varchar(2) DEFAULT NULL,
  `sitcuil` varchar(2) DEFAULT NULL,
  `actividades` varchar(3) DEFAULT NULL,
  `modalidad` varchar(3) DEFAULT NULL,
  `codsini` varchar(2) DEFAULT NULL,
  `apadios` varchar(8) DEFAULT NULL,
  `version` varchar(2) DEFAULT NULL,
  `rem5` varchar(11) DEFAULT NULL,
  `esposa` varchar(1) DEFAULT NULL,
  `excosapo` varchar(12) DEFAULT NULL,
  `indret` varchar(1) DEFAULT NULL,
  `indexccon` varchar(1) DEFAULT NULL,
  `fecpresent` varchar(10) DEFAULT NULL,
  `fecproc` varchar(10) DEFAULT NULL,
  `origrect` varchar(1) DEFAULT NULL,
  `filler` varchar(34) DEFAULT NULL,
  `remcont` varchar(11) DEFAULT NULL,
  `release_ver` varchar(2) DEFAULT NULL,
  `usofut` varchar(23) DEFAULT NULL,
  `fecha_carga` int(4) DEFAULT NULL,
  `quincena` int(1) DEFAULT NULL,
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
