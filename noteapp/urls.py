from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('create/', views.note_form, name='note_create'),
    path('<int:pk>/edit/', views.note_form, name='note_update'),
]