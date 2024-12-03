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
--

LOCK TABLES `rooms` WRITE;
/*!40000 ALTER TABLE `rooms` DISABLE KEYS */;
INSERT INTO `rooms` VALUES

(1,1,'Classic',100,1),(2,1,'Classic',101,1),(3,1,'Classic',102,1),(4,1,'Classic',103,1),(5,1,'Classic',104,1),(6,1,'Classic',105,1),(7,1,'Classic',106,1),(8,1,'Classic',107,1),(9,1,'Classic',108,1),(10,1,'Classic',109,1),(11,1,'Classic',110,1),(12,1,'Classic',111,1),(13,1,'Classic',112,1),(14,1,'Doble',113,1),(15,1,'Doble',114,1),(16,1,'Doble',115,1),(17,1,'Doble',116,1),(18,1,'Doble',117,1),(19,1,'Doble',118,1),(20,1,'Doble',119,1),(21,1,'Doble',120,1),(22,1,'Doble',121,1),(23,1,'Doble',122,1),(24,1,'Doble',123,1),(25,1,'Doble',124,1),(26,1,'Doble',125,1),(27,1,'Premium',126,1),(28,1,'Premium',127,1),(29,1,'Premium',128,1),(30,1,'Premium',129,1),(31,1,'Premium',130,1),(32,1,'Premium',131,1),(33,1,'Premium',132,1),(34,1,'Premium',133,1),(35,1,'Premium',134,1),(36,1,'Premium',135,1),(37,1,'Premium',136,1),(38,1,'Premium',137,1),(39,1,'Premium',138,1),(40,1,'Deluxe',139,1),(41,1,'Deluxe',140,1),(42,1,'Deluxe',141,1),(43,1,'Deluxe',142,1),(44,1,'Deluxe',143,1),(45,1,'Deluxe',144,1),(46,1,'Deluxe',145,1),(47,1,'Deluxe',146,1),(48,1,'Deluxe',147,1),(49,1,'Deluxe',148,1),(50,1,'Deluxe',149,1),(51,1,'Deluxe',150,1),(52,1,'Deluxe',151,1),(53,1,'Classic',200,2),(54,1,'Classic',201,2),(55,1,'Classic',202,2),(56,1,'Classic',203,2),(57,1,'Classic',204,2),(58,1,'Classic',205,2),(59,1,'Classic',206,2),(60,1,'Classic',207,2),(61,1,'Classic',208,2),(62,1,'Classic',209,2),(63,1,'Classic',210,2),(64,1,'Classic',211,2),(65,1,'Doble',212,2),(66,1,'Doble',213,2),(67,1,'Doble',214,2),(68,1,'Doble',215,2),(69,1,'Doble',216,2),(70,1,'Doble',217,2),(71,1,'Doble',218,2),(72,1,'Doble',219,2),(73,1,'Doble',220,2),(74,1,'Doble',221,2),(75,1,'Doble',222,2),(76,1,'Doble',223,2),(77,1,'Doble',224,2),(78,1,'Doble',225,2),(79,1,'Premium',226,2),(80,1,'Premium',227,2),(81,1,'Premium',228,2),(82,1,'Premium',229,2),(83,1,'Premium',230,2),(84,1,'Premium',231,2),(85,1,'Premium',232,2),(86,1,'Premium',233,2),(87,1,'Premium',234,2),(88,1,'Premium',235,2),(89,1,'Premium',236,2),(90,1,'Premium',237,2),(91,1,'Premium',238,2),(92,1,'Deluxe',239,2),(93,1,'Deluxe',240,2),(94,1,'Deluxe',241,2),(95,1,'Deluxe',242,2),(96,1,'Deluxe',243,2),(97,1,'Deluxe',244,2),(98,1,'Deluxe',245,2),(99,1,'Deluxe',246,2),(100,1,'Deluxe',247,2),(101,1,'Deluxe',248,2),(102,1,'Deluxe',249,2),(103,1,'Deluxe',250,2),(104,1,'Deluxe',251,2),(105,1,'Classic',300,3),(106,1,'Classic',301,3),(107,1,'Classic',302,3),(108,1,'Classic',303,3),(109,1,'Classic',304,3),(110,1,'Classic',305,3),(111,1,'Classic',306,3),(112,1,'Classic',307,3),(113,1,'Classic',308,3),(114,1,'Classic',309,3),(115,1,'Classic',310,3),(116,1,'Classic',311,3),(117,1,'Doble',312,3),(118,1,'Doble',313,3),(119,1,'Doble',314,3),(120,1,'Doble',315,3),(121,1,'Doble',316,3),(122,1,'Doble',317,3),(123,1,'Doble',318,3),(124,1,'Doble',319,3),(125,1,'Doble',320,3),(126,1,'Doble',321,3),(127,1,'Doble',322,3),(128,1,'Doble',323,3),(129,1,'Doble',324,3),(130,1,'Doble',325,3),(131,1,'Premium',326,3),(132,1,'Premium',327,3),(133,1,'Premium',328,3),(134,1,'Premium',329,3),(135,1,'Premium',330,3),(136,1,'Premium',331,3),(137,1,'Premium',332,3),(138,1,'Premium',333,3),(139,1,'Premium',334,3),(140,1,'Premium',335,3),(141,1,'Premium',336,3),(142,1,'Premium',337,3),(143,1,'Premium',338,3),(144,1,'Deluxe',339,3),(145,1,'Deluxe',340,3),(146,1,'Deluxe',341,3),(147,1,'Deluxe',342,3),(148,1,'Deluxe',343,3),(149,1,'Deluxe',344,3),(150,1,'Deluxe',345,3),(151,1,'Deluxe',346,3),(152,1,'Deluxe',347,3),(153,1,'Deluxe',348,3),(154,1,'Deluxe',349,3),(155,1,'Deluxe',350,3),(156,1,'Deluxe',351,3),(157,1,'Classic',400,4),(158,1,'Classic',401,4),(159,1,'Classic',402,4),(160,1,'Classic',403,4),(161,1,'Classic',404,4),(162,1,'Classic',405,4),(163,1,'Classic',406,4),(164,1,'Classic',407,4),(165,1,'Classic',408,4),(166,1,'Classic',409,4),(167,1,'Classic',410,4),(168,1,'Classic',411,4),(169,1,'Doble',412,4),(170,1,'Doble',413,4),(171,1,'Doble',414,4),(172,1,'Doble',415,4),(173,1,'Doble',416,4),(174,1,'Doble',417,4),(175,1,'Doble',418,4),(176,1,'Doble',419,4),(177,1,'Doble',420,4),(178,1,'Doble',421,4),(179,1,'Doble',422,4),(180,1,'Doble',423,4),(181,1,'Doble',424,4),(182,1,'Doble',425,4),(183,1,'Premium',426,4),(184,1,'Premium',427,4),(185,1,'Premium',428,4),(186,1,'Premium',429,4),(187,1,'Premium',430,4),(188,1,'Premium',431,4),(189,1,'Premium',432,4),(190,1,'Premium',433,4),(191,1,'Premium',434,4),(192,1,'Premium',435,4),(193,1,'Premium',436,4),(194,1,'Premium',437,4),(195,1,'Premium',438,4),(196,1,'Deluxe',439,4),(197,1,'Deluxe',440,4),(198,1,'Deluxe',441,4),(199,1,'Deluxe',442,4),(200,1,'Deluxe',443,4),(201,1,'Deluxe',444,4),(202,1,'Deluxe',445,4),(203,1,'Deluxe',446,4),(204,1,'Deluxe',447,4),(205,1,'Deluxe',448,4),(206,1,'Deluxe',449,4),(207,1,'Deluxe',450,4),(208,1,'Deluxe',451,4),(1,1,'Classic',100,1),

(209,2,'Classic',100,1),(210,2,'Classic',101,1),(211,2,'Classic',102,1),(211,2,'Classic',102,1),(212,2,'Classic',103,1),(213,2,'Classic',104,1),(214,2,'Classic',105,1),(215,2,'Classic',106,1),(216,2,'Classic',107,1),(217,2,'Classic',108,1),(218,2,'Classic',109,1),(219,2,'Classic',110,1),(220,2,'Classic',111,1),(221,2,'Classic',112,1),(222,2,'Doble',113,1),(223,2,'Doble',114,1),(224,2,'Doble',115,1),(225,2,'Doble',116,1),(226,2,'Doble',117,1),(227,2,'Doble',118,1),(228,2,'Doble',119,1),(229,2,'Doble',120,1),(230,2,'Doble',121,1),(231,2,'Doble',122,1),(232,2,'Doble',123,1),(233,2,'Doble',124,1),(234,2,'Doble',125,1),(235,2,'Premium',126,1),(236,2,'Premium',127,1),(237,2,'Premium',128,1),(238,2,'Premium',129,1),(239,2,'Premium',130,1),(240,2,'Premium',131,1),(241,2,'Premium',132,1),(242,2,'Premium',133,1),(243,2,'Premium',134,1),(244,2,'Premium',135,1),(245,2,'Premium',136,1),(246,2,'Premium',137,1),(247,2,'Premium',138,1),(248,2,'Deluxe',139,1),(249,2,'Deluxe',140,1),(250,2,'Deluxe',141,1),(251,2,'Deluxe',142,1),(252,2,'Deluxe',143,1),(253,2,'Deluxe',144,1),(254,2,'Deluxe',145,1),(255,2,'Deluxe',146,1),(256,2,'Deluxe',147,1),(257,2,'Deluxe',148,1),(258,2,'Deluxe',149,1),(259,2,'Deluxe',150,1),(260,2,'Deluxe',151,1),(261,2,'Classic',200,2),(262,2,'Classic',201,2),(263,2,'Classic',202,2),(264,2,'Classic',203,2),(265,2,'Classic',204,2),(266,2,'Classic',205,2),(267,2,'Classic',206,2),(268,2,'Classic',207,2),(269,2,'Classic',208,2),(270,2,'Classic',209,2),(271,2,'Classic',210,2),(272,2,'Classic',211,2),(273,2,'Doble',212,2),(274,2,'Doble',213,2),(275,2,'Doble',214,2),(276,2,'Doble',215,2),(277,2,'Doble',216,2),(278,2,'Doble',217,2),(279,2,'Doble',218,2),(280,2,'Doble',219,2),(281,2,'Doble',220,2),(282,2,'Doble',221,2),(283,2,'Doble',222,2),(284,2,'Doble',223,2),(285,2,'Doble',224,2),(286,2,'Doble',225,2),(287,2,'Premium',226,2),(288,2,'Premium',227,2),(289,2,'Premium',228,2),(290,2,'Premium',229,2),(291,2,'Premium',230,2),(292,2,'Premium',231,2),(293,2,'Premium',232,2),(294,2,'Premium',233,2),(295,2,'Premium',234,2),(296,2,'Premium',235,2),(297,2,'Premium',236,2),(298,2,'Premium',237,2),(299,2,'Premium',238,2),(300,2,'Deluxe',239,2),(301,2,'Deluxe',240,2),(302,2,'Deluxe',241,2),(303,2,'Deluxe',242,2),(304,2,'Deluxe',243,2),(305,2,'Deluxe',244,2),(306,2,'Deluxe',245,2),(307,2,'Deluxe',246,2),(308,2,'Deluxe',247,2),(309,2,'Deluxe',248,2),(310,2,'Deluxe',249,2),(311,2,'Deluxe',250,2),(312,2,'Deluxe',251,2),(313,2,'Classic',300,3),(314,2,'Classic',301,3),(315,2,'Classic',302,3),(316,2,'Classic',303,3),(317,2,'Classic',304,3),(318,2,'Classic',305,3),(319,2,'Classic',306,3),(320,2,'Classic',307,3),(321,2,'Classic',308,3),(322,2,'Classic',309,3),(323,2,'Classic',310,3),(324,2,'Classic',311,3),(325,2,'Doble',312,3),(326,2,'Doble',313,3),(327,2,'Doble',314,3),(328,2,'Doble',315,3),(329,2,'Doble',316,3),(330,2,'Doble',317,3),(331,2,'Doble',318,3),(332,2,'Doble',319,3),(333,2,'Doble',320,3),(334,2,'Doble',321,3),(335,2,'Doble',322,3),(336,2,'Doble',323,3),(337,2,'Doble',324,3),(338,2,'Doble',325,3),(339,2,'Premium',326,3),(340,2,'Premium',327,3),(341,2,'Premium',328,3),(342,2,'Premium',329,3),(343,2,'Premium',330,3),(344,2,'Premium',331,3),(345,2,'Premium',332,3),(346,2,'Premium',333,3),(347,2,'Premium',334,3),(348,2,'Premium',335,3),(349,2,'Premium',336,3),(350,2,'Premium',337,3),(351,2,'Premium',338,3),(352,2,'Deluxe',339,3),(353,2,'Deluxe',340,3),(354,2,'Deluxe',341,3),(355,2,'Deluxe',342,3),(356,2,'Deluxe',343,3),(357,2,'Deluxe',344,3),(358,2,'Deluxe',345,3),(359,2,'Deluxe',346,3),(360,2,'Deluxe',347,3),(361,2,'Deluxe',348,3),(362,2,'Deluxe',349,3),(363,2,'Deluxe',350,3),(364,2,'Deluxe',351,3),(365,2,'Classic',400,4),(366,2,'Classic',401,4),(367,2,'Classic',402,4),(368,2,'Classic',403,4),(369,2,'Classic',404,4),(370,2,'Classic',405,4),(371,2,'Classic',406,4),(372,2,'Classic',407,4),(373,2,'Classic',408,4),(374,2,'Classic',409,4),(375,2,'Classic',410,4),(376,2,'Classic',411,4),(377,2,'Doble',412,4),(378,2,'Doble',413,4),(379,2,'Doble',414,4),(380,2,'Doble',415,4),(381,2,'Doble',416,4),(382,2,'Doble',417,4),(383,2,'Doble',418,4),(384,2,'Doble',419,4),(385,2,'Doble',420,4),(386,2,'Doble',421,4),(387,2,'Doble',422,4),(388,2,'Doble',423,4),(389,2,'Doble',424,4),(390,2,'Doble',425,4),(391,2,'Premium',426,4),(392,2,'Premium',427,4),(393,2,'Premium',428,4),(394,2,'Premium',429,4),(395,2,'Premium',430,4),(396,2,'Premium',431,4),(397,2,'Premium',432,4),(398,2,'Premium',433,4),(399,2,'Premium',434,4),(400,2,'Premium',435,4),(401,2,'Premium',436,4),(402,2,'Premium',437,4),(403,2,'Premium',438,4),(404,2,'Deluxe',439,4),(405,2,'Deluxe',440,4),(406,2,'Deluxe',441,4),(407,2,'Deluxe',442,4),(408,2,'Deluxe',443,4),(409,2,'Deluxe',444,4),(410,2,'Deluxe',445,4),(411,2,'Deluxe',446,4),(412,2,'Deluxe',447,4),(413,2,'Deluxe',448,4),(414,2,'Deluxe',449,4),(415,2,'Deluxe',450,4),(416,2,'Deluxe',451,4),

(417,3,'Classic',100,1),(418,3,'Classic',101,1),(419,3,'Classic',102,1),(420,3,'Classic',103,1),(421,3,'Classic',104,1),(422,3,'Classic',105,1),(423,3,'Classic',106,1),(424,3,'Classic',107,1),(425,3,'Classic',108,1),(426,3,'Classic',109,1),(427,3,'Classic',110,1),(428,3,'Classic',111,1),(429,3,'Classic',112,1),(430,3,'Doble',113,1),(431,3,'Doble',114,1),(432,3,'Doble',115,1),(433,3,'Doble',116,1),(434,3,'Doble',117,1),(435,3,'Doble',118,1),(436,3,'Doble',119,1),(437,3,'Doble',120,1),(438,3,'Doble',121,1),(439,3,'Doble',122,1),(440,3,'Doble',123,1),(441,3,'Doble',124,1),(442,3,'Doble',125,1),(443,3,'Premium',126,1),(444,3,'Premium',127,1),(445,3,'Premium',128,1),(446,3,'Premium',129,1),(447,3,'Premium',130,1),(448,3,'Premium',131,1),(449,3,'Premium',132,1),(450,3,'Premium',133,1),(451,3,'Premium',134,1),(452,3,'Premium',135,1),(453,3,'Premium',136,1),(454,3,'Premium',137,1),(455,3,'Premium',138,1),(456,3,'Deluxe',139,1),(457,3,'Deluxe',140,1),(458,3,'Deluxe',141,1),(459,3,'Deluxe',142,1),(460,3,'Deluxe',143,1),(461,3,'Deluxe',144,1),(462,3,'Deluxe',145,1),(463,3,'Deluxe',146,1),(464,3,'Deluxe',147,1),(465,3,'Deluxe',148,1),(466,3,'Deluxe',149,1),(467,3,'Deluxe',150,1),(468,3,'Deluxe',151,1),(469,3,'Classic',200,2),(470,3,'Classic',201,2),(471,3,'Classic',202,2),(472,3,'Classic',203,2),(473,3,'Classic',204,2),(474,3,'Classic',205,2),(475,3,'Classic',206,2),(476,3,'Classic',207,2),(477,3,'Classic',208,2),(478,3,'Classic',209,2),(479,3,'Classic',210,2),(480,3,'Classic',211,2),(481,3,'Doble',212,2),(482,3,'Doble',213,2),(483,3,'Doble',214,2),(484,3,'Doble',215,2),(485,3,'Doble',216,2),(486,3,'Doble',217,2),(487,3,'Doble',218,2),(488,3,'Doble',219,2),(489,3,'Doble',220,2),(490,3,'Doble',221,2),(491,3,'Doble',222,2),(492,3,'Doble',223,2),(493,3,'Doble',224,2),(494,3,'Doble',225,2),(495,3,'Premium',226,2),(496,3,'Premium',227,2),(497,3,'Premium',228,2),(498,3,'Premium',229,2),(499,3,'Premium',230,2),(500,3,'Premium',231,2),(501,3,'Premium',232,2),(502,3,'Premium',233,2),(503,3,'Premium',234,2),(504,3,'Premium',235,2),(505,3,'Premium',236,2),(506,3,'Premium',237,2),(507,3,'Premium',238,2),(508,3,'Deluxe',239,2),(509,3,'Deluxe',240,2),(510,3,'Deluxe',241,2),(511,3,'Deluxe',242,2),(512,3,'Deluxe',243,2),(513,3,'Deluxe',244,2),(514,3,'Deluxe',245,2),(515,3,'Deluxe',246,2),(516,3,'Deluxe',247,2),(517,3,'Deluxe',248,2),(518,3,'Deluxe',249,2),(519,3,'Deluxe',250,2),(520,3,'Deluxe',251,2),(521,3,'Classic',300,3),(522,3,'Classic',301,3),(523,3,'Classic',302,3),(524,3,'Classic',303,3),(525,3,'Classic',304,3),(526,3,'Classic',305,3),(527,3,'Classic',306,3),(528,3,'Classic',307,3),(529,3,'Classic',308,3),(530,3,'Classic',309,3),(531,3,'Classic',310,3),(532,3,'Classic',311,3),(533,3,'Doble',312,3),(534,3,'Doble',313,3),(535,3,'Doble',314,3),(536,3,'Doble',315,3),(537,3,'Doble',316,3),(538,3,'Doble',317,3),(539,3,'Doble',318,3),(540,3,'Doble',319,3),(541,3,'Doble',320,3),(542,3,'Doble',321,3),(543,3,'Doble',322,3),(544,3,'Doble',323,3),(545,3,'Doble',324,3),(546,3,'Doble',325,3),(547,3,'Premium',326,3),(548,3,'Premium',327,3),(549,3,'Premium',328,3),(550,3,'Premium',329,3),(551,3,'Premium',330,3),(552,3,'Premium',331,3),(553,3,'Premium',332,3),(554,3,'Premium',333,3),(555,3,'Premium',334,3),(556,3,'Premium',335,3),(557,3,'Premium',336,3),(558,3,'Premium',337,3),(559,3,'Premium',338,3),(560,3,'Deluxe',339,3),(561,3,'Deluxe',340,3),(562,3,'Deluxe',341,3),(563,3,'Deluxe',342,3),(564,3,'Deluxe',343,3),(565,3,'Deluxe',344,3),(566,3,'Deluxe',345,3),(567,3,'Deluxe',346,3),(568,3,'Deluxe',347,3),(569,3,'Deluxe',348,3),(570,3,'Deluxe',349,3),(571,3,'Deluxe',350,3),(572,3,'Deluxe',351,3),(573,3,'Classic',400,4),(574,3,'Classic',401,4),(575,3,'Classic',402,4),(576,3,'Classic',403,4),(577,3,'Classic',404,4),(578,3,'Classic',405,4),(579,3,'Classic',406,4),(580,3,'Classic',407,4),(581,3,'Classic',408,4),(582,3,'Classic',409,4),(583,3,'Classic',410,4),(584,3,'Classic',411,4),(585,3,'Doble',412,4),(586,3,'Doble',413,4),(587,3,'Doble',414,4),(588,3,'Doble',415,4),(589,3,'Doble',416,4),(590,3,'Doble',417,4),(591,3,'Doble',418,4),(592,3,'Doble',419,4),(593,3,'Doble',420,4),(594,3,'Doble',421,4),(595,3,'Doble',422,4),(596,3,'Doble',423,4),(597,3,'Doble',424,4),(598,3,'Doble',425,4),(599,3,'Premium',426,4),(600,3,'Premium',427,4),(601,3,'Premium',428,4),(602,3,'Premium',429,4),(603,3,'Premium',430,4),(604,3,'Premium',431,4),(605,3,'Premium',432,4),(606,3,'Premium',433,4),(607,3,'Premium',434,4),(608,3,'Premium',435,4),(609,3,'Premium',436,4),(610,3,'Premium',437,4),(611,3,'Premium',438,4),(612,3,'Deluxe',439,4),(613,3,'Deluxe',440,4),(614,3,'Deluxe',441,4),(615,3,'Deluxe',442,4),(616,3,'Deluxe',443,4),(617,3,'Deluxe',444,4),(618,3,'Deluxe',445,4),(619,3,'Deluxe',446,4),(620,3,'Deluxe',447,4),(621,3,'Deluxe',448,4),(622,3,'Deluxe',449,4),(623,3,'Deluxe',450,4),(624,3,'Deluxe',451,4),

(625,4,'Classic',100,1),(626,4,'Classic',101,1),(627,4,'Classic',102,1),(628,4,'Classic',103,1),(629,4,'Classic',104,1),(630,4,'Classic',105,1),(631,4,'Classic',106,1),(632,4,'Classic',107,1),(633,4,'Classic',108,1),(634,4,'Classic',109,1),(635,4,'Classic',110,1),(636,4,'Classic',111,1),(637,4,'Classic',112,1),(638,4,'Doble',113,1),(639,4,'Doble',114,1),(640,4,'Doble',115,1),(641,4,'Doble',116,1),(642,4,'Doble',117,1),(643,4,'Doble',118,1),(644,4,'Doble',119,1),(645,4,'Doble',120,1),(646,4,'Doble',121,1),(647,4,'Doble',122,1),(648,4,'Doble',123,1),(649,4,'Doble',124,1),(650,4,'Doble',125,1),(651,4,'Premium',126,1),(652,4,'Premium',127,1),(653,4,'Premium',128,1),(654,4,'Premium',129,1),(655,4,'Premium',130,1),(656,4,'Premium',131,1),(657,4,'Premium',132,1),(658,4,'Premium',133,1),(659,4,'Premium',134,1),(660,4,'Premium',135,1),(661,4,'Premium',136,1),(662,4,'Premium',137,1),(663,4,'Premium',138,1),(664,4,'Deluxe',139,1),(665,4,'Deluxe',140,1),(666,4,'Deluxe',141,1),(667,4,'Deluxe',142,1),(668,4,'Deluxe',143,1),(669,4,'Deluxe',144,1),(670,4,'Deluxe',145,1),(671,4,'Deluxe',146,1),(672,4,'Deluxe',147,1),(673,4,'Deluxe',148,1),(674,4,'Deluxe',149,1),(675,4,'Deluxe',150,1),(676,4,'Deluxe',151,1),(677,4,'Classic',200,2),(678,4,'Classic',201,2),(679,4,'Classic',202,2),(680,4,'Classic',203,2),(681,4,'Classic',204,2),(682,4,'Classic',205,2),(683,4,'Classic',206,2),(684,4,'Classic',207,2),(685,4,'Classic',208,2),(686,4,'Classic',209,2),(687,4,'Classic',210,2),(688,4,'Classic',211,2),(689,4,'Doble',212,2),(690,4,'Doble',213,2),(691,4,'Doble',214,2),(692,4,'Doble',215,2),(693,4,'Doble',216,2),(694,4,'Doble',217,2),(695,4,'Doble',218,2),(696,4,'Doble',219,2),(697,4,'Doble',220,2),(698,4,'Doble',221,2),(699,4,'Doble',222,2),(700,4,'Doble',223,2),(701,4,'Doble',224,2),(702,4,'Doble',225,2),(703,4,'Premium',226,2),(704,4,'Premium',227,2),(705,4,'Premium',228,2),(706,4,'Premium',229,2),(707,4,'Premium',230,2),(708,4,'Premium',231,2),(709,4,'Premium',232,2),(710,4,'Premium',233,2),(711,4,'Premium',234,2),(712,4,'Premium',235,2),(713,4,'Premium',236,2),(714,4,'Premium',237,2),(715,4,'Premium',238,2),(716,4,'Deluxe',239,2),(717,4,'Deluxe',240,2),(718,4,'Deluxe',241,2),(719,4,'Deluxe',242,2),(720,4,'Deluxe',243,2),(721,4,'Deluxe',244,2),(722,4,'Deluxe',245,2),(723,4,'Deluxe',246,2),(724,4,'Deluxe',247,2),(725,4,'Deluxe',248,2),(726,4,'Deluxe',249,2),(727,4,'Deluxe',250,2),(728,4,'Deluxe',251,2),(729,4,'Classic',300,3),(730,4,'Classic',301,3),(731,4,'Classic',302,3),(732,4,'Classic',303,3),(733,4,'Classic',304,3),(734,4,'Classic',305,3),(735,4,'Classic',306,3),(736,4,'Classic',307,3),(737,4,'Classic',308,3),(738,4,'Classic',309,3),(739,4,'Classic',310,3),(740,4,'Classic',311,3),(741,4,'Doble',312,3),(742,4,'Doble',313,3),(743,4,'Doble',314,3),(744,4,'Doble',315,3),(745,4,'Doble',316,3),(746,4,'Doble',317,3),(747,4,'Doble',318,3),(748,4,'Doble',319,3),(749,4,'Doble',320,3),(750,4,'Doble',321,3),(751,4,'Doble',322,3),(752,4,'Doble',323,3),(753,4,'Doble',324,3),(754,4,'Doble',325,3),(755,4,'Premium',326,3),(756,4,'Premium',327,3),(757,4,'Premium',328,3),(758,4,'Premium',329,3),(759,4,'Premium',330,3),(760,4,'Premium',331,3),(761,4,'Premium',332,3),(762,4,'Premium',333,3),(763,4,'Premium',334,3),(764,4,'Premium',335,3),(765,4,'Premium',336,3),(766,4,'Premium',337,3),(767,4,'Premium',338,3),(768,4,'Deluxe',339,3),(769,4,'Deluxe',340,3),(770,4,'Deluxe',341,3),(771,4,'Deluxe',342,3),(772,4,'Deluxe',343,3),(773,4,'Deluxe',344,3),(774,4,'Deluxe',345,3),(775,4,'Deluxe',346,3),(776,4,'Deluxe',347,3),(777,4,'Deluxe',348,3),(778,4,'Deluxe',349,3),(779,4,'Deluxe',350,3),(780,4,'Deluxe',351,3),(781,4,'Classic',400,4),(782,4,'Classic',401,4),(783,4,'Classic',402,4),(784,4,'Classic',403,4),(785,4,'Classic',404,4),(786,4,'Classic',405,4),(787,4,'Classic',406,4),(788,4,'Classic',407,4),(789,4,'Classic',408,4),(790,4,'Classic',409,4),(791,4,'Classic',410,4),(792,4,'Classic',411,4),(793,4,'Doble',412,4),(794,4,'Doble',413,4),(795,4,'Doble',414,4),(796,4,'Doble',415,4),(797,4,'Doble',416,4),(798,4,'Doble',417,4),(799,4,'Doble',418,4),(800,4,'Doble',419,4),(801,4,'Doble',420,4),(802,4,'Doble',421,4),(803,4,'Doble',422,4),(804,4,'Doble',423,4),(805,4,'Doble',424,4),(806,4,'Doble',425,4),(807,4,'Premium',426,4),(808,4,'Premium',427,4),(809,4,'Premium',428,4),(810,4,'Premium',429,4),(811,4,'Premium',430,4),(812,4,'Premium',431,4),(813,4,'Premium',432,4),(814,4,'Premium',433,4),(815,4,'Premium',434,4),(816,4,'Premium',435,4),(817,4,'Premium',436,4),(818,4,'Premium',437,4),(819,4,'Premium',438,4),(819,4,'Premium',438,4),(820,4,'Deluxe',439,4),(821,4,'Deluxe',440,4),(822,4,'Deluxe',441,4),(823,4,'Deluxe',442,4),(824,4,'Deluxe',443,4),(825,4,'Deluxe',444,4),(826,4,'Deluxe',445,4),(827,4,'Deluxe',446,4),(828,4,'Deluxe',447,4),(829,4,'Deluxe',448,4),(830,4,'Deluxe',449,4),(831,4,'Deluxe',450,4),(832,4,'Deluxe',451,4),

(833,5,'Classic',100,1),(834,5,'Classic',101,1),(835,5,'Classic',102,1),(836,5,'Classic',103,1),(837,5,'Classic',104,1),(838,5,'Classic',105,1),(839,5,'Classic',106,1),(840,5,'Classic',107,1),(841,5,'Classic',108,1),(842,5,'Classic',109,1),(843,5,'Classic',110,1),(844,5,'Classic',111,1),(845,5,'Classic',112,1),(846,5,'Doble',113,1),(847,5,'Doble',114,1),(848,5,'Doble',115,1),(849,5,'Doble',116,1),(850,5,'Doble',117,1),(851,5,'Doble',118,1),(852,5,'Doble',119,1),(853,5,'Doble',120,1),(854,5,'Doble',121,1),(855,5,'Doble',122,1),(856,5,'Doble',123,1),(857,5,'Doble',124,1),(858,5,'Doble',125,1),(859,5,'Premium',126,1),(860,5,'Premium',127,1),(861,5,'Premium',128,1),(862,5,'Premium',129,1),(863,5,'Premium',130,1),(864,5,'Premium',131,1),(865,5,'Premium',132,1),(866,5,'Premium',133,1),(867,5,'Premium',134,1),(868,5,'Premium',135,1),(869,5,'Premium',136,1),(870,5,'Premium',137,1),(871,5,'Premium',138,1),(872,5,'Deluxe',139,1),(873,5,'Deluxe',140,1),(874,5,'Deluxe',141,1),(875,5,'Deluxe',142,1),(876,5,'Deluxe',143,1),(877,5,'Deluxe',144,1),(878,5,'Deluxe',145,1),(879,5,'Deluxe',146,1),(880,5,'Deluxe',147,1),(881,5,'Deluxe',148,1),(882,5,'Deluxe',149,1),(883,5,'Deluxe',150,1),(884,5,'Deluxe',151,1),(885,5,'Classic',200,2),(886,5,'Classic',201,2),(887,5,'Classic',202,2),(888,5,'Classic',203,2),(889,5,'Classic',204,2),(890,5,'Classic',205,2),(891,5,'Classic',206,2),(892,5,'Classic',207,2),(893,5,'Classic',208,2),(894,5,'Classic',209,2),(895,5,'Classic',210,2),(896,5,'Classic',211,2),(897,5,'Doble',212,2),(898,5,'Doble',213,2),(899,5,'Doble',214,2),(900,5,'Doble',215,2),(901,5,'Doble',216,2),(902,5,'Doble',217,2),(903,5,'Doble',218,2),(904,5,'Doble',219,2),(905,5,'Doble',220,2),(906,5,'Doble',221,2),(907,5,'Doble',222,2),(908,5,'Doble',223,2),(909,5,'Doble',224,2),(910,5,'Doble',225,2),(911,5,'Premium',226,2),(912,5,'Premium',227,2),(913,5,'Premium',228,2),(914,5,'Premium',229,2),(915,5,'Premium',230,2),(916,5,'Premium',231,2),(917,5,'Premium',232,2),(918,5,'Premium',233,2),(919,5,'Premium',234,2),(920,5,'Premium',235,2),(921,5,'Premium',236,2),(922,5,'Premium',237,2),(923,5,'Premium',238,2),(924,5,'Deluxe',239,2),(925,5,'Deluxe',240,2),(926,5,'Deluxe',241,2),(927,5,'Deluxe',242,2),(928,5,'Deluxe',243,2),(929,5,'Deluxe',244,2),(930,5,'Deluxe',245,2),(931,5,'Deluxe',246,2),(932,5,'Deluxe',247,2),(933,5,'Deluxe',248,2),(934,5,'Deluxe',249,2),(935,5,'Deluxe',250,2),(936,5,'Deluxe',251,2),(937,5,'Classic',300,3),(938,5,'Classic',301,3),(939,5,'Classic',302,3),(940,5,'Classic',303,3),(941,5,'Classic',304,3),(942,5,'Classic',305,3),(943,5,'Classic',306,3),(944,5,'Classic',307,3),(945,5,'Classic',308,3),(946,5,'Classic',309,3),(947,5,'Classic',310,3),(948,5,'Classic',311,3),(949,5,'Doble',312,3),(950,5,'Doble',313,3),(951,5,'Doble',314,3),(952,5,'Doble',315,3),(953,5,'Doble',316,3),(954,5,'Doble',317,3),(955,5,'Doble',318,3),(956,5,'Doble',319,3),(957,5,'Doble',320,3),(958,5,'Doble',321,3),(959,5,'Doble',322,3),(960,5,'Doble',323,3),(961,5,'Doble',324,3),(962,5,'Doble',325,3),(963,5,'Premium',326,3),(964,5,'Premium',327,3),(965,5,'Premium',328,3),(966,5,'Premium',329,3),(967,5,'Premium',330,3),(968,5,'Premium',331,3),(969,5,'Premium',332,3),(970,5,'Premium',333,3),(971,5,'Premium',334,3),(972,5,'Premium',335,3),(973,5,'Premium',336,3),(974,5,'Premium',337,3),(975,5,'Premium',338,3),(976,5,'Deluxe',339,3),(977,5,'Deluxe',340,3),(978,5,'Deluxe',341,3),(979,5,'Deluxe',342,3),(980,5,'Deluxe',343,3),(981,5,'Deluxe',344,3),(982,5,'Deluxe',345,3),(983,5,'Deluxe',346,3),(984,5,'Deluxe',347,3),(985,5,'Deluxe',348,3),(986,5,'Deluxe',349,3),(987,5,'Deluxe',350,3),(988,5,'Deluxe',351,3),(989,5,'Classic',400,4),(990,5,'Classic',401,4),(991,5,'Classic',402,4),(992,5,'Classic',403,4),(993,5,'Classic',404,4),(994,5,'Classic',405,4),(995,5,'Classic',406,4),(996,5,'Classic',407,4),(997,5,'Classic',408,4),(998,5,'Classic',409,4),(999,5,'Classic',410,4),(1000,5,'Classic',411,4),(1001,5,'Doble',412,4),(1002,5,'Doble',413,4),(1003,5,'Doble',414,4),(1004,5,'Doble',415,4),(1005,5,'Doble',416,4),(1006,5,'Doble',417,4),(1007,5,'Doble',418,4),(1008,5,'Doble',419,4),(1009,5,'Doble',420,4),(1010,5,'Doble',421,4),(1011,5,'Doble',422,4),(1012,5,'Doble',423,4),(1013,5,'Doble',424,4),(1014,5,'Doble',425,4),(1015,5,'Premium',426,4),(1016,5,'Premium',427,4),(1017,5,'Premium',428,4),(1018,5,'Premium',429,4),(1019,5,'Premium',430,4),(1020,5,'Premium',431,4),(1021,5,'Premium',432,4),(1022,5,'Premium',433,4),(1023,5,'Premium',434,4),(1024,5,'Premium',435,4),(1025,5,'Premium',436,4),(1026,5,'Premium',437,4),(1027,5,'Premium',438,4),(1028,5,'Deluxe',439,4),(1029,5,'Deluxe',440,4),(1030,5,'Deluxe',441,4),(1031,5,'Deluxe',442,4),(1032,5,'Deluxe',443,4),(1033,5,'Deluxe',444,4),(1034,5,'Deluxe',445,4),(1035,5,'Deluxe',446,4),(1036,5,'Deluxe',447,4),(1037,5,'Deluxe',448,4),(1038,5,'Deluxe',449,4),(1039,5,'Deluxe',450,4),(1040,5,'Deluxe',451,4);
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

CREATE TABLE `services` (
  `id_service` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_service`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Insertar algunos servicios
INSERT INTO `services` (`name`, `description`, `price`) VALUES
('Spa', 'Acceso al spa con todos los servicios incluidos', 120),
('Masajes', 'Masajes relajantes de 1 hora', 50),
('Desayuno', 'Desayuno buffet incluido', 30),
('Cena Gourmet', 'Cena de lujo en nuestro restaurante principal', 70),
('Cata de Vinos', 'Degustacion de vinos con sommelier profesional', 50),
('Clases de Yoga', 'Sesion de yoga de 1 hora con instructor profesional', 20),
('Guía Turístico', 'Servicios de guía turístico para excursiones locales', 50.00),
('Gimnasio', 'Acceso al gimnasio 24/7', 15),
('Servicio de Lavandería', 'Servicios de lavandería y planchado', 15.00),
('Transporte Aeropuerto', 'Servicio de transporte desde y hacia el aeropuerto', 50),
('Limpieza de Habitación', 'Servicio diario de limpieza y mantenimiento de la habitación', 10.00);

-- Creación de la tabla `reservation_services` para vincular reservas y servicios
CREATE TABLE `reservation_services` (
  `id_reservation` int(11) NOT NULL,
  `id_service` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_reservation`, `id_service`),
  FOREIGN KEY (`id_reservation`) REFERENCES `reservations` (`id_reservation`),
  FOREIGN KEY (`id_service`) REFERENCES `services` (`id_service`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Insertar algunos servicios en reservas
INSERT INTO `reservation_services` (`id_reservation`, `id_service`) VALUES
(1, 1),
(1, 2);
