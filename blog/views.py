from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from blog.models import Article

def posts_page(request):
    context = {'articles': Article.objects.filter(draft=False).order_by('-published_date')}
    html_string = render(request, 'posts.html', context)
    return HttpResponse(html_string)

def post_show(request, id):
    post = Article.objects.get(pk=id)
    context = {'post': post}
    html_string = render(request, 'post.html', context)
    return HttpResponse(html_string)

def root(request):
    return HttpResponseRedirect('posts')
