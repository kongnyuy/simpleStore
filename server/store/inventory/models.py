from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'app_users'
        verbose_name_plural = 'users'


class UserSession(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,
                             db_column='user_id',
                             on_delete=models.CASCADE)
    startTime = models.DateTimeField(default=timezone.now)
    endTime = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users_sessions'
        verbose_name_plural = 'sessions'


class ArticleKind(models.Model):
    #id = -1
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'article_kinds'
        verbose_name_plural = 'article_kinds'


class ArticleCategory(models.Model):
    #id = -1
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100)
    description = models.TextField()
    dateAdded = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'article_categories'
        verbose_name_plural = 'categories'


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=150)
    maker = models.CharField(max_length=150)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    category = models.ForeignKey(ArticleCategory,
                                 null=True,
                                 db_column='category_id',
                                 on_delete=models.SET_NULL)
    kind = models.ForeignKey(ArticleKind,
                             db_column='article_kind_id',
                             null=True,
                             on_delete=models.SET_NULL)
    dateAdded = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'articles_stock'
        verbose_name_plural = 'articles'


class StoreArticle(models.Model):
    article = models.OneToOneField(Article,
                                   db_column='article_id',
                                   on_delete=models.DO_NOTHING)
    count = models.IntegerField(default=0)
    shelf = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'articles_store'
        verbose_name_plural = 'store_articles'


class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,
                             db_column='user_id',
                             on_delete=models.CASCADE)
    article = models.ForeignKey(Article,
                                db_column='article_id',
                                null=True,
                                on_delete=models.SET_NULL)
    articleCount = models.IntegerField(default=0)
    session = models.ForeignKey(UserSession,
                                db_column='session_id',
                                on_delete=models.CASCADE)
    isAvail = models.BooleanField()
    dateCreated = models.DateTimeField(default=timezone.now,
                                       db_column='date_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
