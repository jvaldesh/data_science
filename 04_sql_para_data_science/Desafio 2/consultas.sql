-- 1
create database spotify;

create table artista(
	nombre_artista varchar(100) primary key,
	fecha_de_nacimiento date,
	nacionalidad varchar(50)
);

create table cancion(
	titulo_cancion varchar(100) primary key,
	artista varchar(100) references artista(nombre_artista),
	album varchar(100),
	numero_del_track integer
);

create table album(
	titulo_album varchar(100) primary key,
	artista varchar(100) references artista(nombre_artista),
	anio integer
);

-- 2
copy artista(nombre_artista, fecha_de_nacimiento, nacionalidad) from '/Users/julio/Data science con python/04_sql_para_data_science/Desafio 2/Artista.csv' delimiters ',' NULL as ' ' csv header encoding 'latin1';
copy album(titulo_album, artista, anio) from '/Users/julio/Data science con python/04_sql_para_data_science/Desafio 2/Album.csv' delimiters ',' NULL as ' ' csv header encoding 'latin1';
copy cancion(titulo_cancion, artista, album, numero_del_track) from '/Users/julio/Data science con python/04_sql_para_data_science/Desafio 2/Cancion.csv' delimiters ',' NULL as ' ' csv header encoding 'latin1';

select cancion.titulo_cancion from cancion
inner join album on cancion.album = album.titulo_album
where album.anio = 2018;

select album.titulo_album, artista.nacionalidad from album
inner join artista on album.artista = artista.nombre_artista
order by album.titulo_album;

select cancion.numero_del_track, cancion.titulo_cancion, album.titulo_album, album.anio, artista.nombre_artista
from cancion
inner join album on cancion.album = album.titulo_album
inner join artista on cancion.artista = artista.nombre_artista
order by album.anio, album.titulo_album, artista.nombre_artista;