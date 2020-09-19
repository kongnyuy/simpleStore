from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Entry(models.Model):
    user = models.ForeignKey(User)
    pattern = models.CharField(max_length=255)
    test_string = models.CharField(max_length=255)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'entries'


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'app_users'
        verbose_name_plural = 'users'


class UserSession(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User)
    startTime = models.DateTimeField(default=timezone.now)
    endTime = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'users_sessions'
        verbose_name_plural = 'sessions'


class ArticleKind(models.Model):
    #id = -1
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'article_kinds'
        verbose_name_plural = 'article_kinds'


class ArticleCategory(models.Model):
    #id = -1
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100)
    description = models.TextField()
    dateAdded = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'article_categories'
        verbose_name_plural = 'categories'


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    model = models.CharField()
    maker = models.CharField()
    cost = models.DecimalField()
    quantity = models.IntegerField()
    cateory = models.ForeignKey(ArticleCategory)
    kind = models.ForeignKey(ArticleKind)
    dateAdded = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'articles_stock'
        verbose_name_plural = 'articles'


class StoreArticle(Article):
    shelf = models.CharField(max_length=155)

    class Meta:
        db_table = 'articles_store'
        verbose_name_plural = 'store_articles'


class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, db_column='user_id')
    article = models.ForeignKey(StoreArticle,db_column='article_id')
    session = models.ForeignKey(UserSession,db_column='session_id')
    dateCreated = models.DateTimeField(default=timezone.now, db_column='date_created')