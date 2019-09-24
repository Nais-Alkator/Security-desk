# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны — это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

### Как установить
Запросите доступ к БД у менеджера вашего банка. Для доступа вам понадобятся хост, порт, имя базы данных, имя пользователя базы данных, пароль и секретный ключ. 
В корне проекта нужно создать файл .env со следующим содержанием:  

```
DATABASES_HOST=<ваши данные>
DATABASES_PORT=<ваши данные>
DATABASES_NAME=<ваши данные>
DATABASES_USER=<ваши данные>
DATABASES_PASSWORD=<ваши данные>
SECRET_KEY=<ваши данные>
DEBUG=True
```

Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:  

    pip install -r requirements.txt


### Как запустить

Для запуска проекта используйте команду в консоли:  

    python manage.py runserver

После успешного запуска, сайт можно найти на localhost:8000

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).