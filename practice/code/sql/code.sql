DROP DATABASE IF EXISTS cinema;
CREATE DATABASE IF NOT EXISTS cinema;
USE cinema;

-- -----------------------------------
----------- administrators -----------
-- -----------------------------------
CREATE TABLE IF NOT EXISTS admins(
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    names VARCHAR(25) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
    last_name_m VARCHAR(15),
    job_title VARCHAR(25) NOT NULL,
    birthdate DATE NOT NULL,
    PRIMARY KEY(username)
)ENGINE = InnoDB;

-- -----------------------------------
---------------- users ---------------
-- -----------------------------------
CREATE TABLE IF NOT EXISTS users(
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    names VARCHAR(25) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
    last_name_m VARCHAR(15),
    birthdate DATE NOT NULL,
    PRIMARY KEY(username)
)ENGINE = InnoDB;

-- -----------------------------------
---------------- movies --------------
-- -----------------------------------
CREATE TABLE IF NOT EXISTS movies(
    movie_id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(25),
    duration INT NOT NULL,
    sinopsis VARCHAR(150) NOT NULL,
    director VARCHAR(35) NOT NULL,
    genre VARCHAR(15) NOT NULL,
    rating VARCHAR(5) NOT NULL,
    release_date DATE NOT NULL,
    PRIMARY KEY(movie_id)
)ENGINE = InnoDB;

-- -----------------------------------
---------------- halls ---------------
-- -----------------------------------
CREATE TABLE IF NOT EXISTS halls(
    hall_id VARCHAR(5) NOT NULL,
    hall_type VARCHAR(15),
    n_rows INT NOT NULL,
    n_seats_row INT NOT NULL,
    PRIMARY KEY(hall_id)
)ENGINE = InnoDB;

-- -----------------------------------
-------------- schedules -------------
-- -----------------------------------
CREATE TABLE IF NOT EXISTS schedules(
    schedule_id INT NOT NULL AUTO_INCREMENT,
    movie_id INT NOT NULL,
    hall_id VARCHAR(5) NOT NULL,
    day DATE,
    hour TIME,
    PRIMARY KEY(schedule_id),
    CONSTRAINT fk_schedules_movies FOREIGN KEY(movie_id)
        REFERENCES movies(movie_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_schedules_halls FOREIGN KEY(hall_id)
        REFERENCES halls(hall_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
)ENGINE = InnoDB;

-- -----------------------------------
---------------- seats ---------------
-- -----------------------------------
CREATE TABLE IF NOT EXISTS seats(
    seat_id INT NOT NULL AUTO_INCREMENT,
    schedule_id INT NOT NULL,
    row VARCHAR(1) NOT NULL,
    number INT NOT NULL,
    aviable SET('N', 'Y'),
    PRIMARY KEY(seat_id),
    CONSTRAINT fk_seats_schedules FOREIGN KEY(schedule_id)
        REFERENCES schedules(schedule_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
)ENGINE = InnoDB;

-- -----------------------------------
--------------- tickets --------------
-- -----------------------------------
CREATE TABLE IF NOT EXISTS tickets(
    seat_id INT NOT NULL,
    username VARCHAR(20) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    buy_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(seat_id, username),
    CONSTRAINT fk_tickets_seats FOREIGN KEY(seat_id)
        REFERENCES seats(seat_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_tickets_users FOREIGN KEY(username)
        REFERENCES users(username)
        ON UPDATE CASCADE
        ON DELETE CASCADE
)ENGINE = InnoDB;