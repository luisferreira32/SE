from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('<int:pk>/', views.UserView.as_view(), name='userdetail'),
    path('<int:pk>/update', login_required(views.ProfileUpdate.as_view()), name='updateprof'),
]
