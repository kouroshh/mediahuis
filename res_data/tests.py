import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from res_data.models import Restaurant
from res_data.serializers import RestaurantSerializer


class BasicTest(TestCase):
    def test_fields(self):
        restaurant = Restaurant()
        restaurant.restaurant_name = "restaurant test"
        restaurant.opening_days = "Mon,Tue,Fri"
        restaurant.opening_hours = "10 am - 11 pm"
        restaurant.save()

        record = Restaurant.objects.get(pk=1)
        self.assertEqual(record, restaurant)


class RestaurantTestCase(APITestCase):
    def setUp(self):
        restaurant = Restaurant()
        restaurant.restaurant_name = "restaurant test"
        restaurant.opening_days = "Mon,Tue,Fri"
        restaurant.opening_hours = "10 am - 11 pm"
        restaurant.save()

    def test_get_all_restaurants(self):
        response = self.client.get("/restaurantall/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_restaurants_on_Mon(self):

        response = self.client.get("/restaurant/Mon")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]["restaurant_name"], 'restaurant test')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]["day_from"], 'Mon')

    def test_get_all_restaurants_with_keyword(self):

        response = self.client.get("/restaurantname/test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]["restaurant_name"], 'restaurant test')
        self.assertEqual(len(response.data), 1)
