from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('userhome', views.userhome, name='userhome'),
    path('eror',views.eror, name='eror'),
    path('upload', views.upload, name='upload'),
    path('home', views.index, name='index'),
    path('signout', views.signout, name='lot')

]