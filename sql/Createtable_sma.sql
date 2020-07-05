CREATE TABLE `sma` (\
  `id` int(11) NOT NULL AUTO_INCREMENT,\
  `equity` varchar(50) NOT NULL,\
  `date` datetime NOT NULL,\
  `sme20` decimal(10,0) DEFAULT NULL,\
  `sme50` decimal(10,0) DEFAULT NULL,\
  `sme100` decimal(10,0) DEFAULT NULL,\
  `sme200` decimal(10,0) DEFAULT NULL,\
  PRIMARY KEY (`id`)\
) ENGINE=InnoDB DEFAULT CHARSET=utf8