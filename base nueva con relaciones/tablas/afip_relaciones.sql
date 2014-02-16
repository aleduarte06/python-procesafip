# ************************************************************
# Sequel Pro SQL dump
# Versión 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 192.168.1.37 (MySQL 5.5.32-0ubuntu0.12.04.1)
# Base de datos: test2
# Tiempo de Generación: 2014-02-14 15:58:02 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Volcado de tabla afip_relaciones
# ------------------------------------------------------------

DROP TABLE IF EXISTS `afip_relaciones`;

CREATE TABLE `afip_relaciones` (
  `cuit` varchar(11) DEFAULT NULL,
  `cuil` varchar(11) DEFAULT NULL,
  `apellido_nombre` varchar(55) DEFAULT NULL,
  `fecha_inicio_relacion` varchar(10) DEFAULT NULL,
  `fecha_fin_relacion` varchar(10) DEFAULT NULL,
  `renos` varchar(6) DEFAULT NULL,
  `clave_alta_registro` varchar(20) DEFAULT NULL,
  `fecha_clave_registro` varchar(10) DEFAULT NULL,
  `separador` varchar(1) DEFAULT NULL,
  `hora_clave_alta` varchar(5) DEFAULT NULL,
  `clave_baja_registro` varchar(20) DEFAULT NULL,
  `fecha_clave_baja` varchar(10) DEFAULT NULL,
  `separor2` varchar(1) DEFAULT NULL,
  `hora_clave_baja` varchar(5) DEFAULT NULL,
  `codigo_contrato` varchar(3) DEFAULT NULL,
  `marca_trabajador_agro` varchar(2) DEFAULT NULL,
  `regimen_aportes` varchar(2) DEFAULT NULL,
  `codigo_sit_baja` varchar(2) DEFAULT NULL,
  `filler1` varchar(5) DEFAULT NULL,
  `fecha_mov` varchar(10) DEFAULT NULL,
  `separador3` varchar(1) DEFAULT NULL,
  `hora_mov` varchar(8) DEFAULT NULL,
  `codigo_mov` varchar(2) DEFAULT NULL,
  `rem_bruta` varchar(11) DEFAULT NULL,
  `cod_modalidad_liq` varchar(1) DEFAULT NULL,
  `cod_sucursal_exp` varchar(5) DEFAULT NULL,
  `cod_actividad` varchar(6) DEFAULT NULL,
  `cod_puesto` varchar(4) DEFAULT NULL,
  `fecha_telegrama_renuncia` varchar(10) DEFAULT NULL,
  `filler2` varchar(4) DEFAULT NULL,
  `marca_rectificacion` varchar(1) DEFAULT NULL,
  `area_reservada` varchar(48) DEFAULT NULL,
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
