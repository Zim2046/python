-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema magazine_subscription_red
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `magazine_subscription_red` ;

-- -----------------------------------------------------
-- Schema magazine_subscription_red
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `magazine_subscription_red` DEFAULT CHARACTER SET utf8 ;
USE `magazine_subscription_red` ;

-- -----------------------------------------------------
-- Table `magazine_subscription_red`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `magazine_subscription_red`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `eamil` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `magazine_subscription_red`.`magazines`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `magazine_subscription_red`.`magazines` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `description` TINYTEXT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  PRIMARY KEY (`id`),
  INDEX `fk_magazines_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_magazines_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `magazine_subscription_red`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
