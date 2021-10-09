from django.urls import path
from .views import *

app_name='jobs'
urlpatterns = [
    path('', jobs_all, name='jobs_all'),
    path('create/', job_create, name='job_create'),
    path('<str:slug>/edit/', job_update, name='job_update'),
    path('<str:slug>/delete/', job_delete, name='job_delete'),
    path('<str:slug>/', job_detail, name='job_detail'),
    
]
