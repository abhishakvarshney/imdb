-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Aug 30, 2020 at 12:08 PM
-- Server version: 5.7.28
-- PHP Version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `platform_imdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `Movies`
--

CREATE TABLE `Movies` (
  `movie_id` varchar(255) NOT NULL,
  `name` longtext,
  `director` longtext,
  `imdb_score` longtext,
  `popularity` longtext,
  `genre` longtext,
  `isActive` tinyint(1) NOT NULL,
  `createdOn` datetime(6) NOT NULL,
  `updatedOn` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Movies`
--
ALTER TABLE `Movies`
  ADD PRIMARY KEY (`movie_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
