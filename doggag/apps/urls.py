from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ScrollView.as_view(), name="home"),
]
