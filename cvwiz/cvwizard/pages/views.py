from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request, *args, **kwargs):
    #return HttpResponse("<h1>hello world</h1>")
    return render(request, 'fp.html')

def second_page(request, *args, **kwargs):
    #return HttpResponse("<h1>second page ok</h1>")
    return render(request, 'regg.html')
