from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import status
from res_data.models import Restaurant
from res_data.serializers import RestaurantSerializer
from django.db.models import Q


class restaurantListAll(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        rs = RestaurantSerializer(restaurants, many=True)
        return Response(rs.data)


class restaurantListFilterDay(APIView):
    def get(self, request, day):
        restaurants = Restaurant.objects.filter(
            Q(opening_days__contains=day.title()))
        rs = RestaurantSerializer(restaurants, many=True)
        return Response(rs.data)


class restaurantListFilterName(APIView):
    def get(self, request, keyword):
        restaurants = Restaurant.objects.filter(
            restaurant_name__iregex=r'^{0}\s.*|.*\s{0}$|.*\s{0}\s.*|{0}$'.format(keyword))
        rs = RestaurantSerializer(restaurants, many=True)
        return Response(rs.data)
