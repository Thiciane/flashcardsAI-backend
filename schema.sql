create table if not exists category (
    id primary key autoincrement,
    name varchar(255) not null unique
);

create table if not exists word (
    id primary key autoincrement,
    word varchar(150) not null,
    translation varchar(150) not null,
    category_id integer references category(id)
);

create table if not exists deck (
    id primary key autoincrement,
    title varchar(100) not null,
    description varchar(500)
);

create table if not exists deck_word (
    deck_id integer references deck(id),
    word_id integer references word(id),
    primary key (deck_id, word_id)
);


INSERT INTO category (name) VALUES ('Adjetivo'), ('Advérbio'), ('Conjunção'), ('Interjeição'), ('Substantivo'), ('Artigo'), ('Preposição'), ('Outro'), ('Numeral'), ('Pronome'), ('Verbo');
