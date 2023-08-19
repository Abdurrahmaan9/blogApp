from django.urls import path
from . import views

app_name = 'blog' #to organize URLS by application

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_details, name='post_details'), 
]