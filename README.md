## Установка проекта

Перейдите в папку:

``````
cd orders
``````

Необходимо создать и активировать виртуальное окружение.

``````
python3 -m venv env
``````

``````
source env/bin/activate
``````

Установите зависимости из файла **requirements.txt**:

``````
pip install -r requirements.txt
``````

В проекте есть предустановленная база данных sqlite

### Для создания новой базы данных необходимо сделать следующие шаги:

``````
python manage.py makemigrations
``````

``````
python manage.py migrate
``````

## Создание суперпользователя для Django-admin

По умолчанию установлен пользователь:

login:admin@gmail.com

password:74admin1986

Создание нового супер пользователя:

``````
python manage.py createsuperuser
``````

* Команда для запуска приложения

``````
python manage.py runserver
``````

* API  POSTMAN:

https://www.postman.com/maintenance-technologist-54848571/workspace/ig-api/documentation/30746902-b07e4bd6-c886-4831-9a08-1e5650d0f693
