from django.db import models

# Create your models here.


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=150)
    opening_days = models.CharField(max_length=50)
    opening_hours = models.CharField(max_length=50)

    def __str__(self):
        return self.restaurant_name

    class Meta:
        db_table = "restaurant"
