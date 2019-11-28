from django.contrib import admin

from apps.comunes.views import get_app_list
from .models import Article, Post, Comment

admin.AdminSite.get_app_list = get_app_list

admin.site.register(Article)
admin.site.register(Post)
admin.site.register(Comment)
