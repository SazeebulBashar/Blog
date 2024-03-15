from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse


def Index(request):
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))
