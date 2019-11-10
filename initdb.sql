create table if not exists function_log
(
    function text,
    chat_id int,
    user_id int,
    encounter date,
    misc text
);

create table if not exists status_texts
(
    text_id integer primary key autoincrement,
    text text
);
insert into status_texts(text) values ('Сука, падла');
insert into status_texts(text) values ('Где тут дрын, какой-нибудь?!');
insert into status_texts(text) values ('Никак вы, блять, не научитесь');
insert into status_texts(text) values ('Вот ссука');
insert into status_texts(text) values ('Статус, статус. Хуй те а не статус!');
insert into status_texts(text) values ('Лютик, блять!');
insert into status_texts(text) values ('Я тя на хер пошлю, ты меня. И чё?\nОбнимемся и вместе пойдем');
insert into status_texts(text) values ('С нами лучше не балуй.\nЛишь бы цел остался...');
insert into status_texts(text) values ('Найдите себе другое развлечение. Не знаю, наловите лягушек, навставляйте им в жопы соломинок');
insert into status_texts(text) values ('Ламберт, Ламберт, хер моржовый.\nЛамберт, Ламберт, вредный хуй.');

create table if not exists nintendo_texts
(
    text_id integer primary key autoincrement,
    text text
);
insert into nintendo_texts(text) values ('Нинтендо сосёт');
insert into nintendo_texts(text) values ('Свитч хрень, игор нет');
insert into nintendo_texts(text) values ('А сонька круче');
