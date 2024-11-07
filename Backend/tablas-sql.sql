CREATE TABLE IF NOT EXISTS users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL,
    apellido VARCHAR(80) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono INT(10) NOT NULL,
    password VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);

CREATE TABLE IF NOT EXISTS hotel (
    id_hotel INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(80) NOT NULL,
    description VARCHAR(500) NOT NULL,
    image VARCHAR(120),
    cant_rooms INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);

CREATE TABLE IF NOT EXISTS rooms (
    id_room INT AUTO_INCREMENT PRIMARY KEY,
    id_hotel INT,
    number_room INT (3),
    title VARCHAR(80) NOT NULL,
    description VARCHAR(500) NOT NULL,
    image VARCHAR(120),
    max_guests INT NOT NULL,
    price FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_hotel) REFERENCES hotel(id_hotel)
);

CREATE TABLE IF NOT EXISTS reservations (
    id_user INT,
    id_room INT,
    id_hotel INT,
    number_room INT (3),
    check_in TIMESTAMP,
    check_out TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_user) REFERENCES users(id_user),
    FOREIGN KEY (id_room) REFERENCES rooms(id_room),
    FOREIGN KEY (id_hotel) REFERENCES hotel(id_hotel)
);
