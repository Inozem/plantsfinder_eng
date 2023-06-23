from django.urls import path

from . import views

app_name = 'plants'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('plants/<str:category>/', views.plants_list, name='plants_list'),
    path(
        'plants/<str:category>/<str:plant_slug>/',
        views.plant_info,
        name='plant_info'
    ),
]
