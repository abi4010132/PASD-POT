# Generated by Django 4.1.5 on 2023-01-27 12:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('send_date', models.DateField(null=True, verbose_name='Date sent')),
                ('sender_country', models.CharField(max_length=50, null=True)),
                ('receiver_country', models.CharField(max_length=50, null=True)),
                ('x', models.SmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('y', models.SmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('z', models.SmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
            ],
        ),
    ]
