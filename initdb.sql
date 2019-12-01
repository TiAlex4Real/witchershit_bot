create table if not exists witchershit_log
(
	chat_id integer primary key,
	last_enc text
);


create table if not exists status_phrases
(
    phrase_id integer primary key,
    text text
);
insert or ignore into status_phrases values (1, 'Сука, падла');
insert or ignore into status_phrases values (2, 'Ща господин ведьмак вам таких пиздюлей отвесит, вовек не забудете! Где тут дрын какой-нибудь?!');
insert or ignore into status_phrases values (3, 'Никак вы, блядь, не научитесь');
insert or ignore into status_phrases values (4, 'Вот сука');
insert or ignore into status_phrases values (5, 'Статус, статус. Хуй те а не статус!');
insert or ignore into status_phrases values (6, 'Лютик, блядь!');
insert or ignore into status_phrases values (7, 'Отъебись, Ламберт.');
insert or ignore into status_phrases values (8, 'А у третьей нету правил, лишь бы кто-нибудь да вставил.');
insert or ignore into status_phrases values (9, 'Найдите себе другое развлечение. Не знаю, наловите лягушек, навставляйте им в жопы соломинок');

create table if not exists status_log
(
    chat_id integer,
	phrase_id integer,
    encounter text
);

create trigger if not exists sl_autoclean before insert on status_log begin
    delete from status_log where encounter < datetime('now', '-1 month');
end;


create table if not exists nintendo_phrases
(
    phrase_id integer primary key,
    text text
);
insert or ignore into nintendo_phrases values (1, 'А играть на свитче до сих пор не во что.');
insert or ignore into nintendo_phrases values (2, 'Сонька всё равно круче.');
insert or ignore into nintendo_phrases values (3, 'Зельда и Марио - наше всё.');
insert or ignore into nintendo_phrases values (4, 'Больше переизданий игр 10-летней давности!');
insert or ignore into nintendo_phrases values (5, 'Эксклюзивы? Не, не слышал.');

create table if not exists nintendo_log
(
	chat_id integer,
	phrase_id integer,
	encounter text
);

create trigger if not exists nl_autoclean before insert on nintendo_log begin
    delete from nintendo_log where encounter < datetime('now', '-1 month');
end;


create table if not exists beautiful_log
(
	chat_id integer primary key,
	last_enc text
);
