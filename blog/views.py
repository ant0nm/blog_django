from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime

def home_page(request):
    date = datetime.today().strftime('%Y-%m-%d')
    context = {'current_date': date}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def root(request):
    return HttpResponseRedirect('home')
