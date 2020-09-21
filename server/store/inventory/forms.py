from django.forms import ModelForm
from .models import *


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = [
            'name', 'model', 'maker', 'cost', 'quantity', 'category', 'kind',
            'dateAdded'
        ]


class ArticleKindForm(ModelForm):
    class Meta:
        models = ArticleKind
        fields = ['id', 'label', 'description', 'created_at', 'updated_at']


class StoreArticleForm(ModelForm):
    class Meta:
        models = StoreArticle
        fields = '__all__'