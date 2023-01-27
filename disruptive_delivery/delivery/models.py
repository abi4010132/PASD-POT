from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Order(models.Model):

    id = models.PositiveBigIntegerField(primary_key=True)
    send_date = models.DateField('Date sent', null = True)
    sender_name = models.CharField(max_length = 50, null = True),
    sender_street = models.CharField(max_length = 100, null = True),
    sender_zipcode = models.CharField(max_length = 10, null = True),
    sender_city = models.CharField(max_length = 50, null = True),
    sender_country = models.CharField(max_length = 50, null = True)

    receiver_name = models.CharField(max_length = 50, null = True),
    receiver_street = models.CharField(max_length = 100, null = True),
    receiver_zipcode = models.CharField(max_length = 10, null = True),
    receiver_city = models.CharField(max_length = 50, null = True),
    receiver_country = models.CharField(max_length = 50, null = True)
    x = models.SmallIntegerField(null = True, validators=[
            MinValueValidator(1)
        ])
    y = models.SmallIntegerField(null = True, validators=[
            MinValueValidator(1)
        ])
    z = models.SmallIntegerField(null = True, validators=[
            MinValueValidator(1)
        ])
    price = models.DecimalField(null = True, max_digits = 4, decimal_places=2)
    # delivery_status = (
    #     ('Delivered', 'Delivered')
    #     ('Sent', 'Sent'),
    #     ('Not sent', 'Not sent')
    # )

