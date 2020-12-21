from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """栏目"""
    name = models.CharField('名称', max_length=50, help_text='名称')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name='上级',
                            db_index=True, on_delete=models.CASCADE, help_text='上级')
    is_hidden = models.BooleanField('隐藏', default=False, help_text='隐藏')

    class Meta:
        verbose_name = '01.栏目'
        verbose_name_plural = verbose_name


class Article(models.Model):
    """文章"""
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='articles', help_text='栏目')
    title = models.CharField('标题', max_length=255, help_text='标题')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    create_user = models.ForeignKey('usercenter.User', on_delete=models.SET_NULL,
                                    null=True, blank=True, verbose_name='创建人', help_text='创建人')
    content = models.TextField('内容', null=True, blank=True, help_text='内容')

    class Meta:
        verbose_name = '02. 文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_time', 'category']

    def __str__(self):
        return self.title

    @property
    def create_time_display(self):
        return self.create_time.strftime('%Y-%m-%d %H:%M:%S')


class ArticlePicture(models.Model):
    """文章图片"""
    picture = models.FileField('媒体文件', upload_to='article/media/%Y/%m/%d/')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '03. 媒体文件'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    @property
    def create_time_display(self):
        return self.create_time.strftime('%Y-%m-%d %H:%M:%S')


class ArticleFile(models.Model):
    """文章附件"""
    article_file = models.FileField('附件', upload_to='article/files/%Y/%m/%d/')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '04. 附件'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    @property
    def create_time_display(self):
        return self.create_time.strftime('%Y-%m-%d %H:%M:%S')
