from django.urls import path
from pwinside import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('output', views.output, name="output")
]