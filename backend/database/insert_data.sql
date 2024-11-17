-- Insertar datos de ejemplo en la tabla users
INSERT INTO users (id_user, name, lastname, email, phone, dni)
VALUES 
    (NULL, 'Juan', 'Pérez', 'juan.perez@example.com', 5551234567,12345678),
    (NULL, 'Ana', 'García', 'ana.garcia@example.com', 5552345678, 87654321),
    (NULL, 'Carlos', 'Lopez', 'carlos.lopez@example.com', 5553456789, 11223344),
    (NULL, 'Lucía', 'Martínez', 'lucia.martinez@example.com', 5554567890, 22334455),
    (NULL, 'Pedro', 'Rodríguez', 'pedro.rodriguez@example.com', 5555678901, 33445566);


-- Insertar datos de ejemplo en la tabla rooms
INSERT INTO rooms (id_room, id_hotel, number_room, title, description, image, status, max_guests, price)
VALUES 
    (NULL, 1, 101, 'Habitación Classic', 'Una habitación estándar con todas las comodidades necesarias', 'habitacion_claccic.jpg', 'available', 3, 99.99),
    (NULL, 1, 102, 'Habitación Deluxe', 'Una habitación deluxe con cama king-size y vista a la ciudad', 'habitacion_deluxe.jpg', 'available', 4, 159.99),
    (NULL, 1, 103, 'Habitacion Doble', 'Una habitacion ideal para compañeros de trabajo, con camas individuales separadas', 'habitacion_doble.jpg', 'not available', 2, 69.99),
    (NULL, 2, 201, 'Habitación Individual', 'Una habitación pequeña ideal para viajeros solos', 'habitacion_individual.jpg', 'available', 1, 49.99),
    (NULL, 2, 202, 'Habitación Familiar', 'Una habitación grande para familias, con 2 camas queen-size', 'habitacion_familiar.jpg', 'available', 5, 129.99);


-- Insertar datos de ejemplo en la tabla hotel 
INSERT INTO hotel (id_hotel, title, description, image, cant_rooms)
VALUES 
    (NULL, 'Trivium Mendoza', 'Trivium Hoteles en Mendoza, ofreciendo una experiencia única en el corazón de los viñedos y la cultura del vino.', 'hotel1.jpg', 50),
    (NULL, 'Trivium Costa Atlántica', 'Trivium Hoteles en la costa atlántica, un refugio frente al mar con todas las comodidades para disfrutar de la playa.', 'hotel2.jpg', 30),
    (NULL, 'Trivium Refugio Córdoba', 'Trivium Hoteles en las sierras de Córdoba, ideal para una escapada de montaña con actividades al aire libre y descanso.', 'hotel3.jpg', 15),
    (NULL, 'Trivium Buenos Aires', 'Trivium Hoteles en Buenos Aires, en el centro de la ciudad, a pasos de teatros, museos y la vida nocturna porteña.', 'hotel4.jpg', 20),
    (NULL, 'Trivium Patagonia', 'Trivium Hoteles en la Patagonia argentina, con vistas espectaculares a los lagos y montañas más impresionantes del sur.', 'hotel5.jpg', 10);

-- Insertar datos de ejemplo en la tabla reservations

INSERT INTO reservations (id_user, id_room, id_hotel, number_room, check_in, check_out)
VALUES 
    (1, 1, 1, 101, '2024-11-20 12:00:00', '2024-11-20 19:00:00'),
    (2, 2, 2, 102, '2024-11-21 12:00:00', '2024-11-21 19:00:00'),
    (3, 3, 3, 103, '2024-11-25 12:00:00', '2024-11-25 19:00:00'),
    (4, 4, 4, 104, '2024-11-18 12:00:00', '2024-11-18 19:00:00'),
    (5, 5, 5, 105, '2024-11-15 12:00:00', '2024-11-15 19:00:00');