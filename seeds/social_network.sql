/*

As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

NOUNS - account, email, username, posts, title, content, views

DESIGN

account
id | email | username

posts
id | title | content | views | account_id

*/

DROP TABLE IF EXISTS accounts:
DROP TABLE IF EXISTS posts;

DROP SEQUENCE IF EXISTS account_id_seq;
DROP SEQUENCE IF EXISTS post_id_seq;

CREATE SEQUENCE account_id_seq;
CREATE SEQUENCE post_id_seq;

CREATE TABLE accounts (
    id serial PRIMARY KEY ,
    email VARCHAR(255),
    username VARCHAR(255)
);

CREATE TABLE posts (
    id serial PRIMARY KEY ,
    title VARCHAR(255),
    content VARCHAR(255),
    views INTEGER,
    account_id INTEGER,
    constraint fk_account_id foreign key (account_id) references accounts(id) on delete cascade
);

INSERT INTO accounts (email, username) VALUES ('johnsmith@gmail.com', 'johnsmith');
INSERT INTO accounts (email, username) VALUES ('johndoe@outlook.com', 'johndoe');
INSERT INTO accounts (email, username) VALUES ('katemoor@hotmail.com', 'katemoor');
INSERT INTO posts (title, content, views, account_id) VALUES ('My first post', 'This is my first post', 0, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('My second post', 'This is my second post', 0, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('Success', 'I got the job!', 2, 3);