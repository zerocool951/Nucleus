from django.shortcuts import render_to_response
from django.http import HttpResponse
from website.models import Website
from neo4jrestclient.client import GraphDatabase
# Create your views here.

def home(request):
	return render_to_response("main/home.html", {'hello': "Hello World!"});

def building1(request):
	return render_to_response("main/building-1.html", {'hello': "Hello World!"});

def building2(request):
	return render_to_response("main/building-2.html", {'hello': "Hello World!"});

def building3(request):
	return render_to_response("main/building-3.html", {'hello': "Hello World!"});

def finish(request):
	return render_to_response("main/finish.html", {'hello': "Hello World!"});

def producten(request):
	return render_to_response("main/producten.html", {'hello': "Hello World!"});

def order(request):
	return render_to_response("main/order.html", {'hello': "Hello World!"});

def contact(request):
	return render_to_response("main/contact.html", {'hello': "Hello World!"});
