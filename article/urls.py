from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api


router = DefaultRouter()

router.register(r'category', api.CategoryViewSet)
router.register(r'flatcategory', api.FlatCategoryViewSet)
router.register(r'article', api.ArticleViewSet)
router.register(r'articlepicture', api.ArticlePictureViewSet)
router.register(r'articlefile', api.ArticleFileViewSet)

urlpatterns = (
    path('api/v1/', include(router.urls)),
)
