from django.contrib import admin
from django.urls import path
from authapp import views as authapp_views
app_name = 'authapp'
urlpatterns = [
    path('login/', authapp_views.login, name='login'),
    path('logout/', authapp_views.logout, name='logout'),
    path('register/',authapp_views.register, name= 'register'),
    path('edit/',authapp_views.edit,name ='edit')

]