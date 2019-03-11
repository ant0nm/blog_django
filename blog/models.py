from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from datetime import date, datetime
from pytz import timezone

min_length = MinLengthValidator(limit_value=2)

class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(validators=[min_length])
    draft = models.BooleanField()
    published_date = models.DateField(help_text='yyyy/mm/dd')
    author = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="topics")

    def __str__(self):
        return self.title

    def sort_comment_set(self):
        return self.comments.order_by('created_at')

class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.message

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'draft', 'published_date', 'author', 'topic']

    def clean_published_date(self):
        # localizing both dates
        publishedDate = self.cleaned_data['published_date']
        presentDate = date.fromtimestamp(datetime.now(timezone('America/Toronto')).timestamp())
        print(presentDate)
        print(publishedDate)
        isDraft = self.cleaned_data['draft']
        if isDraft:
            if publishedDate < presentDate:
                raise ValidationError('Specified date must be in the future!')
            else:
                return publishedDate
        else:
            if publishedDate > presentDate:
                raise ValidationError('Specified date must be in the past!')
            else:
                return publishedDate
