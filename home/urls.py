
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("signup", views.signup,name='signup'),
    path("login", views.handlelogin,name='handlelogin'),
    path("profile", views.profile, name='profile'),
    path("contact", views.contact, name='contact'),
   
]

