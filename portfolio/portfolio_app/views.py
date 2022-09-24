from django.shortcuts import render
from portfolio_app.models import Project, Contact


def home(request):
    context = {
        'text': "Hello, this is my personal page! Here you can find everything you want about me."
    }
    return render(request=request, template_name='converter_app/index.html', context=context)


def projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects
    }
    return render(request=request, template_name='converter_app/projects.html', context=context)


def contacts(request):
    return render(request=request, template_name='converter_app/contacts.html')
