from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.core import serializers

from .forms import *
from .models import *

# Create your views here.

def DashboardView(request):
	return render(request, 'project_admin/index.html')

class DetailView(generic.DetailView):
	model = Project
	template_name = 'project_admin/detail.html'

def projectsView(request, mode):
	return render(request, 'project_admin/projects.html', {'mode':mode})

def json(request, mode):
	if mode == 'active':
		projects = Project.objects.filter(status=1)
	if mode == 'history':
		projects = Project.objects.all()
	data = serializers.serialize('json', projects, use_natural_foreign_keys=True)
	return HttpResponse(data, content_type='application/json')

def get_project(request):
	if request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			project = form.save(commit=False)
			project.status = 1
			project.save()
			return HttpResponseRedirect('/projects/active/')
	else:
		form = ProjectForm()
	return render(request, 'project_admin/get_project.html', {'form': form})

def get_client(request):
	if request.method == 'POST':
		form = ClientForm(request.POST)
		if form.is_valid():
			client = form.save(commit=False)
			client.status = 1
			client.save()
			return HttpResponseRedirect('/projects/active/')
	else:
		form = ClientForm()
	return render(request, 'project_admin/get_client.html', {'form': form})

def get_itemcost(request):
	if request.method == 'POST':
		item_form = ItemForm(request.POST)
		cost_form = CostForm(request.POST)
		if item_form.is_valid() and cost_form.is_valid():
			item = item_form.save(commit=False)
			item.category = 5
			item.save()
			cost = cost_form.save(commit=False)
			cost.item = item
			cost.supplier = 1
			cost.save()
			return HttpResponseRedirect('/projects/active/')
	else:
		item_form = ItemForm()
		cost_form = CostForm()
	return render(request, 'project_admin/get_itemcost.html', {'item_form': item_form, 'cost_form': cost_form})


#def login(request):
#	username = request.POST['username']
#	password = request.POST['password']
#	user = authenticate(username=username, password=password)
#	if user is not None:
#		if user.is_active:
#			login(request, user)
#			return render(request, 'project_admin/index.html', context)
#		else:
#			return render(request, 'project_admin/detail.html', context)
#	else:
#		return render(request, 'project_admin/detail.html', context)