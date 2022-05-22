from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name ='contact') # write the name to use it in action form for html

]