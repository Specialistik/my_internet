# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from . import helpers


def index(request):
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(request))


def login(request, user, password):
    return JsonResponse({'token': helpers.generate_token(user, password)})
