CREATE TABLE users(id SERIAL PRIMARY KEY, email TEXT unique, "name" varchar(255), password varchar(64) );

CREATE TYPE beer_style AS ENUM ('IPA', 'Stout');
CREATE TABLE beers(
    id SERIAL PRIMARY KEY, 
    user_id integer not null, 
    "name" TEXT not null, 
    image_url text,   
    "type" varchar(30),  
    miscellaneous TEXT, 
    style beer_style not null,
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(id) );
    
    


-- for style's will need to create specific parametres for each then an if statemnet to check if style parameters are true or false. 

