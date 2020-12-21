from django.db.models import OuterRef, Subquery
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers
from . import models


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.order_by('-create_time')
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ('name', 'parent__name', )
    search_fields = ('name',)


class FlatCategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.order_by('-create_time')
    serializer_class = serializers.FlatCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ('name',)
    search_fields = ('name',)


class ArticleViewSet(ModelViewSet):
    queryset = models.Article.objects.order_by('-create_time')
    serializer_class = serializers.ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ('category', )
    search_fields = ('title', 'category',)

    def get_queryset(self):
        qs = super().get_queryset()
        next_article = qs.filter(
            create_time__gt=OuterRef('create_time')
        ).order_by('create_time')
        prev_article = qs.filter(
            create_time__lt=OuterRef('create_time')
        ).order_by('-create_time')
        return qs.annotate(
            next_article=Subquery(next_article.values('id')[:1]),
            prev_article=Subquery(prev_article.values('id')[:1]),
        )


class ArticlePictureViewSet(ModelViewSet):
    queryset = models.ArticlePicture.objects.order_by('pk')
    serializer_class = serializers.ArticlePictureSerializer
    permission_classes = (AllowAny, )

    def perform_update(self, serializer):
        return

    def perform_destroy(self, instance):
        return


class ArticleFileViewSet(ModelViewSet):
    queryset = models.ArticleFile.objects.order_by('pk')
    serializer_class = serializers.ArticleFileSerializer
