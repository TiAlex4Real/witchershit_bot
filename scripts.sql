create table if not exists witcher_log
(
	chat_id int primary key,
	last_enc date
);

create table if not exists nintendo_log
(
	chat_id int primary key,
	last_enc date
);

create table if not exists alive_log
(
    user_id int primary key,
    last_enc date,
    counter int default 0
);