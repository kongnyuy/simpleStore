from rest_framework import serializers

from .models import *



class ArticleSerializer(serializers.Serializer):
    #id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = Article
        fields = [
            'id', 'name', 'model', 'maker', 'cost', 'quantity','category', 'kind', 'dateAdded',
            'created_at', 'updated_at'
        ]



class ArticleKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleKind
        fields = ['id', 'label', 'description', 'created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'created_at', 'updated_at']


class ArticleCategorySerializer(serializers.ModelSerializer)        :
    class Meta:
        model = ArticleCategory
        fields = ['id', 'label', 'description', 'dateAdded', 'created_at', 'updated_at']


class StoreArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreArticle
        fields = ['id', 'count', 'shelf', 'article', 'created_at', 'updated_at']


class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ['id', 'startTime','endTime', 'user', 'created_at', 'updated_at']

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ['id', 'articleCount', 'isAvail', 'date_created', 'article', 'session', 'user', 'created_at', 'updated_at']