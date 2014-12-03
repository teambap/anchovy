import datetime
from django import forms
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from wish.models import Item


class ItemForm(forms.Form):
    name = forms.CharField()
    link = forms.CharField()


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

    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            link = form.cleaned_data['link']

            if request.user != None:
                user_id = request.user.id
                item = Item()
                item.user_id = user_id
                item.link = link
                item.name = name
                item.status = 'W'
                item.created = datetime.datetime.today()
                item.modified = datetime.datetime.today()

            if item != None:
                item.save()

        return redirect('list')

    else:
        form = ItemForm()
        return render(request, 'wish/add.html', {'form':form})