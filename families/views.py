from django.shortcuts import render
from django.http import HttpResponse

from . models import Family


def index(request):
    families = Family.objects.all()
    context  = {'families': families}
    return render( request, 'families/index.html', context )

def detail(request, family_id):
    return HttpResponse("Hello, world. You're at the families index.")

def create(request):
    return HttpResponse("creating.")

def edit(request, family_id):
    return HttpResponse("editing.")

def delete(request, family_id):
    return HttpResponse("deleting.")