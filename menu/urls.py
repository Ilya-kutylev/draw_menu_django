from django.urls import path

from .views import *

urlpatterns = [
    path('', get_index, name='main_menu'),
    path('<path:path>/', draw_menu, name='draw_menu'),
]
