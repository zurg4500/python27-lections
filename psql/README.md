# Slash commands\Слэш команды
* \l - список всех баз данных
* \c - показывает через какого юзера и к какой базе данных мы подключены
* \с name_of_db - подключение к какой-то базе данных
* \du - список всех юзеров в postges
* \dt - список всех таблиц в текущей базе данных
* \d+ - более подробная информация о таблицах в текущей базе данных
* \d+ название_таблицы - более подробная информация о конретной таблице с данным названием
* \q - выход с СУБД(Система Управления Базой Данных/psql)


# Создание баз данных и таблиц
```sql
CREATE DATABASE name_of_db;
-- создание базы данных
```

```sql
CREATE TABLE name_of_table (
    column1 data_type1,
    column2 data_type2,
    ...
);
-- создание таблицы с полями
```

# Удаление базы данных и таблиц
```sql
DROP DATABASE name_of_db;
-- удаление базы данных
```

```sql
DROP TABLE name_of_table;
-- удаление таблиц
```

# Заполнение таблиц
```sql
INSERT INTO name_of_db VALUES
(val1, val2),
(val1.2, val2.2);
-- запись данных  таблицу(заполнение всех полей)
```

# Вывод данных из таблицы
```sql
SELECT * FROM name_of_table;
-- вывод всех записей со всеми полями
```

```sql
SELECT column1, column3 FROM name_of_table;
-- вывод конкретных полей
```

# Условия
```sql
DELETE FROM name_of_table WHERE condition;
-- удаление всех записей из таблицы соответсвующих данному условию
```
```sql
DELETE FROM name_of_table WHERE column = 'hello';
-- строгое равенство
```
```sql
DELETE FROM name_of_table WHERE column LIKE '%hello';
-- записи включающие в себя данную строку с учетом регистра
-- aaahello
-- hello world
-- hello
-- Hello world - не пройдет (потому что регистр другой)
```

```sql
SELECT * FROM name_of_table WHERE column ILIKE '%hello%';
-- записи включающие в себя данную строку без учета регистра
-- aaahello
-- hello world
-- hello
-- Hello world 
-- HeLLosql
```

```sql
SELECT * FROM name_of_table ORDER BY column;
-- сортировка записей по данному полю в порядке возрастания
```

```sql
SELECT * FROM name_of_table ORDER BY column DESC;
-- сортировка записей по данному полю в порядке возрастания
```

```sql
SELECT * FROM name_of_table LIMIT 10;
-- вывод первых 10 записей
```

```sql
SELECT * FROM name_of_table OFFSET 10;
-- пропускаем первые 10 записей
```

```sql
SELECT * FROM name_of_table LIMIT 10 OFFSET 5;
-- пропускаем первые 5 записей
-- вытаскиваем 10 записей
```
# Обновление таблицы
```sql
ALTER TABLE name_of_table ADD COLUMN col_name col_type constraint;
-- добавляем новую колонку в таблицу
```

```sql
ALTER TABLE name_of_table DROP COLUMN col_name;
-- удаляем колонку из таблицы
```

```sql
ALTER TABLE name_of_table RENAME COLUMN col_name TO new_col_name;
-- переименовывание колонки
```

```sql
ALTER TABLE name_of_table ALTER COLUMN col_name SET DATA TYPE new_type;
-- изменение типа данных у поля
```

# Ограничения (constraints)
* UNIQUE - не разрешает дубликаты
* NOT NULL - требует обязательного заполнения поля
* PRIMARY KEY - как UNIQUE и NOT NULL + строит binary tree для быстрого поиска
* FOREIGN KEY - ссылается на pk в другой таблице и проверяет, существует ли такое id

# Связи
## Виды связей
> Один к одному (one to one)
* один человек - один профиль
* один человек - одна автобиография

> Один ко многим (one to many)
* один блогер - много постов
* одна марка - много моделей
* одна страна - много областей\штатов\колоний
* один продукт - много комментариев

> Многие ко многим (many to many)
* один разработчик - много проектов. один проект - много разработчиков
* один человек - много языков. один язык - много людей владеющих этим языком

## Реализация one2many в postgres

```sql
CREATE TABLE blogger (
    id serial PRIMARY KEY,
    name varchar(50),
    age int
);

CREATE TABLE post (
    id serial PRIMARY KEY,
    title varchar(100),
    body text,
    blogger_id int,

    CONSTRAINT fk_post_blogger
    FOREIGN KEY (blogger_id) REFERENCES blogger (id)
);
```

## реализация one2one в postgres
```sql
CREATE TABLE author (
    id serial PRIMARY KEY,
    name varchar(50),
    last_name varchar(70)
    );

CREATE TABLE authoboigraphy (
    id serial PRIMARY KEY,
    published date,
    body text,
    author_id int UNIQUE, -- чтобы создать one - one,
    добавляем unique

    CONSTRAINT fk_author_bio
    FOREIGN KEY (author_id) REFERENCES author (id)
    );  
```

## реализация manu2many в postgres
```sql
CREATE TABLE developer (
    id serial PRIMARY KEY,
    name varchar(50),
    age int,
    experience int
    );

CREATE TABLE project (
    id serial PRIMARY KEY,
    title varchar(100)
    tz text,
    deadline date,
    );

CREATE TABLE dev_proj (
    dev_id int,
    proj_id int,
    
    CONSTRAINT fk_dev_m2m
    FOREIGN KEY (dev_id) REFERENCES developer (id),

    CONSTRAINT fk_proj_m2m
    FOREIGN KEY (proj_id) REFERENCES project (id)
);
```


# Joins
> **JOIN** - инструкция, которая позволяет одним SELECT, брать данные из двух таблиц (у которых есть связанные поля)
> **INNER JOIN** (JOIN) - достаются только те записи у которых есть данные в обоих таблицах FULL JOIN - достаются все записи и с первой таблицы и со второй
> **FULL JOIN** - достаются все записи 

```sql
SELECT * FROM table1
 JOIN table2 ON table1.id = table2t_id;
```

```sql
--one to one / one to many
SELECT * FROM blogger
JOIN post ON blogger.id = post.blogger_id;
```

```sql
-- many to many
SELECT * FROM developer
JOIN dev_proj ON developer.id = dev_proj.dev_id
JOIN project ON project.id = dev_proj.proj_id;
```
# Агрегатные функции
> все агрегатные функции используются с group by
> **SUM** - считает сумму всех записей в сгруппированном поле

```sql
SELECT customer.name, SUM(product.price)
FROM customer
JOIN cart ON customer.id = cart.customer_id
JOIN product ON product.id = cart product_id
GROUP BY (customer.id);
--     name    | sum
-- ------------+------
--  customer 2 |  470
--  customer 3 |  688
--  customer 1 | 1079
```
> **AVG** - считает среднее значение всех записей в сгруппированном поле

```sql
SELECT customer.name, AVG(product.price)
FROM customer
JOIN cart ON customer.id = cart.customer_id
JOIN product ON product.id = cart product_id
GROUP BY (customer.id);
--     name    | avg
-- ------------+--------
--  customer 2 | 470.00
--  customer 3 | 344.00
--  customer 1 | 359.67
```
> **ARRAy_AGG** - собирает значение всех записей в сгруппированном поле в массив(список)

```sql
SELECT blogger.name, ARRAY_AGG(post.body) FROM blogger
JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.id);
--    name    |                         array_agg
-- -----------+-----------------------------------------------------------
--  blogger 1 | {"my first blog","today is a good day","it is my b-day!"}
--  blogger 2 | {"my first post","some post"}
--  blogger 3 | {"i am not a blogger"}
```

> **MIN/MAX** - выбирает минимальное/максимальное значение из всех записей в сгруппированном поле
```sql
SELECT blogger.name, MAX(post.created_at), MIN(post.created_at)
FROM blogger
JOIN post on blogger.id = post.blogger_id
GROUP BY (blogger.id);
--    name    |    max     |    min
-- -----------+------------+------------
--  blogger 2 | 2022-12-06 | 2013-10-05
--  blogger 3 | 2022-11-08 | 2022-11-08
--  blogger 1 | 2021-01-09 | 2020-08-01
```

> **COUNT** - считает кол-во записей в сгруппированном поле

```sql
SELECT blogger.name, COUNT(post.id)
FROM blogger
JOIN post on blogger.id = post.blogger_id
GROUP BY (blogger.id);
--    name    | count
-- -----------+-------
--  blogger 2 |     2
--  blogger 3 |     1
--  blogger 1 |     3
```
# Import/Export баз данных

## write from file to db
```sql
psql db_name < file.sql
# при этом db_name должна существовать
```

## write from db to file
```sql
pg_dump db_name > file.sql
```
