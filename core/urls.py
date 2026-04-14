from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_ru, name='home_ru'),   # 👈 DEFAULT (RU)
    path('en/', views.home_en, name='home_en'),
]