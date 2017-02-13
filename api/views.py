from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def root(request):
    context = { }
    return render(request, 'api/base.html', context)
