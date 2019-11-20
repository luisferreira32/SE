from django.contrib import admin
from .models import Profile
from apps.models import Post, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
