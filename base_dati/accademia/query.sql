begin transaction;

select distinct Persona.cognome
from Persona

select nome, cognome
from Persona
where posizione = 'Ricercatore';

select cognome, nome
from Persona
where posizione = 'Professore Associato' and cognome like 'V%';

select cognome, nome
from Persona
where (posizione = 'Professore Associato' or posizione = 'Professore Ordinario') and cognome like 'V%';

select nome
from Progetto
where fine < current_date;

select nome
from Progetto
order by inizio;

select nome
from WP
order by nome;

select distinct Assenza.tipo
from Assenza;

select distinct AttivitaProgetto.tipo
from AttivitaProgetto;

select distinct AttivitaNonProgettuale.giorno
from AttivitaNonProgettuale
where AttivitaNonProgettuale.tipo = 'Didattica';

