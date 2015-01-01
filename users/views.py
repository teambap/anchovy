from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext
from django.contrib.auth import logout as auth_logout

from django.views.decorators.csrf import csrf_exempt


# class UserForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=30)
#     last_name = forms.CharField(label='Last Name', max_length=30)
#     email = forms.CharField(label='email', max_length=40)
#     user_id = forms.CharField(label='Id', max_length=30)
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

def index(request):
    template = loader.get_template('users/index.html')
    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))


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

# @csrf_exempt
# def add(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             user_id = form.cleaned_data['user_id']
#             print("email:%s first_name:%s last_name:%s user_id:%s" % (email, first_name, last_name, user_id))
#
#             user = User()
#             user.email = email
#             user.last_name = last_name
#             user.first_name = first_name
#             user.user_id = user_id
#             user.save()
#
#             return HttpResponseRedirect('./')
#     else:
#         form = UserForm()
#
#
#     return render(request, 'users/add.html', {'form':form})



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
