from django.urls import path
from . import views

app_name = 'ebooklist'
urlpatterns = [
    path('', views.index, name='index'),
    path('ids/', views.ids, name='ids'),
    path('getlist/', views.getlist, name='getlist'),
    path('collect/', views.collect, name='collect'),
    # path('getlist/', views.getlist, name='getlist'),
]
