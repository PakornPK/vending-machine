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
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_categorie_id` int DEFAULT NULL,
  `name` varchar(45) NOT NULL,
  `unit_price` int NOT NULL,
  `path_img` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_categorie_id_idx` (`product_categorie_id`),
  CONSTRAINT `product_categorie_id` FOREIGN KEY (`product_categorie_id`) REFERENCES `product_categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,1,'นกพิราบผักกาดดองเค็มฝาดึง 230 กรัม',32,'https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12075425/51021628_P.jpg'),(2,1,'ซีเล็คทูน่าสเต็กในน้ำเกลือ 165 กรัม',49,'https://cpfmcdn.bygodigit.net/wp-content/uploads/2018/03/06112105/51009434_P.jpg'),(3,1,'อะยัมซาร์ดีนในซอสมะเขือเทศ 155 กรัม',36,'https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12075341/51011628_P.jpg'),(4,1,'ยูเอฟซี เงาะในน้ำเชื่อม 565 กรัม',82,'https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12075429/51021847_P.jpg'),(5,2,'เอ็ม-150 150 มิลลิลิตร',10,'https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222505/51010586_P.jpg'),(6,2,'สปอนเซอร์ 250 มิลลิลิตร',10,'https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222438/51008429_P.jpg'),(7,2,'ลิปตัน เลมอนขวด 445 มิลลิลิตร',20,'https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222756/51033939_P.jpg'),(8,2,'จับใจ สูตรจับเลี้ยง 500 มิลลิลิตร',15,'https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222141/51037887_P.jpg');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-01  1:28:15
