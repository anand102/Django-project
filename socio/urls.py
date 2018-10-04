from django.urls import path
from .import views

app_name='socio'
urlpatterns = [
    path('', views.social_list, name='list'),
    path('create/', views.social_create, name='create'),
    path('<slug:slug>/', views.social_detail, name='detail'),
    
]