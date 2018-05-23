from django.urls import path

from mlm import views

urlpatterns = [
    path('', views.index, name='index'),
]