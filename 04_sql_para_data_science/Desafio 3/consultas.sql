select * 
from cancion 
where artista in 
  (select nombre_artista 
   from artista 
   where nacionalidad = 'Estadounidense' and fecha_de_nacimiento > '1992-12-31' limit 1) 
and numero_del_track = 4;