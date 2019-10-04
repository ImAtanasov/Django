from django.shortcuts import render
from .models import apartment_sell,rent_sell,apartment_buy,rent_buy
from time import gmtime, strftime


def index(request):
    return render(request, 'index.html', {})
	
	
def description(request):
    return render(request, 'description.html', {})
	
def procedure(request):
    return render(request, 'procedure.html', {})
	
def signup(request):
    return render(request, 'signup.html', {})
	
def login(request):
    return render(request, 'login.html', {})
	
	
def findapartment(request):
    return render(request, 'findapartment.html', {})
	
def giveapartment(request):
	a_list = apartment_sell.objects.all()
	a = apartment_sell()
	if request.method == 'POST':
		
		
		a.location = request.POST.get('location')
		a.date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		a.venue = request.POST.get('venue')
		a.person = request.POST.get('name')
		a.description = request.POST.get('description')
		a.save()
		
	return render(request, 'giveapartment.html', {'apartment_sell':a_list})
	
	
	
def findrent(request):
    return render(request, 'findrent.html', {})
	
def giverent(request):
	a_list = apartment_sell.objects.all()
	a = apartment_sell()
	if request.method == 'POST':
		
		
		a.location = request.POST.get('location')
		a.date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		a.venue = request.POST.get('venue')
		a.person = request.POST.get('name')
		a.description = request.POST.get('description')
		a.save()
		
	return render(request, 'giverent.html', {'apartment_rent':a_list})