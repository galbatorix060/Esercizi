create table Nazione(
    nome varchar not null,
    primary key (nome)
);

create table Regione(
    nome varchar not null,
    nazione varchar not null,
    primary key (nome,nazione)
    foreign key nazione references Nazione(nome)
);

create table Citta(
    nome varchar not null,
    regione varchar not null,
    nazione varchar not null,
    primary key(nome, regione, nazione),
    foreign key(regione, nazione) references Regione(nome, nazione)
);

create table Sede(
    id serial primary key not null,
    indirizzo indirizzo not null,
    nome varchar not null,
    citta varchar not null,
    regione varchar not null,
    nazione varchar not null,
    foreign key (citta,regione,nazione) references Citta(nome, regione, nazione)
);

create table Sala(
    nome varchar not null,
    sede integer not null,
    primary key (nome, sede),
    foreign key (sede) references Sede(id)
);

create table Settore(
    id serial primary key not null,
    nome varchar not null,
    sala varchar not null,
    sede integer not null,
    unique(nome,sala,sede),
    foreign key (sala, sede) references Sala(nome, sede)
);

create table Posto(
    fila integer not null,
    colonna integer not null,
    settore integer not null,
    primary key (fila,colonna,settore),
    foreign key settore references Settore (id)
);

create table Artista(
    nome varchar not null,
    cognome varchar not null,
    nome_arte varchar,
    id serial primary key not null,
);

create table TipologiaSpettacolo(
    nome varchar primary key not null
);

create table Genere(
    nome varchar primary key not null
):

create table Spettacolo(
    id serial not null,
    nome varchar not null,
    durata_min PosInteger not null,
    tipologiaspettacolo varchar not null,
    genere varchar not null,
    primary key (id),
    foreign key (tipologiaspettacolo) references TipologiaSpettacolo(nome),
    foreign key (genere) references Genere(nome)
    --v.incl id occore in Partecipa(spettacolo)
);

create table Spettacolo_Artista(
    spettacolo integer not null,
    artista integer not null,
    primary key(spettacolo,artista),
    foreign key spettacolo references Spettacolo(id),
    foreign key artista references Artista(id)
);

create table TipoTariffa(
    nome varchar not null,
    primary key nome
);

create table Tariffa(
    prezzo Denaro not null,
    tipotariffa varchar not null,
    settore 
);

create table Evento(
    id serial not null,
    data date not null,
    orario time not null,
    spettacolo integer not null,
    sala varchar not null,
    sede varchar not null,
    primary key (id, spettacolo,sala,sede),
    foreign key spettacolo references Spettacolo(id),
    foreign key (sala,sede) references Sala(nome,sede)
);

create table Pre_Posto(
    prenotazione integer not null,
    fila integer not null,
    colonna integer not null,
    settore integer not null,
    tipotariffa varchar not null,
    primary key (prenotazione, fila,colonna),
    foreign key prenotazione references Prenotazione(id),
    foreign key (fila, colonna, settore) references Posto(fila,colonna,settore),
    foreign key tipotariffa references TipoTariffa(nome)
);

create table Prenotazione(
    id serial primary key not null,
    evento integer not null,
    utente CF not null,
    foreign key evento references Evento(id),
    foreign key utente references Utente(cf)
);

create table Utente(
    nome varchar not null,
    cognome varchar not null,
    cf CF not null,
    primary key (cf)
);