from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from blog.models import Article

def home_page(request):
    context = {'articles': Article.objects.filter(draft=False).order_by('-published_date')}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def root(request):
    return HttpResponseRedirect('home')
