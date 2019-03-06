from django.contrib import admin
from blog.models import Article, Comment

# registering Article with the admin back-end
admin.site.register(Article)
# registering Comment with the admin back-end
admin.site.register(Comment)
