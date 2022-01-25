from django.db import models
from django.utils import timezone


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    address = models.TextField()
    number = models.IntegerField()
    email = models.EmailField(max_length=250, unique=True, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


    def __str__(self):
        fields = [
            self.first_name + self.last_name,
            self.email
        ]
        return fields