-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-11-2024 a las 00:33:54
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `triviumdb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consultations`
--

CREATE TABLE `consultations` (
  `id_consultations` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `lastname` varchar(80) NOT NULL,
  `email` varchar(100) NOT NULL,
  `affair` varchar(100) NOT NULL,
  `message` varchar(500) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `faq`
--

CREATE TABLE `faq` (
  `id` int(11) NOT NULL,
  `question` varchar(200) NOT NULL,
  `answer` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `faq`
--

INSERT INTO `faq` (`id`, `question`, `answer`) VALUES
(1, '¿Cuál es el horario de check-in y check-out?', 'El horario de check-in es a partir de las 11:00 horas y el check-out es hasta las 00:00 horas.'),
(2, '¿Cuál es la política de cancelación?', 'La política de cancelación varía según la tarifa seleccionada. Por favor, consulte las condiciones de la tarifa antes de realizar la reserva.'),
(3, '¿Se admiten mascotas?', 'Si, se admiten mascotas en el hotel. Por favor, póngase en contacto con nosotros para más información.'),
(4, '¿Hay servicio de transporte al aeropuerto?', 'No, no ofrecemos servicio de transporte al aeropuerto. Por favor, póngase en contacto con nosotros para más información.'),
(5, '¿Se puede fumar en las habitaciones?', 'Si, se permite fumar en las habitaciones unicamente en los balcones. Por favor, póngase en contacto con nosotros para más información.'),
(6, '¿Hay aparcamiento disponible?', 'Sí, disponemos de aparcamiento gratuito para nuestros huéspedes.'),
(7, '¿Se puede solicitar una cama adicional?', 'No, no es posible solicitar una cama adicional en las habitaciones.'),
(8, '¿Hay conexión Wi-Fi gratuita?', 'Sí, ofrecemos conexión Wi-Fi gratuita en todas nuestras instalaciones.'),
(9, '¿Se puede solicitar un servicio de habitaciones?', 'Sí, ofrecemos servicio de habitaciones las 24 horas del día.'),
(10, '¿Hay piscina en el hotel?', 'Sí, disponemos de una piscina al aire libre para el disfrute de nuestros huéspedes.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `hotels`
--

CREATE TABLE `hotels` (
  `id_hotel` int(11) NOT NULL,
  `location` varchar(80) NOT NULL,
  `description` varchar(500) NOT NULL,
  `image` varchar(120) DEFAULT NULL,
  `cant_rooms` int(11) NOT NULL,
  `floors` int(11) NOT NULL,
  `stars` int(1) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `hotels`
--

INSERT INTO `hotels` (`id_hotel`, `location`, `description`, `image`, `cant_rooms`, `floors`, `stars`, `created_at`) VALUES
(1, 'Misiones', 'Ubicado en la exuberante provincia de Misiones, Argentina, este hotel ofrece una experiencia única rodeada de naturaleza, selva y la majestuosa Cataratas del Iguazú. Un lugar perfecto para quienes buscan una escapada al aire libre sin renunciar al confort.', 'images/hotel-misiones.jpg', 208, 4, 5, '2024-11-25 22:13:45'),
(2, 'Córdoba', 'Situado en el corazón de la provincia de Córdoba, Argentina, este hotel destaca por su calidez, historia y su cercanía a las sierras. Ideal para explorar el encanto colonial y la belleza natural de la región, con un servicio que te hará sentir como en casa.', 'images/hotel-cordoba.jpg', 208, 4, 4, '2024-11-25 22:13:45'),
(3, 'Salta', 'Salta', 'Este hotel en Salta te sumerge en la cultura norteña de Argentina. Con su arquitectura colonial y vistas espectaculares de los cerros, es el lugar perfecto para descubrir la historia, el folklore y la gastronomía de una de las provincias más fascinantes del país.', 'images/hotel-salta.jpg', 208, 4, 4, '2024-11-25 22:13:45'),
(4, 'Santa Cruz', 'Ubicado en la provincia de Santa Cruz, Argentina, este hotel ofrece un refugio en un entorno único, ideal para los amantes del sur patagónico. La cercanía con el glaciar Perito Moreno y el Parque Nacional Los Glaciares lo convierte en el destino ideal para los aventureros.', 'images/hotel-santacruz.jpg', 208, 4, 5, '2024-11-25 22:13:45'),
(5, 'Mendoza', 'En la cuna del vino argentino, Mendoza te ofrece este hotel de ensueño rodeado de viñedos y montañas. Disfruta de un ambiente relajado, con un toque de elegancia, mientras degustas los mejores vinos en una de las regiones vitivinícolas más prestigiosas del mundo.', 'images/hotel-mendoza.jpg', 208, 4, 3, '2024-11-25 22:13:45'),
(6, 'Buenos Aires', 'Ubicado en la vibrante ciudad de Buenos Aires, este hotel te sumerge en el dinamismo de la capital argentina. Con una ubicación privilegiada, cerca de los principales teatros, museos y restaurantes, es el lugar ideal para explorar el arte, la cultura y la gastronomía porteña.', 'images/hotel-buenosaires.jpg', 208, 4, 3, '2024-11-25 22:13:45');
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservations`
--

CREATE TABLE `reservations` (
  `id_reservation` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `id_room` int(11) DEFAULT NULL,
  `id_hotel` int(11) DEFAULT NULL,
  `number_people` int(11) DEFAULT NULL,
  `type_room` int(11) DEFAULT NULL,
  `check_in` timestamp NULL DEFAULT NULL,
  `check_out` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rooms`
--

CREATE TABLE `rooms` (
  `id_room` int(11) NOT NULL,
  `id_hotel` int(11) DEFAULT NULL,
  `type_room` varchar(80) NOT NULL,
  `number_room` int(11) NOT NULL,
  `floor_room` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rooms`
--

INSERT INTO `rooms` (`id_room`, `id_hotel`, `type_room`, `number_room`, `floor_room`) VALUES
(1, 1, 'Classic', 100, 1),
(2, 1, 'Classic', 101, 1),
(3, 1, 'Classic', 102, 1),
(4, 1, 'Classic', 103, 1),
(5, 1, 'Classic', 104, 1),
(6, 1, 'Classic', 105, 1),
(7, 1, 'Classic', 106, 1),
(8, 1, 'Classic', 107, 1),
(9, 1, 'Classic', 108, 1),
(10, 1, 'Classic', 109, 1),
(11, 1, 'Classic', 110, 1),
(12, 1, 'Classic', 111, 1),
(13, 1, 'Classic', 112, 1),
(14, 1, 'Doble', 113, 1),
(15, 1, 'Doble', 114, 1),
(16, 1, 'Doble', 115, 1),
(17, 1, 'Doble', 116, 1),
(18, 1, 'Doble', 117, 1),
(19, 1, 'Doble', 118, 1),
(20, 1, 'Doble', 119, 1),
(21, 1, 'Doble', 120, 1),
(22, 1, 'Doble', 121, 1),
(23, 1, 'Doble', 122, 1),
(24, 1, 'Doble', 123, 1),
(25, 1, 'Doble', 124, 1),
(26, 1, 'Doble', 125, 1),
(27, 1, 'Premium', 126, 1),
(28, 1, 'Premium', 127, 1),
(29, 1, 'Premium', 128, 1),
(30, 1, 'Premium', 129, 1),
(31, 1, 'Premium', 130, 1),
(32, 1, 'Premium', 131, 1),
(33, 1, 'Premium', 132, 1),
(34, 1, 'Premium', 133, 1),
(35, 1, 'Premium', 134, 1),
(36, 1, 'Premium', 135, 1),
(37, 1, 'Premium', 136, 1),
(38, 1, 'Premium', 137, 1),
(39, 1, 'Premium', 138, 1),
(40, 1, 'Deluxe', 139, 1),
(41, 1, 'Deluxe', 140, 1),
(42, 1, 'Deluxe', 141, 1),
(43, 1, 'Deluxe', 142, 1),
(44, 1, 'Deluxe', 143, 1),
(45, 1, 'Deluxe', 144, 1),
(46, 1, 'Deluxe', 145, 1),
(47, 1, 'Deluxe', 146, 1),
(48, 1, 'Deluxe', 147, 1),
(49, 1, 'Deluxe', 148, 1),
(50, 1, 'Deluxe', 149, 1),
(51, 1, 'Deluxe', 150, 1),
(52, 1, 'Deluxe', 151, 1),
(53, 1, 'Classic', 200, 2),
(54, 1, 'Classic', 201, 2),
(55, 1, 'Classic', 202, 2),
(56, 1, 'Classic', 203, 2),
(57, 1, 'Classic', 204, 2),
(58, 1, 'Classic', 205, 2),
(59, 1, 'Classic', 206, 2),
(60, 1, 'Classic', 207, 2),
(61, 1, 'Classic', 208, 2),
(62, 1, 'Classic', 209, 2),
(63, 1, 'Classic', 210, 2),
(64, 1, 'Classic', 211, 2),
(65, 1, 'Doble', 212, 2),
(66, 1, 'Doble', 213, 2),
(67, 1, 'Doble', 214, 2),
(68, 1, 'Doble', 215, 2),
(69, 1, 'Doble', 216, 2),
(70, 1, 'Doble', 217, 2),
(71, 1, 'Doble', 218, 2),
(72, 1, 'Doble', 219, 2),
(73, 1, 'Doble', 220, 2),
(74, 1, 'Doble', 221, 2),
(75, 1, 'Doble', 222, 2),
(76, 1, 'Doble', 223, 2),
(77, 1, 'Doble', 224, 2),
(78, 1, 'Doble', 225, 2),
(79, 1, 'Premium', 226, 2),
(80, 1, 'Premium', 227, 2),
(81, 1, 'Premium', 228, 2),
(82, 1, 'Premium', 229, 2),
(83, 1, 'Premium', 230, 2),
(84, 1, 'Premium', 231, 2),
(85, 1, 'Premium', 232, 2),
(86, 1, 'Premium', 233, 2),
(87, 1, 'Premium', 234, 2),
(88, 1, 'Premium', 235, 2),
(89, 1, 'Premium', 236, 2),
(90, 1, 'Premium', 237, 2),
(91, 1, 'Premium', 238, 2),
(92, 1, 'Deluxe', 239, 2),
(93, 1, 'Deluxe', 240, 2),
(94, 1, 'Deluxe', 241, 2),
(95, 1, 'Deluxe', 242, 2),
(96, 1, 'Deluxe', 243, 2),
(97, 1, 'Deluxe', 244, 2),
(98, 1, 'Deluxe', 245, 2),
(99, 1, 'Deluxe', 246, 2),
(100, 1, 'Deluxe', 247, 2),
(101, 1, 'Deluxe', 248, 2),
(102, 1, 'Deluxe', 249, 2),
(103, 1, 'Deluxe', 250, 2),
(104, 1, 'Deluxe', 251, 2),
(105, 1, 'Classic', 300, 3),
(106, 1, 'Classic', 301, 3),
(107, 1, 'Classic', 302, 3),
(108, 1, 'Classic', 303, 3),
(109, 1, 'Classic', 304, 3),
(110, 1, 'Classic', 305, 3),
(111, 1, 'Classic', 306, 3),
(112, 1, 'Classic', 307, 3),
(113, 1, 'Classic', 308, 3),
(114, 1, 'Classic', 309, 3),
(115, 1, 'Classic', 310, 3),
(116, 1, 'Classic', 311, 3),
(117, 1, 'Doble', 312, 3),
(118, 1, 'Doble', 313, 3),
(119, 1, 'Doble', 314, 3),
(120, 1, 'Doble', 315, 3),
(121, 1, 'Doble', 316, 3),
(122, 1, 'Doble', 317, 3),
(123, 1, 'Doble', 318, 3),
(124, 1, 'Doble', 319, 3),
(125, 1, 'Doble', 320, 3),
(126, 1, 'Doble', 321, 3),
(127, 1, 'Doble', 322, 3),
(128, 1, 'Doble', 323, 3),
(129, 1, 'Doble', 324, 3),
(130, 1, 'Doble', 325, 3),
(131, 1, 'Premium', 326, 3),
(132, 1, 'Premium', 327, 3),
(133, 1, 'Premium', 328, 3),
(134, 1, 'Premium', 329, 3),
(135, 1, 'Premium', 330, 3),
(136, 1, 'Premium', 331, 3),
(137, 1, 'Premium', 332, 3),
(138, 1, 'Premium', 333, 3),
(139, 1, 'Premium', 334, 3),
(140, 1, 'Premium', 335, 3),
(141, 1, 'Premium', 336, 3),
(142, 1, 'Premium', 337, 3),
(143, 1, 'Premium', 338, 3),
(144, 1, 'Deluxe', 339, 3),
(145, 1, 'Deluxe', 340, 3),
(146, 1, 'Deluxe', 341, 3),
(147, 1, 'Deluxe', 342, 3),
(148, 1, 'Deluxe', 343, 3),
(149, 1, 'Deluxe', 344, 3),
(150, 1, 'Deluxe', 345, 3),
(151, 1, 'Deluxe', 346, 3),
(152, 1, 'Deluxe', 347, 3),
(153, 1, 'Deluxe', 348, 3),
(154, 1, 'Deluxe', 349, 3),
(155, 1, 'Deluxe', 350, 3),
(156, 1, 'Deluxe', 351, 3),
(157, 1, 'Classic', 400, 4),
(158, 1, 'Classic', 401, 4),
(159, 1, 'Classic', 402, 4),
(160, 1, 'Classic', 403, 4),
(161, 1, 'Classic', 404, 4),
(162, 1, 'Classic', 405, 4),
(163, 1, 'Classic', 406, 4),
(164, 1, 'Classic', 407, 4),
(165, 1, 'Classic', 408, 4),
(166, 1, 'Classic', 409, 4),
(167, 1, 'Classic', 410, 4),
(168, 1, 'Classic', 411, 4),
(169, 1, 'Doble', 412, 4),
(170, 1, 'Doble', 413, 4),
(171, 1, 'Doble', 414, 4),
(172, 1, 'Doble', 415, 4),
(173, 1, 'Doble', 416, 4),
(174, 1, 'Doble', 417, 4),
(175, 1, 'Doble', 418, 4),
(176, 1, 'Doble', 419, 4),
(177, 1, 'Doble', 420, 4),
(178, 1, 'Doble', 421, 4),
(179, 1, 'Doble', 422, 4),
(180, 1, 'Doble', 423, 4),
(181, 1, 'Doble', 424, 4),
(182, 1, 'Doble', 425, 4),
(183, 1, 'Premium', 426, 4),
(184, 1, 'Premium', 427, 4),
(185, 1, 'Premium', 428, 4),
(186, 1, 'Premium', 429, 4),
(187, 1, 'Premium', 430, 4),
(188, 1, 'Premium', 431, 4),
(189, 1, 'Premium', 432, 4),
(190, 1, 'Premium', 433, 4),
(191, 1, 'Premium', 434, 4),
(192, 1, 'Premium', 435, 4),
(193, 1, 'Premium', 436, 4),
(194, 1, 'Premium', 437, 4),
(195, 1, 'Premium', 438, 4),
(196, 1, 'Deluxe', 439, 4),
(197, 1, 'Deluxe', 440, 4),
(198, 1, 'Deluxe', 441, 4),
(199, 1, 'Deluxe', 442, 4),
(200, 1, 'Deluxe', 443, 4),
(201, 1, 'Deluxe', 444, 4),
(202, 1, 'Deluxe', 445, 4),
(203, 1, 'Deluxe', 446, 4),
(204, 1, 'Deluxe', 447, 4),
(205, 1, 'Deluxe', 448, 4),
(206, 1, 'Deluxe', 449, 4),
(207, 1, 'Deluxe', 450, 4),
(208, 1, 'Deluxe', 451, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `type_rooms`
--

CREATE TABLE `type_rooms` (
  `id_room` int(11) DEFAULT NULL,
  `id_hotel` int(11) DEFAULT NULL,
  `type_room` varchar(80) NOT NULL,
  `description` varchar(500) NOT NULL,
  `image` varchar(120) DEFAULT NULL,
  `price` float NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `type_rooms`
--

INSERT INTO `type_rooms` (`id_room`, `id_hotel`, `type_room`, `description`, `image`, `price`, `created_at`) VALUES
(NULL, 1, 'Classic', 'Una habitación sencilla, perfecta para aquellos que buscan comodidad a un precio accesible. Cuenta con una cama individual, ideal para una persona, y un baño privado para mayor privacidad y confort. Esta habitación es ideal para estancias cortas o viajeros solitarios.', 'images/habitacion_classic.jpg', 500, '2024-11-25 22:22:42'),
(NULL, 1, 'Doble', 'Habitación espaciosa con dos camas individuales, lo que la convierte en la opción ideal para dos personas. El baño privado asegura un mayor confort y privacidad. Es perfecta para amigos, familiares o compañeros de trabajo que necesiten un espacio compartido, pero con las comodidades de un baño privado', 'images/habitacion_doble.jpg', 750, '2024-11-25 22:22:42'),
(NULL, 1, 'Premium', 'Una habitación de mayor categoría que ofrece una cama doble, baño privado y un balcón que permite disfrutar del aire fresco. Esta habitación está diseñada para quienes buscan una estancia más lujosa y relajante, con un ambiente más amplio y un toque extra de confort y elegancia.', 'images/habitacion_premium.jpg', 1000, '2024-11-25 22:22:42'),
(NULL, 1, 'Deluxe', 'La opción más lujosa y espaciosa del hotel, con dos camas dobles, un baño privado de lujo, un balcón y un jacuzzi. Esta habitación está pensada para quienes desean disfrutar de un ambiente exclusivo y cómodo, perfecta para una estancia prolongada o para ocasiones especiales, ofreciendo una experiencia única de relax y confort.', 'images/habitacion_deluxe.jpg', 1250, '2024-11-25 22:22:42');
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id_user` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `lastname` varchar(80) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(80) NOT NULL,
  `dni` int(8) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `testimonial` (
  `testimonio` varchar(800) NOT NULL,
  `name` varchar(40) NOT NULL,
  `location` varchar(40) NOT NULL
);


INSERT INTO `testimonial` (`testimonio`, `name`, `location`) VALUES
('Sin duda, una de las mejores experiencias hoteleras que he tenido! Desde que llegue al hotel, me senti como en casa. 
La atencion del personal es excelente y las instalaciones sonde primer nivel. Sin duda, volveria a hospedarme en el Hotel Trivium.', 'Agustina Salerno', 'Bs-As, Argentina'),
('¡Trivium fue una elección soñada! La estancia fue impecable de principio
a fin. La decoración es moderna y elegante, y cada rincón está pensado para el confort de los huéspedes.
Honestamente lo super recomiendo', 'Maria Lopez', 'Mendoza, Argentina'),
('Este hotel fue una experiencia maravillosa. Las habitaciones son cómodas, limpias
y bien decoradas, y el personal siempre está dispuesto a ayudar con una sonrisa. La ubicación es ideal para
explorar la ciudad; ¡sin duda volvería a hospedarme aquí!', 'Elena Costas', 'Salta, Argentina');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `consultations`
--
ALTER TABLE `consultations`
  ADD PRIMARY KEY (`id_consultations`),
  ADD KEY `id_user` (`id_user`);

--
-- Indices de la tabla `faq`
--
ALTER TABLE `faq`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `hotels`
--
ALTER TABLE `hotels`
  ADD PRIMARY KEY (`id_hotel`),
  ADD KEY `location_disponibility` (`location`);

--
-- Indices de la tabla `reservations`
--
ALTER TABLE `reservations`
  ADD PRIMARY KEY (`id_reservation`),
  ADD KEY `id_user` (`id_user`),
  ADD KEY `id_room` (`id_room`),
  ADD KEY `id_hotel` (`id_hotel`);

--
-- Indices de la tabla `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`id_room`),
  ADD KEY `id_hotel` (`id_hotel`);

--
-- Indices de la tabla `type_rooms`
--
ALTER TABLE `type_rooms`
  ADD KEY `id_hotel` (`id_hotel`),
  ADD KEY `id_room` (`id_room`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `dni` (`dni`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `consultations`
--
ALTER TABLE `consultations`
  MODIFY `id_consultations` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `faq`
--
ALTER TABLE `faq`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `hotels`
--
ALTER TABLE `hotels`
  MODIFY `id_hotel` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `reservations`
--
ALTER TABLE `reservations`
  MODIFY `id_reservation` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rooms`
--
ALTER TABLE `rooms`
  MODIFY `id_room` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=209;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `consultations`
--
ALTER TABLE `consultations`
  ADD CONSTRAINT `consultations_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`);

--
-- Filtros para la tabla `reservations`
--
ALTER TABLE `reservations`
  ADD CONSTRAINT `reservations_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`),
  ADD CONSTRAINT `reservations_ibfk_2` FOREIGN KEY (`id_room`) REFERENCES `rooms` (`id_room`),
  ADD CONSTRAINT `reservations_ibfk_3` FOREIGN KEY (`id_hotel`) REFERENCES `hotels` (`id_hotel`);

--
-- Filtros para la tabla `rooms`
--
ALTER TABLE `rooms`
  ADD CONSTRAINT `rooms_ibfk_1` FOREIGN KEY (`id_hotel`) REFERENCES `hotels` (`id_hotel`);

--
-- Filtros para la tabla `type_rooms`
--
ALTER TABLE `type_rooms`
  ADD CONSTRAINT `type_rooms_ibfk_1` FOREIGN KEY (`id_hotel`) REFERENCES `hotels` (`id_hotel`),
  ADD CONSTRAINT `type_rooms_ibfk_2` FOREIGN KEY (`id_room`) REFERENCES `rooms` (`id_room`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
