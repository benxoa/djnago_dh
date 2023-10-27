from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')

        Form.objects.create(
            name=name, image=image
        )


    return render(request, 'home.html')
