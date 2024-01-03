from django.shortcuts import render, get_object_or_404
from .models import Projects

# Create your views here.
def home(request):
    projects = Projects.objects.all()
    return render(request, 'home.html',{
        'projects' : projects
    })
    

