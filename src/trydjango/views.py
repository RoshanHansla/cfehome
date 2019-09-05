from django.shortcuts import render, HttpResponse

def home(request):
	return render(request,'home.html')

def nextpage(request):
	return render(request,'home2.html')
