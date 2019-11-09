from django.urls import path, include
#not advisable in produciton, keeping images in the server
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "apps"
urlpatterns = [
    path('upload/',views.upload,name='upload'),
    path('', views.ScrollView.as_view(), name="home"),
    path('<int:post_id>/up/', views.ScrollView.upvote, name="upvote"),
    path('<int:post_id>/down/', views.ScrollView.downvote, name="downvote"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
