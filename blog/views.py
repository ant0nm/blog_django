from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from blog.models import Article, Comment, Topic, CommentForm, ArticleForm

def posts_page(request):
    context = {'title': "Anton's Blog", 'articles': Article.objects.filter(draft=False).order_by('-published_date')}
    html_string = render(request, 'posts.html', context)
    return HttpResponse(html_string)

def post_show(request, id):
    post = Article.objects.get(pk=id)
    context = {'title': post.title, 'post': post, 'comment_form':CommentForm()}
    html_string = render(request, 'post.html', context)
    return HttpResponse(html_string)

def new_post(request):
    context = {'title':'Create a new post', 'article_form': ArticleForm()}
    html_string = render(request, 'new_post.html', context)
    return HttpResponse(html_string)

def create_post(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        new_article = form.save()
        return HttpResponseRedirect("/posts/")
    else:
        html_string = render(request, 'new_post.html', {'title': 'Create a new post', 'article_form': ArticleForm(request.POST)})
        return HttpResponse(html_string)

def create_comment(request):
    article = Article.objects.get(pk=request.POST['post_id'])
    form = CommentForm(request.POST)
    path = '/posts/' + str(article.pk)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.article = article
        new_comment.save()
        return HttpResponseRedirect(path)
    else:
        print(form.errors)

def root(request):
    return HttpResponseRedirect('/posts/')
