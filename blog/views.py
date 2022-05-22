from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#create a view to return the home html page
def home(request):
    return render(request, "home.html")

#create a view to render an about me html page
def about(request):
    return render(request, "about.html") 

#create a view to render a contacts html page
def contact(request):
    return render(request, "contact.html")