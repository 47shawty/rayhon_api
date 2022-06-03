from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.admin import User

from .managers import CategoryManager
from django.urls import reverse


class Category(MPTTModel):
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children",
                            verbose_name=_('Parent'))
    name = models.CharField(max_length=255, verbose_name=_('Name'), null=True, blank=True)
    slug = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Slug'))
    icon = models.ImageField(upload_to="icons/", blank=True, null=True, verbose_name=_('Icon'))

    objects = CategoryManager()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=250)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='icons/', blank=True, null=True)
    slug = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    is_top = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name


class TopWorker(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='workers/', blank=True, null=True)


    def __str__(self):
        return self.name


class Statistics(models.Model):
    name = models.CharField(max_length=250)
    count = models.IntegerField(default='0')

    def __str__(self):
        return self.name


class Review(models.Model):
    RATE_CHOICES = [
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]
    rate = models.IntegerField(choices=RATE_CHOICES)
    message = models.TextField()

    def __str__(self):
        return str(self.rate)
