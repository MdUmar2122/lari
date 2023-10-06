from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.template import loader


# Create your views here.

def umar(request):
    context = {}
    return render(request, 'index.html', context)

def mark1_detail(request):
    site = "https://www.google.com/"
    return HttpResponse(f"Here <a href={site}>Google Here</a>")

