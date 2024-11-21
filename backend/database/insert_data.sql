-- Insertar datos en la tabla faq
INSERT INTO faq (id, question, answer)
VALUES 
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

-- Insertar datos de ejemplo en la tabla type_rooms
INSERT INTO type_rooms (type_room, title, description, image, price)
VALUES
('Classic', 'Habitación clásica con cama individual y baño privado.', 'images/habitacion_classic.jpg', 500),
('Doble', 'Habitación doble con dos camas individuales y baño privado.', 'images/habitacion_doble.jpg', 750),
('Premium', 'Habitación premium con cama doble, baño privado y balcón.', 'images/habitacion_premium.jpg', 1000),
('Deluxe', 'Habitación deluxe con dos camas dobles, baño privado, balcón y jacuzzi.', 'images/habitacion_deluxe.jpg', 1250);


-- Insertar datos de ejemplo en la tabla hotel 
INSERT INTO hotel (id_hotel, location, description, image, cant_rooms)
VALUES
(1, 'Misiones', 'Hotel ubicado en la provincia de Misiones, Argentina.', 'images/hotel-misiones.jpg', 208),
(2, 'Córdoba', 'Hotel ubicado en la provincia de Córdoba, Argentina.', 'images/hotel-cordoba.jpg', 208),
(3, 'Salta', 'Hotel ubicado en la provincia de Salta, Argentina.', 'images/hotel-salta.jpg', 208),
(4, 'Santa Cruz', 'Hotel ubicado en la provincia de Santa Cruz, Argentina.', 'images/hotel-santacruz.jpg', 208),
(5, 'Mendoza', 'Hotel ubicado en la provincia de Mendoza, Argentina.', 'images/hotel-mendoza.jpg', 208),
(6, 'Buenos Aires', 'Hotel ubicado en la provincia de Buenos Aires, Argentina.', 'images/hotel-buenosaires.jpg', 208);

-- Insertar datos de ejemplo en la tabla rooms_disponibility

INSERT INTO rooms_disponibility (id_room, type_room, number_room, floor_room) 
VALUES 
(1, 'Classic', 100, 1),
(2, 'Classic', 101, 1),
(3, 'Classic', 102, 1),
(4, 'Classic', 103, 1),
(5, 'Classic', 104, 1),
(6, 'Classic', 105, 1),
(7, 'Classic', 106, 1),
(8, 'Classic', 107, 1),
(9, 'Classic', 108, 1),
(10, 'Classic', 109, 1),
(11, 'Classic', 110, 1),
(12, 'Classic', 111, 1),
(13, 'Classic', 112, 1),
(14, 'Doble', 113, 1),
(15, 'Doble', 114, 1),
(16, 'Doble', 115, 1),
(17, 'Doble', 116, 1),
(18, 'Doble', 117, 1),
(19, 'Doble', 118, 1),
(20, 'Doble', 119, 1),
(21, 'Doble', 120, 1),
(22, 'Doble', 121, 1),
(23, 'Doble', 122, 1),
(24, 'Doble', 123, 1),
(25, 'Doble', 124, 1),
(26, 'Doble', 125, 1),
(27, 'Premium', 126, 1),
(28, 'Premium', 127, 1),
(29, 'Premium', 128, 1),
(30, 'Premium', 129, 1),
(31, 'Premium', 130, 1),
(32, 'Premium', 131, 1),
(33, 'Premium', 132, 1),
(34, 'Premium', 133, 1),
(35, 'Premium', 134, 1),
(36, 'Premium', 135, 1),
(37, 'Premium', 136, 1),
(38, 'Premium', 137, 1),
(39, 'Premium', 138, 1),
(40, 'Deluxe', 139, 1),
(41, 'Deluxe', 140, 1),
(42, 'Deluxe', 141, 1),
(43, 'Deluxe', 142, 1),
(44, 'Deluxe', 143, 1),
(45, 'Deluxe', 144, 1),
(46, 'Deluxe', 145, 1),
(47, 'Deluxe', 146, 1),
(48, 'Deluxe', 147, 1),
(49, 'Deluxe', 148, 1),
(50, 'Deluxe', 149, 1),
(51, 'Deluxe', 150, 1),
(52, 'Deluxe', 151, 1),
(53, 'Classic', 200, 2),
(54, 'Classic', 201, 2),
(55, 'Classic', 202, 2),
(56, 'Classic', 203, 2),
(57, 'Classic', 204, 2),
(58, 'Classic', 205, 2),
(59, 'Classic', 206, 2),
(60, 'Classic', 207, 2),
(61, 'Classic', 208, 2),
(62, 'Classic', 209, 2),
(63, 'Classic', 210, 2),
(64, 'Classic', 211, 2),
(65, 'Doble', 212, 2),
(66, 'Doble', 213, 2),
(67, 'Doble', 214, 2),
(68, 'Doble', 215, 2),
(69, 'Doble', 216, 2),
(70, 'Doble', 217, 2),
(71, 'Doble', 218, 2),
(72, 'Doble', 219, 2),
(73, 'Doble', 220, 2),
(74, 'Doble', 221, 2),
(75, 'Doble', 222, 2),
(76, 'Doble', 223, 2),
(77, 'Doble', 224, 2),
(78, 'Doble', 225, 2),
(79, 'Premium', 226, 2),
(80, 'Premium', 227, 2),
(81, 'Premium', 228, 2),
(82, 'Premium', 229, 2),
(83, 'Premium', 230, 2),
(84, 'Premium', 231, 2),
(85, 'Premium', 232, 2),
(86, 'Premium', 233, 2),
(87, 'Premium', 234, 2),
(88, 'Premium', 235, 2),
(89, 'Premium', 236, 2),
(90, 'Premium', 237, 2),
(91, 'Premium', 238, 2),
(92, 'Deluxe', 239, 2),
(93, 'Deluxe', 240, 2),
(94, 'Deluxe', 241, 2),
(95, 'Deluxe', 242, 2),
(96, 'Deluxe', 243, 2),
(97, 'Deluxe', 244, 2),
(98, 'Deluxe', 245, 2),
(99, 'Deluxe', 246, 2),
(100, 'Deluxe', 247, 2),
(101, 'Deluxe', 248, 2),
(102, 'Deluxe', 249, 2),
(103, 'Deluxe', 250, 2),
(104, 'Deluxe', 251, 2),
(105, 'Classic', 300, 3),
(106, 'Classic', 301, 3),
(107, 'Classic', 302, 3),
(108, 'Classic', 303, 3),
(109, 'Classic', 304, 3),
(110, 'Classic', 305, 3),
(111, 'Classic', 306, 3),
(112, 'Classic', 307, 3),
(113, 'Classic', 308, 3),
(114, 'Classic', 309, 3),
(115, 'Classic', 310, 3),
(116, 'Classic', 311, 3),
(117, 'Doble', 312, 3),
(118, 'Doble', 313, 3),
(119, 'Doble', 314, 3),
(120, 'Doble', 315, 3),
(121, 'Doble', 316, 3),
(122, 'Doble', 317, 3),
(123, 'Doble', 318, 3),
(124, 'Doble', 319, 3),
(125, 'Doble', 320, 3),
(126, 'Doble', 321, 3),
(127, 'Doble', 322, 3),
(128, 'Doble', 323, 3),
(129, 'Doble', 324, 3),
(130, 'Doble', 325, 3),
(131, 'Premium', 326, 3),
(132, 'Premium', 327, 3),
(133, 'Premium', 328, 3),
(134, 'Premium', 329, 3),
(135, 'Premium', 330, 3),
(136, 'Premium', 331, 3),
(137, 'Premium', 332, 3),
(138, 'Premium', 333, 3),
(139, 'Premium', 334, 3),
(140, 'Premium', 335, 3),
(141, 'Premium', 336, 3),
(142, 'Premium', 337, 3),
(143, 'Premium', 338, 3),
(144, 'Deluxe', 339, 3),
(145, 'Deluxe', 340, 3),
(146, 'Deluxe', 341, 3),
(147, 'Deluxe', 342, 3),
(148, 'Deluxe', 343, 3),
(149, 'Deluxe', 344, 3),
(150, 'Deluxe', 345, 3),
(151, 'Deluxe', 346, 3),
(152, 'Deluxe', 347, 3),
(153, 'Deluxe', 348, 3),
(154, 'Deluxe', 349, 3),
(155, 'Deluxe', 350, 3),
(156, 'Deluxe', 351, 3),
(157, 'Classic', 400, 4),
(158, 'Classic', 401, 4),
(159, 'Classic', 402, 4),
(160, 'Classic', 403, 4),
(161, 'Classic', 404, 4),
(162, 'Classic', 405, 4),
(163, 'Classic', 406, 4),
(164, 'Classic', 407, 4),
(165, 'Classic', 408, 4),
(166, 'Classic', 409, 4),
(167, 'Classic', 410, 4),
(168, 'Classic', 411, 4),
(169, 'Doble', 412, 4),
(170, 'Doble', 413, 4),
(171, 'Doble', 414, 4),
(172, 'Doble', 415, 4),
(173, 'Doble', 416, 4),
(174, 'Doble', 417, 4),
(175, 'Doble', 418, 4),
(176, 'Doble', 419, 4),
(177, 'Doble', 420, 4),
(178, 'Doble', 421, 4),
(179, 'Doble', 422, 4),
(180, 'Doble', 423, 4),
(181, 'Doble', 424, 4),
(182, 'Doble', 425, 4),
(183, 'Premium', 426, 4),
(184, 'Premium', 427, 4),
(185, 'Premium', 428, 4),
(186, 'Premium', 429, 4),
(187, 'Premium', 430, 4),
(188, 'Premium', 431, 4),
(189, 'Premium', 432, 4),
(190, 'Premium', 433, 4),
(191, 'Premium', 434, 4),
(192, 'Premium', 435, 4),
(193, 'Premium', 436, 4),
(194, 'Premium', 437, 4),
(195, 'Premium', 438, 4),
(196, 'Deluxe', 439, 4),
(197, 'Deluxe', 440, 4),
(198, 'Deluxe', 441, 4),
(199, 'Deluxe', 442, 4),
(200, 'Deluxe', 443, 4),
(201, 'Deluxe', 444, 4),
(202, 'Deluxe', 445, 4),
(203, 'Deluxe', 446, 4),
(204, 'Deluxe', 447, 4),
(205, 'Deluxe', 448, 4),
(206, 'Deluxe', 449, 4),
(207, 'Deluxe', 450, 4),
(208, 'Deluxe', 451, 4);