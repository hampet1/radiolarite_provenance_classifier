from django import forms

class ElementForm(forms.Form):
    # Define form fields for all possible elements
    H = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    He = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    Li = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    Be = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    B = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    C = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    N = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    O = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    F = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    Ne = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    Na = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    #Mg = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    # Add other elements as needed 'Ti', 'Mn', 'Fe', 'Ni', 'Cu', 'Zn', 'As', 'Rb', 'Sr'
    Ti = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    Mn = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    Fe = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    Ni = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    Cu = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    Zn = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    As = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    Rb = forms.DecimalField(max_digits=8, decimal_places=6, required=False)
    Sr = forms.DecimalField(max_digits=8, decimal_places=6, required=False)