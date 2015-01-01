from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext
from django.contrib.auth import logout as auth_logout
from rest_framework.renderers import JSONRenderer
from users.serializers import ProfileSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    # http://abipictures.tistory.com/915
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json; charset=UTF-8'
        super(JSONResponse, self).__init__(content, **kwargs)


def info(request):

    result = {}
    result['code'] = "200"
    result['desc'] = "OK"

    if request.user.is_authenticated():
        user = request.user
        profile = user.profile
        print("image:%s" % (profile.profile_image_url))

        serializer = ProfileSerializer(profile)

        data = {}
        data['profile'] = serializer.data

        result['data'] = data
    else:
        result['code'] = '401'
        result['desc'] = 'Authorize Error'

    return JSONResponse(result)


def home(request):

    if request.user != None:
        user = request.user
        if user.is_active == True:
            # profile = Profile.objects.get(user=user)
            profile = user.profile
            print("image:%s" % (profile.profile_image_url))

            # return HttpResponseRedirect('/wwish/index.html')

    context = RequestContext(request,
                           {'request':request,
                            'user': request.user})
    return render_to_response('users/home.html',
                             context_instance=context)

def logout(request):

    result = {}
    result['code'] = "200"
    result['desc'] = "OK"

    if request.user.is_authenticated():
        auth_logout(request)
    else:
        result['code'] = '401'
        result['desc'] = 'Authorize Error'

    return JSONResponse(result)
