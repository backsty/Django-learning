from django.db import models


class Phone(models.Model):
    name = models.CharField(u'Имя', max_length=256)
    price = models.FloatField(u'Цена')
    image = models.CharField(u'Изображение', max_length=256)
    release_date = models.DateField(u'Дата выпуска')
    lte_exists = models.BooleanField(u'Наличие LTE', default=False)
    slug = models.SlugField(unique=True)
