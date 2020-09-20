from django.forms import ModelForm
from .models import *


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = [
            'name', 'model', 'maker', 'cost', 'quantity', 'category',
            'kind', 'dateAdded'
        ]
