from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('receita/<int:receita_id>/', views.receita, name = 'receita'),
    path('ssearch/', views.search, name = 'search')
]