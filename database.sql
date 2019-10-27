DROP TABLE IF EXISTS food_menu_voting_app.employee;
DROP TABLE IF EXISTS food_menu_voting_app.menu;
DROP TABLE IF EXISTS food_menu_voting_app.restaurant;


CREATE TABLE IF NOT EXISTS food_menu_voting_app.employee(
    id INT(11) PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(30) UNIQUE,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(128) NOT NULL
)ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS food_menu_voting_app.restaurant(
    id INT(11) PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) UNIQUE,
    telephone VARCHAR(12) NOT NULL
)ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS food_menu_voting_app.menu(
    id INT(11) PRIMARY KEY AUTO_INCREMENT,
    item VARCHAR(30) NOT NULL,
    description TEXT NOT NULL,
    votes INTEGER NOT NULL,
    restaurant_id INT(11) NOT NULL,
    _date DATE NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES restaurant(id) ON DELETE CASCADE
)ENGINE=INNODB;