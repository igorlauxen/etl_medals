# SQL commands to be executed

SQLite cant create Foreing Keys during table creation so we have to add later. Check more information in [this stackoverflow question](https://stackoverflow.com/questions/1884818/how-do-i-add-a-foreign-key-to-an-existing-sqlite-table)

## Commands

### Atletas

```
ALTER TABLE atletas ADD COLUMN pais_id INTEGER REFERENCES paises(id);
ALTER TABLE atletas ADD COLUMN jogo_id INTEGER REFERENCES jogos(id);
ALTER TABLE atletas ADD COLUMN time_id INTEGER REFERENCES times(id);
```

### Treinadores

```
ALTER TABLE treinadores ADD COLUMN pais_id INTEGER REFERENCES paises(id);
ALTER TABLE treinadores ADD COLUMN jogo_id INTEGER REFERENCES jogos(id);
ALTER TABLE treinadores ADD COLUMN evento_id INTEGER REFERENCES eventos(id);
```

### Medalhas

ALTER TABLE medalhas ADD COLUMN pais_id INTEGER REFERENCES paises(id);

### Times

```
ALTER TABLE times ADD COLUMN pais_id INTEGER REFERENCES paises(id); 
ALTER TABLE times ADD COLUMN jogo_id INTEGER REFERENCES jogos(id);
ALTER TABLE times ADD COLUMN evento_id INTEGER REFERENCES eventos(id);
```

