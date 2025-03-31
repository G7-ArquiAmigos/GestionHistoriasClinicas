from django.urls import path
from . import views
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [path('',views.historias_clinicas_view,name='historias_clinicas_view'),
               path('historiacreate/', csrf_exempt(views.historias_create), name='historiacreate'),]
