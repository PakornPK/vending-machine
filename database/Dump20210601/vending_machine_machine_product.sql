-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: vending_machine
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `machine_product`
--

DROP TABLE IF EXISTS `machine_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `machine_product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `machine_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `product_qty` int DEFAULT NULL,
  `reload` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mp_m_id_idx` (`machine_id`),
  KEY `mp_p_id_idx` (`product_id`),
  CONSTRAINT `mp_m_id` FOREIGN KEY (`machine_id`) REFERENCES `machines` (`id`),
  CONSTRAINT `mp_p_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `machine_product`
--

LOCK TABLES `machine_product` WRITE;
/*!40000 ALTER TABLE `machine_product` DISABLE KEYS */;
INSERT INTO `machine_product` VALUES (1,1,1,20,0),(2,1,2,20,0),(3,1,3,20,0),(4,1,4,20,0),(5,1,5,20,0),(6,1,6,20,0),(7,1,7,20,0),(8,1,8,20,0),(9,2,1,20,0),(10,2,2,20,0),(11,2,3,20,0),(12,2,4,20,0),(13,2,5,20,0),(14,2,6,20,0),(15,2,7,20,0),(16,2,8,20,0),(17,3,1,20,0),(18,3,2,20,0),(19,3,3,19,0),(20,3,4,20,0),(21,3,5,20,0),(22,3,6,20,0),(23,3,7,20,0),(24,3,8,20,0);
/*!40000 ALTER TABLE `machine_product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-01  1:28:14
