from django import forms

class ElementForm(forms.Form):
    # Define form fields for all possible elements
    H = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    He = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    Li = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    Be = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    B = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    C = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    N = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    O = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    F = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    Ne = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    Na = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    Mg = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    # Add other elements as needed
