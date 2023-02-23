## Тестовое задание python backend developer

Написать серверную часть приложения для новостей

Задача :
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6 )Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8)На отрисовку каждого меню требуется ровно 1 запрос к БД
 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
 При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.


<p align="left">
     <a href="https://imgbb.com/"><img src="https://i.ibb.co/SdDscty/903158347.jpg" alt="903158347" border="0"></a>
</p>


## Решение


<p align="left">
     <a href="https://imgbb.com/"><img src="https://i.ibb.co/kKHz4hZ/unSidg5H.jpg" alt="unSidg5H" border="0"></a>
</p>


<p align="left">
   <img src="https://img.shields.io/badge/django-4.1.6-blueviolet" alt="django Version" >
   <img src="https://img.shields.io/badge/sqllite-3-blue" alt="DRF Version">
</p>

## Редактируется в стандартной админке Django
<p align="left">
     <a href="https://ibb.co/hVdf2F5"><img src="https://i.ibb.co/1TX6RGV/image.png" alt="image" border="0"></a>
</p>

