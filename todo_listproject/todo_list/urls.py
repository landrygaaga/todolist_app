from django.urls import path
from . import views

urlpatterns = [
    # Route pour la page d'accueil (liste + ajout)
    path('', views.index, name='index'),
    
    # Route pour la modification (attend un ID / clé primaire)
    path('update/<str:pk>/', views.updateTask, name='update_task'),
    
    # Route pour la suppression (attend un ID / clé primaire)
    path('delete/<str:pk>/', views.deleteTask, name='delete_task'),
]
