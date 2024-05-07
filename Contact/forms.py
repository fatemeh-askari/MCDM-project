from django.forms import ModelForm, forms
from .models import ContactUs

class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']