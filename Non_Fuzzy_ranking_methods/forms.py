from django import forms
from .models import Method, Indicator, Choice

class MethodForm(forms.ModelForm):
    class Meta:
        model = Method
        fields = ['name', 'hyperparameter_value']

class IndicatorForm(forms.ModelForm):
    class Meta:
        model = Indicator
        fields = ['name', 'type', 'weight']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['name']