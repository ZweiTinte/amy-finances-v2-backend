from django.db import models

# Create your models here.
class Account(models.Model):
    iban = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    balance = models.DecimalField(max_digits=20, decimal_places=3)
    accountType = models.CharField(max_length=120)

    def _str_(self):
        return self.name
    
class Transaction(models.Model):
    transactionType = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    date = models.CharField(max_length=120)
    recurringEnd = models.CharField(max_length=120)
    recurringPeriod = models.CharField(max_length=120)
    recurringGap = models.IntegerField()

    def _str_(self):
        return self.name
    
class Order(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    date = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    sum = models.DecimalField(max_digits=20, decimal_places=3)
    cost = models.DecimalField(max_digits=20, decimal_places=3)
    orderType = models.CharField(max_length=120)

    def _str_(self):
        return self.date
    
class Stock(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    isin = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    link = models.TextField()
    name = models.CharField(max_length=120)
    watchlisted = models.BooleanField(default=False)

    def _str_(self):
        return self.name
    
class Dividend(models.Model):
    amountBeforeTax = models.DecimalField(max_digits=20, decimal_places=3)
    payDate = models.CharField(max_length=120)
    taxAmount = models.DecimalField(max_digits=20, decimal_places=3)
    exDate = models.CharField(max_length=120)

    def _str_(self):
        return self.payDate
    
class Category(models.Model):
    type = models.IntegerField()
    name = models.CharField(max_length=120)

    def _str_(self):
        return self.name