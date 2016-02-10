from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone
from api.forms import DonorForm
from api.models import Donor
from django_tables2   import RequestConfig
from api.tables  import DonorTable



@login_required(login_url='/login/')
def record(request):
	context = RequestContext(request)
	if request.POST:
		form = DonorForm(request.POST)
		if form.is_valid():
			new_donor = form.save()
			return HttpResponseRedirect('/main/')
	return render_to_response('api/add.html',context)






@login_required(login_url='/login/')
def search(request):
	context=RequestContext(request)
	group = request.GET.get('blood_group')
	rh = request.GET.get('rh_factor')
	valid_date=(timezone.now()-datetime.timedelta(days=120)).date()
	data = DonorTable(Donor.objects.filter(blood_group=group,rh_factor=rh,last_donation__lt=valid_date))
	RequestConfig(request).configure(data)
	return render_to_response('api/search.html',{"data":data},context)
