from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Project
from .forms import ContactForm

def portfolio_view(request):
    return render(request, 'portfolio/portfolio.html')

def about_view(request):
    return render(request, 'portfolio/about.html')

def skills_view(request):
    return render(request, 'portfolio/skills.html')

def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def contact_view(request):
    message_sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send the email
            send_mail(
                f'Message from {name} ({email})',  # Subject
                message,  # Message
                email,  # From email
                [settings.EMAIL_HOST_USER],  # To email
                fail_silently=False,
            )
            
            # Set the flag to true for successful submission
            message_sent = True
            form = ContactForm()  # Reset the form after submission

    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form, 'message_sent': message_sent})
