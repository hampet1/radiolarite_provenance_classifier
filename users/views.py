from django.shortcuts import render
from .forms import ElementForm
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


from django.http import JsonResponse


def process_elements_form(request):
    """
    process all data and feed them the model
    """
    if request.method == 'POST':
        form = ElementForm(request.POST)
        if form.is_valid():
            # all values from the file
            total_sum = sum(value for value in form.cleaned_data.values() if value is not None)
            return JsonResponse({'total_sum': total_sum})
        else:
            # Return form errors as JSON
            return JsonResponse({'error': form.errors.as_json()}, status=400)

    # If it's not a POST request, return an error
    return JsonResponse({'error': 'Invalid request'}, status=400)



def test_ajax(request):
    print("ajax is working")
    return JsonResponse({"message": "Hello from Django!"})