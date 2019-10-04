from django.urls import path
from mvp import views

urlpatterns = [
    path('', views.index, name='index'),
	path('description', views.description, name='description'),
	path('procedure', views.procedure, name='procedure'),
	path('signup', views.signup, name='signup'),
	path('login', views.login, name='login'),
	path('findapartment', views.findapartment, name='findapartment'),
	path('giveapartment', views.giveapartment, name='giveapartment'),
	path('findrent', views.findrent, name='findrent'),
	path('giverent', views.giverent, name='giverent'),
]