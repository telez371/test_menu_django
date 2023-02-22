from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.MenuItemListView.as_view(), name='menu'),
]

# from .views import draw_menu

# app_name = 'draw_menu'
#
# urlpatterns = [
#     path('<str:menu_name>/', draw_menu, name='draw_menu'),
# ]