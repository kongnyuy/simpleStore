from django.contrib import admin
from .models import *


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Articles in stock', {
            'fields': [
                'name', 'model', 'maker', 'cost', 'quantity', 'category',
                'kind', 'dateAdded'
            ]
        }),
        #nest tuple
    ]

    list_display = [
        'name', 'model', 'maker', 'cost', 'quantity', 'category', 'kind',
        'dateAdded'
    ]
    list_filter = ['model', 'maker']
    search_fields = ['maker', 'model']


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    fieldsets = [('Article categories', {
        'fields': ['label', 'description', 'dateAdded']
    })]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = [('Application users', {'fields': ['name']})]


@admin.register(ArticleKind)
class ArticleKindAdmin(admin.ModelAdmin):
    fieldsets = [('Kinds of article sold', {
        "fields": ['label', 'description']
    })]


@admin.register(StoreArticle)
class StoreArticleAdmin(admin.ModelAdmin):
    fieldsets = [('Articles in the store', {
        #'fields': ['articleId', 'shelf', 'count']
        'fields': [ 'shelf', 'count']
    })]


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    fieldsets = [(
        'User created baskets',
        {
            'fields': [
                'articleCount', 'isAvail', 'dateCreated'
                #'article_id', 'user_id', 'articleCount', 'session_id', 'isAvail',
            ]
        })]


@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
    fieldsets = [('User sessions', {
        'fields': ['startTime', 'endTime']
    })]
