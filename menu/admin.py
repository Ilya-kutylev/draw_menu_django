from django.contrib import admin

from .models import *


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'menu', 'parent')
    list_display_links = ('id', 'name')
    list_filter = ('menu',)
    prepopulated_fields = {'slug': ('name',)}
