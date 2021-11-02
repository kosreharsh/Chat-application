from django.urls import path
from .views import index, join_room

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('chat/<str:room_name>/', join_room, name='room'),
]
