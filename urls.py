from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_student_form, name='add_student'),  # Form page
    path('', views.dashboard, name='dashboard'),               # Dashboard page
]