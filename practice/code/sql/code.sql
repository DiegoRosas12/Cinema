DROP cinema;
CREATE DATABASE IF NOT EXISTS cinema;
USE cinema;

CREATE TABLE IF NOT EXISTS admins(
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    names VARCHAR(25),
    last_name VARCHAR(15),
    last_name_m VARCHAR(15),
    job title VARCHAR(25),
    birthdate DATE NOT NULL,
    PRIMARY KEY(username)
);

CREATE TABLE IF NOT EXISTS users(
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    names VARCHAR(25),
    last_name VARCHAR(15),
    last_name_m VARCHAR(15),
    birthdate DATE NOT NULL,
    PRIMARY KEY(username)
);

CREATE TABLE IF NOT EXISTS movies(
    movie_id INT NOT NULL,
    title VARCHAR(25),
    duration INT NOT NULL,
    sinopsis VARCHAR(150) NOT NULL,
    director VARCHAR(35) NOT NULL,
    genre VARCHAR(15) NOT NULL,
    rating VARCHAR(5) NOT NULL,
    release DATE NOT NULL,
    PRIMARY KEY(movie_id)
);

CREATE TABLE IF NOT EXISTS halls(
    hall_id VARCHAR(5) NOT NULL,
    type VARCHAR(10),
    n_rows INT NOT NULL,
    n_sets_row INT NOT NULL,
    PRIMARY KEY(hall_id)
);

CREATE TABLE IF NOT EXISTS schedules(
    schedule_id INT NOT NULL,
    movie_id INT NOT NULL,
    hall_id VARCHAR(5) NOT NULL,
    day DATE,
    hour TIME,
    PRIMARY KEY(schedule_id),
    CONSTRAINT fk_schedules_movies FOREIGN KEY
        REFERENCES movies(movie_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_schedules_halls FOREIGN KEY
        REFERENCES halls(hall_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS seats(
    seat_id INT NOT NULL,
    schedule_id INT NOT NULL,
    row VARCHAR(1) NOT NULL,
    number INT NOT NULL,
    aviable SET('N', 'Y'),
    PRIMARY KEY(seat_id),
    CONSTRAINT fk_seats_schedules FOREIGN KEY
        REFERENCES schedules(schedule_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tickets(
    seat_id INT NOT NULL,
    username VARCHAR(20) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY(seat_id, username),
    CONSTRAINT fk_tickets_seats FOREIGN KEY
        REFERENCES seats(seat_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_tickets_users FOREIGN KEY
        REFERENCES users(username)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);