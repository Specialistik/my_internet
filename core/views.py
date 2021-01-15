# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Person


def index(request):
    return render(request, 'index.html')


@require_http_methods(["POST"])
@csrf_exempt
def login(request):
    try:
        person = Person.objects.get(login=request.POST['username'], password=request.POST['password'])
        return JsonResponse({'result': True, 'token': person.token})
    except Person.DoesNotExist:
        return JsonResponse({'result': False, 'token': '', 'message': 'person not found'})


@require_http_methods(["POST"])
def payment(request):
    pass


@require_http_methods(["POST"])
def profile(request):
    pass