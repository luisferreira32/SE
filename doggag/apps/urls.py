from django.urls import path, include
from . import views

app_name = "apps"
urlpatterns = [
    path('', views.ScrollView.as_view(), name="home"),
    path('<int:post_id>/up/', views.ScrollView.upvote, name="upvote"),
    path('<int:post_id>/down/', views.ScrollView.downvote, name="downvote"),
]
