from django.shortcuts import render
from django.views import View
from .models import WebPost

# Create your views here.

def home(request):
    webpost = WebPost.objects.all()
    return render(request, 'home.html', {'webpost': webpost})

class Home(View):
    def get(self, request):
        webpost = WebPost.objects.all()
        return render(request, 'home.html', {'webpost': webpost})