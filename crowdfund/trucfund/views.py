from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	return render_to_response("trucfund/index.html")

def discover(request):
	return render_to_response("trucfund/browse.html")

def project(request):
	return render_to_response("trucfund/project.html")

def profile(request):
	return render_to_response("trucfund/profile.html")

def create(request):
	return render_to_response("trucfund/create.html")