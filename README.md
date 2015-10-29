table creation:
CREATE TABLE tbl_entry ( id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, amt FLOAT NOT NULL, date DATE NOT NULL, description VARCHAR(64),  category  VARCHAR(64) NOT NULL);
CREATE TABLE tbl_entry ( id serial PRIMARY KEY, amt FLOAT NOT NULL, date DATE NOT NULL, description VARCHAR(64),  category  VARCHAR(64) NOT NULL);


heroku pg:psql --app heroku-postgres-4739976d

git status
git add <file names>
git commit -m"message"

git push
password: i2118

git push heroku master