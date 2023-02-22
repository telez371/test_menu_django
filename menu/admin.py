from django.contrib import admin
from .models import MenuItem
from .forms import MenuItemForm

class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm
    list_display = ('title', 'url', 'parent')

admin.site.register(MenuItem, MenuItemAdmin)

