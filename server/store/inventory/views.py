import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required

#from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
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

    akinds = ArticleKind.objects.all()
    cats = ArticleCategory.objects.all()
    usess = UserSession.objects.all()
    users = User.objects.all()
    articles = Article.objects.all()
    sarticles = StoreArticle.objects.all()
    baskets = Basket.objects.all()
    return render(request,
                  'dashboard.html',
                  context={
                      'kinds': akinds,
                      'categories': cats,
                      'usessions': usess,
                      'appUsers': users,
                      'articles': articles,
                      'sarticles': sarticles,
                      'baskets': baskets,
                  })


def parseQuery(q):
    if "&" in q:
        sq = q.split('&')
        for i, e in enumerate(sq):
            if "q" in e:
                return e.split('=')[1]
    else:
        print(f'out: {q}')
        sq = q.split('=')
        if "q" in sq:
            return sq[1]




@api_view(['GET', 'POST'])
def search_view(request):
    if request.method == 'GET':
        #query_str = request.META['QUERY_STRING']
        query_str = request.GET.urlencode()
        if query_str.strip() == '':
            return render(request, 'search.html', context={})
        query = parseQuery(query_str.strip())
        print(f'>>>> {query}')
        farts = Article.objects.filter(name__contains=query)
        size = farts.count()
        return render(request, 'search.html', context={'articles': farts, 'size': size})
    elif request.method == 'POST':
        #Article.objects.annotate(search=SearchVector('body_text') + SearchVector('blog__tagline'),).filter(search='Cheese')
        #Articles.objects.filter(body_text__search='Cheese')
        pass


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


@api_view(['POST'])
def basket_data_save(request):
    #body_unicode = request.body.decode('utf-8')
    #body = json.loads(body_unicode)
    #content = body['content']
    content = request.data
    for id, qty in content.items():
        art = Article.objects.get(id=id)
        print(f'Article: {art.name} -> [{art.quantity}]')
        if (art.quantity > qty):
            art.quantity -= qty
            art.save()
        else:
            res = json.dumps({
                'state':
                'FAILED',
                'reason':
                f'Only {art.quantity} items left for the article',
                'message':
                'Sorry for the inconvinience, we will restock as soon as possible, in the mean time please browse other articles'
            })
        print(f'Article: {art.name} -> [{art.quantity}]')

    #print(content)
    res = json.dumps({
        'state': 'OK',
        'reason': '',
        'message': 'Thank you for your purchase'
    })
    return JsonResponse(res, safe=False)


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