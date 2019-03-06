from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from blog.models import Article, Comment

def posts_page(request):
    context = {'articles': Article.objects.filter(draft=False).order_by('-published_date')}
    html_string = render(request, 'posts.html', context)
    return HttpResponse(html_string)

def post_show(request, id):
    post = Article.objects.get(pk=id)
    context = {'post': post}
    html_string = render(request, 'post.html', context)
    return HttpResponse(html_string)

def create_comment(request):
    request_dict = request.POST
    article = Article.objects.get(pk=request_dict['post'])
    name = request_dict['comment-name']
    message = request_dict['comment-message']
    new_comment = Comment.objects.create(name=name, message=message, article=article)
    path = '/posts/' + str(article.pk)
    return HttpResponseRedirect(path)
    
def root(request):
    return HttpResponseRedirect('posts')
