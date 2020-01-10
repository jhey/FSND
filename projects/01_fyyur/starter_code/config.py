import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://postgres@localhost:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# INSERT INTO "Venue" (id, name, city, state, address, phone, image_link, facebook_link) VALUES(1, 'The Musical Hop', 'San Francisco', 'CA', '444 Roseville', '6512222222', 'link', 'link2');

# create database fyyur;   
# DROP DATABASE target_database;

# \c fyyur


# create table book(                                                      
#     id integer,                                                                     
#     description varchar not null);

# INSERT INTO book (id, description) VALUES (1, 'The Mus');
# SELECT * from book;

# DELETE FROM book • WHERE id = 1;

# DROP TABLE book;

# flask db init;
# flask db migrate;
# flask db upgrade;

#SELECT * from "Artist";

#
# INSERT INTO public."Artist"(
# 	id, name, city, state, phone, genres, image_link, facebook_link)
# 	VALUES (2, 'smit oke', 'okok', '["okok", "rap" ]', 'okok', 'okok', 'okok', 'okok');


# INSERT INTO public."Artist"(
# 	id, name, city, state, phone, genres, image_link, facebook_link)
# 	VALUES (4, 'amikeoke', 'Houston', 'Texas', '832-555-5555', '"rap", "pop"', 'https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80', 'https://www.facebook.com/groups/houstontattooartists/');

# INSERT INTO public."Artist"(
# 	id, name, genres, city, state, phone, website, facebook_link, seeking_venue, seeking_description, image_link)
# 	VALUES (3, 'iceice',  'rap,two', 'Houston', 'Texas', '832-555-5555', 'www.jhey.com', 'fb.com/jhey', True, 'got jobs ?', 'https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80');

# INSERT INTO public."Artist"(
# 	id, name, genres, city, state, phone, website, facebook_link, seeking_venue, seeking_description, image_link)
# 	VALUES (4, 'iceice',  'rap,two', 'Houston', 'Texas', '832-555-5555', 'www.jhey.com', 'fb.com/jhey', True, 'got jobs ?', 'https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80');


# https://picsum.photos/200/300?grayscale
# https://i.picsum.photos/id/237/200/300.jpg
# https://i.picsum.photos/id/200/200/200.jpg


# INSERT INTO public."Venue"(
# 	id, name, city, state, address, phone, image_link, facebook_link, genres, seeking_description, seeking_talent, website)
# 	VALUES (3, 'cafehtx', 'Houston', 'Texas', '123 Main st.', '832-555-5555', 'img', 'fb.com/url', '[one,two]', 'looking 4 art', TRUE, 'www.com');

# INSERT INTO public."Venue"(
# 	id, name, city, state, address, phone, image_link, facebook_link, genres, seeking_description, seeking_talent, website)
# 	VALUES (4, 'RockCafe', 'Houston', 'Texas', '123 Main st.', '832-555-5555', 'https://i.picsum.photos/id/237/200/300.jpg', 'fb.com/url', 'abcx', 'hiring talent', TRUE, 'www.com.com');


# INSERT INTO public."Show"(
# 	id, venue_id, artist_id, start_time)
# 	VALUES (2, 3, 2, '2035-04-01T20:00:00.000Z');

# INSERT INTO public."Show"(
# 	id, venue_id, artist_id, start_time, artist_image_link, artist_name)
# 	VALUES (4, 3, 2, '2035-04-01T20:00:00.000Z', ' https://picsum.photos/200/300?grayscale', 'name of artist herer');

# INSERT INTO public."Show"(
# 	id, venue_id, artist_id, start_time, artist_image_link, artist_name, venue_name)
# 	VALUES (8, 3, 3, '2020-04-01T20:00:00.000Z', 'https://picsum.photos/200/200?grayscale', 'fitzgeraols', 'banda');


# DELETE FROM "Show"
# WHERE "Show".id = 3;

# DELETE FROM "Artist"
# WHERE "Artist".id = 1

# export FLASK_APP=app
# export FLASK_DEBUG=1 
# flask run


# https://{{YOUR_DOMAIN}}/authorize?audience={{API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}

# https://https://brighth20.auth0.com/authorize?audience=image&response_type=token&client_id=jy3eCPD6Xa3gn1vnQp6Fl4orugNX49xA&redirect_uri=http://localhost:8080/login-results

