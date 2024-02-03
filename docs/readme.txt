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

2. Никакого оверинжиниригна, пока не готов MVP. Не додумываем ТЗ.
До разработки MVP ТЗ трактуется буквально
и в пользу программиста (не упомянуто - не сделано, непонятно упомянуто - трактуем так, как легче сделать).

На этом этапе: не упомянута пагинация - ее нет. Не упомянут футер - его нет. И т.п.

NB! Это только на этапе MVP. Без хорошо выглядящего сайта хорошей оценки не будет.
Поэтому позже доработаем дизайн и мелкие удобства.

3. Никаких красивостей и мелочей, пока не готов MVP. Останется время - добавите.
Верстка крупными блоками копированием и вставкой из Zeal.
Не надо верстать самостоятельно. Самостоятельно - только мелкие правки верстки.
Только копирование / вставка.

4. Данный материал - исключительно для подготовки к демонстрационному экзамену.
Задача местами близка к олимпиадному программированию. Не воспринимайте как
руководство для реального проекта.

III. Стратегия

Есть товар.
Есть пользователь.
Есть корзина пользователя.

Пользователь кладет товар в корзину.
У одного пользователя много корзин, но текущая - одна (или ни одной).
Связь: один ко многим (один пользователь - много корзин).

В одной корзине много товаров: связь один ко многим.

Есть отдельно заказ. У заказа связь с корзиной - один к одному.
Иначе говоря, в корзине находится товар.
При создании заказа у корзины заполняется поле "Заказ".
Теперь это уже история.

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
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



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

<p>{{ object.id }}</p>
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


23. Перенести из base.html верстку в шаблон списка товара.

В base.html под

{% include 'general/header.html' %}

пишем:

{% block content %}{% endblock %}

Переносим верстку из base.html в product_list.html и организуем блок:

{% block content %}
...
Верстка
...
{% endblock %}


На первой строке пишем:
{% extends 'general/base.html' %}

Пусть наш цикл уйдет за блок.
Теперь он не виден.

Проверяем в работе на списке товаров: видим примерно то, что мы взяли как пример
из документации Bootstrap.

Документация: https://docs.djangoproject.com/en/5.0/ref/templates/language/#template-inheritance
Zeal: django: template inheritance


24. Доработать заготовку списка товаров

В product_list.html из предложенной верстки для списка товаров надо выбрать понравившийся вариант
для отображения одного товара.

Пусть это будет вариант посередине - с синей кнопкой и белым верхом.

Удаляем остальные ненужные элементы списка товаров, оставляем один.

Таблица Compare plans нам не нужна. Удаляем ее и все сопутстующее (заголовок, контейнер и т.п.).

В шаблон списка товаров из view был передан object_list.

Организуем цикл. Найдем класс, который в Bootstrap отвечает за ряд.
И в нем пишем:

{% for object in object_list %}

Вот так:
    <div class="row row-cols-1 row-cols-md-3 mb-3 text-center">
      {% for object in object_list %}

И перед закрывающим тегом для ряда:
      {% endfor %}

Цикл за блоком content удаляем.

Проверяем в работе: по числу отображаемых товаров будут созданы карточки. Внимательно:
отображаются только товары, которые есть вналичии.


Документация: https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-for
Zeal: templatetag


25. Наполнить базу данных содержимым

Пусть у нас будет:
1. Две страны.
2. Три цвета.
3. Три категории.
6. Семь товаров.

Страны: Россия, Казахстан.
Цвета: Красный, Зеленый, Белый / красный, Розовый, Белый.
Категории: Цветы, Упаковка, Дополнительно.

Семь товаров - потому что 5 для слайдера и еще чуть-чуть.

Изображения, которые сейчас вам доступны в doc / images,
уже подготовлены для web кроме bouquet-2.jpg.

Это изображение 1.4 MB и произвольного разрешения и размера.
Мы для себя решаем, что будем загружать изображения 500 x 500 px.

Формат выбираем webp. Открываем изображение в Gimp и:
1. Приводим его к нужному размеру.
2. Разрешению (масштабируем до нужного визуального размера и
уменьшаем разрешение до минимально приемлемого).
3. Экспортируем в формате webp.

Теперь оно весит 31 килобайт и подходит нам по длине и ширине.
Очень важно не допустить, чтобы изображения оказались
в верстке визуально разного размера.

Результат оптимизации расположен рядом (bouquet-2.webp).

Проверить, как работает список товаров (должно быть количество
карточек по числу товаров).


25. Доработать карточки в списке товаров
В теге с элементом card-header расположим изображение товара вместо h4:
<img src="{{ object.photo.url }}" alt="{{ object.name }}">

NB! Очень важно задать alt. Если не задать, будет ошибка валидации.

Изображение получилось выходящим за пределы карточек.

Зададим класс img-fluid:

<img class="img-fluid" src="{{ object.photo.url }}" alt="{{ object.name }}">

Где класс card-title, пишем:

Заменяем список:
<li>Артикул: {{ object.id }}</li>
<li>Цена: {{ object.price }}</li>
<li>В наличии: {{ object.stock }}</li>
<li>Категория/вид товара: {{ object.category }}</li>
<li>Цвет: {{ object.color }}</li>
<li>Страна-производитель: {{ object.origin }}</li>
<li>Поступил в продажу: {{ object.added }}</li>

ТЗ не требует от нас вывода этой информации в список товаров.
Но мы стараемся для удобства экзаменатора и, кстати, самого себя:
так можно проверять, как работают фильтры и сортировки.

Сейчас мы видим сортировку от новых товаров к старым.


Изменим текст кнопки:
<button type="button" class="w-100 btn btn-lg btn-primary">В корзину</button>

Нажатие в любое место карточки (кроме кнопки) должно вести на
детальную информацию о товаре.

Обрамим нужные участки в тег <a>:

1)
          <a href="{{ object.get_absolute_url }}">
            <div class="card-header py-3">
              <img class="img-fluid" src="{{ object.photo.url }}" alt="{{ object.name }}">
            </div>
          </a>

2)

            <a href="{{ object.get_absolute_url }}">
              <h1 class="card-title pricing-card-title">{{ object.name }}</h1>
              <ul class="list-unstyled mt-3 mb-4">
                <li>Артикул: {{ object.id }}</li>
                <li>Цена: {{ object.price }}</li>
                <li>В наличии: {{ object.stock }}</li>
                <li>Категория/вид товара: {{ object.category }}</li>
                <li>Цвет: {{ object.color }}</li>
                <li>Страна-производитель: {{ object.origin }}</li>
                <li>Поступил в продажу: {{ object.added }}</li>
              </ul>
            </a>

Стиль текста поменялся на стиль ссылок. Пока не исправляем, дальше делаем MVP.



Документация: https://getbootstrap.com/docs/4.0/content/images/#responsive-images
Zeal: responsive images


26. Организуем заголовок для списка товаров

Заголовок страницы (h1) остался в header.html.

В header.html сначала обрамим контейнер с заголовком в блок headline:

{% block headline %}
<div class="pricing-header p-3 pb-md-4 mx-auto text-center">
  <h1 class="display-4 fw-normal text-body-emphasis">Pricing</h1>
  <p class="fs-5 text-body-secondary">Quickly build an effective pricing table for your potential customers with this Bootstrap example. It’s built with default Bootstrap components and utilities with little customization.</p>
</div>
{% endblock %}

Вырежем этот блок, вставим в product_list.html.

А в base.html втавим только пустой блок:

{% block headline %}
{% endblock %}

Причина переноса блока: Django не поддерживает блоки в
файлах, подключенных через include.

Проверим.

Теперь изменим содержимое блока:

{% block headline %}
<div class="pricing-header p-3 pb-md-4 mx-auto text-center">
  <h1 class="display-4 fw-normal text-body-emphasis">Каталог</h1>
</div>
{% endblock %}


27. Создать форму сортировки и фильтрации для каталога товаров

В приложении products создадим файл const.py.

SORT_CHOICES = {
    "added": "Дата поступления в продажу",
    "origin": "Страна происхождения",
    "category": "Вид товара",
    "price": "Цена",
}

Ключи - имена полей в модели Product.
Значения - их представления для пользователя.
Применяется в ProductSortFilterForm.
Из формы получим выбор от пользователя - это будет
какой-то из ключей. И удобно будет применить его для
сортировки средствами ORM.

Три варианта выбора для сортировки нам объявлено.
И еще один - по дате поступления товара - упоминался как выбор по умолчанию.
Поэтому мы его тоже включаем в список.


В приложении products создадим файл forms.py. В нем:

def get_choices():
    choices = [(k, v) for k, v in SORT_CHOICES.items()]
    return choices

class ProductSortFilterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].required = False

    order_by = forms.ChoiceField(choices=get_choices, label="Сортировать по", required=False)


    class Meta:
        model = Product
        fields = ["category"]
        labels = {
            "category": "Фильтр"
        }

В Django есть ModelForm: из модели делается форма.
И особенностью является то, что если встретился в модели внешний ключ,
то выпадающий список вариантов будет для нас подготовлен средствами Django
из коробки. Так экономим время: иначе бы пришлось выбор категорий писать вручную.

Поэтому берем модель Product. Она большая, а нам нужно из нее только категория.
Поэтому fields = ["category"].

Категория у товара в модели - обязательна к заполнению. А в форме - не обязательна.
Поэтому так объявляем, для чего переопределим конструктор формы.

Так как в модели Product ничего не было про сортировку, добавим поле order_by.

Документация:
1) https://docs.djangoproject.com/en/5.0/ref/forms/fields/#choicefield
2) https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/

Zeal:
1) choicefield
2) Creating forms from models



28. Добавить форму сортировки и фильтрации в шаблон

Форму надо добавить из view в контекст шаблона.
Очень удобно копировать нужный участок кода из документации к TemplateView.

Добавим в ProductListView:

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
        context_data["sort_filter_form"] = GoodsSortFilterForm(self.request.GET)
        return context_data

Дополним шаблон:

    <div class="mb-5">
        <form>
            <table>
                {{ sort_filter_form.as_table }}
            </table>
            <button>Показать</button>
        </form>
    </div>

Обратите внимание: форма отправляет данные GET-запросом.
Мы в контекст передаем всегда созданную заново форму GoodsSortFilterForm(self.request.GET).

Мы могли бы создать форму, не передавая в нее параметры GET-запроса (вот так GoodsSortFilterForm()).
Но мы бы потеряли выбор пользователя, потому что классический веб работает с перезагрузкой
страницы. Потеря выбора пользователя недопустима.



Документация:
1) https://docs.djangoproject.com/en/5.0/ref/forms/api/#checking-which-form-data-has-changed
2) https://docs.djangoproject.com/en/5.0/ref/forms/api/#bound-and-unbound-forms

Zeal:
1) Checking which form data has changed
2) Bound and unbound forms


29. Доработать ProductListView, чтобы заработала сортировка и фильтрация

Изменим метод get_queryset:

    def get_queryset(self):
        queryset = Product.in_stock.all()

        category = self.request.GET.get("category")
        order_by = self.request.GET.get("order_by")

        if order_by:
            if order_by == 'price' or order_by == 'added':
                # По убыванию цены и даты добавления.
                queryset = queryset.order_by("-" + order_by)

            else:
                assert (order_by == 'category' or order_by == 'origin')
                queryset = queryset.order_by(order_by + "__name")

        if category:
            queryset = queryset.filter(category_id=category)

        return queryset


Мы во view, экземпляр класса знает о том запросе, который получен.
Поэтому обращаемся к запросу, получаем категорию и имя поля, по которому упорядочивать.
И применяем в запросе к базе данных через ORM.

Объекты типа QuerySet можно дополнять новыми условиями (так сказать, сhaining,
т.е. строить цепочку). Объекты ленивы, поэтому цепочку сначала готовим, а в базу данных
запрос будет сделан сильно позже (например, когда надо будет выводить список,
а это случится в шаблоне).




Документация:
1) https://docs.djangoproject.com/en/5.0/topics/db/queries/
2) https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.order_by
3) https://docs.djangoproject.com/en/5.0/ref/models/querysets/#filter
4) https://docs.djangoproject.com/en/5.0/topics/db/queries/#querysets-are-lazy

Zeal:
1) Making queries
2) order_by
3) Сначала в форме поиска ввести "Making queries", а потом ctrl + f "Retrieving specific objects with filters".
4) QuerySets are lazy


27. Доработка карточки товара в product_detail.html

Добавим в product_detail.html

{% extends 'general/base.html' %}

{% block content %}
{% endblock %}

Карточка товара в каталоге нам подходит по содержанию.
Скопируем ее из product_list.html (все содержимое цикла for) и
вставим блок content в product_detail.html.

Старое содержание карточки, которое сейчас оказалось вне блока
content, удалим.

Проверим.

Карточка занимает всю ширину экрана.
Многое некрасиво.

А именно:
1) Изображение занимает только часть экрана.
Исправим это, добавив класс w-100


<img class="w-100 img-fluid" src="{{ object.photo.url }}" alt="{{ object.name }}">

2) Кнопка растянута на всю ширину экрана.

Уберем у нее класс w-100.

<button type="button" class="btn btn-lg btn-primary">В корзину</button>



28. Создать страницу "О нас"

Щелчок правой кнопкой мыши на companies.
New / File

templates/companies/about.html

В нем:
{% extends 'general/base.html' %}
{% load static %}

Копируем из страницы каталга блок headline

Вставляем, меняем текстh1:

{% block headline %}
<div class="pricing-header p-3 pb-md-4 mx-auto text-center">
  <h1 class="display-4 fw-normal text-body-emphasis">О нас</h1>
</div>
{% endblock %}

Дополним этот блок слоганом:
<h2 class="fw-normal text-body-emphasis">Каждому жителю по цветку</h2>

И логотипом:
<img class="about-logo" src="{% static 'companies/img/logo.svg' %}" alt="logo">

Создадим view:

class AboutCompanyView(TemplateView):
    template_name = "companies/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Product.in_stock.all()[:5]
        return context



Нам нужен object_list, в котором будет 5 последних добавленных товаров.
Очень удобно - в документации к TemplateView все есть, как нам надо - доработать
совсем немного.

У нас in_stock уже отсортированы по новизне. Берем только последние 5.



Дополним urlpatterns:

urlpatterns = [
    ...
    path("about/", AboutCompanyView.as_view(), name="about"),
]

Дополним style.css:

.about-logo {
    width: 5em;
}

Для слайдера идем в Zeal:

Симпатичен слайдер, который с надписями. Копируем, вставляем
в about.html

Оставляем только по одному элементу, который active, остальные убираем:
 1) carousel-item.
 2) carousel-indicators.

 Добавляем класс carousel-dark.

 1. Пишем цикл.
 2. Пишем условие, что активным и aria-current по умолчанию будет нулевой элемент.


 Если позже захотите, и будет время,
 оберните все в условие: не показывать слайдер, если товаров нет.
 Сейчас не тратим на это время: магазин же чем-то торгует, значит, товаров
 не может не быть.


{% extends 'general/base.html' %}
{% load static %}

{% block headline %}
<div class="pricing-header p-3 pb-md-4 mx-auto text-center">
  <h1 class="display-4 fw-normal text-body-emphasis">О нас</h1>
  <h2 class="fw-normal text-body-emphasis">Каждому жителю по цветку</h2>

  <img class="about-logo" src="{% static 'companies/img/logo.svg' %}" alt="logo">
</div>
{% endblock %}

{% block content %}
<div id="carouselExampleCaptions" class="carousel carousel-dark slide" data-bs-ride="carousel">

  <div class="carousel-indicators">
    {% for object in object_list %}
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="{{ forloop.counter0 }}" {% if forloop.first %}class="active" aria-current="true"{% endif %} aria-label="Slide {{ forloop.counter }}"></button>
    {% endfor %}
  </div>
  <div class="carousel-inner">
    {% for object in object_list %}
    <div class="carousel-item {% if forloop.first %}active{% endif %}">
      <img src="{{ object.photo.url }}" class="d-block w-100" alt="{{ object.name }}">
      <div class="carousel-caption d-none d-md-block">
        <h5>{{ object.name }}</h5>
        <p>В продаже с {{ object.added }}</p>
      </div>
    </div>
    {% endfor %}
  </div>

  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
{% endblock %}


Документация:
1) https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.TemplateView
2) https://getbootstrap.com/docs/5.3/components/carousel/#captions
3) https://getbootstrap.com/docs/5.3/components/carousel/#autoplaying-carousels

Zeal:
1) templateview
2) Captions
3) Autoplaying carousels

29. Создать UserMixin.
Мы предвидим, что пользователь нам нужен для двух моделей:
1) Заказ.
2) Корзина.

Поэтому сразу в general/model_mixins.py:

class UserMixin(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name="Пользователь", )

    class Meta:
        abstract = True


29. Создать приложение carts и модель Cart.

python manage.py startapp carts

Добавить carts в INSTALLED_APPS.

Модель Cart:

class Cart(UserMixin,
           models.Model):
    """
    Пользователь добавляет товар в корзину.
    Пока поле order пустое, товар в корзине.
    Когда поле order непустое, это уже заказ.

    Таким образом организуется и текущая корзина,
    и история заказов.
    """

    product = models.ForeignKey("products.Product",
                                  on_delete=models.CASCADE,
                                  verbose_name="Товар")
    # Магазин торгует только штучными товарами.
    # Теоретически, возможна продажа весового товара (например, удобрений).
    # Но для интернет-магазина это довольно странно. А т.к. в ТЗ ничего не сказано,
    # поэтому трактуем самостоятельно: только штучный.
    quantity = models.PositiveIntegerField(blank=False,
                                           null=False,
                                           default=0,
                                           verbose_name="Количество")

    order = models.ForeignKey("orders.Order",
                              on_delete=models.CASCADE,
                              null=True,
                              blank=True, )

    def price(self):
        return self.product.price

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзинах"

Зарегистрируем ее в административной панели:

class CartAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["id", "user", "order", "product", "price", "quantity", ]


admin.site.register(Cart, CartAdmin)


30. Создайте view - метод-заглушку для добавления товара в корзину и соответствующий URL.

class AddToCart(LoginRequiredMixin,
                View):
    def post(self, request):
        return HttpResponse("Ok")

Обратите внимание на LoginRequiredMixin.
Просто добавив этот миксин, мы обеспечили невозможность
обращения к этой view неавторизованному пользователю.

Используем самый общий из классов для view - класс View.
Причина: эта вьюшка  не будет отдавать того, для чего
сделаны готовые классы (типа ListView или DetailView).

От этой вьюшки нам надо задействовать  только метод post.

Эта view будет:
1) Выполнять редирект в случае успешного добавления товаров в корзину.
2) Возвращать статус - ошибку в случае неудачи.

В Django есть FormView, но она нам для упомянутых целей подходит плохо.


В urlpatterns:

    urlpatterns = [
        path("cart/add/", AddToCart.as_view(), name="add-to-cart"),
    ]

Пока проверить не можем. Но проверка на дым - просто запустите.
При наличии грубых ошибок даже запуститься не удастся.


Документация:
1) https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-loginrequiredmixin-mixin
2) https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse

Zeal:
1) loginrequiredmixin
2) HttpResponse



30. Создайте форму для добавления товаров в корзину.

В приложении carts создайте файл:

templates/carts/parts /add_to_cart_form.html

В нем:

{% comment %}

Необязательные: addend, button_text

Пример использования:
{% include 'carts/parts/add_to_cart_form.html' with product_id=object.id addend=-1 button_text="+" %}

{% endcomment %}



<form id="to-cart-form" class="to-cart-form" method="post" action="{% url 'add-to-cart' %}">
    {% csrf_token %}
    <input type="hidden" name="product_id" value="{{ product_id }}">
    <input type="hidden" name="addend" value="{{ addend|default:'1' }}">
    <button id="to-cart-button" class="to-cart-button btn btn-primary">{{ button_text|default:"В корзину" }}</button>
</form>

Положить товар в корзину можно из каталога, из карточки и из самой корзины.
Поэтому обособим этот функционал в отдельном файле.

Здесь: addend - слагаемое. По умолчанию 1.
В корзине можно еще и убрать товар - тогда передадим -1.

В корзине мы будем делать две кнопки: + и -, поэтому можно передать еще и текст.

Задействован фильтр default, документация ниже.

Документация:
1) https://docs.djangoproject.com/en/5.0/howto/csrf/#how-to-use-django-s-csrf-protection
2) https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#default
3) https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#include

Zeal:
1) How to use Django’s CSRF protection
2) default
3) include


31. В каталоге и карточке товаров предусмотрите, что только залогиненный пользователь
видит кнопку "В корзину"

В шаблоне:

    {% if user.is_authenticated %}
    <div class="card-footer py-3">
        {% include 'carts/parts/add_to_cart_form.html' with product_id=object.id %}
    </div>
    {% endif %}

В контексте шаблона есть пользователь. Вы можете его видеть по тегу {% debug %}.


Попробуйте:
1) Залогиненный пользователь видит кнопку. У вас есть сейчас один пользователь - admin.
2) В режиме инкогнито кнопки не видны.
3) В панели разработчика посмотрите, что в форме есть и слагаемое, и идентификатор продукта.

Документация:
1) https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.User.is_authenticated

Zeal:
1) is_authenticated


32. Создайте функцию для добавления товара в корзину

В carts создайте файл service.py. Причина: вьюшки должны быть тощими.

В service.py:

def add_product_to_cart(product_id, user, addend):
    product = Product.in_stock.filter(pk=product_id).first()

    assert product is not None

    if product:

        the_product_already_in_cart = Cart.objects.filter(user=user, product=product, order=None).first()

        if the_product_already_in_cart:
            the_product_already_in_cart.quantity = (the_product_already_in_cart.quantity + addend)

            if the_product_already_in_cart.quantity == 0:
                the_product_already_in_cart.delete()
            else:
                the_product_already_in_cart.save()

        else:
            Cart.objects.create(user=user, product=product, quantity=1)
        status = 200

        act = "добавлен в корзину" if addend > 0 else "убран из корзины"

        message = 'Товар "{}" {}.'.format(product.name, act)
    else:
        # Страховка. Не должны сюда попасть.
        status = 400
        message = "Wrong product id"

    return {"status": status, "message": message}

Filter и first использованы - потому что так можно избежать необходимости
обрабатывать исключение. Потому что метод альтернатива примерно такова:

try:
    Cart.objects.get(...
except DoesNotExist:
    ...

Если продукт уже в корзине, увеличиваем его количество.
Товары добавляются всегда по одному. ТЗ о другом ничего не говорит.

Если в корзине 0 таких товаров, убираем товар из корзины.

Возвращаем код и сообщение пользователю.

Документация:
1) https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-a-single-object-with-get

Zeal:
1) Retrieving a single object with get


32. Доработайте AddToCart: добавить товар в корзину

    def post(self, request):
        """
        Добавить или убрать товар из корзины.
        Если товар не может быть добавлен в корзину, сообщить об этом.

        product_id - id товара.
        addend - может быть +1 (добавить) или -1 (удалить).

        Товар можно добавить из каталога, карточки товара и из корзины.
        Т.е. из разных мест.
        Поэтому сообщение показать на странице, где добавлялся товар.
        """
        product_id = request.POST.get('product_id')
        addend = int(request.POST.get('addend'))

        assert (addend == 1 or addend == -1)

        status = add_product_to_cart(product_id, request.user, addend)

        if status["status"] == 200:
            messages.add_message(request, messages.INFO, status["message"])
            return redirect(request.META['HTTP_REFERER'])
        else:
            return HttpResponse(status["message"], status=status["status"])


Проверьте в работе: из каталога добавляем одинаковые и разные товары кнопкой "В корзину".

Готовимся показать сообщение пользователю: добавим его в контекст.


Документация:
1) https://docs.djangoproject.com/en/5.0/ref/contrib/messages/
2) https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#redirect

Zeal:
1) messages
2) redirect


33. Создайте отдельный файл с частью шаблона для отображения сообщения.

В приложении general создайте шаблон message.html

{% comment %}
    Пример использования:
    {% include 'general/message.html' %}
{% endcomment %}


{% if messages %}
    {% for message in messages %}
        <span class="d-block p-2 {% if message.tags == 'info' %}bg-success{% else %}bg-danger{% endif %} mb-3">{{ message }}</span>
    {% endfor %}
{% endif %}



Документация:
1) https://docs.djangoproject.com/en/5.0/ref/contrib/messages/
2) https://getbootstrap.com/docs/4.0/utilities/colors/#background-color
3) https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#if

Zeal:
1) messages
2) color
3) if


34. Примените message.html в каталоге:


{% block headline %}
...

{% include 'general/message.html' %}

{% endblock %}

Проверьте: из каталога добавьте товар. Сообщения должны появляться.

Полностью функционал проверить на данном этапе слишком сложно.
Можно: подменять значения на точке останова. Но это чересчур.
Поэтому предупреждение с выводом сообщения об опасности не проверяем.


Документация:
1) https://docs.djangoproject.com/en/5.0/ref/contrib/messages/

Zeal:
1) messages


36. Организуйте добавление товара в корзину из карточки товара

В product_detail.html:

1) Добавьте:

{% block headline %}
  {% include 'general/message.html' %}
{% endblock %}

2) Замените кнопку на:

{% if user.is_authenticated %}
    {% include 'carts/parts/add_to_cart_form.html' with product_id=object.id %}
{% endif %}

Проверьте: из карточки товара добавьте товар. Сообщения должны появляться.

37. Создайте функцию для получения содержимого корзины

В carts/service.py:

def get_cart_contents(user):
    """
    В корзине лежат товары пользователя,
    которым еще не создан заказ.
    """
    object_list = Cart.objects.filter(user=user).filter(order=None)

    return object_list


37. Создайте в первом приближении view для просмотра корзины.

В первом приближении означает, что еще придется дорабатывать:
будет еще функционал для формирования заказа.

def get_total(a_queryset):
    sum = 0
    [sum := sum + elem.product.price * elem.quantity for elem in a_queryset]
    return sum

class CartDetailView(LoginRequiredMixin,
                     TemplateView):
    template_name = "carts/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = get_cart_contents(self.request.user)
        context["object_list"] = object_list
        context["total"] = get_total(object_list)
        return context

Обратите внимание: пользователь в запросе присутствует.

Django в шаблоне не может перемножать цифры.
Чтобы имея количество и цену вычислить сумму, нужно писать
собственный тэг для шаблона. Это долго. В ТЗ нет
указания о том, что корзина должна содержать сумму построчно.

Да, эта корзина будет хуже, чем возможно. Но принимаем на себя
разумный риск: за это оценку, скорее всего, не снизят.

А общую сумму для товаров в корзине считаем в функции get_total.

Проверить работу метода можно на точке останова.




38. Создайте в первом приближении шаблон для просмотра корзины.


Создать заказ мы пока не сможем.

Возьмем за основу таблицы тот же самый шаблон из примеров Bootstrap,
который целиком лежит в основе нашего фронтенда.
Он называется Pricing.

Копируем эту таблицу и дорабатываем.

{% extends 'general/base.html' %}
{% load static %}

{% block headline %}
  {% include 'general/message.html' %}
{% endblock %}


{% block content %}



{% if object_list %}
<div class="table-responsive">
    <table class="table table-striped table-sm">
        <thead>
        <tr>
            <th scope="col">Артикул</th>
            <th scope="col">Наименование</th>
            <th class="text-center" scope="col">Цена</th>
            <th scope="col"></th>
            <th scope="col"></th>
            <th class="text-center" scope="col">Количество</th>
        </tr>
        </thead>
        <tbody>
        {% for object in object_list %}
        <tr>
            <td>{{ object.product.id }}</td>
            <td>{{ object.product.name }} {% if object.product.color %} ({{ object.product.color }}) {% endif %}</td>
            <td class="text-center">{{ object.product.price }}</td>
            <td class="text-end">
            {% include 'carts/parts/add_to_cart_form.html' with product_id=object.product.id button_text="+" %}
            </td>

            <td class="text-start">
            {% include 'carts/parts/add_to_cart_form.html' with product_id=object.product.id addend=-1 button_text="-" %}
            </td>

            <td class="text-center">{{ object.quantity }}</td>
        </tr>
        {% endfor %}


        <tr>
            <td style="background-color: var(--bs-dark-bg-subtle);" colspan="12"> </td>
        </tr>
        <tr>
            <td colspan="3" >Сумма, руб.</td>
            <td colspan="2" class="text-center">{{ total }}</td>
            <td></td>
        </tr>

        </tbody>
    </table>
</div>
{% else %}

<div class="px-4 py-5 my-5 text-center">
    <h1 class="display-5 fw-bold text-body-emphasis">В корзине пока пусто</h1>
</div>
{% endif %}

{% include 'orders/order_form.html' %}

{% endblock %}



Документация:
1) https://getbootstrap.com/docs/5.3/examples/pricing/


38. Вычлените в шаблоне сумму

Сумма нам понадобится также в заказе. Поэтому в приложении general создадим шаблон total.html.

{% comment %}
{% include 'general/total.html' %}
{% endcomment %}

<tr>
    <td style="background-color: var(--bs-dark-bg-subtle);" colspan="12"> </td>
</tr>
<tr>
    <td colspan="3" >Сумма, руб.</td>
    <td colspan="2" class="text-center">{{ total }}</td>
    <td></td>
</tr>


В шаблоне cart.html вместо этого участка кода:
{% include 'general/total.html' %}


38. Добавьте url для просмотра корзины

urlpatterns = [
    ...
    path("cart/add/", AddToCart.as_view(), name="add-to-cart"),
    path("cart/", CartDetailView.as_view(), name="cart-detail"),
]

Обязательно cart/ должно следовать за cart/add/ во избежания
попадания не в ту вьюшку.

Попробуйте: в корзине должны работать кнопки добавления и удаления товара.


39. Добавьте стиль для кнопок добавления / удаления товаров

.to-cart-button {
    min-width: 2.5em;
}

Когда кнопки большие и с одинаковым текстом, все было неплохо.
А в случае корзины символы "+" и "-" имеют разную ширину.
И под палец на мобильных устройствах лучше больше простора.


40. Создать приложение orders и модель Order.

python manage.py startapp orders

Добавить orders в INSTALLED_APPS.

В приложении orders создайте файл const.py.

ORDER_STATUS = [
    ("NEW", "Новый"),
    ("CONFIRMED", "Подтвержден"),
    ("CANCELLED", "Отменен"),
]

Создайте модель Order:

class Order(UserMixin,
            models.Model):

    ordered = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Дата заказа")
    status = models.CharField(max_length=9,
                              choices=ORDER_STATUS,
                              verbose_name="Статус",
                              blank=True,
                              null=False,
                              default="NEW")

    cancellation_cause = models.TextField(verbose_name="Причина отказа",
                                          default="",
                                          null=False,
                                          blank=True)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"



Документация:
1) https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.DateTimeField
2) https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.CharField
3) https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
4) https://docs.djangoproject.com/en/5.0/ref/models/fields/#textfield



41. Создайте форму для создания заказа.

В приложении orders создайте файл forms.py.

В нем:

class PasswordField(forms.CharField):
    widget = forms.PasswordInput

class OrderForm(forms.Form):
     password = PasswordField(label="Пароль")


В Django нет специального поля для ввода пароля. Поэтому создаем собственное
поле, в котором применяется виджет.

Документация:
1) https://docs.djangoproject.com/en/5.0/ref/forms/widgets/#passwordinput
2) https://docs.djangoproject.com/en/5.0/ref/forms/fields/#label

Zeal:
1) passwordinput
2) label

42. Создайте заглушки view и url для создания заказа и для просмотра списка заказов.


class CreateOrder(LoginRequiredMixin,
                  View):

    def post(self, request):
        pass


class OrdersListView(LoginRequiredMixin,
                     ListView):
    model = Order


urlpatterns = [
    ...
    path("orders/create/", CreateOrder.as_view(), name="create-order"),
    path("orders/", OrdersListView.as_view(), name="orders-list"),

    ]


43. Создайте функцию для создания заказа.

В приложении orders cоздайте service.py.

В нем:

@transaction.atomic
def create_order(user):
    """
    Создать заказ и обновить корзину (добавить значение для внешнего ключа - номер заказа).

    """
    carts = Cart.objects.filter(user=user, order=None)

    new_order = Order.objects.create(user=user)

    carts.update(order=new_order)

    return new_order.pk


Делаем в транзакции. Потому что надо и создать заказ, и обновить корзину.
Транзакция: либо все, либо ничего.

Документация:
1) https://docs.djangoproject.com/en/5.0/ref/models/querysets/#create
2) https://docs.djangoproject.com/en/5.0/ref/models/querysets/#update
3) https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic

Zeal:
1) create
2) update
3) atomic


43. Создайте полноценную view и url для создания заказа.

class CreateOrder(LoginRequiredMixin,
                  View):
    def post(self, request):

        user = request.user
        password = request.POST.get("password")

        password_correct_for_user = auth.authenticate(request, username=user.username, password=password)

        if not password_correct_for_user:
            messages.add_message(request, messages.ERROR, "Неверный пароль")
            return redirect("cart-detail")

        new_order_id = create_order(user)

        messages.add_message(request, messages.INFO, "Ваш заказ номер {} принят к исполнению.".format(new_order_id))

        return redirect("orders-list")


Есть готовый метод authenticate.

Заказ формируется только из корзины. Поэтому об ошибке валидации сообщаем
в CartDetail.

Если заказ создать удалось, редирект на список заказов.


Документация:
1) https://docs.djangoproject.com/en/5.0/topics/auth/default/#authenticating-users

Zeal:
1) authenticate



44. Доработайте CartDetailView - передайте в контекст форму с паролем.

class CartDetailView(LoginRequiredMixin,
                     TemplateView):
    ...

    def get_context_data(self, **kwargs):
        ...
        context["order_form"] = OrderForm()
        ...
        return context


45. Добавьте форму создания заказа в корзину

В приложении orders создайте:

templates/orders/order_form.html


В нем:

{% comment %}

{% include 'orders/order_form.html' %}

{% endcomment %}



{% if object_list %}

<form id="create-order" class="row g-3 mt-3" method="post" action="{% url 'create-order' %}">
    {% csrf_token %}

    <div class="col-md-4">
        {{ order_form }}

        <button class="btn btn-primary mt-3" type="submit">Сформировать заказ</button>

    </div>
</form>

{% endif %}

Идет запрос на модификацию данных. Поэтому метод - POST.

Мы обязаны указать action, потому что запрос будет направлен
не в ту view, которая отрендерила шаблон. Иначе говоря, отрендерило шаблон приложение
CartDetailView, а запрос будет отправлен в CreateOrder.

В cart.html после условия:

{% include 'orders/order_form.html' %}




Документация:
1) https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#url

Zeal:
1) Built-in tag reference    , дальше поиском - "url".


44. Добавьте вью для просмотра списка заказов.

class OrdersListView(LoginRequiredMixin,
                     ListView):
    model = Order

45. Добавьте заглушку шаблона для просмотра списка товаров.

В файле templates/orders/order_list.html написать любой текст.
Например, "Order list".

46. Проверьте создание заказ в работе

При вводе неправильного пароля должно выводиться соответствующее сообщение.
Его цвет должен быть красным.

47. Дополните OrderListView функционалом сортировки заказов

Заказы должны выводиться от новых к старым.

    Дополните OrderListView:


    def get_queryset(self):
        result = Order.objects.filter(user=self.request.user).order_by(
            "-ordered")
        return result




49. Создайте заглушку метода OrderDetailView. Создайте URL.

class OrderDetailView(LoginRequiredMixin,
                      DetailView):
    model = Order



path("orders/<str:pk>/", OrderDetailView.as_view(), name="order-detail"),

50. Дополните модель Order методом get_absolute_url.

    def get_absolute_url(self):
        return reverse('order-detail', kwargs={"pk": self.id})


50. Создайте заглушку шаблона order_detail.html

{% extends 'general/base.html' %}

{% block content %}
Order detail.
{% endblock %}




48. Сверстайте шаблон списка заказов в первом приближении

Функционал удаления заказов пока реализовывать не будем.

{% extends 'general/base.html' %}

{% block content %}
{% include 'general/message.html' %}

<div class="table-responsive small">
    {% if object_list %}
    <table class="table table-striped table-sm">
        <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Заказ</th>
            <th scope="col">Время заказа</th>
            <th scope="col">Статус</th>
        </tr>
        </thead>
        <tbody>

        {% for obj in object_list %}
        <tr>
            <td>{{ forloop.counter }}</td>
            <td><a href="{{ obj.get_absolute_url }}">{{ obj.pk}} </a></td>
            <td>{{ obj.ordered }}</td>
            <td>{{ obj.get_status_display }}</td>
        </tr>
        {% endfor %}
        </tbody>
    </table>
    {% else %}
        <div class="display-6 text-center mb-4">Нет заказов.</div>
    {% endif %}
</div>
{% endblock %}



50. Создайте в первом приближении шаблон просмотра заказа.

Пока не реализуем удаление нового заказа.


{% extends 'general/base.html' %}

{% block headline %}
<h1>Заказ</h1>
{% endblock %}

{% block content %}
<div class="table-responsive">
    <table class="table table-striped table-sm">
        <tbody>
        <tr>
            <td>Номер заказа</td>
            <td>{{ order.id }}</td>
        </tr>
        <tr>
            <td>Дата размещения</td>
            <td>{{ order.ordered }}</td>
        </tr>
        <tr>
            <td>Статус</td>
            <td>{{ order.get_status_display }}</td>
        </tr>
        {% if order.status == 'CANCELLED' %}
        <tr>
            <td>Причина отказа</td>
            <td>{{ order.cancellation_cause }}</td>
        </tr>
        {% endif %}
        </tbody>
    </table>


    <table class="table table-striped table-sm">
        <thead>
        <tr>
            <th scope="col">№</th>
            <th scope="col">Артикул</th>
            <th scope="col">Наименование</th>
            <th scope="col">Цена, руб.</th>
            <th scope="col">Количество, шт.</th>
        </tr>
        </thead>
        <tbody>
        {% for obj in goods%}
        <tr>
            <td scope="col">{{ forloop.counter }}</td>
            <td scope="col">{{ obj.id }}</td>
            <td scope="col">{{ obj.goods.name }}</td>
            <td scope="col">{{ obj.price }}</td>
            <td scope="col">{{ obj.quantity }}</td>
        </tr>


        {% endfor %}

        {% include 'carts/parts/total.html' %}
        </tbody>
    </table>

</div>



{% endblock %}







I. Предварительная подготовка

Изучить tutorial: https://docs.djangoproject.com/en/5.0/
Примечание: Advanced Tutorials изучать не нужно. Учить только
Part 1: Requests and responses
Part 2: Models and the admin site
Part 3: Views and templates
Part 4: Forms and generic views
Part 5: Testing
Part 6: Static files
Part 7: Customizing the admin site
Part 8: Adding third-party packages