-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-04-2020 a las 13:00:36
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_series`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_series`
--

CREATE TABLE `tabla_series` (
  `id` int(11) NOT NULL,
  `titulo` char(255) NOT NULL,
  `sinopsis` char(255) NOT NULL,
  `temporadas` int(11) NOT NULL,
  `fecha_lanzamiento` int(11) NOT NULL,
  `vista_si_no` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_series`
--

INSERT INTO `tabla_series` (`id`, `titulo`, `sinopsis`, `temporadas`, `fecha_lanzamiento`, `vista_si_no`) VALUES
(1, 'Outlander', 'La serie sigue a Claire Beauchamp, una enfermera de combate de 1945 casada con Frank Randall en el siglo XX, que misteriosamente es llevada a través del tiempo hasta 1743. Ahí conoce a Jamie Fraser, un joven guerrero escocés, caballeroso y romántico, se c', 5, 2014, 'SI'),
(3, 'El Ministerio del Tiempo', 'El Ministerio del Tiempo es una institución gubernamental secreta que depende directamente de la Presidencia del Gobierno español. Solo monarcas, presidentes y un número exclusivo de personas saben de él.', 3, 2015, 'SI'),
(5, 'Grimm', 'La vida del detective de homicidios de Portland (Oregón), Nick Burkhardt, toma un giro inesperado y peligroso cuando su tía materna, la mujer que lo crio (Marie Kessler), le revela que es una persona dotada con la capacidad de reconocer a toda clase de cr', 6, 2014, 'SI'),
(6, 'The Walking Dead', 'Tras despertar de un coma en un hospital abandonado, el oficial de policía Rick Grimes (Andrew Lincoln) se da cuenta que el mundo que conocía ya no existe y de que el caos se ha apoderado de la ciudad debido a que inexplicablemente los muertos caminantes', 10, 2010, 'NO'),
(7, 'Penny Dreadful', 'Londres Victoriano', 5, 2014, 'SI'),
(8, 'El Caso: Crónica de sucesos', 'En el Madrid de los años 1960, dos periodistas del diario \'El Caso\', Jesús Expósito (Fernando Guillén Cuervo), un expolicía con un pasado turbio, y Clara López (Verónica Sánchez), especializada en prensa sensacionalista, están condenados a entenderse para', 1, 2016, 'SI');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tabla_series`
--
ALTER TABLE `tabla_series`
  ADD PRIMARY KEY (`id`,`titulo`,`sinopsis`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tabla_series`
--
ALTER TABLE `tabla_series`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
