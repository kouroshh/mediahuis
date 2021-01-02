"""restaurants URL Configuration

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
from django.urls import path, include
from pages.views import hello_world
from rest_framework.urlpatterns import format_suffix_patterns
from res_data.views import restaurantListAll
from res_data.views import restaurantListFilterName
from res_data.views import restaurantListFilterDay

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world, name='hello'),
    path('restaurantall/', restaurantListAll.as_view()),
    path('restaurant/<str:day>', restaurantListFilterDay.as_view()),
    path('restaurantname/<str:keyword>', restaurantListFilterName.as_view())
]
