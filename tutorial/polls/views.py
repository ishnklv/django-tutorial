# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<button>Download<button>")
def test(request):
    return HttpResponse("Debug")


