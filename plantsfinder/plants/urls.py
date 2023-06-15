from django.urls import path

from . import views

app_name = 'plants'

urlpatterns = [
    path('<str:category>/', views.plants_list, name='plants_list'),
    path(
        '<str:category>/<str:plant_slug>/',
        views.plant_info,
        name='plant_info'
    ),
]
