from django.urls import path
from .views import *
app_name='profiles'
urlpatterns = [
    path('', profiles_all, name='profiles_all'),
    path('<str:slug>/', profile_detail, name='profile_detail'),
    path('<str:slug>/edit/', profile_update, name='profile_update'),
    path('<str:slug>/delete/', profile_delete, name='profile_delete'),
    
]