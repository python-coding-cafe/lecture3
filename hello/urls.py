from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mo', views.mo, name='mo'),
    path('<str:name>', views.greet, name='greet'),
]