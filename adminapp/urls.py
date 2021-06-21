
from django.urls import path
from . import views

app_name = 'adminapp'
urlpatterns = [
    path('', views.Index, name="index"),
]
