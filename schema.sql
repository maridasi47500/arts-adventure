create table if not exists user(
        id integer primary key autoincrement,
        email text,
            username text,
            date_joined text,
            password text,
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
