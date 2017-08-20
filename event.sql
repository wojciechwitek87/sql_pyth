create database event;
use event;
CREATE TABLE uzytkownik (
    id_u INT NOT NULL AUTO_INCREMENT,
    imie_u TEXT,
    pseudo_u TEXT,
    sex_u TEXT,
    kraj_u TEXT,
    woj_u TEXT,
    miasto_u TEXT,
    haslo text, 
    PRIMARY KEY (id_u)
);

CREATE TABLE event_1 (
    id_e INT NOT NULL AUTO_INCREMENT,
    nazwa_e TEXT NOT NULL,
    ikraj_u TEXT,
    woj_u TEXT,
    miasto_u TEXT,
    data_es DATE,
    data_ek DATE,
    PRIMARY KEY (id_e)
); # foreign key (id_u) references organizator(id_u));  #ilosc_u int not null,  
CREATE TABLE goscie (
    id_g INT NOT NULL AUTO_INCREMENT,
    pseudo_g TEXT NOT NULL,
    kraj_g TEXT,
    woj_g TEXT,
    miasto_g TEXT,
    PRIMARY KEY (id_g)
); 
#create table info (id_e int not null auto_increment, dzielnica_e text,  opis text, foreign key (id_e) references organizator(id_e));
/*
CREATE TABLE info (
    id_e INT NOT NULL AUTO_INCREMENT,
    klasa TEXT,
    ile_os TEXT,
    diff TEXT,
);
CREATE TABLE klasa (
    id_e INT NOT NULL AUTO_INCREMENT,
    do_3 INT,
    od_4 INT
);
CREATE TABLE nr_os (
    id_e INT NOT NULL AUTO_INCREMENT,
    potrzeba INT,
    jest INT
);
CREATE TABLE diff (
    id_e INT NOT NULL AUTO_INCREMENT,
    stopien_trudnosci TEXT
);
*/
#drop table organizator;
#insert into event values (null, 'Szachy', 'Warszawa');

#drop table uzytkownik;
#select * from uzytkownik;

#drop table event_1;
#select * from event_1;

#drop database event; 
