from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [path('',views.historias_clinicas_view,name='historias_clinicas_view'),]
