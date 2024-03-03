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


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt  # Temporarily disable CSRF token for simplicity
def process_elements_form(request):
    if request.method == 'POST':
        # Extract and sum the values from the form data
        print("process was called")
        total_sum = sum(float(value) for key, value in request.POST.items() if value.isdigit())
        print("total sum is", total_sum)
        # Return the sum as JSON response
        return JsonResponse({'total_sum': total_sum})

    # Handle non-POST requests, though this example focuses on POST
    return JsonResponse({'error': 'Invalid request'}, status=400)


def test_ajax(request):
    print("ajax is working")
    return JsonResponse({"message": "Hello from Django!"})