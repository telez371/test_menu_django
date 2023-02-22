from django.shortcuts import render
from django.views.generic import ListView
from .models import MenuItem


class MenuItemListView(ListView):
    queryset = MenuItem.objects.filter(parent=None).prefetch_related('children')
    context_object_name = 'menu_items'
    template_name = 'menu/menu.html'

# def draw_menu(request, menu_name):
#     menu_items = MenuItem.objects.filter(parent=None).prefetch_related('children')
#     return render(request, 'menu/menu.html', {'menu_items': menu_items, 'menu_name': menu_name})

