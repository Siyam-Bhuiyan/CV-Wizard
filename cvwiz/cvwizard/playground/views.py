from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainview(request):
    return render(request, 'fromss.html')