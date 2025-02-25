
from django.contrib import admin
from django.urls import path
from quickapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('about/', views.about),
]
