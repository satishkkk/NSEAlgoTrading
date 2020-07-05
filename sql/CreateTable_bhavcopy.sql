CREATE TABLE `algotreading`.`bhavcopy` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `symbol` VARCHAR(20) NOT NULL,
  `open` DECIMAL NOT NULL,
  `high` DECIMAL NOT NULL,
  `low` DECIMAL NOT NULL,
  `close` DECIMAL NOT NULL,
  `last` DECIMAL NOT NULL,
  `previous_close` DECIMAL NOT NULL,
  `total_traded_quantity` BIGINT NOT NULL,
  `total_traded_value` DECIMAL NOT NULL,
  `date` TIMESTAMP NOT NULL,
  `active_status` VARCHAR(20),
  `created_date` TIMESTAMP,
  `updated_Date` TIMESTAMP,
  `is_delete` INT,
   KEY(`id`),
  PRIMARY KEY (`symbol`)
);


INSERT INTO `algotreading`.`bhavcopy`
	(
	`symbol`,
	`open`,
	`high`,
	`low`,
	`close`,
	`last`,
	`previous_close`,
	`total_traded_quantity`,
	`total_traded_value`,
	`date`,
	`active_status`,
	`created_date`,
	`updated_Date`,
	`is_delete`
	)
	VALUES
	(
	'21STCENMGM',
	'8.4',
	'8.4',
	'8.4',
	'8.4',
	'8.4',
	'8.5',
	'100',
	'840',
	'2000-12-20 10:01:00',
	'1',
	CURDATE(),
	CURDATE(),
	'0'
	);