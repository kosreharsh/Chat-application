from django.urls import path
from .views import index, room

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]
