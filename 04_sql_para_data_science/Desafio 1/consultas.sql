-- 1
create database biblioteca;

-- 2
create table libro(
	id_libro serial,
	nombre_libro varchar(100),
	autor varchar(50),
	genero char(50),
	PRIMARY KEY (id_libro)
);

-- 3
insert into libro (nombre_libro, autor, genero) VALUES ('Sapo y Sepo', 'Arnold Lobel', 'Infantil');

--4
insert into libro (nombre_libro, autor, genero) VALUES ('La metamorfosis', 'Franz Kafka', 'Novela');

-- 5
create table prestamo(
	id_prestamo serial PRIMARY KEY,
	id_libro integer REFERENCES libro(id_libro),
	nombre_persona varchar(50),
	fecha_inicio date,
	fecha_termino date
);

-- 6
alter table libro add column prestado boolean;

-- 7
update libro set prestado = false where nombre_libro = 'Sapo y Sepo';

-- 8
update libro set prestado = true where nombre_libro = 'La metamorfosis';

-- 9
insert into prestamo (id_libro, nombre_persona, fecha_inicio, fecha_termino) values (1, 'Amaury Gatica', '2019-08-01', '2019-08-05');
insert into prestamo (id_libro, nombre_persona, fecha_inicio, fecha_termino) values (1, 'Isaias Cardenas', '2019-08-06', '2019-08-10');
insert into prestamo (id_libro, nombre_persona, fecha_inicio, fecha_termino) values (1, 'Sergio Zepeda', '2019-08-11', '2019-08-15');
insert into prestamo (id_libro, nombre_persona, fecha_inicio, fecha_termino) values (1, 'Tania Torres', '2019-08-16', '2019-08-20');
insert into prestamo (id_libro, nombre_persona, fecha_inicio, fecha_termino) values (1, 'Gonzalo Correa', '2019-08-21', '2019-08-25');

-- 10
insert into prestamo (id_libro, nombre_persona, fecha_inicio, fecha_termino) values (2, 'Amaury Gatica', '2019-09-21', '2019-09-30');
insert into prestamo (id_libro, nombre_persona, fecha_inicio, fecha_termino) values (2, 'Isaias Cardenas', '2019-09-16', '2019-09-20');
insert into prestamo (id_libro, nombre_persona, fecha_inicio, fecha_termino) values (2, 'Sergio Zepeda', '2019-09-11', '2019-09-15');
insert into prestamo (id_libro, nombre_persona, fecha_inicio, fecha_termino) values (2, 'Tania Torres', '2019-09-06', '2019-09-10');
insert into prestamo (id_libro, nombre_persona, fecha_inicio, fecha_termino) values (2, 'Gonzalo Correa', '2019-09-01', '2019-09-05');
insert into prestamo (id_libro, nombre_persona, fecha_inicio, fecha_termino) values (2, 'Hernán Paz', '2019-10-01', '2019-10-05');

-- 11
insert into libro (nombre_libro, autor, genero) VALUES ('El principito', 'Antoine de Saint-Exupéry', 'Fábula');

-- 12
select libro.nombre_libro, prestamo.nombre_persona
from libro
inner join prestamo on libro.id_libro = prestamo.id_libro
order by libro.nombre_libro, prestamo.fecha_inicio;

-- 13
select prestamo.* from prestamo
inner join libro on libro.id_libro = prestamo.id_libro
where libro.nombre_libro = 'Sapo y Sepo'
order by prestamo.fecha_inicio desc;
