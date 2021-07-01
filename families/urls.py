from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='family.index'),
    path('<int:family_id>/', views.detail, name='family.detail'),
    path('<int:family_id>/create/', views.create, name='family.create'),
    path('<int:family_id>/edit/', views.edit, name='family.edit'),
    path('<int:family_id>/delete/', views.edit, name='family.delete'),
]