CREATE TABLE  IF NOT EXISTS contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id) 
      REFERENCES contacts (contact_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id) 
      REFERENCES groups (group_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '1', 'anonyme', 'noname', 'anonymous@email.fr', '+2653546434');
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '2', 'anne onim', 'onim', 'anne.onim@email.com', '+86877779898');
create table if not exists user(
        id integer primary key autoincrement,
        email text,
            username text,
            date_joined text,
            name text,
            country_id text,
            phone text,
            dateofbirth text
                    );
create table if not exists profile_image(
        id integer primary key autoincrement,
        user_id text,
            pic text
                    );
create table if not exists people_photos(
        id integer primary key autoincrement,
        profile_image_id text,
            personsname text
                    );
create table if not exists user_video(
        id integer primary key autoincrement,
        user_id text,
            vid text
                    );
create table if not exists radio_voice(
        id integer primary key autoincrement,
        user_id text,
            recording text
                    );
create table if not exists subscriber(
        id integer primary key autoincrement,
        user_id text,
            subscriber_id text
                    );
create table if not exists comment_photo(
        id integer primary key autoincrement,
        profile_image_id text,
            user_id text,
            content text
                    );
create table if not exists posts(
        id integer primary key autoincrement,
        user_id text,
            content text
                    );
create table if not exists country(
        id integer primary key autoincrement,
        name text
                    );
