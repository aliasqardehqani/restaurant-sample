# Generated by Django 4.0.1 on 2022-01-23 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_remove_cartitems_total_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]