from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render_to_response("main/home.html", {'hello': "Hello World!"});

def building(request):
	return render_to_response("main/building.html", {'hello': "Hello World!"});

def producten(request):
	return render_to_response("main/producten.html", {'hello': "Hello World!"});

def aboutus(request):
	return render_to_response("main/aboutus.html", {'hello': "Hello World!"});

def contact(request):
	return render_to_response("main/contact.html", {'hello': "Hello World!"});
