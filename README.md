# Проект Платформа для онлайн-обучения
## Описание
Платформа для онлайн-обучения, на которой каждый желающий может размещать свои полезные материалы или курсы.
___
## Активация django в виртуальном окружении
- python3 -m venv .venv - Создайте виртуальное окружение
- .venv\Scripts\activate (Windows) - Активируйте виртуальное окружение
- для poetry: poetry add django далее poetry export -f requirements.txt --output requirements.txt
- для venv: pip install django далее pip freeze > requirements.txt
___
## Работа с django
- django-admin startproject config . - инициализирует проект в корневой директории
- вариант 2 - django-admin startproject <название_проекта> - инициализирует проект в отдельной директории
- python manage.py startapp <название_приложения> - создает директорию с приложением запускает работу приложения
- pip install psycopg2-binary - установка библиотеки для работы с базами данных Postgres
- pip freeze > requirements.txt - обновление файла с зависимостями
- pip install python-dotenv - установка библиотеки для работы с защитой секретных данных
- pip freeze > requirements.txt - обновление файла с зависимостями
- pip install Pillow - установка библиотеки для работы с изображениями
- pip install django_filter - установка фильтрации, добавить в settings/INSTALLED_APPS = ['django_filters',]
- pip install drf-yasg - (+доп.настройки settings, urls) drf-yasg предоставляет возможности для автоматической генерации документации на основе ваших 
сериализаторов, представлений и URL-шаблонов
- pip install django-cors-headers - (+доп.настройки settings) механизм безопасности браузера
- pip install requests - установка Requests — библиотека для работы с HTTP-запросами
- pip install redis - Установка брокера redis
- pip install celery - Установка Celery
- pip install eventlet - Для работы на Windows необходимо также установить пакет eventlet через пакетный менеджер.
- pip install django-celery-beat - настроить периодически выполняемые задачи, 
установите дополнительный пакет celery-beat и добавьте его в установленные приложения
+ 
- python manage.py runserver - запускает сервер
- python manage.py makemigrations app_name - создает миграцию, которая зафиксирует эти изменения.
- python manage.py migrate - применяет миграцию к базе данных
- - python manage.py migrate app_name migration_name - откатить миграцию до конкретной версии, указав имя приложения и номер миграции
- - python manage.py migrate app_name zero - откатить все миграции и вернуть базу данных в состояние, когда ни одна миграция не была применена
- python manage.py createsuperuser - Для создания суперпользователя
- pip install ipython - установите пакет ipython, Чтобы Django shell был удобным в использовании
- poetry add ipython - для poetry
- python manage.py shell -i ipython - запустите Django shell с IPython
- Для выхода из Django Shell используйте команды exit(), quit() или сочетание клавиш Ctrl + D или Ctrl + Z
- python -Xutf8 manage.py dumpdata [приложение].[модель] --output [файл.json] --indent 4 - Выгрузка данных из БД в файл на Windows
- python manage.py loaddata файл.json --format json - Загрузка данных из файла в БД с указанием формата файла на Windows
- python manage.py команда - Вызов кастомной команды
- pip install coverage - установить Для подсчета покрытия тестами
- coverage run --source='.' manage.py tests - После установки важно запустить подсчет покрытия и вывести отчет
- coverage report - и вывести отчет
- celery -A config worker -l INFO (-P eventlet (добавить для Windows)) - Для запуска обработчика worker 
___
## Создание и настройка приложения `material`:

*   Создано новое Django-приложение под названием `material` с помощью команды `python manage.py startapp material`.
*   Приложение `material` зарегистрировано в настройках проекта (в `INSTALLED_APPS` в файле `config/settings.py`). 
*   Настроена маршрутизация для приложения:
    *   Создан файл `urls.py` в директории приложения `material`.
    *   В главном файле `BASE_DIR/urls.py` проекта добавлено подключение маршрутов приложения `material` с использованием функции `path` и `include`.

**Реализация контроллеров ViewSet (viewsets.ModelViewSet):**

*   В файле `views.py` приложения `material` созданы контроллера на ViewSet:
    *   Контроллер для отображения курсов - CourseViewSet.
*   В файле `views.py` приложения `material` созданы контроллера на generics:
    *   Контроллер для создания уроков курса - LessonCreateApiView.
    *   Контроллер для отображения уроков курса - LessonListApiView.
    *   Контроллер для отображения 1 урока курса - LessonRetrieveApiView.
    *   Контроллер для обновления уроков курса - LessonUpdateApiView.
    *   Контроллер для удаления уроков курса - LessonDestroyApiView.

**Настройка маршрутизации для контроллеров:**

*   Зарегистрировать роутер:
router = SimpleRouter()  # или DefaultRouter
router.register("", CourseViewSet)
*   В файле `urls.py` приложения `material` настроена маршрутизация для контроллеров с использованием функции `path`:
    *   например: path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
*   к urlpatterns добавить роутер: urlpatterns = [] + router.urls

**Запуск проекта и доступ к страницам:**

*   Для запуска проекта необходимо перейти в терминал и выполнить команду `python manage.py runserver`.
*   Доступ к домашней странице осуществляется по адресу `http://127.0.0.1:8000/` (или другому адресу, указанному в выводе команды `runserver`).
*   Доступ к странице контактов осуществляется по адресу `http://127.0.0.1:8000/contacts/`.
*   Или проверить через Postman

# Запуск проекта с использованием Docker Compose
Этот файл docker-compose.yml определяет конфигурацию для запуска всех необходимых сервисов вашего проекта: 
веб-приложения Django, базы данных PostgreSQL, Redis и Celery (worker и beat).

## Предварительные требования
- Docker установлен и работает.
- Docker Compose установлен (обычно входит в состав Docker Desktop).
- Файл .env с необходимыми переменными окружения (например, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD). 

### Процесс запуска
1. Сборка и запуск всех сервисов.
Перейдите в корневую директорию вашего проекта (где находится файл docker-compose.yml и Dockerfile). 
2. Затем выполните следующую команду:
docker-compose up --build или docker-compose -f docker-compose.yml up

### Полезные команды

Сбилдить образы без запуска: docker-compose build

Запустить контейнеры в фоне (демоне): docker-compose up -d

Просмотр логов: docker-compose logs -f

Подключиться в терминал работающего контейнера, например web: docker exec -it online-education bash

# Инструкции по настройке удаленного сервера и деплоя
## Настройка удаленного сервера
1. Обновление системы
- Откройте терминал и выполните команду для обновления списка пакетов:
sudo apt update
- Затем выполните команду для обновления всех установленных пакетов до их последних версий:
sudo apt upgrade

2. Для управления файрволом в Ubuntu используется утилита ufw (Uncomplicated Firewall).
- Сначала проверьте состояние файрвола с помощью команды:
sudo ufw status
- Если файрвол отключен, активируйте его:
sudo ufw enable
- Теперь откройте необходимые порты:
-- Порт 80 для HTTP:
sudo ufw allow 80/tcp
-- Порт 443 для HTTPS:
sudo ufw allow 443/tcp
-- Порт 22 для SSH:
sudo ufw allow 22/tcp
- Проверьте настройки файрвола:
sudo ufw status

3. Ожидаемый результат:
В результате выполнения команды вы должны увидеть, что порт 22 находится в состоянии 
ALLOW наряду с портами 80 и 443. Это означает, что ваш сервер будет доступен для 
SSH-подключений, а также для веб-трафика.

## Настройка деплоя

Первый шаг в деплое приложения — это скачивание его исходного кода. 
Часто разработчики размещают свои проекты на платформе GitHub, что позволяет легко получать 
доступ к коду и управлять его версиями.

1. Установка Git
- Откройте терминал на сервере и выполните команду:
sudo apt update и 
sudo apt install git
- Убедитесь, что Git установлен корректно, выполнив команду:
git --version
- Если всё установлено правильно, команда выведет номер версии Git.

2. Клонирование репозитория с GitHub
- Перейдите в директорию, где вы хотите разместить код вашего приложения. Например:
cd /var/www
Где /var/www — это директория, куда вы хотите склонировать проект.

- Затем выполните команду для клонирования репозитория:
git clone https://github.com/username/repository.git
Замените username/repository  на путь к вашему репозиторию. 
После выполнения этой команды весь код из репозитория будет скопирован на ваш сервер в 
указанную директорию.

## Документация:
Для получения дополнительной информации обратитесь к [документации](README.md).
## Лицензия:
Этот проект лицензирован по [лицензии MIT](LICENSE).