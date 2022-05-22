from django.urls import path
from . import views

urlpatterns = [
    path("section2",views.section2, name = "section2")
]