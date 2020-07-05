CREATE TABLE `instruments` (
  `ID` int(20) NOT NULL AUTO_INCREMENT,
  `security_code` varchar(20) NOT NULL,
  `security_id` varchar(20) NOT NULL,
  `security_name` varchar(100) DEFAULT NULL,
  `isin_number` varchar(20) NOT NULL,
  `instrument` varchar(20) DEFAULT 'Equity',
  `industry` varchar(50) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_Date` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `is_delete` int(11) DEFAULT NULL,
  PRIMARY KEY (`security_id`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8