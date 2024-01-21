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

2. В Chrome в Developer tools на вкладке Network сразу включаем
Disable cache.

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
Видим в браузере, что работает проект на Django.

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

NB! Это только на этапе MVP. Без хорошо выглядящего сайта хорошей оценки не будет.
Поэтому позже доработаем.

3. Никаких красивостей и мелочей, пока не готов MVP. Останется время - добавите.
Вертка крупными блоками копированием и вставкой из Zeal.
Не надо верстать самостоятельно. Самостоятельно - только мелкие правки верстки.
Только копирование / вставка.

4. Данный материал - исключительно для подготовки к демонстрационному экзамену.
Задача местами к олимпиадному программированию. Не воспринимайте как
руководство для реального проекта.

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

VI. Стиль
1. Приложения называем во множественном числе.
Документация: https://docs.djangoproject.com/en/5.0/intro/tutorial01/
Zeal: tutorial / Advanced tutorial: How to write reusable apps 
По ссылкам дойти до Tutorial 1.

2. Модели называем в единственном числе.
Документация: https://docs.djangoproject.com/en/5.0/intro/tutorial02/
Zeal: tutorial / Advanced tutorial: How to write reusable apps 
По ссылкам дойти до Tutorial 2.


VII. Работа над проектом

1. Создать приложение products.

Открыть терминал в PyCharm. Именно так, а не в ОС.
Причина: сразу будет активировано виртуальное окружение, сразу попадаете в рабочий катало, чем экономите время.


Выбор наименования: goods всегда во множественном числе, commodity - слишком сложно
для запоминания. Пусть будет products. Это товары.

python manage.py startapp products

В settings.py добавить в INSTALLED_APPS products.

Документация: https://docs.djangoproject.com/en/5.0/ref/django-admin/#startapp
Zeal: startapp

2. Создать модель Country

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

    def __str__(self):
        return self.name

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

3. Выполнить миграции и создать суперюзера.
Миграции - текстовые файлы с командами, последовательно изменяющими состояние базы данных.
Аналог системы контроля версий, только для базы данных.

В Django по умолчанию уже есть модель User. И у него уже созданы файлы миграций.
Поэтому надо их применить.


В терминале:
python manage.py migrate

Документация: https://docs.djangoproject.com/en/5.0/topics/migrations/
Zeal: migrate


python manage.py createsuperuser
Документация: https://docs.djangoproject.com/en/5.0/ref/django-admin/#createsuperuser
Zeal: createsuper

Задаем имя пользователя, как в ТЗ.
Электронная почта - любая. Пишите a@a.ru. Не теряйте время на придумывание почты.
Пароль - как в ТЗ.
Соглашаемся на простой пароль.


4. Добавить страну в административную панель.
В admin.py:

from products.models import Country

admin.register(Country)

Запускаем, проверяем:
http://127.0.0.1:8000/admin

URL административной панели - как нам нужно по ТЗ.

В админке видим: появились страны.

Но при попытке добавления стран мы столкнемся с ошибкой, потому что
база данных еще не изменена с учетом добавленной модели.

Надо сделать миграции.

python manage.py makemigrations

Документация: https://docs.djangoproject.com/en/5.0/ref/django-admin/#makemigrations
Zeal: makemigrations

python manage.py migrate

Теперь можно в административной панели добавлять страну. Добавим Россию.


5. Добавить модель Category.

В products/models.py

class Category(models.Model):
    name = models.CharField(max_length=100,
                            null=False,
                            blank=False,
                            default="",
                            verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория/Вид товара"
        verbose_name_plural = "Категории/Виды товаров"

Сразу мигрируем.

Откройте текстовый редактор и сохраните себе.

python manage.py makemigrations
python manage.py migrate

Теперь копируем в буфер обмена сразу две строки.
И вставляем в терминал. Так экономим время.


6. Создать приложение general

В general будем располагать общие миксины, константы, шаблоны и т.п.

Исключение из правил конвенции об именовании, т.к. general - прилагательное.

python manage.py startapp general


Добавим general в settings.py в INSTALLED_APPS.

Пока проверить сделанное не можем.



7. Создать NameMixin и применить его к Country и Category.

Видим, что задвоенный код. Наименование совпадает. И метод str.

В приложении general создадим файл model_mixins.py.

В нем пишем:

from django.db import models


class NameMixin(models.Model):
    name = models.CharField(max_length=100,
                            null=False,
                            blank=False,
                            default="",
                            verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

Нюанс: надо объявить, что класс абстрактный.
Иначе в базе данных создастся таблица: ведь класс наследует от модели.

Применить миксин в упомянутых моделях. Теперь они выглядят так:
class Country(NameMixin, models.Model):
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Category(NameMixin, models.Model):
    class Meta:
        verbose_name = "Категория/Вид товара"
        verbose_name_plural = "Категории/Виды товаров"


Проверить в работе.


8. Добавить модели Country и Category в административную панель.

В products/admin.py:

from products.models import Country, Category

admin.site.register(Country)
admin.site.register(Category)

Проверьте в работе: добавьте страну и категорию.


9. Создайте модель Color и добавьте ее в административную панель.

В products/models.py:

class Color(NameMixin, models.Model):
    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

В products/admin.py:
admin.site.register(Color)

Выполните миграции (! У вас две команды в открытом текстовом редакторе).
Проверьте в работе: добавьте цвет.



10. Дополните настройки для работы со статическими файлами.

Документация: https://docs.djangoproject.com/en/5.0/howto/static-files/
Zeal: static files

В settings.py:
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

Если MEDIA_ROOT не обозначить, файлы, загруженные пользователями, будут
попадать в корень проекта.

Документация: https://docs.djangoproject.com/en/5.0/ref/settings/#media-url
Zeal: media

В flower_shop/urls.py:

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



11. Создайте модель Product и добавьте ее в административную панель.

В products/models.py:

class Product(NameMixin, models.Model):
    added = models.DateTimeField(auto_now_add=True,
                                 verbose_name="Дата добавления")

    # 500 x 500 px.
    photo = models.ImageField(verbose_name="Фото. Рекомендовано 500 x 500 px", blank=False)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name="Цена",
                                validators=[MinValueValidator(Decimal('0.01'))])
    origin = models.ForeignKey(
        "Country",
        on_delete=models.CASCADE,
        verbose_name="Страна-производитель",
    )

    color = models.ForeignKey(
        "Color",
        on_delete=models.CASCADE,
        verbose_name="Цвет",
    )

    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        verbose_name="Категория / Вид товара",
    )

    stock = models.PositiveIntegerField(default=0,
                                        null=False,
                                        blank=False,
                                        verbose_name="Остаток товара")


    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


Документация:
1) https://docs.djangoproject.com/en/5.0/ref/models/fields/#datetimefield
2) https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ImageField
3) https://docs.djangoproject.com/en/5.0/ref/models/fields/#decimalfield
4) https://docs.djangoproject.com/en/5.0/ref/validators/#minvaluevalidator
5) https://docs.djangoproject.com/en/5.0/ref/models/fields/#foreignkey
6) https://docs.djangoproject.com/en/5.0/ref/models/fields/#positiveintegerfield


Zeal:
1) datetimefield
2) imagefield
3) decimalfield
4) minvaluevalidator
5) foreignkey
6) positiveintegerfield

В admin.py:

class ProductAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["id", "name", "color", "stock", ]


admin.site.register(Product, ProductAdmin)

Документация:
1) https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#modeladmin-objects
2) https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.exclude
3) https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display


Zeal:
1) ModelAdmin objects
2) Неизвестно.
3) list_display

Проверьте в работе. Обратите внимание: надо обрезать изображения (500 х 500 px).
Посмотрите, что загруженные пользователем изображения попадают в каталог media.


12. Создайте метод-заглушку и шаблон для отображения карточки товара. Настройте URL.

В products/views.py:

class ProductDetailView(DetailView):
    model = Product

В flowershop_urls.py:
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),

Обратите внимание:
1) Нужно обязательно вызвать метод as_view().
2) Мы именуем путь. Так можно в любом месте всегда получить этот путь по имени.
Так соблюдается принцип DRY: теперь путь можно поменять только в одном месте,
а не во многих.



Создадим шаблон в приложении products:
    templates/products/product_detail.html

Документация: https://docs.djangoproject.com/en/5.0/intro/tutorial03/#write-views-that-actually-do-something
Zeal: tutorial, отмотать до Writing your first Django app, part 3.

Цитата: Within the templates directory you have just created, create another directory called polls, and within that create a file called index.html. In other words, your template should be at polls/templates/polls/index.html. Because of how the app_directories template loader works as described above, you can refer to this template within Django as polls/index.html.

Т.е. применяется конвенция об именовании. Django ищет шаблоны
по каталогам templates всех приложений. Но программист так не может: структура
проекта должна быть четкой. Самый простой путь добавить конкретику - всегда создавать с именем
приложения в каталоге templates этого приложения. Теперь мы можем ссылаться
на созданный шаблон general/base.html. И понятно, что он находится в приложении general.

В нем напишем любое слово. Допустим, detail.

Проверьте (посмотрев id товара в админке):
http://localhost:8000/products/4/
Здесь 4 - это id товара.

Достаточно важно назвать шаблон правильно. В документации есть пример, как назвать.
Здесь convention over configuration: как видите, шаблон не указан, но работает.

Если вдруг забудется, как называть шаблон, то зажимаем ctrl и клик на DetailView.
Затем, не отпуская ctrl, клик на SingleObjectTemplateResponseMixin.
И видим, какое нужно имя шаблона: тут и суффикс, и метод получения имени шаблона.
Т.е. мы видим суффикс _detail, который будет присоединен к имени модели (в нижнем регистре).

Если совсем забудется, то всегда можно указать шаблон явно, в переменной template_name.



Документация:
1) https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#detailview
2) https://docs.djangoproject.com/en/5.0/topics/http/urls/#example
3) https://docs.djangoproject.com/en/5.0/topics/http/urls/#path-converters
4) https://docs.djangoproject.com/en/5.0/topics/http/urls/#naming-url-patterns
5) https://docs.djangoproject.com/en/5.0/topics/class-based-views/#usage-in-your-urlconf

Zeal:
1) detailview
2) urls
3) path converters
4) naming url patterns
5) usage in your urlconf


13. Доработайте шаблон product_detail.html, чтобы отображал данные.

<p>{{ object.name }}</p>
<p>{{ object.added }}</p>
<p>{{ object.photo.url }}</p>
<p>{{ object.price }}</p>
<p>{{ object.origin }}</p>
<p>{{ object.color }}</p>
<p>{{ object.category }}</p>
<p>{{ object.stock }}</p>

Обратите внимание:
1) В шаблон передан контекст. Работает магия. В контексте есть object.
2) Осмотреться (что есть в контексте) в шаблоне можно, написав {% debug %}.
2) Метод в шаблоне вызывается без круглых скобок.
3) Доступ к полям и методам - через точку.


14. Доработайте модель product, создав в ней метод get_absolute_url.

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={"pk": self.id})

Это удобно, и это общепринятая практика.

Попробуем этот метод в шаблоне.

<p>{{ object.get_absolute_url }}</p>

Уберите эту строку: мы опробовали метод, но сейчас он нам в шаблоне не нужен.


Документация:
1) https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse
2) https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.get_absolute_url
3) https://docs.djangoproject.com/en/5.0/ref/templates/api/#variables-and-lookups


Zeal:
1) reverse
2) get_absolute_url
3) template language


15. Добавьте менеджер в модель Product.

Т.к. все товары, которые показываются пользователю, должно быть в наличии,
сразу сделаем себе специальный менеджер. И заодно упорядочим товары так, как нам
чаще всего надо.

При этом надо сохранить менеджер по умолчанию (хранимый в переменной objects).

В products/models.py:

class ProductManager(models.Manager):
    def get_queryset(self):
        # В наличии и упорядоченные по убыванию даты добавления товара.
        return super().get_queryset().filter(stock__gte=1).order_by("-added")

class Product(NameMixin,
            models.Model):
    objects = models.Manager()  # По умолчанию. Нужен для админки.
    in_stock = ProductManager()


Документация:
1) https://docs.djangoproject.com/en/5.0/topics/db/managers/#modifying-a-manager-s-initial-queryset
2) https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-specific-objects-with-filters
3) https://docs.djangoproject.com/en/5.0/ref/models/querysets/#gte
4) https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.order_by
5) https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#debug

Zeal:
1) manager
2) queries
3) gte
4) order_by
5) template tags



16. Создайте метод и шаблон для отображения списка товара. Настройте URL.

В products/views.py:

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = Product.in_stock.all()
        return queryset

В products/templates/product_list.html:

{% for object in object_list %}
    <p><a href={{ object.get_absolute_url }}>{{ object.id }} {{ object.name }}</p>
{% endfor %}


В urls.py:
path("products/", ProductListView.as_view(), name="product-list"),

Обратите внимание:
1) Работает магия: назовите правильно шаблон, и не придется писать его имя специально.
Но если забылось, можно всегда указать явно template_name.
2) Нам надо задействовать свой менеджер in_stock. Для этого вмешиваемся в работу алгоритма:
переопределяем метод get_queryset.
3) Обязательно расположить этот путь ниже, чем product-detail. Выбор маршрута
идет сверху вниз, поэтому данный путь перехватит запрос на карточку товара, если его расположить
выше.

Для эксперимента: в админке товару поставьте нулевой остаток. И убедитесь, что
товар пользователю не показывается.





17. Создать в приложении general базовый шаблон.

На general ПКМ / New / File / templates/general/base.html

Открываем в Zeal любой материал про Bootstrap.
Скроллим вниз и в футере находим Examples.

Находим понравившийся шаблон. В данном случае - Pricing.
Правой кнопкой мыши в любом месте. Открыть в браузере.
Скопировать себе html.

В Chrome:
1) ctrl + u
2) ctrl + a
3) Переходим в base.html
4) ctrl + v

Очистить html:
1) Бегло скроллим и удаляем js и css, которых нет
в инфраструктурном листе.
<script src="../../assets/js/color-modes.js"></script>
<link rel="stylesheet" href="../../../../../cdn.jsdelivr.net/npm/%40docsearch/css%403.css">
<link href="pricing.css" rel="stylesheet">

2) Фавайконы кроме ico.
<link rel="apple-touch-icon" href="../../assets/img/favicons/apple-touch-icon.png" sizes="180x180">
<link rel="icon" href="../../assets/img/favicons/favicon-32x32.png" sizes="32x32" type="image/png">
<link rel="icon" href="../../assets/img/favicons/favicon-16x16.png" sizes="16x16" type="image/png">
<link rel="manifest" href="../../assets/img/favicons/manifest.json">
<link rel="mask-icon" href="../../assets/img/favicons/safari-pinned-tab.svg" color="#712cf9">

В products/templates/product_detail.html первой строкой добавить:
{% extends 'general/base.html' %}

Проверить в работе, открыв карточку товара.
Увидим пример из документации Bootstrap без стилей.
Данных о нашем товаре - не видим.



Документация: https://docs.djangoproject.com/en/5.0/ref/templates/language/#template-inheritance

Zeal: template inheritance


18. Подключить Bootstrap и jQuery.
В приложении general создайте каталог static\general.
Принцип тот же, что и с шаблонами: Django собирает статические файлы
по всем каталогам static всех приложений. Но программисту надо знать,
в каком приложении лежит конкретный файл. Проще всего это сделать,
расположив файлы в каталоге наименованием приложения.

В static\general создайте каталоги:
    1) css
    2) js

Скопируйте в них файлы Bootstrap и jQuery.

В base.html на первой строке пишем:
{% load static %}

Находим в general.html и меняем:

1)
<link href="../../dist/css/bootstrap.min.css" rel="stylesheet">
на
<link href="{% static 'general/css/bootstrap.min.css' %}" rel="stylesheet">

2)
<script src="../../dist/js/bootstrap.bundle.min.js"></script>
на
<script src="{% static 'general/js/bootstrap.bundle.min.js' %}"></script>

В head
<script src="{% static 'general/js/jquery.min.js' %}"></script>
NB! В реальном проекте так не делается, потому что произойдет блокировка рендеринга.
Нам это сейчас нужно для очень специфических задач. Забегая вперед:
мы будем писать скрипт на jQuery непосредственно в html.
Но как только мы напишем jQuery, сразу получим ошибку, потому что
html отрендерится раньше, чем загрузится библиотека.

Проверить:
1. Подключилось ли CSS.
2. Верстка стала адаптивной.
3. В консоли пишем jQuery, ошибок нет.
4. Заработала кнопка переключения светлой и темной темы (т.е.
заработал скрипт Bootstrap.

Убрать кнопку переключения светлой и темной темы.

На этом этапе в консоли Chrome нет ошибок кроме 404 для логотипа.

Документация: https://docs.djangoproject.com/en/5.0/howto/static-files/
Zeal: manage static


19. Создать приложение companies.

python manage.py startapp companies

В INSTALLED_APPS добавляем companies.

В нем создаем каталог static/companies/img


20. Создать логотип и использовать в шаблоне.
Открытая из Zeal страница в браузере внизу содержит логотип Bootstrap.
Кликаем по нему правой кнопкой мыши, сохраняем.
Открываем в InkScape.

Букву "B" заменяем на уместную в данном случае "М".

Меняем название файла на logo.svg.

Создаем каталог для статики, в нем каталог img и помещаем в него логотип.

Таким образом, в приложении companies:

static/companies/img/logo.svg

В шаблоне путь до логотипа в футере правим на:
{% static 'companies/img/logo.svg' %}

Получаем:
<img class="mb-2" src="{% static 'companies/img/logo.svg' %}" alt="" width="24" height="19">

Копируем этот элемент, ищем лого в хедере и заменяем svg на указанный выше.
<img class="mb-2" src="{% static 'companies/img/logo.svg' %}" alt="" width="24" height="19">

Правим:
1) Удаляем марджин.
2) Добавляем свой класс.
3) Удаляем ширину и высоту:


<img class="home-logo" src="{% static 'companies/img/logo.svg' %}">


21. Подключить style.css и написать стиль для логотипа

В приложении general в
    static/general/css

создадим файл style.css.

В нем:

.home-logo {
    width: 2em;
}


В head шаблона base.html пишем:

<link href="{% static 'general/css/style.css' %}" rel="stylesheet">

Проверим в работе на карточке товара.


22. Разбить base.html на header, footer, base.html

Создадим рядом с base.html:
    1) header.html,
    2) footer.html

В base.htm поиском найдем </header>

Все что выше - вырезать и вставить в header.html.

В base.htm поиском найдем <footer. Все что ниже - вырезить и вставить в footer.html.

Дописать в footer.html на первой строке:
{% load static %}

В base.html
1) Первой строкой:
{% include 'general/header.html' %}

2) Последней строкой:
{% include 'general/footer.html' %}

Проверить на карточке товара: ничего для карточки не должно измениться.


23. Перенести из base.html верстку в карточку товара.

В base.html под

{% include 'general/header.html' %}

пишем:

{% block content %}{% endblock %}

Переносим верстку из base.html в product_detail.html и организуем блок:

{% block content %}
...
Верстка
...
{% endblock %}

Пусть наши предыдущие обращения к переменным вроде {{ object.name }} уйдут за блок.
Теперь они не видны.

Проверяем в работе на карточке товара: видим примерно то, что мы взяли как пример
из документации Bootstrap.

Документация: https://docs.djangoproject.com/en/5.0/ref/templates/language/#template-inheritance
Zeal: django: template inheritance

