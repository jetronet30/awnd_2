from django.urls import path
from . import views

app_name = 'ocres'

urlpatterns = [
    path('', views.index, name='ocres'),
]