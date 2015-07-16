from django.http import *
#from api.forms import DonorForm
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import datetime



@login_required(login_url='/login/')
def addrecord(request):
	#if request.POST:
    #    form = DonorForm(request.POST)
     #  	new_donor = form.save()
     #  	return HttpResponseRedirect('/main/')

    return render_to_response('api/add.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def search(request):
    return render_to_response('api/search.html')