# ************************************************************
# Sequel Pro SQL dump
# Versión 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 192.168.1.37 (MySQL 5.5.32-0ubuntu0.12.04.1)
# Base de datos: test2
# Tiempo de Generación: 2014-02-14 19:34:13 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Volcado de tabla afip_domicilio
# ------------------------------------------------------------

DROP TABLE IF EXISTS `afip_domicilio`;

CREATE TABLE `afip_domicilio` (
  `cuit` varchar(11) DEFAULT NULL,
  `cod_mov` varchar(2) DEFAULT NULL,
  `tipo_externo` varchar(1) DEFAULT NULL,
  `calle` varchar(60) DEFAULT NULL,
  `nro` varchar(6) DEFAULT NULL,
  `torre` varchar(5) DEFAULT NULL,
  `bloque` varchar(5) DEFAULT NULL,
  `piso` varchar(5) DEFAULT NULL,
  `departamento` varchar(5) DEFAULT NULL,
  `cp` varchar(8) DEFAULT NULL,
  `localidad` varchar(60) DEFAULT NULL,
  `provincia` varchar(2) DEFAULT NULL,
  `sucursal` varchar(5) DEFAULT NULL,
  `actividad` varchar(6) DEFAULT NULL,
  `fecha_hora_mov` varchar(26) DEFAULT NULL,
  `area_reservada` varchar(43) DEFAULT NULL,
  `fecha` varchar(10) DEFAULT NULL,
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
