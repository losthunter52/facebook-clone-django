from core import views
from django.urls import path

#HOME
urlpatterns = [
    path('home/', views.home, name='home'),
]