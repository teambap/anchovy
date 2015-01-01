#-*- coding: utf-8 -*-
import datetime
from django import forms
from django.contrib.auth.models import AnonymousUser
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework.renderers import JSONRenderer
from wish.models import Item
from wish.serializers import ItemSerializer
from django.utils import timezone

class ItemForm(forms.Form):
    name = forms.CharField()
    link = forms.CharField()

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    # http://abipictures.tistory.com/915
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json; charset=UTF-8'
        super(JSONResponse, self).__init__(content, **kwargs)



def list(request):

    items = []
    user_id = None
    if request.user != None:
        user_id = request.user.id
        items = Item.objects.filter(user_id=user_id)

    context = RequestContext(request,
                           {'request':request,
                            'items':items,
                            'user': request.user})
    return render_to_response('wish/list.html',
                             context_instance=context)

def list_json(request):

    items = []
    user_id = None

    result = {}
    result['code'] = "200"
    result['desc'] = "OK"

    to = request.GET.get('to', 1)
    length = request.GET.get('length', 20)

    if request.user.is_authenticated():
        user_id = request.user.id
        item_list = Item.objects.filter(user_id=user_id).order_by('-created')

        paginator = Paginator(item_list, length)
        items = paginator.page(to)

        serializer = ItemSerializer(items, many=True)

        data = {}
        data['items'] = serializer.data

        result['data'] = data
    else:
        result['code'] = '401'
        result['desc'] = 'Authorize Error'

    return JSONResponse(result)

def add_form(request):
    form = ItemForm()
    return render_to_response('wish/add.html', {'form':form})

@csrf_exempt
def add(request):

    result = {}
    result['code'] = '200'
    result['desc'] = 'OK'

    if not request.user.is_authenticated():
        result['code'] = '401'
        result['desc'] = 'Authorize Error'
        return result


    if request.method == 'POST':
        # form = ItemForm(request.POST)

        # if form.is_valid():
        name = request.POST.get('name')
        link = request.POST.get('link')

        if name == None or link == None:
            result['code'] = '400'
            result['desc'] = 'Bad Request'
            return JSONResponse(result)

        user_id = request.user.id
        item = Item()
        item.user_id = user_id
        item.link = link
        item.name = name
        item.status = 'W'
        item.created = timezone.localtime(timezone.now())
        item.modified = timezone.localtime(timezone.now())

        item.save()

    else:
        result['code'] = '400'
        result['desc'] = 'Bad Request'

    return JSONResponse(result)



@csrf_exempt
def remove(request, item_id):
    result = {}
    result['code'] = '200'
    result['desc'] = 'OK'

    if request.user.is_authenticated():

        id = item_id

        if id == None:
            result['code'] = '400'
            result['desc'] = 'Bad Request'

        user = request.user
        item = Item.objects.filter(user_id=user.id).filter(id=id)
        if item.exists():
            item.delete()
        else:
            result['code'] = '404'
            result['desc'] = 'Not Found'

    else:
        result['code'] = '401'
        result['desc'] = 'Authorize Error'


    return JSONResponse(result)