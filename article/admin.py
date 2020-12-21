from django.contrib import admin
from . import models


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'category', 'title', 'create_time', 'create_user', ]


@admin.register(models.ArticlePicture)
class ArticlePictureAdmin(admin.ModelAdmin):
    list_display = ['pk', 'picture', 'create_time', ]


@admin.register(models.ArticleFile)
class ArticleFileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'article_file', 'create_time', ]
