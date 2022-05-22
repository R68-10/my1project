from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name = "index"), #index 
    path('country', views.country, name = "country"),
    path('about', views.about, name = "about"), #render return html file + it must be templates
]