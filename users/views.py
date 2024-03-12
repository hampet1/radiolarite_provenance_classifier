from django.shortcuts import render
from .forms import ElementForm
import numpy as np
from joblib import load
# Create your views here.

lda_model = load('lda_model_xrf.joblib')



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
            print("values: ", form.cleaned_data.values())
            values_ = [float(value) for value in form.cleaned_data.values() if value is not None]
            print("values now: ", values_)
            # Ensure the input is in the correct shape (1 row with 7 columns)
            input_array = np.array([values_])


            if hasattr(lda_model, "predict_proba"):
                # Get the probability estimates for all classes
                probabilities = lda_model.predict_proba(input_array)

                # Get the index of the highest probability
                class_index = np.argmax(probabilities, axis=1)[0]

                # Adjust the index to match your class labels
                predicted_class_label = class_index + 1

                # Obtain the highest probability
                highest_probability = probabilities[0, class_index]

                regions_name = {1: "Northern Calcareous Alps (Austria)",
                                2: "St. Veit Klippen Belt (Austria)",
                                3: "Gerecse Mountains (Hungary)",
                                4: "Palava Hills (Czech Republic)",
                                5: "Western Slovakia",
                                6: "Pieniny (Poland)",
                                7: "Artefacts (Czech Republic)"}


                res = f"{regions_name[predicted_class_label]} with a probability of {highest_probability*100:.2f}%"

                #total_sum = sum(value for value in form.cleaned_data.values() if value is not None)
                return JsonResponse({'total_sum': res})
        else:
            # Return form errors as JSON
            return JsonResponse({'error': form.errors.as_json()}, status=400)

    # If it's not a POST request, return an error
    return JsonResponse({'error': 'Invalid request'}, status=400)



def test_ajax(request):
    print("ajax is working")
    return JsonResponse({"message": "Hello from Django!"})