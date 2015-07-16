#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import *
#from django.views.decorators.csrf import csrf_protect
#from django.shortcuts import render_to_response
#from django.http import HttpResponseRedirect
#from django.template import RequestContext

from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')
    
def login_view(request):

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
             
        if user is not None:
           if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('login/login.html', context_instance=RequestContext(request))



@login_required(login_url='/login/')
def home(request):
    return render_to_response('login/home.html') 