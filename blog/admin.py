from django.contrib import admin
from blog.models import Article

# registering Article with the admin back-end
admin.site.register(Article)
