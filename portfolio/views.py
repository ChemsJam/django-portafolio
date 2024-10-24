from django.shortcuts import render, get_object_or_404
from .models import Projects
from certificates.models import Certificate

# Create your views here.
def home(request):
    projects = Projects.objects.all()
    certificates = Certificate.objects.all()
    
    return render(request, 'home.html',{
        'projects' : projects,
        'certificates' : certificates
    })
    

