# Generated by Django 4.0.1 on 2022-01-23 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='total_items',
        ),
    ]
