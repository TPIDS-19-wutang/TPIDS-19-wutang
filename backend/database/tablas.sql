CREATE TABLE IF NOT EXISTS users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    lastname VARCHAR(80) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    dni INT(8) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE users
  AUTO_INCREMENT = 2;



CREATE TABLE IF NOT EXISTS consultations (
    id_consultations INT AUTO_INCREMENT PRIMARY KEY,
    id_user INT NOT NULL,
    name VARCHAR(80) NOT NULL,
    lastname VARCHAR(80) NOT NULL,
    email VARCHAR(100) NOT NULL,
    affair VARCHAR(100) NOT NULL,
    message VARCHAR(500) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_user) REFERENCES users (id_user)
);



CREATE TABLE IF NOT EXISTS faq (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question VARCHAR(200) NOT NULL,
    answer VARCHAR(200) NOT NULL
);



CREATE TABLE IF NOT EXISTS hotels (
    id_hotel INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(80) NOT NULL,
    description VARCHAR(500) NOT NULL,
    image VARCHAR(120),
    cant_rooms INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE hotels
  ADD KEY location_disponibility (location);



CREATE TABLE IF NOT EXISTS type_rooms (
    id_room INT AUTO_INCREMENT PRIMARY KEY,
    id_hotel INT,
    type_room VARCHAR(80) NOT NULL,
    title VARCHAR(80) NOT NULL,
    description VARCHAR(500) NOT NULL,
    image VARCHAR(120),
    price FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_hotel) REFERENCES hotels (id_hotel)
);

ALTER TABLE type_rooms
  ADD KEY id_hotel (id_hotel);

ALTER TABLE type_rooms
  MODIFY id_room AUTO_INCREMENT=209;



CREATE TABLE IF NOT EXISTS rooms_disponibility (
    id_room INT NOT NULL,
    type_room VARCHAR(80) NOT NULL,
    number_room INT NOT NULL,
    floor_room INT NOT NULL,
    FOREIGN KEY (id_room) REFERENCES type_rooms(id_room)

);



CREATE TABLE IF NOT EXISTS occupation_rooms (
    id_occupied INT AUTO_INCREMENT PRIMARY KEY,
    id_room INT NOT NULL,
    check_in TIMESTAMP NOT NULL,
    check_out TIMESTAMP NOT NULL,
    FOREIGN KEY (id_room) REFERENCES rooms_disponibility (id_room)
)

ALTER TABLE occupation_rooms
  MODIFY id_occupied AUTO_INCREMENT=2;



CREATE TABLE IF NOT EXISTS reservations (
    id_reservation INT AUTO_INCREMENT PRIMARY KEY,
    id_user INT NOT NULL,
    id_room INT,
    id_hotel INT,
    number_people INT,
    type_room INT,
    check_in TIMESTAMP,
    check_out TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_user) REFERENCES users (id_user),
    FOREIGN KEY (id_room) REFERENCES rooms_disponibility (id_room),
    FOREIGN KEY (id_hotel) REFERENCES hotels (id_hotel)
);

ALTER TABLE reservations
  ADD KEY id_user (id_user),
  ADD KEY id_room (id_room),
  ADD KEY id_hotel (id_hotel);