"""doggag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView #will not be needed after moving LOGIN to the app

urlpatterns = [
    path('', include('apps.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), #order is important
    path('accounts/', include('django.contrib.auth.urls')),

    # this templates will be "on" the apps, I'll do the merge later.
    path('testingLogin/', TemplateView.as_view(template_name='home.html'), name='home'),
]
