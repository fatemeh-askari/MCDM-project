from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/contact.html')
    else:
        form = ContactForm()

    return render(request, './Contact/Contact.html', {'form': form})
