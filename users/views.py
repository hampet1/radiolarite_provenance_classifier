from django.shortcuts import render

# Create your views here.

def index(request):
    # Logic for the home view
    return render(request, 'index.html')  # Make sure 'home.html' exists in your templates directory

def guideline(request):
    # Logic for the guideline view
    return render(request, 'guideline.html')  # Make sure 'guideline.html' exists in your templates directory

def about(request):
    # Logic for the about project view
    return render(request, 'about.html')  # Make sure 'about_project.html' exists in your templates directory

def maps(request):
    # Logic for the maps view
    return render(request, 'maps.html')  # Make sure 'maps.html' exists in your templates directory


def classify(request):
    return render(request)