import datetime
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from wish.models import Item


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


def add(request):

    print("add called")

    item = None

    if request.user != None:
        user_id = request.user.id
        item = Item()
        item.user_id = user_id
        item.link = 'http://www.nikestore.co.kr/goods/showGoodsDetailCache.lecs?goodsNo=NK31041887&colorOptionValueCode=698902-003'
        item.name = '에어맥스 2015'
        item.status = 'W'
        item.created = datetime.datetime.today()
        item.modified = datetime.datetime.today()

    if item != None:
        item.save()

    return redirect('list')