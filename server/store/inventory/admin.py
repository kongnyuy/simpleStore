from django.contrib import admin
from .models import *
from .forms import *


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

    readonly_fields = ('created_at', 'updated_at')
    list_display = [
        'id', 'name', 'model', 'maker', 'cost', 'quantity', 'category', 'kind',
        'dateAdded'
    ]
    list_filter = ['model', 'maker', 'category', 'kind']
    search_fields = ['maker', 'model']


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    fieldsets = [('Article categories', {
        'fields': ['label', 'description', 'dateAdded']
    })]

    list_display = ['id', 'label', 'description', 'created_at', 'updated_at']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = [('Application users', {'fields': ['name']})]

    readonly_fields = ('id', 'created_at', 'updated_at')
    list_display = ['id', 'name', 'created_at', 'updated_at']


@admin.register(ArticleKind)
class ArticleKindAdmin(admin.ModelAdmin):
    fieldsets = [('Kinds of article sold', {
        "fields": ['label', 'description']
    })]

    readonly_fields = ('created_at', 'updated_at')

    list_display = ['id', 'label', 'description', 'created_at', 'updated_at']


@admin.register(StoreArticle)
class StoreArticleAdmin(admin.ModelAdmin):
    fieldsets = [(
        'Articles in the store',
        {
            'fields': ['article', 'shelf', 'count']
            #'fields': [ 'shelf', 'count']
        })]

    form = StoreArticleForm
    readonly_fields = ('created_at', 'updated_at')

    #list_display  = ['id', 'article', 'article__id', 'shelf', 'count', 'created_at', 'updated_at']
    list_display = [
        'id', 'article', 'shelf', 'count', 'created_at', 'updated_at'
    ]

    def get_article(self, obj):
        return obj.article.name

    get_article.admin_order_field = 'Article'  #Allows column order sorting
    get_article.short_description = 'Article Name'  #Renames column head


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    fieldsets = [(
        'User created baskets',
        {
            'fields': [
                'user', 'article', 'session', 'articleCount', 'isAvail',
                'dateCreated'
                #'article_id', 'user_id', 'articleCount', 'session_id', 'isAvail',
            ]
        })]

    readonly_fields = ('user', 'article', 'session', 'articleCount', 'isAvail',
                       'dateCreated')
    list_display = [
        'user', 'article', 'session', 'articleCount', 'isAvail', 'dateCreated'
    ]


@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
    fieldsets = [('User sessions', {'fields': ['user','startTime', 'endTime']})]

    list_display = ['id','user', 'startTime', 'endTime']
