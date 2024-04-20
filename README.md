**Описание.**
Проект freelance это тестовое задание для Anverali Group. Проект представляет из себя сайт с заказчиками и исполнителями работ(биржа).

**Стек используемых технологий.**
* Django 4.2
* PostgreSQL
* python 3.11.3
* bootstrap

**Как развернуть проект.**
1. Клонировать репозиторий и перейти в него в командной строке:
_git clone https://github.com/maximpontryagin/test_task.git_

2. Cоздать и активировать виртуальное окружение:
_python -m venv venv source venv/Scripts/activate_ 

3. Установить зависимости из файла requirements.txt:
_pip install -r requirements.txt_ 

4. Изменить настройки базы данных в файле freelance/freelance/settings.py для работы с вашей базой данных PostgreSQL

4. Выполнить миграции:
_python manage.py migrate_

5. Запустить проект:
_python manage.py runserver_



