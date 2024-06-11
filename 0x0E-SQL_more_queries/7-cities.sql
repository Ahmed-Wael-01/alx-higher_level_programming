-- creates city table inside usa db
CREATE database IF NOT EXISTS hbtn_0d_usa;
CREATE table IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
		state_id INT NOT NULL FOREIGN KEY REFERENCES state(id),
		name VARCHAR(256) NOT NULL);
