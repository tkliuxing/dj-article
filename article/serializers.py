from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from . import models


class CategorySerializer(ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = (
            'pk',
            'name',
            'parent',
            'items',
        )

    def get_items(self, obj):
        children = obj.children.all()
        childrens = CategorySerializer(children, many=True).data
        result = []
        result.extend(childrens)
        return result


class FlatCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = (
            'pk',
            'name',
            'parent',
        )


class ArticleSerializer(ModelSerializer):
    next_article = serializers.SerializerMethodField()
    prev_article = serializers.SerializerMethodField()
    category_info = FlatCategorySerializer(source='category', read_only=True)

    class Meta:
        model = models.Article
        fields = (
            'pk',
            'category',
            'category_info',
            'title',
            'create_time',
            'create_time_display',
            'create_user',
            'content',
            'next_article',
            'prev_article',
        )

    def get_next_article(self, obj):
        pk = getattr(obj, 'next_article', None)
        if pk is None:
            next_article = models.Article.objects.filter(create_time__gt=obj.create_time, category=obj.category)
            if next_article:
                pk = next_article.order_by('create_time').first().pk
        return pk

    def get_prev_article(self, obj):
        pk = getattr(obj, 'prev_article', None)
        if pk is None:
            prev_article = models.Article.objects.filter(create_time__lt=obj.create_time, category=obj.category)
            if prev_article:
                pk = prev_article.order_by('-create_time').first().pk
        return pk


class ArticlePictureSerializer(ModelSerializer):

    class Meta:
        model = models.ArticlePicture
        fields = (
            'pk',
            'picture',
            'create_time',
            'create_time_display',
        )


class ArticleFileSerializer(ModelSerializer):

    class Meta:
        model = models.ArticleFile
        fields = (
            'pk',
            'article_file',
            'create_time',
            'create_time_display',
        )
