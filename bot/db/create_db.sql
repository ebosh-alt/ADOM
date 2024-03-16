create table users(
    id integer primary key,
    count_message integer,
    count_day integer,
    username varchar(200),
    ref_link varchar(200),
    subscribe varchar(200),
    type_ai varchar(200)
);
drop table users;