"""project URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('mvp.urls')),
	path('description', include('mvp.urls')),
	path('procedure', include('mvp.urls')),
	path('signup', include('mvp.urls')),
	path('login', include('mvp.urls')),
	path('findapartment', include('mvp.urls')),
	path('giveapartment', include('mvp.urls')),
	path('findrent', include('mvp.urls')),
	path('giverent', include('mvp.urls')),
]
