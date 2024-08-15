from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
        ordering = ['name']

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URl')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items', verbose_name='Menu_id')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'
        ordering = ['name']

    def __str__(self):
        return self.name
