from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    path(r'view/', view_movie, name='view'),
    path(r'add/', add_movie, name='add'),
    path(r'update/<data>', update_movie, name='update'),
    path(r'delete/<str:movie_name>', delete_movie, name='delete'),
    path(r'search', search_movie, name='search'),
]