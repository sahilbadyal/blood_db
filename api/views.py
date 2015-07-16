from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from api.forms import DonorForm


@login_required(login_url='/login/')
def addrecord(request):
	context = RequestContext(request)
	if request.POST:
		form = DonorForm(request.POST)
		if form.is_valid():
			new_donor = form.save()
			return HttpResponseRedirect('/main/')
	return render_to_response('api/add.html',context)

@login_required(login_url='/login/')
def search(request):
    return render_to_response('api/search.html')