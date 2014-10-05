from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext


def index(request):
    template = loader.get_template('users/index.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))


def info(request):
    return HttpResponse('Hello, world. ')


def add(request):
    return HttpResponse('Hello, world. ')




