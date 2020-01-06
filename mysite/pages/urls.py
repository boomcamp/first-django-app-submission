from django.urls import path

from . import views  # import all views

urlpatterns = [
    path('', views.index, name='index')
]