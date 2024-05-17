from django.urls import path
from.import views


urlpatterns = [
    path('', views.std_app, name = 'std_app'),
]
