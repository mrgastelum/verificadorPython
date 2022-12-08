-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-12-2022 a las 04:39:55
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `excel`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `codigo_barras` varchar(10) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `imagen` varchar(350) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `nombre`, `precio`, `codigo_barras`, `descripcion`, `imagen`) VALUES
(1, 'Dulces', '10.00', '1', 'Dulces Zanditas', 'img/1.png'),
(2, 'Refresco', '9.50', '2', 'Soda de toronja', 'img/2.png'),
(3, 'Pan', '25.00', '3', 'Pan de Dulce', 'img/3.png'),
(4, 'Papas', '8.00', '4', 'Sabritas blancas', 'img/4.png'),
(5, 'Agua', '8.50', '5', 'Agua Epura', 'img/5.png'),
(6, 'Dulces', '10.00', '6', 'Dulces Gummy Pop', 'img/6.png'),
(7, 'Refresco', '9.50', '7', 'Soda de naranja', 'img/7.png'),
(8, 'Pan', '25.00', '8', 'Pan dulce rojo', 'img/8.png'),
(9, 'Papas', '8.00', '9', 'Sabritas rojas', 'img/9.png'),
(10, 'Agua', '8.50', '10', 'Agua Bonafont', 'img/10.png');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
