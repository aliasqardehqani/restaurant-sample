from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from contact.models import Contact
class Foods(models.Model):
    FOOD_TYPE = [
        ("BreakFast", "صبحانه"),
        ("Drink", "نوشیدنی"),
        ("Lunch", "ناهار"),
        ("Dinner", "شام"),
    ]
    food_name = models.CharField(_('نام غذا'), max_length=100)
    description = models.CharField(_("توضیحات"), max_length=300)
    discount = models.IntegerField(default=0)
    rate = models.IntegerField(_("امتیاز"))
    price = models.IntegerField(_("قیمت"))
    photo = models.ImageField(upload_to="media/")
    type_food = models.CharField(_("نوع غذا"), max_length=20, choices=FOOD_TYPE, default='DINNER')
    created = models.DateField(_("زمان  انتشار"), auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.food_name + '       ' + self.type_food

class Comment(models.Model):
    food = models.ForeignKey('Foods', verbose_name='غذا', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(_('ایمیل'),max_length=254)
    message = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=True)