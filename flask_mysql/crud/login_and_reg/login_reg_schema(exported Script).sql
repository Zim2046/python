CREATE DATABASE  IF NOT EXISTS `login_reg_schema` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `login_reg_schema`;
-- MySQL dump 10.13  Distrib 8.0.28, for macos11 (x86_64)
--
-- Host: localhost    Database: login_reg_schema
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'John','Doe','JD@gmail.com','$2b$12$krh/rWLbC2mjx2j1Wlt/ruw1z5ZMCfvZqlqCai7R7LbRptSVYT/6a','2022-03-23 23:15:35','2022-03-23 23:15:35'),(3,'Richard','Feynman','RF@email.com','$2b$12$dL3qSX5CU0sxUcIiKU2YKesMPyeZ7FJeiKKJIosMqWMnghCJDXUTu','2022-03-23 23:21:51','2022-03-23 23:21:51'),(4,'Albert','Einstein','eismc2@caltech.edu','$2b$12$VmdnTnH5EAgahyykTr462OzgMInmwPrRd13kc6g6E0PneYMORfXOO','2022-03-23 23:25:14','2022-03-23 23:25:14'),(5,'Wernher','von Braun','OG@nasa.gov','$2b$12$uh6/NBFP02Sf1NA31BC1s.j6gGf4wdYKowIYPSTtKr2h3rhOvf/..','2022-03-23 23:27:42','2022-03-23 23:27:42'),(6,'Wolfgang','Gustav','WG@caltech.edu','$2b$12$oYr82ZFxVpHNxCdm0Spb5.GD1D3gi1/G.dvBRIPvdCP9AJLKQfV3G','2022-03-23 23:29:55','2022-03-23 23:29:55'),(7,'Theodore','von Kármán','vortex@gmail.com','$2b$12$IXOXgSocCneWKn4AHSi2aOQytW06hnufV8aQjqBcCHkphjbjCGKIy','2022-03-23 23:31:05','2022-03-23 23:31:05'),(8,'Jane','Doe','JaneD@email.com','$2b$12$.HkLxiK5Y.cqa5HllH3unedTZTquMz3TFQRyliBE5Ww7BnBOtjk22','2022-03-24 09:21:05','2022-03-24 09:21:05'),(9,'1234','Doe','asdf@gmail.com','$2b$12$cDBU.ifHf5b8DWOSrYI2NeHqjIObKjjjfivLNBI0HCLL5fox9DbX6','2022-03-24 09:46:04','2022-03-24 09:46:04'),(10,'John','Doe','JD@gmail.com','$2b$12$R0FeDqNWzUEEKeNWoy0xmuGjkvb8JKl/9xfOLjyosTPNQNYRPlKny','2022-03-24 10:40:06','2022-03-24 10:40:06');
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

-- Dump completed on 2022-03-24 11:50:06
