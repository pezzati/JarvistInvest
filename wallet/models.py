from django.db import models


class Asset(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Wallet(models.Model):
    description = models.TextField()
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='wallets')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='wallets')
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='wallets')

    def __str__(self) -> str:
        return f"{self.asset} - {self.category} - {self.market}"
