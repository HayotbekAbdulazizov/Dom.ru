from os import name
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter   # REST-Framework    


app_name = 'api'


urlpatterns = [
# API view
    path('post/', views.PostApiView.as_view(), name='postCreateView'),

]