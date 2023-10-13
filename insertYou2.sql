
use youtube2;
INSERT IGNORE INTO categories ("name")
VALUES ("Mais Curtidos"), ("Animação"), ("Esportes"), ("Notícias"), ("Jogos"), ("Podcasts"), ("Educação");

insert into usuario (id, birthday, name, email, created_at, registered)
VALUES (1, "2000-01-02","Antônio dos Santos", "santos@gmail.com", now(), true), (2,"2001-04-12", "Maria de Jesus", "jesus@outlook.com", now(), true), 
		(3,"2013-04-18", "José da Silva", "silva@gmail.com",now(),false),(4, "1998-05-10", "Marcia Rocha", "rocha@yahoo.com", now(), True),
        (5, "1990-03-11", "Marcos Antonio de Lima", "lima@outlook.com",now(), true),(6, "1987-12-19", "Vinicius Prado", "prado@gmail.com",now(), False ),
        (7,"1995-07-8", "Sabrina Antunes", "antunes@hotmail.com",now(), True ),(8,"1992-01-12", "Luiz Antonio Junior", "junior@hotmail.com",now(), True),
        (9,"1992-01-13", "André Giovanni", "vanni@hotmail.com",now(), True),(10,"2003-10-21", "João Junior", "jjao@hotmail.com",now(), True);
insert into videos (title, description,usuario_id, category_id,created_at)
VALUES ("Aulão de Banco de Dados", "Aula de 50 minutos com o básico do MYSQL",5, 7,now()),
		("Decadência do Coxa", "Fatos que contribuiram para aqueda do Coxa",8,3,now()),
        ("Meu primeiro desenho animado", "minha primeira tentativa ao fazer desenho animado, tomara que gostem",2,2,now()),
        ("Explorador dos 5 mares", "maior hit do album Navegar",1,1,now()),
        ("Zerando 100% em 1 dia", "Vou tentar zerar tudo em 24h",4,5,now()),
        ("Polêmica com Xamuel", "Schurer fala sobre Xamuel",7,6,now());
