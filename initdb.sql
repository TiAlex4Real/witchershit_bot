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
replace into status_phrases values (1, 'Сука, падла');
replace into status_phrases values (2, 'Ща господин ведьмак вам таких пиздюлей отвесит, вовек не забудете! Где тут дрын какой-нибудь?!');
replace into status_phrases values (3, 'Никак вы, блядь, не научитесь');
replace into status_phrases values (4, 'Вот сука');
replace into status_phrases values (5, 'Статус, статус. Хуй те а не статус!');
replace into status_phrases values (6, 'Лютик, блядь!');
replace into status_phrases values (7, 'Отъебись, Ламберт.');
replace into status_phrases values (8, 'А у третьей нету правил, лишь бы кто-нибудь да вставил.');
replace into status_phrases values (9, 'Найдите себе другое развлечение. Не знаю, наловите лягушек, навставляйте им в жопы соломинок');

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
replace into nintendo_phrases values (1, 'Играть на свитче до сих пор не во что.');
replace into nintendo_phrases values (2, 'Зельда и Марио - наше всё.');
replace into nintendo_phrases values (3, 'Больше переизданий игр 10-летней давности!');
replace into nintendo_phrases values (4, 'Эксклюзивы? Не, не слышал.');
replace into nintendo_phrases values (5, 'Батя тут чуть не спалил что у меня свитч. Пришлось сказать что я гей.');
replace into nintendo_phrases values (6, 'Говорят, Марио спит с Луиджи. Потому что на нинтендо ему больше не с кем спать.');

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


create table if not exists miss_me_log
(
	chat_id integer primary key,
	last_enc text
);
