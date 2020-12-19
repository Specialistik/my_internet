# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth import authenticate

from .models import Person


def index(request):
    return render(request, 'index.html')

    

def login(request):
    if request.method == "POST":
        try:
            person = Person.objects.get(login=request.POST['username'], password=request.POST['password'])
            return JsonResponse({'token': person.token})
        except Person.DoesNotExist:
            return redirect('/')
        #do something if form is valid
    else:
        return render(request, 'index.html')
