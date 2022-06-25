from django.urls import path
from Home.views import index, new, robo_api

urlpatterns = [
    path('', index),
    path('api', robo_api),
    path('new', new)
]
