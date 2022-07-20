DROP TABLE IF EXISTS want_to_visit;
DROP TABLE IF EXISTS vistited;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS users;


CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    continent VARCHAR(255) NOT NULL
);

CREATE TABLE cities(
    id SERIAL PRIMARY KEY,
    country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
    name VARCHAR(255),
    attraction_1 VARCHAR(255),
    attraction_2 VARCHAR(255),
    attraction_3 VARCHAR(255),
    UNIQUE(name, country_id)
);

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    password VARCHAR(255),
    logged_in BOOLEAN DEFAULT false
);

CREATE TABLE vistited (
    id SERIAL PRIMARY KEY,
    city_id INT NOT NULL REFERENCES cities(id) ON DELETE CASCADE UNIQUE,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE(city_id, user_id)
);
CREATE TABLE want_to_visit (
    id SERIAL PRIMARY KEY,
    city_id INT NOT NULL REFERENCES cities(id) ON DELETE CASCADE,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE(city_id, user_id)
);