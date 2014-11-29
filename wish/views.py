from django.shortcuts import render, render_to_response
from django.template import RequestContext


def list(request):

    context = RequestContext(request,
                           {'request':request,
                            'user': request.user})
    return render_to_response('wish/list.html',
                             context_instance=context)