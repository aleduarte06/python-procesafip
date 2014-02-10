# ************************************************************
# Sequel Pro SQL dump
# Versión 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 192.168.10.08 (MySQL 5.5.32-0ubuntu0.12.04.1)
# Base de datos: os111308_old
# Tiempo de Generación: 2014-02-08 15:12:10 -0300
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Volcado de tabla afip_autogestion
# ------------------------------------------------------------

DROP TABLE IF EXISTS `afip_autogestion`;

CREATE TABLE `afip_autogestion` (
  `renos` varchar(4) DEFAULT NULL,
  `nro_exp` varchar(9) DEFAULT NULL,
  `fecha_proceso` varchar(10) DEFAULT NULL,
  `fecha_tranf` varchar(10) DEFAULT NULL,
  `cod_clas` varchar(2) DEFAULT NULL,
  `importe_exp` varchar(15) DEFAULT NULL,
  `nro_cuota` varchar(4) DEFAULT NULL,
  `importe` varchar(15) DEFAULT NULL,
  `cred_deb` varchar(1) DEFAULT NULL,
  `periodo` varchar(6) DEFAULT NULL,
  `nro_exp_orig` varchar(9) DEFAULT NULL,
  `cod_hospita` varchar(8) DEFAULT NULL,
  `ref_externa` varchar(30) DEFAULT NULL,
  `obs` varchar(50) DEFAULT NULL,
  `juzgado` varchar(100) DEFAULT NULL,
  `secretaria` varchar(50) DEFAULT NULL,
  `autos` varchar(1024) DEFAULT NULL,
  `detalle_fact` varchar(200) DEFAULT NULL,
  `filler` varchar(53) DEFAULT NULL,
  `fecha` varchar(8) DEFAULT NULL,
  `idautogestion` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idautogestion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `afip_autogestion` WRITE;
/*!40000 ALTER TABLE `afip_autogestion` DISABLE KEYS */;

INSERT INTO `afip_autogestion` (`renos`, `nro_exp`, `fecha_proceso`, `fecha_tranf`, `cod_clas`, `importe_exp`, `nro_cuota`, `importe`, `cred_deb`, `periodo`, `nro_exp_orig`, `cod_hospita`, `ref_externa`, `obs`, `juzgado`, `secretaria`, `autos`, `detalle_fact`, `filler`, `fecha`, `idautogestion`)
VALUES
	(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1);

/*!40000 ALTER TABLE `afip_autogestion` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
