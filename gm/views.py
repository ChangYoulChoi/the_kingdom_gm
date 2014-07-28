# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.core.context_processors import csrf
import hashlib
from gm.models import *
from django import forms

@csrf_exempt
def gm_login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id', '')
        if user_id:
            user_pw = request.POST.get('user_pw', '')
            hashed_passwrod = hashlib.md5(user_pw).hexdigest()
            try:
                manager = Manager.objects.get(user_id=user_id)
                if manager.user_pw == hashed_passwrod:
                    return HttpResponseRedirect('/gm/main/')
                else:
                    error_msg = 'Invaild USER PASSWORD'
            except:
                error_msg = 'Invaild USER ID'

            return render_to_response('login.html', {'form_error':error_msg})
    else:
        return render_to_response('login.html')


def gm_main(request):
    return render_to_response('main.html')


@csrf_exempt
def manager_create(request):
    return render_to_response('manager_form.html')

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form, 'err_msg':'Massage Error'})

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


"""


def gm_login_proc(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    manager = Manager(user_id=username)
    hashed_password = hashlib.md5(password).hexdigest()
    print hashed_password
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/gm/main/')
    else:
        return HttpResponseRedirect('/gm/login/')

def manager_create(request):
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    user.is_staff = True
    user.save()
    return HttpResponseRedirect('/gm/login/')


def gm_main(request):
    return render_to_response('main.html', {'full_name':request.user.username})

"""