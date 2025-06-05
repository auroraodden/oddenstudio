from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import About, Education, Experience, Project, Skill
from .forms import ContactForm

def home_view(request):
    return render(request, 'core/home.html')

def about_view(request):
    about = About.objects.first()
    return render(request, 'core/about.html', {'about': about})

def education_view(request):
    education = Education.objects.all()
    return render(request, 'core/education.html', {'education': education})

def experience_view(request):
    experience = Experience.objects.all()
    return render(request, 'core/experience.html', {'experience': experience})

def project_view(request):
    projects = Project.objects.all()
    return render(request, 'core/projects.html', {'projects': projects})

def skill_view(request):
    skills = Skill.objects.all()
    return render(request, 'core/skills.html', {'skills': skills})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('contact_success')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'core/contact_success.html')
