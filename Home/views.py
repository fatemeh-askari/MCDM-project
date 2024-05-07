from django.shortcuts import render
from Blog.models import Article
from Contact.forms import ContactForm

def home(request):
    latest_articles = Article.objects.filter(is_active=True)[:10]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can add a success message here
            return render(request, 'Home/Home.html')  # Replace 'success_url' with the URL name of your success page
    else:
        form = ContactForm()
    return render(request, 'Home/Home.html', {'latest_articles': latest_articles, 'form': form,})



