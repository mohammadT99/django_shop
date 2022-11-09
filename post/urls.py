
from django.urls import path
from .views import *
app_name='web'
urlpatterns = [
    path('home/' , home , name="home" ),

    path('',index,name="index"),

    path('detail/<slug:slug>',detail,name='detail'),

    path('about/',about,name='about'),

    path('contact/',Contact, name='contact'),



]
