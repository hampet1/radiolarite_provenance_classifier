from django.shortcuts import render
from .forms import ElementForm
import numpy as np
from joblib import load
# Create your views here.

# for xrf using lda
xrf_model = load('lda_model_xrf.joblib')
# for ablation, using randomforest
ablation_model = load('ablation_model.joblib')
# for multimodal, using randomforest
multimodal_model = load('multimodal_model.joblib')



def index(request):
    # Logic for the home view
    return render(request, 'index.html')  # Make sure 'home.html' exists in your templates directory

def guideline(request):
    # Logic for the guideline view
    return render(request, 'guideline.html')  # Make sure 'guideline.html' exists in your templates directory

def about(request):
    # Logic for the about project view
    return render(request, 'about.html')  # Make sure 'about_project.html' exists in your templates directory


def classify(request):
    return render(request)


from django.http import JsonResponse


def process_elements_form(request):
    """
    process all data and feed them the model
    """
    if request.method == 'POST':
        # passing a type of the model
        # At the beginning of your process_elements_form view
        print("the whole request: ",request.POST)  # This should print out the full POST data

        form = ElementForm(request.POST)
        if form.is_valid():
            # all values from the file
            try:
                model_type = request.POST.get('method')
                print("model is: ", model_type)
                print("values: ", form.cleaned_data.values())
                print("all values: ", request.POST)

                all_elements = []
                all_values_in_post = request.POST
                for num, val in enumerate(all_values_in_post.values()):
                    print(f'{num} and {val}')
                    if num == 1:
                        model_type = val
                    if num > 1:
                        all_elements.append(float(val))
                #values_ = [float(value) for value in form.cleaned_data.values() if value is not None]
                print("values now: ", all_elements)
                print("values now: ", model_type)

                input_elements = all_elements
                print("hdsjk", input_elements)
                print("input elemsensts ", type(input_elements))
                # Ensure the input is in the correct shape (1 row with 7 columns)
                input_array = np.array([input_elements])
                print(f"my input is :", input_array)
                print(f"type :", type(input_array))
                print("model is, ", model_type)
                if model_type == "openXRF":
                    model = xrf_model
                elif model_type == "openAblation":
                    model = ablation_model
                elif model_type == "openMultimodal":
                    model = multimodal_model
                else:
                    print("none of the models were used")


                print("current mocel", model)
                if hasattr(model, "predict_proba"):
                    print("we are good")
                    print("ïnput is, ", input_array)
                    # Get the probability estimates for all classes
                    probabilities = model.predict_proba(input_array)
                    print("probability is: ", probabilities)
                    # Get the index of the highest probability
                    class_index = np.argmax(probabilities, axis=1)[0]
                    print("class index is: ", class_index)
                    # Adjust the index to match your class labels
                    predicted_class_label = class_index + 1
                    print("predicted class index is", predicted_class_label)
                    # Obtain the highest probability
                    highest_probability = probabilities[0, class_index]

                    regions_name = {1: "Northern Calcareous Alps (Austria)",
                                    2: "St. Veit Klippen Belt (Austria)",
                                    3: "Gerecse Mountains (Hungary)",
                                    4: "Palava Hills (Czech Republic)",
                                    5: "Western Slovakia",
                                    6: "Pieniny (Poland)",
                                    7: "Bakony Mts. (Hungary)"}


                    res = f"{regions_name[predicted_class_label]} with a probability of {highest_probability*100:.2f}%"
                    print("res is : ", res)
                    #total_sum = sum(value for value in form.cleaned_data.values() if value is not None)
                    return JsonResponse({'total_sum': res})

            except Exception as e:
                print(f"the error is: {e}")

        else:
            # Return form errors as JSON
            return JsonResponse({'error': form.errors.as_json()}, status=400)

    # If it's not a POST request, return an error
    return JsonResponse({'error': 'Invalid request'}, status=400)



def test_ajax(request):
    print("ajax is working")
    return JsonResponse({"message": "Hello from Django!"})