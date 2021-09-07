Для запуска приложения: открываем терминал и выполняем следующие команды:  

`git clone https://github.com/dnantonov/backend_eis/ && cd backend_eis`

Установка необходимых пакетов:  
`pip install -r requirements.txt`

Создаем миграции:  
`python3 crud/manage.py migrate --run-syncdb`

Далее создаем суперпользователя:

`python3 crud/manage.py createsuperuser`

Запускаем сервер:

`python3 crud/manage.py runserver`

Открываем следующие страницы:

http://127.0.0.1:8000/actions/  

http://127.0.0.1:8000/payments/