-- creates city table inside usa db
CREATE database IF NOT EXISTS hbtn_0d_usa;
CREATE table IF NOT EXISTS hbtn_0d_usa.cities (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
		state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
		name VARCHAR(256) NOT NULL);
