from django.urls import path
from . import views

urlpatterns = [
    path('input_information/', views.mainview)
]
