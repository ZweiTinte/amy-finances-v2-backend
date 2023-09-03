from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class Account(models.Model):
    iban = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    balance = models.DecimalField(max_digits=20, decimal_places=3)
    accountType = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    
class Category(models.Model):
    type = models.IntegerField()
    name = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    
class Transaction(models.Model):
    transactionType = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    date = models.CharField(max_length=120)
    recurringEnd = models.CharField(max_length=120)
    recurringPeriod = models.CharField(max_length=120)
    recurringGap = models.IntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, blank = True, null = True)
    fromAccount = models.ForeignKey(Account, on_delete = models.CASCADE, blank = True, null = True, related_name='transactionFromAccount')
    toAccount = models.ForeignKey(Account, on_delete = models.CASCADE, blank = True, null = True, related_name='transactionToAccount')
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    
class Stock(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    isin = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    link = models.TextField()
    name = models.CharField(max_length=120)
    watchlisted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    
class Order(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    date = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    sum = models.DecimalField(max_digits=20, decimal_places=3)
    cost = models.DecimalField(max_digits=20, decimal_places=3)
    orderType = models.CharField(max_length=120)
    fromAccount = models.ForeignKey(Account, on_delete = models.CASCADE, blank = True, null = True, related_name='orderFromAccount')
    toAccount = models.ForeignKey(Account, on_delete = models.CASCADE, blank = True, null = True, related_name='orderToAccount')
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, blank = True, null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    
class Dividend(models.Model):
    amountBeforeTax = models.DecimalField(max_digits=20, decimal_places=3)
    payDate = models.CharField(max_length=120)
    taxAmount = models.DecimalField(max_digits=20, decimal_places=3)
    exDate = models.CharField(max_length=120)
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, blank = True, null = True)
    toAccount = models.ForeignKey(Account, on_delete = models.CASCADE, blank = True, null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    