# QuestionsForTheQuiz

## Описание
Веб-сервис запрашивает с публичного API указанное количество вопросов для викторин, сохраняет их в БД. Возвращает предыдущий сохраненный вопрос, в случае его отсутствия - пустой объект.

### REST Эндпоинты
| Маршрут | Метод | Описание |
| ------- | ----- | -------- |
| /questions/ | POST | Добавляет новые вопросы в БД. Возвращает предыдущий добавленный вопрос. |

### Пример запроса
#### /questions/
Запрос:
```
curl -X 'POST' \
  'http://localhost:8000/questions/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 5
}'
```
Ответ:
```
{
  "question_id": 41619,
  "question_text": "This dam on the Columbia River has a generating capacity of nearly 6.5 million kilowatts",
  "answer": "Grand Coulee Dam",
  "created_at": "2022-12-30T18:54:57.820000+00:00"
}
```

### Установка и запуск сервиса в Docker
1. Склонировать репозиторий
```
git clone https://github.com/sat-brr/bewise-test-task1.git
```
2. Создать файл .env в корневой папке проекта и заполнить его.
```
POSTGRES_DB=Имя БД
POSTGRES_USER=Имя Пользователя БД
POSTGRES_PASSWORD=Пароль от пользователя БД
APP_PORT=Порт, который будет обслуживать веб-сервис(по умолчанию указывать 8000)
```
3. Построить контейнеры
```
cd bewise-test-task1
make build
```
4. Запустить контейнеры
```
make run_app
```
