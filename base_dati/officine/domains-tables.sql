create table Nazione(
    nome varchar not null,
    primary key(nome)
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

create table Officina(
    nome varchar not null,
    indirizzo Indirizzo not null,
    id integer not null,
    citta varchar not null,
    regione varchar not null,
    nazione varchar not null,
    primary key(id),
    foreign key(citta,regione,nazione) references Citta(nome,regione,nazione)
);

create table Riparazione(
    riconsegna timestamp,
    codice integer not null,
    inizio timestamp not null,
    officina integer not null,
    veicolo targa not null,
    primary key (codice),
    foreign key (officina) references Officina(id)
    foreign key (veicolo) references Veicolo(targa)
);

create table Marca(
    nome varchar not null,
    primary key (nome)
);

create table Modello(
    nome varchar not null,
    marca varchar not null,
    tipoveicolo varchar not null,
    primary key(nome, marca),
    foreign key marca references Marca(nome),
    foreign key tipoveicolo references TipoVeicolo(nome)
);

create table TipoVeicolo(
    nome varchar not null
    primary key (nome)
);

create table Veicolo(
    targa Targa not null,
    immatricolazione integer not null,
    modello varchar not null,
    marca varchar not null,
    cliente CodFisc not null,
    primary key(targa),
    foreign key (modello,marca) references Modello(nome,marca)
    foreign key (cliente) references Cliente(persona)
);

create table Cliente(
    persona CodFisc not null,
    primary key (persona),
    foreign key (persona) references Persona(cf),
    v.incl.persona occorre in Veicolo(cliente)
);

create table Persona(
    cf CodFisc not null,
    nome varchar not null,
    indirizzo Indirizzo not null,
    telefono varchar not null,
    primary key (cf),
    
)