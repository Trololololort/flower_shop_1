I. Анализ инструментов 
II. Уяснение задачи и стратегия
III. Стратегия
IV. Документация проекта
V. Поэтапный план
VI. Стиль


I. Анализ и подготовка инструментов

Обязательно внимательно проанализируйте инфраструктурный лист. 
На момент подоготовки 
https://bom.firpo.ru/public/87

На рабочей станции вы увидите каталог venv.

Нужно проверить наличие:
1. Python 3.12. Если нет 3.12, подойдет любой от 3.10 включительно и старше.
Причина: Django 5 не встанет на раннюю версию Python. А в Zeal будет Django 5.

Активируем виртуальное окружение:
source venv/bin/activate

Проверим, какой путь до интерпретатора Python:
which python

Путь должен вести до вашего виртуального окружения.

Проверим версию: 
python -v

3. Проверим установленные пакеты:
pip freeze

4. Создадим проект:
1) Находясь в своем каталоге 
2) с активированным виртуальным окружением
Пишем:
django-admin startproject flower_shop

Документация: https://docs.djangoproject.com/en/5.0/ref/django-admin/#startproject

Zeal: startproject

Проверка: 
ls

Видим файлы проекта.

5. Запустим PyCharm.

6. Open / Выбираем каталог, flower_shop. 
Смотрим структуру проекта. 
Вы увидите 2 вложенных каталога: 
flower_shop / flower_shop

Документация (почему два вложенных каталога): https://docs.djangoproject.com/en/5.0/intro/tutorial01/#creating-a-project

7. PyCharm не знает о виртуальном окружении.
File / Settings / Project / Python interpreter / Add interpreter / Add local interpreter / Existing / 

Задаем Питон, который в нашем виртуальном окружении. Примерно вот такой путь:
/media/michael/750/Programming/pkgh/102-56/venv/bin/python

Проверка: сразу становятся видимы пакеты, включая Django. 
Закрываем настройки.

8. В верхней панели рядом с кнопкой запуска дебаггера (жук) есть выпадающий список с надписью Current File.
Раскрыть выпадающий список. 

Edit Configurations.
+ / Python 

Name: run (произвольное имя)
Script: flower_shop/manage.py
Script parameters: runserver

Документация: https://docs.djangoproject.com/en/5.0/intro/tutorial01/#the-development-server
Zeal: runserver

Комментарий: django-admin и python manage.py - одно и то же. 
Цитата: In addition, manage.py is automatically created in each Django project. It does the same thing as django-admin...
Ссылка на документацию - выше.

Запустим проект (нажимаем жука).
В консоли видим, на каком порту стартовал проект. Нажимаем в консоли на этот адрес.

Комментарий: часто бывает, что порт занят. Мы включаем / выключаем дебаггер. И запущенный нами процесс может не отпустить порт.

В терминале:
lsof -i :8000

Как искать в Google: what is listening on port ubuntu

Завершить процесс: sudo kill -9 <pid>


9. Проверить в Zeal:
1)  Django / Django FAQ / FAQ: Installation
И увидим список версий. Самая последняя - наша.

10. Работаем в Sqlite. Она идет с Python, ее не надо подключать: уже подключено.
Так экономим время.
Иначе говоря, вам Sqlite дали организаторы экзамена, поэтому даже если ее нет
в инфраструктурном листе, вам ее уже дали, разрешив Python.

II. Уяснение задачи 

Общие принципы:
1. Сначала создадим MVP. В чем-то ущербный, не полностью соответствующий спецификации. Но работающий.
Причина: заработать 100 балллов невозможно. Вы вынуждены жертвовать чем-то. 
Мы начинаем с жертвы. А именно: не дорабатываем модель пользователя. Доработка пользователя трудоемко.
Но пользователь уже есть. Пока возьмем существующую модель. Останется время - доработаем.

2. Никакого оверинжиниригна, пока не готов MVP. Не додумывае ТЗ. До разработки MVP ТЗ трактуется буквально
и в пользу программиста (не упомянуто - не сделано, непонятно упомянуто - трактуем так, как легче сделать).

На этом этапе: не упомянута пагинация - ее нет. Не упомянут футер - его нет. И т.п. 

3. Никаких красивостей, пока не готов MVP. Останется время - раскрасите. 
Вертка крупными блоками копированием и вставкой из Zeal.
Не надо верстать самостоятельно. Самостоятельно - только мелкие правки вертки.
Только копирование / вставка.


III. Стратегия

Есть товар.
Есть пользователь.
Есть корзина пользователя.

Пользователь кладет товар в корзину. 


Есть отдельно заказ. У заказа связь с корзиной - один к одному. 

Иначе говоря, товар в корзину добавлен. При создании заказа у корзины заполняется поле "Заказ".

По сути дела,  история заказов - это история переводов корзин в статус заказов.

IV. Документация проекта

В проекте расположен каталог doc. 
Это служебный каталог. Вам его на экзамене создавать не нужно.
Но в реальной жизни его желательно создавать: в нем все о проекте (версия Python, requirements.txt - список пакетов для автоматической установки через 
pip install -r requirements.txt и т.п.). 


V. Поэтапный план
Детальный план для самоподготовки (сначала с опорой на методические рекомендации, 
затем самостоятельно, если не получается и посмотрел в методические рекомендации,
попытка не засчитывается).

См. plan.txt.

VI. Стиль:

Документация: https://docs.djangoproject.com/en/5.0/internals/contributing/writing-code/coding-style/

Zeal: не содержит.

VI. Исполнение поэтапного плана
1. Приложения называем во множественном числе.
Документация: https://docs.djangoproject.com/en/5.0/intro/tutorial01/
Zeal: tutorial / Advanced tutorial: How to write reusable apps 
По ссылкам дойти до Tutorial 1.

2. Модели называем в единственном числе.
Документация: https://docs.djangoproject.com/en/5.0/intro/tutorial02/
Zeal: tutorial / Advanced tutorial: How to write reusable apps 
По ссылкам дойти до Tutorial 2.


1. Создать приложение general

Открыть терминал в PyCharm. Именно так, а не в ОС.
Причина: сразу будет активировано виртуальное окружение, сразу попадаете в рабочий катало, чем экономите время.


В general будем располагать общие миксины, константы, шаблоны и т.п.

Исключение из правил конвенции об именовании, т.к. general - прилагательное.

python manage.py startapp general

Документация: https://docs.djangoproject.com/en/5.0/ref/django-admin/#startapp
Zeal: startapp

Добавим general в settings.py в INSTALLED_APPS.

Пока проверить сделанное не можем.

2. Создать в general базовый шаблон.

На general ПКМ / New / File / templates/general/base.html

Документация: https://docs.djangoproject.com/en/5.0/intro/tutorial03/#write-views-that-actually-do-something

Цитата: Within the templates directory you have just created, create another directory called polls, and within that create a file called index.html. In other words, your template should be at polls/templates/polls/index.html. Because of how the app_directories template loader works as described above, you can refer to this template within Django as polls/index.html.

Т.е. применяется конвенция об именовании. Django ищет шаблоны 
по каталогам templates всех приложений. Но программист так не может: структура
проекта должна быть четкой. Самый простой путь добавить конкретику - всегда создавать с именем
приложения в каталоге templates этого приложения. Теперь мы можем ссылаться
на созданный шаблон general/base.html. И понятно, что он находится в приложении general.

В base.html пока ничего не пишем.

Пока проверить созданное не можем.

3. Создать приложение products.

Выбор наименования: goods всегда во множественном числе, commodity - слишком сложно
для запоминания. Пусть будет products. Это товары.

python manage.py startapp products

В settings.py добавить в INSTALLED_APPS products.

4. Создать модель Country

Нам надо знать, из какой страны товар происходит.

В приложении products в models.py создадим все модели, так или иначе связанные
с товаром. А именно модели для страны происхождения, цвета, и категории.

Так можно экономить время. Может быть, в реальном проекте можно было каждой из этих
сущностей выделить свое приложение. Но мы экономим время на развертывание приложения.


class Country(models.Model):
    name = models.CharField(max_length=100,
                            null=False,
                            blank=False,
                            default="",
                            verbose_name="Наименование")
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


Документация:

1) https://docs.djangoproject.com/en/5.0/topics/db/models/
2) https://docs.djangoproject.com/en/5.0/ref/models/fields/#charfield

Zeal:
1) models
2) CharField / django.db.models.CharField


Если не задать, __str__ в админке товар не объект иметь смыслоразличительного имени.

blank=False - нельзя оставить поле пустым в админке.
