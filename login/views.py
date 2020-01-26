from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import logout


def group_check(request):
	group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
	group_name=str(group_name[0]) # convert to string

	if "Caddy" == group_name:
		return redirect('http://127.0.0.1:8000/caddy/')
	elif "Golfer" == group_name:
		return redirect('http://127.0.0.1:8000/golfer/')

def logout_view(request):
	logout(request)
	return redirect('http://127.0.0.1:8000/')


class register_golfer(TemplateView):
  template_name = "register_golfer.html"

class register_caddy(TemplateView):
  template_name = "register_caddy.html"
