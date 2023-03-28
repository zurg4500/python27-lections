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
-- переименовывание типа данных
```

```sql
ALTER TABLE name_of_table ALTER COLUMN col_name SET DATA TYPE new_type;
-- изменение типа данных у поля
```

# Ограничения (constraints)
* UNIQUE - не разрешает дубликаты
* NOT NULL - требует обязательного заполнения поля


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

