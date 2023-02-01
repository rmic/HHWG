from django.urls import path
from . import views

urlpatterns = [
    path('query/', views.my_view, name='my_view'),
]