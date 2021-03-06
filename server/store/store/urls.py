"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#from pages.views import home_view, about_view, contact_view
from inventory.views import *

from django.urls import path, include
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from rest_framework import routers, serializers, viewsets
from django.contrib import admin



# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path(r'stock/', dashboard_view, name="dashboard_view"),
    #url(r'^api-auth/', include('rest_framework.urls')),
    #authentication urls
    # path(r'accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    #backend entity and relationship routes
    path('be/articles/', all_articles, name="all_articles"),
    path('be/akinds/', all_akinds, name="all_kinds"),
    path('be/categories/', all_categories, name='all_categories'),
    path('be/usessions/', all_user_sessions, name="usessions"),
    path('be/ausers/', all_app_users, name="ausers"),
    path('be/baskets/', all_baskets, name="baskets"),
    path('be/sarticles/', all_store_articles, name="sarticles"),

    path(r'be/baskets/buy',basket_data_save, name="basket_data_save"),
    path(r'search/', search_view, name="search_view")
]
