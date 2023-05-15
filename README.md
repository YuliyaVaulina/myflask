# myflask

### В файле .env необходимо указать имя пользователя, пароль и название базы данных:

PG_USER=#your_username

PG_PASSWORD=#your_password

PG_DATABASE=#your_database

## Задание

Вам нужно написать REST API (backend) для сайта объявлений.

Должны быть реализованы методы создания/удаления/редактирования объявления.

У объявления должны быть следующие поля:

- заголовок
- описание
- дата создания
- владелец
- 
Результатом работы является API, написанное на Flask.

Этапы выполнения задания:

1. Сделайте роут на Flask.
2. POST метод должен создавать объявление, GET - получать объявление, DELETE - удалять объявление.
