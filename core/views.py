# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Person


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def login(request):
    if request.method != "POST":
        return render(request, 'login.html')
    else:
        try:
            person = Person.objects.get(login=request.POST['username'], password=request.POST['password'])
            return JsonResponse({'result': True, 'token': person.token})
        except Person.DoesNotExist:
            return JsonResponse({'result': False, 'token': '', 'message': 'person not found'})
