from django.urls import path, include
#not advisable in produciton, keeping images in the server
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "apps"
urlpatterns = [
    path('', views.ScrollView.as_view(), name="home"),
    path('upload/',views.CreatePostView.as_view(),name='upload'),
    path('<int:pk>/', views.PostView.as_view(), name="detail"),
    path('<int:post_id>/comm/', views.PostView.commentpost, name="comment"),
    path('<int:post_id>/up/', views.ScrollView.upvote, name="upvote"),
    path('<int:post_id>/down/', views.ScrollView.downvote, name="downvote"),
    path('<int:post_id>/upD/', views.PostView.upvote, name="upvoteD"),
    path('<int:post_id>/downD/', views.PostView.downvote, name="downvoteD"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
