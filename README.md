# Что за проект?

Опыты по разделению данных на разные проекты. К примеру: Авторизация вынесена в отдельный проект, а некоторый иной функционал - в другой. Как это будет работать? Что для этого нужно?

# Как запустить для проверки
> При открытии терминала всегда активируем виртуальное окружение `. venv/Source/activate/`

* В первом терминале:
```sh
cd eca/
. run.sh
```

* Во втором терминале:
```sh
cd feature_project/
. run.sh
```

## Примеры запросов:

POST http://localhost:8000/api/auth/register/ - для регистрации
```json
{
    "username": "arefiture",
    "password": "P@ssw0rd123",
    "email": "arefiture@example.com"
}
```

POST http://localhost:8000/api/auth/login/ - для получения токенов
```json
{
    "username": "arefiture",
    "password": "P@ssw0rd123"
}
```

GET http://localhost:8001/api/data/ - обратите внимание, другой порт и проект. Требует токен авторизации Bearer от прошлого запроса

**Вернёт** такое:
```json
{
    "message": "Hello, arefiture!",
    "user_id": 2
}
```