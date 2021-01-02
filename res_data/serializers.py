from rest_framework import serializers

from res_data.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('restaurant_name', 'opening_days', 'opening_hours')

    def to_representation(self, instance):
        return {'restaurant_name': instance.restaurant_name,
                'day_from': instance.opening_days.split(',')[0],
                'day_to': instance.opening_days.split(',')[-1],
                'opening_hours': instance.opening_hours
                }
