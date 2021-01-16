# -*- coding: utf-8 -*-
import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Person, Payment


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
    if ('access_token' in request.headers):
        try:
            person = Person.objects.get(login=request.POST['username'], password=request.POST['password'])
            payment = Payment.objects.create(
                user = person,
                sum = request.POST['sum'],
                datetime = datetime.datetime.now(),
                status = 'in_progress'
            )
            return JsonResponse(person)
        except Person.DoesNotExist:
            return JsonResponse({'result': False, 'token': '', 'message': 'person not found'})


@require_http_methods(["GET"])
def profile(request):
    if ('access_token' in request.headers):
        try:
            person = Person.objects.get(token=request.headers['access_token'])
            return JsonResponse({
                'balance': person.balance,
                'payment_date': person.payment_date,
                'monthly_payment': person.monthly_payment,
                'fio': person.fio,
                'sim': person.sim
            })
        except Person.DoesNotExist:
            return JsonResponse({'result': False, 'token': '', 'message': 'person not found'})
