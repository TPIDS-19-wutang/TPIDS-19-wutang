-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: triviumdb
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `consultations`
--

DROP TABLE IF EXISTS `consultations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consultations` (
  `id_consultations` int NOT NULL AUTO_INCREMENT,
  `id_user` int NOT NULL,
  `name` varchar(80) NOT NULL,
  `lastname` varchar(80) NOT NULL,
  `email` varchar(100) NOT NULL,
  `affair` varchar(100) NOT NULL,
  `message` varchar(500) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_consultations`),
  KEY `id_user` (`id_user`),
  CONSTRAINT `consultations_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consultations`
--

LOCK TABLES `consultations` WRITE;
/*!40000 ALTER TABLE `consultations` DISABLE KEYS */;
/*!40000 ALTER TABLE `consultations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faq`
--

DROP TABLE IF EXISTS `faq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faq` (
  `id` int NOT NULL AUTO_INCREMENT,
  `question` varchar(200) NOT NULL,
  `answer` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faq`
--

LOCK TABLES `faq` WRITE;
/*!40000 ALTER TABLE `faq` DISABLE KEYS */;
INSERT INTO `faq` VALUES (1,'¿Cuál es el horario de check-in y check-out?','El horario de check-in es a partir de las 11:00 horas y el check-out es hasta las 00:00 horas.'),(2,'¿Cuál es la política de cancelación?','La política de cancelación varía según la tarifa seleccionada. Por favor, consulte las condiciones de la tarifa antes de realizar la reserva.'),(3,'¿Se admiten mascotas?','Si, se admiten mascotas en el hotel. Por favor, póngase en contacto con nosotros para más información.'),(4,'¿Hay servicio de transporte al aeropuerto?','No, no ofrecemos servicio de transporte al aeropuerto. Por favor, póngase en contacto con nosotros para más información.'),(5,'¿Se puede fumar en las habitaciones?','Si, se permite fumar en las habitaciones unicamente en los balcones. Por favor, póngase en contacto con nosotros para más información.'),(6,'¿Hay aparcamiento disponible?','Sí, disponemos de aparcamiento gratuito para nuestros huéspedes.'),(7,'¿Se puede solicitar una cama adicional?','No, no es posible solicitar una cama adicional en las habitaciones.'),(8,'¿Hay conexión Wi-Fi gratuita?','Sí, ofrecemos conexión Wi-Fi gratuita en todas nuestras instalaciones.'),(9,'¿Se puede solicitar un servicio de habitaciones?','Sí, ofrecemos servicio de habitaciones las 24 horas del día.'),(10,'¿Hay piscina en el hotel?','Sí, disponemos de una piscina al aire libre para el disfrute de nuestros huéspedes.');
/*!40000 ALTER TABLE `faq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotels`
--

DROP TABLE IF EXISTS `hotels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hotels` (
  `id_hotel` int NOT NULL AUTO_INCREMENT,
  `location` varchar(80) NOT NULL,
  `description` varchar(500) NOT NULL,
  `image` varchar(120) DEFAULT NULL,
  `cant_rooms` int NOT NULL,
  `floors` int NOT NULL,
  `stars` int NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_hotel`),
  KEY `location_disponibility` (`location`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotels`
--

LOCK TABLES `hotels` WRITE;
/*!40000 ALTER TABLE `hotels` DISABLE KEYS */;
INSERT INTO `hotels` VALUES (1,'Misiones','Hotel ubicado en la provincia de Misiones, Argentina.','/images/hotel-misiones.jpg',208,4,5,'2024-11-25 22:13:45'),(2,'Córdoba','Hotel ubicado en la provincia de Córdoba, Argentina.','/images/hotel-cordoba.jpg',208,4,4,'2024-11-25 22:13:45'),(3,'Salta','Hotel ubicado en la provincia de Salta, Argentina.','/images/hotel-salta.jpg',208,4,4,'2024-11-25 22:13:45'),(4,'Santa Cruz','Hotel ubicado en la provincia de Santa Cruz, Argentina.','/images/hotel-santacruz.jpg',208,4,5,'2024-11-25 22:13:45'),(5,'Mendoza','Hotel ubicado en la provincia de Mendoza, Argentina.','/images/hotel-mendoza.jpg',208,4,3,'2024-11-25 22:13:45'),(6,'Buenos Aires','Hotel ubicado en la provincia de Buenos Aires, Argentina.','/images/hotel-buenosaires.jpg',208,4,3,'2024-11-25 22:13:45');
/*!40000 ALTER TABLE `hotels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations`
--

DROP TABLE IF EXISTS `reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservations` (
  `id_reservation` int NOT NULL AUTO_INCREMENT,
  `id_user` int NOT NULL,
  `id_room` int DEFAULT NULL,
  `id_hotel` int DEFAULT NULL,
  `number_people` int DEFAULT NULL,
  `type_room` int DEFAULT NULL,
  `check_in` timestamp NULL DEFAULT NULL,
  `check_out` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_reservation`),
  KEY `id_user` (`id_user`),
  KEY `id_room` (`id_room`),
  KEY `id_hotel` (`id_hotel`),
  CONSTRAINT `reservations_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`),
  CONSTRAINT `reservations_ibfk_2` FOREIGN KEY (`id_room`) REFERENCES `rooms` (`id_room`),
  CONSTRAINT `reservations_ibfk_3` FOREIGN KEY (`id_hotel`) REFERENCES `hotels` (`id_hotel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations`
--

LOCK TABLES `reservations` WRITE;
/*!40000 ALTER TABLE `reservations` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rooms`
--

DROP TABLE IF EXISTS `rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rooms` (
  `id_room` int NOT NULL AUTO_INCREMENT,
  `id_hotel` int DEFAULT NULL,
  `type_room` varchar(80) COLLATE utf8mb4_general_ci NOT NULL,
  `number_room` int NOT NULL,
  `floor_room` int NOT NULL,
  PRIMARY KEY (`id_room`),
  KEY `id_hotel` (`id_hotel`),
  CONSTRAINT `rooms_ibfk_1` FOREIGN KEY (`id_hotel`) REFERENCES `hotels` (`id_hotel`)
) ENGINE=InnoDB AUTO_INCREMENT=209 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rooms`

LOCK TABLES `rooms` WRITE;
/*!40000 ALTER TABLE `rooms` DISABLE KEYS*/;
INSERT INTO `rooms` VALUES(1,1,'Classic',100,1),(2,1,'Classic',101,1),(3,1,'Classic',102,1),(4,1,'Classic',103,1),(5,1,'Classic',104,1),(6,1,'Classic',105,1),(7,1,'Classic',106,1),(8,1,'Classic',107,1),(9,1,'Classic',108,1),(10,1,'Classic',109,1),(11,1,'Classic',110,1),(12,1,'Classic',111,1),(13,1,'Classic',112,1),(14,1,'Doble',113,1),(15,1,'Doble',114,1),(16,1,'Doble',115,1),(17,1,'Doble',116,1),(18,1,'Doble',117,1),(19,1,'Doble',118,1),(20,1,'Doble',119,1),(21,1,'Doble',120,1),(22,1,'Doble',121,1),(23,1,'Doble',122,1),(24,1,'Doble',123,1),(25,1,'Doble',124,1),(26,1,'Doble',125,1),(27,1,'Premium',126,1),(28,1,'Premium',127,1),(29,1,'Premium',128,1),(30,1,'Premium',129,1),(31,1,'Premium',130,1),(32,1,'Premium',131,1),(33,1,'Premium',132,1),(34,1,'Premium',133,1),(35,1,'Premium',134,1),(36,1,'Premium',135,1),(37,1,'Premium',136,1),(38,1,'Premium',137,1),(39,1,'Premium',138,1),(40,1,'Deluxe',139,1),(41,1,'Deluxe',140,1),(42,1,'Deluxe',141,1),(43,1,'Deluxe',142,1),(44,1,'Deluxe',143,1),(45,1,'Deluxe',144,1),(46,1,'Deluxe',145,1),(47,1,'Deluxe',146,1),(48,1,'Deluxe',147,1),(49,1,'Deluxe',148,1),(50,1,'Deluxe',149,1),(51,1,'Deluxe',150,1),(52,1,'Deluxe',151,1),(53,1,'Classic',200,2),(54,1,'Classic',201,2),(55,1,'Classic',202,2),(56,1,'Classic',203,2),(57,1,'Classic',204,2),(58,1,'Classic',205,2),(59,1,'Classic',206,2),(60,1,'Classic',207,2),(61,1,'Classic',208,2),(62,1,'Classic',209,2),(63,1,'Classic',210,2),(64,1,'Classic',211,2),(65,1,'Doble',212,2),(66,1,'Doble',213,2),(67,1,'Doble',214,2),(68,1,'Doble',215,2),(69,1,'Doble',216,2),(70,1,'Doble',217,2),(71,1,'Doble',218,2),(72,1,'Doble',219,2),(73,1,'Doble',220,2),(74,1,'Doble',221,2),(75,1,'Doble',222,2),(76,1,'Doble',223,2),(77,1,'Doble',224,2),(78,1,'Doble',225,2),(79,1,'Premium',226,2),(80,1,'Premium',227,2),(81,1,'Premium',228,2),(82,1,'Premium',229,2),(83,1,'Premium',230,2),(84,1,'Premium',231,2),(85,1,'Premium',232,2),(86,1,'Premium',233,2),(87,1,'Premium',234,2),(88,1,'Premium',235,2),(89,1,'Premium',236,2),(90,1,'Premium',237,2),(91,1,'Premium',238,2),(92,1,'Deluxe',239,2),(93,1,'Deluxe',240,2),(94,1,'Deluxe',241,2),(95,1,'Deluxe',242,2),(96,1,'Deluxe',243,2),(97,1,'Deluxe',244,2),(98,1,'Deluxe',245,2),(99,1,'Deluxe',246,2),(100,1,'Deluxe',247,2),(101,1,'Deluxe',248,2),(102,1,'Deluxe',249,2),(103,1,'Deluxe',250,2),(104,1,'Deluxe',251,2),(105,1,'Classic',300,3),(106,1,'Classic',301,3),(107,1,'Classic',302,3),(108,1,'Classic',303,3),(109,1,'Classic',304,3),(110,1,'Classic',305,3),(111,1,'Classic',306,3),(112,1,'Classic',307,3),(113,1,'Classic',308,3),(114,1,'Classic',309,3),(115,1,'Classic',310,3),(116,1,'Classic',311,3),(117,1,'Doble',312,3),(118,1,'Doble',313,3),(119,1,'Doble',314,3),(120,1,'Doble',315,3),(121,1,'Doble',316,3),(122,1,'Doble',317,3),(123,1,'Doble',318,3),(124,1,'Doble',319,3),(125,1,'Doble',320,3),(126,1,'Doble',321,3),(127,1,'Doble',322,3),(128,1,'Doble',323,3),(129,1,'Doble',324,3),(130,1,'Doble',325,3),(131,1,'Premium',326,3),(132,1,'Premium',327,3),(133,1,'Premium',328,3),(134,1,'Premium',329,3),(135,1,'Premium',330,3),(136,1,'Premium',331,3),(137,1,'Premium',332,3),(138,1,'Premium',333,3),(139,1,'Premium',334,3),(140,1,'Premium',335,3),(141,1,'Premium',336,3),(142,1,'Premium',337,3),(143,1,'Premium',338,3),(144,1,'Deluxe',339,3),(145,1,'Deluxe',340,3),(146,1,'Deluxe',341,3),(147,1,'Deluxe',342,3),(148,1,'Deluxe',343,3),(149,1,'Deluxe',344,3),(150,1,'Deluxe',345,3),(151,1,'Deluxe',346,3),(152,1,'Deluxe',347,3),(153,1,'Deluxe',348,3),(154,1,'Deluxe',349,3),(155,1,'Deluxe',350,3),(156,1,'Deluxe',351,3),(157,1,'Classic',400,4),(158,1,'Classic',401,4),(159,1,'Classic',402,4),(160,1,'Classic',403,4),(161,1,'Classic',404,4),(162,1,'Classic',405,4),(163,1,'Classic',406,4),(164,1,'Classic',407,4),(165,1,'Classic',408,4),(166,1,'Classic',409,4),(167,1,'Classic',410,4),(168,1,'Classic',411,4),(169,1,'Doble',412,4),(170,1,'Doble',413,4),(171,1,'Doble',414,4),(172,1,'Doble',415,4),(173,1,'Doble',416,4),(174,1,'Doble',417,4),(175,1,'Doble',418,4),(176,1,'Doble',419,4),(177,1,'Doble',420,4),(178,1,'Doble',421,4),(179,1,'Doble',422,4),(180,1,'Doble',423,4),(181,1,'Doble',424,4),(182,1,'Doble',425,4),(183,1,'Premium',426,4),(184,1,'Premium',427,4),(185,1,'Premium',428,4),(186,1,'Premium',429,4),(187,1,'Premium',430,4),(188,1,'Premium',431,4),(189,1,'Premium',432,4),(190,1,'Premium',433,4),(191,1,'Premium',434,4),(192,1,'Premium',435,4),(193,1,'Premium',436,4),(194,1,'Premium',437,4),(195,1,'Premium',438,4),(196,1,'Deluxe',439,4),(197,1,'Deluxe',440,4),(198,1,'Deluxe',441,4),(199,1,'Deluxe',442,4),(200,1,'Deluxe',443,4),(201,1,'Deluxe',444,4),(202,1,'Deluxe',445,4),(203,1,'Deluxe',446,4),(204,1,'Deluxe',447,4),(205,1,'Deluxe',448,4),(206,1,'Deluxe',449,4),(207,1,'Deluxe',450,4),(208,1,'Deluxe',451,4),(1,1,'Classic',100,1),
(209,2,'Classic',100,1),
(210,2,'Classic',101,1),
(211,2,'Classic',102,1),
(211,2,'Classic',102,1),
(212,2,'Classic',103,1),
(213,2,'Classic',104,1),
(214,2,'Classic',105,1),
(215,2,'Classic',106,1),
(216,2,'Classic',107,1),
(217,2,'Classic',108,1),
(218,2,'Classic',109,1),
(219,2,'Classic',110,1),
(220,2,'Classic',111,1),
(221,2,'Classic',112,1),
(222,2,'Doble',113,1),
(223,2,'Doble',114,1),
(224,2,'Doble',115,1),
(225,2,'Doble',116,1),
(226,2,'Doble',117,1),
(227,2,'Doble',118,1),
(228,2,'Doble',119,1),
(229,2,'Doble',120,1),
(230,2,'Doble',121,1),
(231,2,'Doble',122,1),
(232,2,'Doble',123,1),
(233,2,'Doble',124,1),
(234,2,'Doble',125,1),
(235,2,'Premium',126,1),
(236,2,'Premium',127,1),
(237,2,'Premium',128,1),
(238,2,'Premium',129,1),
(239,2,'Premium',130,1),
(240,2,'Premium',131,1),
(241,2,'Premium',132,1),
(242,2,'Premium',133,1),
(243,2,'Premium',134,1),
(244,2,'Premium',135,1),
(245,2,'Premium',136,1),
(246,2,'Premium',137,1),
(247,2,'Premium',138,1),
(248,2,'Deluxe',139,1),
(249,2,'Deluxe',140,1),
(250,2,'Deluxe',141,1),
(251,2,'Deluxe',142,1),
(252,2,'Deluxe',143,1),
(253,2,'Deluxe',144,1),
(254,2,'Deluxe',145,1),
(255,2,'Deluxe',146,1),
(256,2,'Deluxe',147,1),
(257,2,'Deluxe',148,1),
(258,2,'Deluxe',149,1),
(259,2,'Deluxe',150,1),
(260,2,'Deluxe',151,1),
(261,2,'Classic',200,2),
(262,2,'Classic',201,2),
(263,2,'Classic',202,2),
(264,2,'Classic',203,2),
(265,2,'Classic',204,2),
(266,2,'Classic',205,2),
(267,2,'Classic',206,2),
(268,2,'Classic',207,2),
(269,2,'Classic',208,2),
(270,2,'Classic',209,2),
(271,2,'Classic',210,2),
(272,2,'Classic',211,2),
(273,2,'Doble',212,2),
(274,2,'Doble',213,2),
(275,2,'Doble',214,2),
(276,2,'Doble',215,2),
(277,2,'Doble',216,2),
(278,2,'Doble',217,2),
(279,2,'Doble',218,2),
(280,2,'Doble',219,2),
(281,2,'Doble',220,2),
(282,2,'Doble',221,2),
(283,2,'Doble',222,2),
(284,2,'Doble',223,2),
(285,2,'Doble',224,2),
(286,2,'Doble',225,2),
(287,2,'Premium',226,2),
(288,2,'Premium',227,2),
(289,2,'Premium',228,2),
(290,2,'Premium',229,2),
(291,2,'Premium',230,2),
(292,2,'Premium',231,2),
(293,2,'Premium',232,2),
(294,2,'Premium',233,2),
(295,2,'Premium',234,2),
(296,2,'Premium',235,2),
(297,2,'Premium',236,2),
(298,2,'Premium',237,2),
(299,2,'Premium',238,2),
(300,2,'Deluxe',239,2),
(301,2,'Deluxe',240,2),
(302,2,'Deluxe',241,2),
(303,2,'Deluxe',242,2),
(304,2,'Deluxe',243,2),
(305,2,'Deluxe',244,2),
(306,2,'Deluxe',245,2),
(307,2,'Deluxe',246,2),
(308,2,'Deluxe',247,2),
(309,2,'Deluxe',248,2),
(310,2,'Deluxe',249,2),
(311,2,'Deluxe',250,2),
(312,2,'Deluxe',251,2),
(313,2,'Classic',300,3),
(314,2,'Classic',301,3),
(315,2,'Classic',302,3),
(316,2,'Classic',303,3),
(317,2,'Classic',304,3),
(318,2,'Classic',305,3),
(319,2,'Classic',306,3),
(320,2,'Classic',307,3),
(321,2,'Classic',308,3),
(322,2,'Classic',309,3),
(323,2,'Classic',310,3),
(324,2,'Classic',311,3),
(325,2,'Doble',312,3),
(326,2,'Doble',313,3),
(327,2,'Doble',314,3),
(328,2,'Doble',315,3),
(329,2,'Doble',316,3),
(330,2,'Doble',317,3),
(331,2,'Doble',318,3),
(332,2,'Doble',319,3),
(333,2,'Doble',320,3),
(334,2,'Doble',321,3),
(335,2,'Doble',322,3),
(336,2,'Doble',323,3),
(337,2,'Doble',324,3),
(338,2,'Doble',325,3),
(339,2,'Premium',326,3),
(340,2,'Premium',327,3),
(341,2,'Premium',328,3),
(342,2,'Premium',329,3),
(343,2,'Premium',330,3),
(344,2,'Premium',331,3),
(345,2,'Premium',332,3),
(346,2,'Premium',333,3),
(347,2,'Premium',334,3),
(348,2,'Premium',335,3),
(349,2,'Premium',336,3),
(350,2,'Premium',337,3),
(351,2,'Premium',338,3),
(352,2,'Deluxe',339,3),
(353,2,'Deluxe',340,3),
(354,2,'Deluxe',341,3),
(355,2,'Deluxe',342,3),
(356,2,'Deluxe',343,3),
(357,2,'Deluxe',344,3),
(358,2,'Deluxe',345,3),
(359,2,'Deluxe',346,3),
(360,2,'Deluxe',347,3),
(361,2,'Deluxe',348,3),
(362,2,'Deluxe',349,3),
(363,2,'Deluxe',350,3),
(364,2,'Deluxe',351,3),
(365,2,'Classic',400,4),
(366,2,'Classic',401,4),
(367,2,'Classic',402,4),
(368,2,'Classic',403,4),
(369,2,'Classic',404,4),
(370,2,'Classic',405,4),
(371,2,'Classic',406,4),
(372,2,'Classic',407,4),
(373,2,'Classic',408,4),
(374,2,'Classic',409,4),
(375,2,'Classic',410,4),
(376,2,'Classic',411,4),
(377,2,'Doble',412,4),
(378,2,'Doble',413,4),
(379,2,'Doble',414,4),
(380,2,'Doble',415,4),
(381,2,'Doble',416,4),
(382,2,'Doble',417,4),
(383,2,'Doble',418,4),
(384,2,'Doble',419,4),
(385,2,'Doble',420,4),
(386,2,'Doble',421,4),
(387,2,'Doble',422,4),
(388,2,'Doble',423,4),
(389,2,'Doble',424,4),
(390,2,'Doble',425,4),
(391,2,'Premium',426,4),
(392,2,'Premium',427,4),
(393,2,'Premium',428,4),
(394,2,'Premium',429,4),
(395,2,'Premium',430,4),
(396,2,'Premium',431,4),
(397,2,'Premium',432,4),
(398,2,'Premium',433,4),
(399,2,'Premium',434,4),
(400,2,'Premium',435,4),
(401,2,'Premium',436,4),
(402,2,'Premium',437,4),
(403,2,'Premium',438,4),
(404,2,'Deluxe',439,4),
(405,2,'Deluxe',440,4),
(406,2,'Deluxe',441,4),
(407,2,'Deluxe',442,4),
(408,2,'Deluxe',443,4),
(409,2,'Deluxe',444,4),
(410,2,'Deluxe',445,4),
(411,2,'Deluxe',446,4),
(412,2,'Deluxe',447,4),
(413,2,'Deluxe',448,4),
(414,2,'Deluxe', 449,4),
(415,2,'Deluxe', 450,4),
(416,2,'Deluxe', 451,4),
;
/*!40000 ALTER TABLE `rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testimonial`
--

DROP TABLE IF EXISTS `testimonial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `testimonial` (
  `testimonio` varchar(800) NOT NULL,
  `name` varchar(40) NOT NULL,
  `location` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testimonial`
--

LOCK TABLES `testimonial` WRITE;
/*!40000 ALTER TABLE `testimonial` DISABLE KEYS */;
INSERT INTO `testimonial` VALUES ('Sin duda, una de las mejores experiencias hoteleras que he tenido! Desde que llegue al hotel, me senti como en casa. \nLa atencion del personal es excelente y las instalaciones sonde primer nivel. Sin duda, volveria a hospedarme en el Hotel Trivium.','Agustina Salerno','Bs-As, Argentina'),('¡Trivium fue una elección soñada! La estancia fue impecable de principio\na fin. La decoración es moderna y elegante, y cada rincón está pensado para el confort de los huéspedes.\nHonestamente lo super recomiendo','Maria Lopez','Mendoza, Argentina'),('Este hotel fue una experiencia maravillosa. Las habitaciones son cómodas, limpias\ny bien decoradas, y el personal siempre está dispuesto a ayudar con una sonrisa. La ubicación es ideal para\nexplorar la ciudad; ¡sin duda volvería a hospedarme aquí!','Elena Costas','Salta, Argentina');
/*!40000 ALTER TABLE `testimonial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_rooms`
--

DROP TABLE IF EXISTS `type_rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type_rooms` (
  `id_room` int DEFAULT NULL,
  `id_hotel` int DEFAULT NULL,
  `type_room` varchar(80) COLLATE utf8mb4_general_ci NOT NULL,
  `description` varchar(500) COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(120) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `price` float NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  KEY `id_hotel` (`id_hotel`),
  KEY `id_room` (`id_room`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type_rooms`
--

LOCK TABLES `type_rooms` WRITE;
/*!40000 ALTER TABLE `type_rooms` DISABLE KEYS */;
INSERT INTO `type_rooms` VALUES (100,1,'Classic','Habitación clásica con cama individual y baño privado.','images/habitacion_classic.jpg',500,'2024-11-25 22:22:42'),(113,1,'Doble','Habitación doble con dos camas individuales y baño privado.','images/habitacion_doble.jpg',750,'2024-11-25 22:22:42'),(126,1,'Premium','Habitación premium con cama doble, baño privado y balcón.','images/habitacion_premium.jpg',1000,'2024-11-25 22:22:42'),(139,1,'Deluxe','Habitación deluxe con dos camas dobles, baño privado, balcón y jacuzzi.','images/habitacion_deluxe.jpg',1250,'2024-11-25 22:22:42');
/*!40000 ALTER TABLE `type_rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id_user` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8mb4_general_ci NOT NULL,
  `lastname` varchar(80) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(80) COLLATE utf8mb4_general_ci NOT NULL,
  `dni` int NOT NULL,
  `phone` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `dni` (`dni`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'user','name','username@gmail.com','root',44555666,'1133334444','2024-11-27 09:55:09'),(12,'Inti','Blanco','intiblanco1@gmail.com','root',44522424,'1127967056','2024-11-27 11:32:30');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-29  8:27:19
