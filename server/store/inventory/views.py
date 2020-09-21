from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required
#from snippets.serializers import SnippetSerializer
from .serializers import *

from .models import *


# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    # Render the HTML template index.html with the data in the context variable
    articles = Article.objects.all()
    akinds = ArticleKind.objects.all()
    cats = ArticleCategory.objects.all()
    return render(request,
                  'index.html',
                  context={
                      'articles': articles,
                      'kinds': akinds,
                      'categories': cats
                  })


@login_required(login_url='/accounts/login/')
def dashboard_view(request):
    if not request.user.is_authenticated:
        return render(request, 'myapp/login_error.html')
    return render(request, 'dashboard.html', context={})


@api_view(['GET'])
def all_articles(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def all_akinds(request):
    akinds = ArticleKind.objects.all()
    serializer = ArticleKindSerializer(akinds, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def all_categories(request):
    cats = ArticleCategory.objects.all()
    serializer = ArticleCategorySerializer(cats, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def all_user_sessions(request):
    usess = UserSession.objects.all()
    serializer = UserSessionSerializer(usess, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def all_app_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def all_store_articles(request):
    sarticles = StoreArticle.objects.all()
    serializer = StoreArticleSerializer(sarticles, many=True)
    return JsonResponse(serializer, safe=False)


@api_view(['GET'])
def all_baskets(request):
    baskets = Basket.objects.all()
    serializer = BasketSerializer(baskets, many=True)
    return JsonResponse(serializer, safe=False)


#Article request handlers
@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, pk):
    """
    Retrieve, update or delete an article
    """
    try:
        #snippet = Snippet.objects.get(pk=pk)
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)