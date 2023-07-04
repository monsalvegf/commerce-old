from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    category = models.CharField(max_length=64)

class Auctions(models.Model):
    auction_name = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Bids(models.Model):
    auction = models.ForeignKey(Auctions, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits=12, decimal_places=2)
    date_bid = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    auction = models.ForeignKey(Auctions, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.DecimalField(max_digits=12, decimal_places=2)
    date_comment = models.DateTimeField(auto_now_add=True)
